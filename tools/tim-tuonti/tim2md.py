#!/usr/bin/env python3
"""TIM-wikin kurssit/jypeli/* -> src/-puu ohj1:n Markdown-murteella.

Lähteet (kaikki välimuistissa scratchpadissa):
  timhtml/<polku>.html   sivun HTML-näkymä: kappalelista, liitännäisten JSON
  timpars/<doc>/<par>    kappaleen raaka Markdown (TIM getBlock)
  timfiles/images|files  kuvat ja videot
  tim/wiki.md            etusivun md-vienti (kysymyslista on viitekappale,
                         jonka lähdettä ei saa luettua)

Kappaleista kootaan TIM-Markdown, koodiaidat ja liitännäiset korvataan
paikkamerkeillä, teksti ajetaan pandocilla GFM:ksi ja paikkamerkkien tilalle
kirjoitetaan valmiit lohkot (```csharp,ignore / csharp,feature-jypeli,
//-piilorivit, HIGHLIGHT-merkinnät, <details>, <video>, taulukot).
"""
import html, json, os, pathlib, re, shutil, subprocess, sys, unicodedata, urllib.parse
from timlib import parse_page, get_block

HERE = pathlib.Path(__file__).resolve().parent
PANDOC = str(HERE / "pvenv/lib/python3.11/site-packages/pypandoc/files/pandoc")
HTML_DIR = HERE / "timhtml"
FILES = HERE / "timfiles"
OUT = HERE / "jypelidocs/src"
TIM = "https://tim.jyu.fi"
PREFIX = "kurssit/jypeli/"

RENAMES = {"wiki": "index", "mallit/alku": "mallit/index"}
# Osiot etusivun "listamaisen" navigoinnin järjestyksessä: otsikko -> hakemisto.
SECTION_DIRS = {
    "Aloittaminen": "perusteet", "Olioiden käsittely": "oliot", "Kentät": "kentat",
    "Pelin kulku": "pelin-kulku", "Tapahtumat": "tapahtumat", "Grafiikka": "grafiikka",
    "Äänet": "aanet", "Aseet": "aseet", "Fysiikka": "fysiikka",
    "Käyttöliittymä": "kayttoliittyma", "Laskurit": "laskurit",
    "Matematiikka": "matematiikka", "Ohjaimet": "ohjaimet", "Ohjelmointi": "ohjelmointi",
}
# Sivut, joita etusivun taulukot eivät luettele: (osio, sen jälkeen minkä sivun, otsikko, sivu)
EXTRA_PAGES = {
    "Grafiikka": [("grafiikka/kuvat", "Kuvan läpinäkyvyys", "muut/kuvan-lapinakyvyys")],
}
# Mallipelit: oma päätason osio Aloittamisen perään; pelit ovat alaosioita ja
# vaiheet niiden sivuja (model_games_summary). Pelin esittely irrotetaan
# mallit/alku-sivun "## <peli>"-osiosta omaksi etusivuksi (split_model_games).
# (otsikko, hakemisto, vaiheiden määrä)
MODEL_GAMES = [("Pong", "mallit/pong", 7), ("Läpsylintu", "mallit/lapsylintu", 11)]

# TIMin makrot %%nimi%%. Ne on määritelty dokumenttien esiasetuksissa
# (preamble), jotka tuonti ohittaa; laajennus on HTML-näkymän mukainen kuva.
MACROS = {
    "kokeile": "![](/images/337213/try_to_run.png)",
    "eitoimi": "![](/images/337214/does_not_work_yet.png)",
    "kysymys": "![](/images/337215/question.png)",
}
MACRO_RE = re.compile(r"%%(\w+)%%")

# Sivut, joilla TIMissä ei ole otsikkoa: lisätään, jotta sivulla on yksi H1 ja
# väliotsikot jäävät samalle tasolle kuin sisarsivuilla (demote_headings).
MISSING_TITLES = {"mallit/pong/vaihe1": "Pong-peli, vaihe 1"}

# Käsin korjattavat kohdat: TIMissäkin rikki olleet ankkurit.
HEADING_FIXES = {
    "kentat/tausta": [("# 1. Kuvatiedostosta", "# 1. Kuvatiedostosta {#taustakuva}")],
}
# Tehdään fix_linksin jälkeen, joten muoto on valmis suhteellinen linkki.
LINK_FIXES = {
    "ohjaimet/liikuttelu": [("#1wdXts95Twpe", "#push")],
    # "Takaisin pong-tutoriaaliin" osoitti mallipelien yhteiseen etusivuun.
    "perusteet/projektin-luonti": [("../mallit/index.md#mallipelit", "../mallit/pong/index.md")],
}
HUB_INTRO = """# Jypeli-ohjeet

Jypeli on Jyväskylän yliopistossa kehitetty, opetuskäyttöön suunniteltu
C#-pelikirjasto. Tälle sivustolle on koottu Jypelin käyttöohjeet aiheittain.
Vasemman reunan valikko luettelee ohjeet aiheen mukaan; alla samat ohjeet
kysymyksittäin.

> [!HUOMAUTUS]
> Ohjeet ovat osittain vielä työn alla, ja osa sisällöstä saattaa olla
> puutteellista. Ohjeet on tuotu [TIMin Jypeli-wikistä](https://tim.jyu.fi/view/kurssit/jypeli/wiki).
"""
COLORS = {"vihrea": "GREEN", "punainen": "RED", "sininen": "BLUE", "keltainen": "YELLOW"}
GAME_RE = re.compile(r"class\s+\w+\s*:\s*(PhysicsGame|Game|TopDownPhysicsGame)\b")
NEEDS_CONTENT_RE = re.compile(
    r"\b(LoadImages?|LoadSoundEffect|LoadFont|LoadLevel|LoadSound|FromLevelAsset|FromFile|"
    r"LoadContent|MediaPlayer\.Play|DataStorage)\b")
HIDDEN_USINGS = ["using System;", "using System.Collections.Generic;", "using Jypeli;",
                 "using Jypeli.Assets;", "using Jypeli.Controls;", "using Jypeli.Effects;",
                 "using Jypeli.Widgets;"]
FENCE_RE = re.compile(r"^(?P<fence>```+|~~~+)\s*(?P<info>.*?)\s*$")
PLACEHOLDER = "TIMBLOCK%04dTIMBLOCK"
PLACEHOLDER_RE = re.compile(r"(?:<p>)?TIMBLOCK(\d{4})TIMBLOCK(?:</p>)?")

current_page = ""
TITLE_IDS: dict[str, set[str]] = {}  # sivu -> otsikon omat tunnukset, kerätään ensimmäisellä kierroksella
PAGES = sorted(f.stem.replace("__", "/") for f in HTML_DIR.glob("*.html"))
warnings: list[str] = []
stats: dict[str, int] = {}
fence_infos: dict[str, int] = {}


def warn(msg):
    warnings.append(msg)


def count(key, n=1):
    stats[key] = stats.get(key, 0) + n


def md_rel(tim_path: str) -> str:
    return RENAMES.get(tim_path, tim_path) + ".md"


def expand_macro(m: re.Match) -> str:
    """%%nimi%% -> MACROS; tuntematon jää näkyviin ja varoittaa. Kirjainkoko
    ei erota: pong/vaihe6:n %%Kokeile%% näkyy TIMissä kuvana."""
    name = m.group(1).lower()
    if name not in MACROS:
        warn(f"{current_page}: tuntematon makro %%{name}%%")
        return m.group(0)
    count("makroja")
    return MACROS[name]


def pandoc(text: str, *args: str) -> str:
    return subprocess.run([PANDOC, *args], input=text, capture_output=True, text=True,
                          check=True, encoding="utf-8").stdout


def md_to_gfm(text: str) -> str:
    return pandoc(text, "-f", "markdown-implicit_figures-smart", "-t", "gfm-smart",
                  "--wrap=none", "--lua-filter", str(HERE / "indented.lua"))


INDENTED_FENCE_RE = re.compile(r"^``` timindented\n(.*?)^```$", re.S | re.M)


def fence_indented(text: str, highlights: dict) -> str:
    """Lähteen sisennetyt koodilohkot (indented.lua merkitsee ne) aidoiksi."""
    def repl(m):
        body = m.group(1).rstrip("\n").split("\n")
        lang = "csharp"
        if not re.search(r"[;{}()=]", "\n".join(body)):
            lang = "bash" if any(l.startswith("dotnet ") for l in body) else "text"
        count("sisennetty lohko aidaksi")
        return code_block(lang, body)
    return INDENTED_FENCE_RE.sub(repl, text)


ID_MARK_RE = re.compile(r"^(#{1,6} .*?)\s*\{#([^}\s]+)\}\s*$", re.M)


def protect_ids(text: str) -> str:
    """Otsikon oma tunnus {#id} tekstimerkiksi, joka selviää pandocista."""
    return ID_MARK_RE.sub(lambda m: f"{m.group(1)} TIMID{m.group(2)}TIMID", text)


def restore_ids(text: str) -> str:
    return re.sub(r"\s*TIMID([^\s]+?)TIMID", r" {#\1}", text)


def demote_headings(text: str) -> str:
    """Yksi H1 per sivu: jos otsikon jälkeen on toinen H1, kaikki sen jälkeiset
    otsikot astetta alemmas. Koodiaidat ohitetaan."""
    lines = text.split("\n")
    in_fence = False
    h1 = [i for i, l in enumerate(lines) if l.startswith("# ")]
    if len(h1) < 2:
        return text
    out = []
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        elif not in_fence and i > h1[0] and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def soft_breaks(text: str) -> str:
    """pandocin kova rivinvaihto (kenoviiva rivin lopussa) -> kaksi välilyöntiä."""
    return re.sub(r"(?<!\\)\\$", "  ", text, flags=re.M)


def slug(text: str) -> str:
    """Python-Markdownin toc-slugify: ääkköset pois, välit viivoiksi."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s]+", "-", text)


# --- linkit ja tiedostot ------------------------------------------------------

def resolve_link(url: str, page: str):
    """TIMin jypeli-linkki -> suhteellinen .md-linkki, muu -> None (ennallaan)."""
    url = html.unescape(url)
    m = re.match(r"^(?:https?:)?(?://tim\.jyu\.fi)?/view/kurssit/jypeli/([^#?]*)(#.*)?$", url)
    if m:
        target, anchor = m.group(1), m.group(2) or ""
    elif re.match(r"^[a-z][a-z0-9+.-]*:", url) or url.startswith(("/", "#")):
        return None
    else:
        joined = urllib.parse.urljoin(f"{TIM}/view/{PREFIX}{page}", url)
        m = re.match(r"^https://tim\.jyu\.fi/view/kurssit/jypeli/([^#?]*)(#.*)?$", joined)
        if not m:
            return None
        target, anchor = m.group(1), m.group(2) or ""
    target = target.strip("/")
    anchor = urllib.parse.unquote(anchor)
    if anchor.lstrip("#") in TITLE_IDS.get(target, set()):
        anchor = ""  # sivun otsikon tunnus: pelkkä sivu riittää
    if target not in PAGES:
        warn(f"{page}: linkki sivuun, jota ei ole: {target}")
        return f"{TIM}/view/{PREFIX}{target}{anchor}"
    if target == page:
        return anchor or md_rel(target).rsplit("/", 1)[-1]
    rel = os.path.relpath(md_rel(target), start=os.path.dirname(md_rel(page)) or ".")
    return rel + anchor


def copy_file(url: str, page: str, name: str | None = None) -> str:
    """/images/<id>/<nimi> -> src/<sivun hakemisto>/images/<nimi>; palauttaa linkin."""
    url = html.unescape(url).split("?")[0]
    src = FILES / url.lstrip("/")
    if not src.exists():
        warn(f"{page}: tiedosto puuttuu: {url}")
        return TIM + url
    dest_dir = OUT / os.path.dirname(md_rel(page)) / "images"
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = name or src.name
    dest = dest_dir / name
    if dest.exists() and dest.read_bytes() != src.read_bytes():
        name = f"{src.stem}-{src.parent.name}{src.suffix}"
        dest = dest_dir / name
    if not dest.exists():
        shutil.copyfile(src, dest)
    count("tiedostoja")
    return f"images/{name}"


def fix_links(text: str, page: str) -> str:
    def md_link(m):
        new = resolve_link(m.group(2), page)
        return f"{m.group(1)}({new}{m.group(3) or ''})" if new else m.group(0)
    text = re.sub(r"(\[[^\]]*\])\(([^)\s]+)(\s+\"[^\"]*\")?\)", md_link, text)
    def html_link(m):
        new = resolve_link(m.group(2), page)
        return f'{m.group(1)}"{new}"' if new else m.group(0)
    text = re.sub(r'(<a\s+[^>]*href=)"([^"]+)"', html_link, text)
    def md_image(m):
        return f"{m.group(1)}({copy_file(m.group(2), page)}{m.group(3) or ''})"
    text = re.sub(r"(!\[[^\]]*\])\((/(?:images|files)/[^)\s]+)(\s+\"[^\"]*\")?\)", md_image, text)
    def html_image(m):
        return f'{m.group(1)}"{copy_file(m.group(2), page)}"'
    text = re.sub(r'(<(?:img|video|source)\s+[^>]*src=)"(/(?:images|files)/[^"]+)"', html_image, text)
    return text


# --- koodilohkot --------------------------------------------------------------

def normalize_lang(info: str):
    """Aidan otsikko -> (kieli, tunnus)."""
    m = re.match(r"^\s*([^\s{]*)\s*(?:\{#([^}\s]+)\})?", info or "")
    lang, ident = (m.group(1) or "").lower(), m.group(2)
    if lang in ("", "csharp", "cs", "c#", "c-sharp", "csharp,"):
        lang = "csharp"
    return lang, ident


def is_runnable(code: str) -> bool:
    return bool(GAME_RE.search(code) and "override void Begin" in code
                and code.count("{") == code.count("}") and not NEEDS_CONTENT_RE.search(code)
                and "static void Main" not in code)


def with_highlights(lines: list[str], colors: dict[int, str]) -> list[str]:
    """Rivinumero -> väri -merkinnät HIGHLIGHT_X_BEGIN/END-riveiksi."""
    if not colors:
        return lines
    out: list[str] = []
    active = None
    for number, line in enumerate(lines, 1):
        color = colors.get(number)
        if color != active:
            if active:
                out.append(f"// HIGHLIGHT_{active}_END")
            if color:
                out.append(f"// HIGHLIGHT_{color}_BEGIN")
            active = color
        out.append(line)
    if active:
        out.append(f"// HIGHLIGHT_{active}_END")
    return out


def code_block(lang: str, lines: list[str], colors=None, hidden_prefix=0, hidden_suffix=0) -> str:
    """Valmis aita. hidden_prefix/suffix: montako riviä alusta/lopusta piiloon."""
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
        hidden_prefix = max(0, hidden_prefix - 1)
    if lang != "csharp":
        count(f"aita:{lang}")
        return "```" + lang + "\n" + "\n".join(lines) + "\n```"
    full = "\n".join(lines)
    runnable = is_runnable(full)
    body = list(lines)
    if runnable and "using Jypeli" not in full:
        body = HIDDEN_USINGS + body
        hidden_prefix += len(HIDDEN_USINGS)
    body = with_highlights(body, colors or {})
    marked = []
    seen = 0
    for line in body:
        is_marker = line.startswith("// HIGHLIGHT_")
        if not is_marker:
            seen += 1
        hidden = not is_marker and (seen <= hidden_prefix or seen > len(lines) - hidden_suffix + (len(body) - len(lines) - sum(1 for l in body if l.startswith('// HIGHLIGHT_'))))
        marked.append(("//-" + line) if hidden else line)
    info = "csharp,feature-jypeli" if runnable else "csharp,ignore"
    count("aita:" + info)
    return "```" + info + "\n" + "\n".join(marked) + "\n```"


def cs_plugin_block(j: dict, page: str):
    """csPlugin -> (md-teksti ennen lohkoa, valmis lohko)."""
    m = j.get("markup", {})
    program = j.get("program") or ""
    by = (j.get("by") or j.get("byCode") or "").rstrip("\n")
    before = []
    if m.get("header"):
        before.append("#### " + m["header"])
    if m.get("stem"):
        before.append(m["stem"])
    by_lines = by.split("\n")
    while by_lines and not by_lines[0].strip():
        by_lines.pop(0)
    if program and "REPLACEBYCODE" in program:
        plines = program.rstrip("\n").split("\n")
        idx = next(i for i, l in enumerate(plines) if "REPLACEBYCODE" in l)
        lines = plines[:idx] + by_lines + plines[idx + 1:]
        block = code_block("csharp", lines, hidden_prefix=idx, hidden_suffix=len(plines) - idx - 1)
    else:
        block = code_block("csharp", by_lines)
    count("csPlugin")
    return "\n\n".join(before), block


def parse_settings(text: str) -> dict[str, dict[int, str]]:
    """Asetuskappaleen css: #koodiN { #cb1-a, #cb1-b { background-color: $väri } }."""
    result: dict[str, dict[int, str]] = {}
    for block in re.finditer(r"#(\w+)\s*\{((?:[^{}]*\{[^{}]*\})*[^{}]*)\}", text):
        ident, body = block.group(1), block.group(2)
        for rule in re.finditer(r"((?:#cb1-\d+\s*,?\s*)+)\{([^}]*)\}", body):
            color = re.search(r"background-color:\s*\$(\w+)", rule.group(2))
            if not color or color.group(1) not in COLORS:
                continue
            for n in re.findall(r"#cb1-(\d+)", rule.group(1)):
                result.setdefault(ident, {})[int(n)] = COLORS[color.group(1)]
    return result


def pre_html_block(text: str) -> str:
    """<pre class="sourceCode"> rivispanneineen -> aita, värjätyt sanat riveiksi."""
    lines, colors = [], {}
    for n, span in enumerate(re.findall(r'<span id="cb\d+-\d+">(.*?)</span>\s*(?=<span id="cb|</code>)', text, re.S), 1):
        if "sanaVihreaksi" in span:
            colors[n] = "GREEN"
        elif "sanaPunaiseksi" in span:
            colors[n] = "RED"
        lines.append(html.unescape(re.sub(r"<[^>]+>", "", span)))
    count("pre-html")
    return code_block("csharp", lines, colors)


# --- muut lohkot --------------------------------------------------------------

def video_block(m: dict, page: str) -> str:
    file, footer = m.get("file", ""), m.get("footer")
    yt = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)", file)
    count("video")
    if yt:
        return f"📺 [{footer or 'Katso video'} (YouTube)](https://www.youtube.com/watch?v={yt.group(1)})"
    if file.startswith("/files/"):
        name = f"{slug(footer)}.mp4" if footer and file.endswith("/output.mp4") else None
        local = copy_file(file, page, name)
        width = f' width="{m["width"]}"' if m.get("width") else ""
        block = f'<video controls{width} src="{local}"></video>'
        return block + (f"\n\n*{footer}*" if footer else "")
    warn(f"{page}: tuntematon video: {file}")
    return f"📺 [{footer or 'Katso video'}]({file})"


def cell_text(cell) -> str:
    while isinstance(cell, dict):
        cell = cell.get("cell", "")
    text = html.unescape(str(cell or "")).strip()
    text = re.sub(r'<img\s+src="([^"]+)"\s*/?>', r"![](\1)", text)
    text = re.sub(r'<a\s+href="([^"]+)">(.*?)</a>', r"[\2](\1)", text, flags=re.S)
    return re.sub(r"\s*\n\s*", "<br>", text).replace("|", "\\|")


def table_block(j: dict, page: str) -> str:
    rows = [[cell_text(c) for c in r.get("row", [])] for r in j.get("table", {}).get("rows", [])]
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return ""
    if all(re.search(r"(previous|next)_arrow", c) for r in rows for c in r):
        count("nuolitaulukko pois")
        return ""
    count("timTable")
    ncol = max(len(r) for r in rows)
    lines = ["|" + "  |" * ncol, "|" + " --- |" * ncol]
    for r in rows:
        r = r + [""] * (ncol - len(r))
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def color_table(text: str) -> str:
    rows = re.findall(r'<div style="background:\s*(#[0-9A-Fa-f]{3,8})"><p[^>]*>([^<]+)</p></div>', text)
    lines = ["| Väri | Nimi |", "| --- | --- |"]
    for hexcode, name in rows:
        swatch = (f'<span style="display:inline-block;width:3em;height:1.2em;'
                  f'vertical-align:middle;background:{hexcode};border:1px solid #8888"></span>')
        lines.append(f"| {swatch} | `Color.{name.strip()}` |")
    count("väritaulukko")
    return "\n".join(lines)


def html_table_block(text: str) -> str:
    count("html-taulukko")
    return pandoc(text, "-f", "html", "-t", "gfm-smart", "--wrap=none").strip()


# --- sivu ---------------------------------------------------------------------

def extract_fences(text: str, blocks: list[str], highlights: dict) -> str:
    """Koodiaidat paikkamerkeiksi; paikkamerkki on oma kappaleensa."""
    out, lines = [], text.split("\n")
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1
            continue
        fence, info = m["fence"], m["info"]
        j = i + 1
        while j < len(lines) and not (lines[j].startswith(fence) and not lines[j].strip(fence[0]).strip()):
            j += 1
        body = lines[i + 1:j]
        fence_infos[info] = fence_infos.get(info, 0) + 1
        lang, ident = normalize_lang(info)
        if not info.strip() and not re.search(r"[;{}()=]", "\n".join(body)):
            lang = "bash" if any(l.startswith("dotnet ") for l in body) else "text"
        blocks.append(code_block(lang, body, highlights.get(ident or "", {})))
        out.extend(["", PLACEHOLDER % (len(blocks) - 1), ""])
        i = j + 1
    return "\n".join(out)


STRAY_P_RE = re.compile(r'<p(?: id="#?(?P<id>[\w-]+)")?>')


def drop_stray_paragraph_tags(text: str, page: str) -> str:
    """TIMin ankkurikikka: sulkematon <p id="#x"> otsikon alla nielisi loppusivun
    raakana HTML:nä. Tagit pois ja tunnus edelliseen otsikkoon."""
    if "</p>" in text or not STRAY_P_RE.search(text):
        return text
    ids = [m.group("id") for m in STRAY_P_RE.finditer(text) if m.group("id")]
    text = STRAY_P_RE.sub("", text)
    count("irto-<p> pois")
    if ids:
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("#") and "{#" not in line:
                lines[i] = line.rstrip() + " {#" + ids[0] + "}"
                break
        else:
            warn(f"{page}: <p id=\"{ids[0]}\"> ilman otsikkoa, tunnus katoaa")
        text = "\n".join(lines)
    return text


def hub_questions(page: str) -> str:
    """Etusivun kysymyslista tim/wiki.md-viennistä (viitekappale, ei lähdettä)."""
    text = (HERE / "tim/wiki.md").read_text(encoding="utf-8")
    seg = text.split("RAWTEXjypeliohjeet", 1)[1].split("ENDRAWTEX", 1)[0]
    out = []
    for block in re.split(r"^::: item\s*$", seg, flags=re.M)[1:]:
        block = block.split("\n:::", 1)[0].strip("\n")
        title, rest = block.split("\n", 1)
        out.append(f"## {title.strip()}\n{rest}")
    return "\n\n".join(out)


def convert_page(page: str):
    global current_page
    current_page = page
    docid, pars = parse_page(HTML_DIR / (page.replace("/", "__") + ".html"))
    blocks: list[str] = []
    md: list[str] = []
    highlights: dict[str, dict[int, str]] = {}
    sections: list[tuple[str, list[tuple[str, str, str]]]] = []  # etusivu: (osio, rivit)
    open_details = False

    def add_block(block: str):
        blocks.append(block)
        md.append(PLACEHOLDER % (len(blocks) - 1))

    for p in pars:
        if p["preamble"]:
            continue
        a = p["attrs"]
        if p["plugin"]:
            kind, j = p["plugin"]["type"], p["plugin"]["json"] or {}
            if kind == "timMenu":
                continue
            if kind == "csPlugin":
                before, block = cs_plugin_block(j, page)
                if before and not (md and md[-1].strip() == before.strip()):
                    md.append(before)
                add_block(block)
            elif kind == "showVideo":
                add_block(video_block(j.get("markup", {}), page))
            elif kind == "timTable":
                block = table_block(j, page)
                if block:
                    add_block(block)
            else:
                warn(f"{page}: tuntematon liitännäinen {kind}")
            continue
        if "rd" in a:
            if page == "wiki":
                md.clear()
                md.append(hub_questions(page))
            else:
                warn(f"{page}: viitekappale ohitettu {a}")
            continue
        if "settings" in a:
            highlights.update(parse_settings(get_block(docid, p["id"]).get("text", "")))
            continue
        text = get_block(docid, p["id"]).get("text")
        if text is None:
            warn(f"{page}: kappaleen {p['id']} lähdettä ei saatu")
            continue
        # TIMin kommentit {!!! ... !!!} eivät näy sivulla.
        text, n = re.subn(r"\{!!!.*?!!!\}", "", text, flags=re.S)
        count("TIM-kommentteja pois", n)
        text = MACRO_RE.sub(expand_macro, text)
        lines = text.split("\n")
        if lines and lines[0].startswith("#-"):
            lines = lines[1:]
        text = "\n".join(lines).strip("\n")
        if "area_end" in a:
            if open_details:
                add_block("</details>")
                open_details = False
            if text:
                md.append(text)
            continue
        if "area" in a:
            if a.get("collapse") == "true":
                summary = pandoc(text, "-f", "markdown-smart", "-t", "html").strip()
                summary = re.sub(r"^<p>|</p>$", "", summary).replace("\n", " ") or a["area"]
                add_block(f"<details>\n<summary>{summary}</summary>")
                open_details = True
                continue
        if not text:
            continue
        text = drop_stray_paragraph_tags(text, page)
        if text.startswith('<div style="background'):
            add_block(color_table(text))
        elif text.startswith("<table"):
            add_block(html_table_block(text))
        elif '<pre class="sourceCode' in text and text.startswith("<"):
            add_block(pre_html_block(text))
        else:
            if page == "wiki":
                heading = re.match(r"^## (.+?)\s*$", text, re.M)
                rows = re.findall(r"^\[(.+?)\]\((\S+?)\)[ \t]*(.*?)[ \t]*$", text, re.M)
                if heading and heading.group(1) in SECTION_DIRS:
                    sections.append((heading.group(1), rows))
                    continue
                if rows and sections and not sections[-1][1]:
                    sections[-1][1].extend(rows)
                    continue
            md.append(extract_fences(text, blocks, highlights))
    if open_details:
        add_block("</details>")
        warn(f"{page}: <details> jäi auki")

    raw = "\n\n".join(md)
    for old, new in HEADING_FIXES.get(page, []):
        if old not in raw:
            warn(f"{page}: korjattavaa otsikkoa ei löydy: {old}")
        raw = raw.replace(old, new)
    text = restore_ids(md_to_gfm(protect_ids(raw)))
    text = fence_indented(text, highlights)
    text = soft_breaks(text)
    text = PLACEHOLDER_RE.sub(lambda m: blocks[int(m.group(1))], text)
    text = re.sub(r"^# Jypelin (käyttöohjeet|Dokumentaatio) » ", "# ", text, flags=re.M)
    title = re.search(r"^# (.*?)\s*\{#([^}\s]+)\}\s*$", text, re.M)
    if title and text.index(title.group(0)) == text.find("# "):
        TITLE_IDS.setdefault(page, set()).add(title.group(2))
        text = text.replace(title.group(0), f"# {title.group(1)}", 1)
    if page in MISSING_TITLES:
        if text.startswith("# "):
            warn(f"{page}: MISSING_TITLES, mutta sivulla on otsikko")
        else:
            text = f"# {MISSING_TITLES[page]}\n\n{text}"
            count("otsikko lisätty")
    text = demote_headings(text)
    text = fix_links(text, page)
    for old, new in LINK_FIXES.get(page, []):
        if old not in text:
            warn(f"{page}: korjattavaa linkkiä ei löydy: {old}")
        text = text.replace(old, new)
    # Vanhan trac-wikin tyhjät liitelinkit "[](https://trac.cc.jyu.fi/...)" kuvan
    # perässä: näkymättömiä, kohde ei vastaa. Pois.
    text, n = re.subn(r" ?\[\]\(https://trac\.cc\.jyu\.fi/[^)]*\)", "", text)
    count("trac-tyhjälinkkejä pois", n)
    # Trac-wikin kuvat: palvelin ei vastaa, joten kuva jää kommentiksi ylläpitäjälle.
    text, n = re.subn(r"!\[[^\]]*\]\((https://trac\.cc\.jyu\.fi/[^)]*)\)",
                      lambda m: f"<!-- kuva puuttuu (trac ei vastaa): {m.group(1)} -->", text)
    count("trac-kuvia kommentiksi", n)
    text, n2 = re.subn(r'<img\s+src="(https://trac\.cc\.jyu\.fi/[^"]*)"[^>]*>',
                       lambda m: f"<!-- kuva puuttuu (trac ei vastaa): {m.group(1)} -->", text)
    count("trac-kuvia kommentiksi", n2)
    if page == "wiki":
        text = HUB_INTRO + "\n" + text
    text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
    return text, sections


def heading_ids(text: str) -> set[str]:
    ids = set()
    in_fence = False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*(?:\{#([^}\s]+)\})?\s*$", line)
        if m and not in_fence:
            ids.add(m.group(2) or slug(m.group(1)))
    return ids


def check_anchors(pages_text: dict[str, str]):
    ids = {page: heading_ids(text) for page, text in pages_text.items()}
    for page, text in pages_text.items():
        for target, anchor in re.findall(r"\]\(([^)\s#]*)#([^)\s]+)\)", text):
            if target.startswith("http"):
                continue
            tpage = page if not target else next(
                (p for p in PAGES if md_rel(p) == os.path.normpath(
                    os.path.join(os.path.dirname(md_rel(page)), target))), None)
            if tpage is None:
                continue
            if slug(urllib.parse.unquote(anchor)) not in {slug(i) for i in ids[tpage]}:
                warn(f"{page}: ankkuria #{anchor} ei ole sivulla {tpage}")


def model_games_summary(title: str, listed: set[str]) -> list[str]:
    """Mallipelit SUMMARY.md:hen: päätason osio, pelit alaosioina, vaiheet sivuina."""
    lines = [f" * [{title}](./{md_rel('mallit/alku')})"]
    for game, d, stages in MODEL_GAMES:
        lines.append(f"   * [{game}](./{d}/index.md)")
        for n in range(1, stages + 1):
            target = f"{d}/vaihe{n}"
            if target not in PAGES:
                warn(f"mallipelit: sivua ei ole: {target}")
                continue
            lines.append(f"     * [Vaihe {n}](./{md_rel(target)})")
            listed.add(target)
    return lines


def split_model_games(text: str, pages_text: dict[str, str]) -> tuple[str, dict[str, str]]:
    """mallit/alku: pelien "## <peli>"-osiot omiksi etusivuiksi.
    -> (mallit/index.md, {pelin hakemisto: sen index.md}).

    Etusivulle jää osioiden tilalle linkkiluettelo ennen ensimmäistä
    väliotsikkoa. Pelin sivulla otsikot nousevat tason, linkit ja kuvapolut
    siirtyvät hakemiston mukaan, ja vaiheluettelo (otsikot sivujen H1:stä)
    lisätään, jos osio ei linkitä jokaiseen vaiheeseen.
    """
    lines = text.split("\n")
    headings = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        elif not in_fence and line.startswith("## "):
            headings.append(i)
    remove: set[int] = set()
    game_pages: dict[str, str] = {}
    for game, d, stages in MODEL_GAMES:
        start = next((i for i in headings if lines[i][3:].strip() == game), None)
        if start is None:
            warn(f"mallit/alku: osiota '## {game}' ei ole")
            continue
        end = next((i for i in headings if i > start), len(lines))
        remove.update(range(start, end))
        sub = d.rsplit("/", 1)[-1]
        body = []
        for line in lines[start + 1:end]:
            if re.match(r"^#{3,6} ", line):
                line = line[1:]
            body.append(line.replace(f"]({sub}/", "](").replace("](images/", "](../images/"))
        page = f"# {game}\n\n" + "\n".join(body).strip("\n") + "\n"
        if not all(f"(vaihe{n}.md)" in page for n in range(1, stages + 1)):
            items = []
            for n in range(1, stages + 1):
                h1 = next((l[2:].strip() for l in pages_text.get(f"{d}/vaihe{n}", "").split("\n")
                           if l.startswith("# ")), f"Vaihe {n}")
                h1 = re.sub(rf"^{re.escape(game)}(-peli)?[:,]\s*", "", h1)
                items.append(f"- [{h1}](vaihe{n}.md)")
            page += "\n## Vaiheet\n\n" + "\n".join(items) + "\n"
        game_pages[d] = page
    kept = [l for i, l in enumerate(lines) if i not in remove]
    first = next((i for i, l in enumerate(kept) if l.startswith("## ")), len(kept))
    kept[first:first] = [f"- [{game}]({d.rsplit('/', 1)[-1]}/index.md)"
                         for game, d, _ in MODEL_GAMES if d in game_pages] + [""]
    index = re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip("\n") + "\n"
    return index, game_pages


def write_hub(hub_text: str, sections, pages_text):
    """Etusivu, osioiden etusivut ja SUMMARY.md."""
    (OUT / "index.md").write_text(hub_text, encoding="utf-8")
    summary = ["# Summary", "", "[Etusivu](./index.md)", "", "---", ""]
    listed: set[str] = set()
    for name, rows in sections:
        d = SECTION_DIRS[name]
        index_rel = f"{d}/index.md"
        table = ["| Ohje | Sisältö |", "| --- | --- |"]
        children = []
        for title, target, desc in rows:
            target = target.strip("/")
            if target not in PAGES:
                warn(f"etusivu: osion {name} sivua ei ole: {target}")
                continue
            rel = os.path.relpath(md_rel(target), start=d)
            table.append(f"| [{title}]({rel}) | {desc.strip()} |")
            if target not in listed:
                children.append((title, target))
                listed.add(target)
        for after, title, target in EXTRA_PAGES.get(name, []):
            rel = os.path.relpath(md_rel(target), start=d)
            table.append(f"| [{title}]({rel}) | |")
            pos = next((i for i, (_, t) in enumerate(children) if t == after), len(children) - 1)
            children.insert(pos + 1, (title, target))
            listed.add(target)
        (OUT / index_rel).parent.mkdir(parents=True, exist_ok=True)
        (OUT / index_rel).write_text(f"# {name}\n\n" + "\n".join(table) + "\n", encoding="utf-8")
        summary.append(f" * [{name}](./{index_rel})")
        games = None
        for title, target in children:
            if target == "mallit/alku":
                games = title  # oma päätason osio tämän osion perään
                continue
            summary.append(f"   * [{title}](./{md_rel(target)})")
        if games:
            summary += model_games_summary(games, listed)
            index_text, game_pages = split_model_games(pages_text["mallit/alku"], pages_text)
            (OUT / md_rel("mallit/alku")).write_text(index_text, encoding="utf-8")
            pages_text["mallit/alku"] = index_text
            for d, text in game_pages.items():
                (OUT / d / "index.md").write_text(text, encoding="utf-8")
    summary += ["", "---", "", "[Jypelin päivityshistoria](./paivitysloki.md)"]
    listed.add("paivitysloki")
    missing = [p for p in PAGES if p not in listed and p != "wiki"]
    if missing:
        warn(f"SUMMARY.md:stä puuttuu: {missing}")
    (OUT / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    pages_text: dict[str, str] = {}
    hub_sections = None
    for page in PAGES:  # 1. kierros: sivujen otsikkotunnukset talteen
        convert_page(page)
    stats.clear(); warnings.clear(); fence_infos.clear()
    for page in PAGES:
        text, sections = convert_page(page)
        if page == "wiki":
            hub_sections = sections
            continue
        path = OUT / md_rel(page)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        pages_text[page] = text
        count("sivuja")
    hub_text, _ = convert_page("wiki")
    write_hub(hub_text, hub_sections, pages_text)
    pages_text["wiki"] = hub_text
    check_anchors(pages_text)
    print("aitojen otsikot:", dict(sorted(fence_infos.items(), key=lambda kv: -kv[1])))
    print("tilastot:", dict(sorted(stats.items())))
    print(f"varoituksia {len(warnings)}:")
    for w in warnings:
        print("  " + w)


if __name__ == "__main__":
    main()
