import re, html, json, base64, pathlib, urllib.request
ATTR_RE = re.compile(r'\s([\w-]+)=(?:"([^"]*)"|\'([^\']*)\')')
PAR_RE = re.compile(r'<div class="par(?P<cls>[^"]*)"(?P<rest>[^>]*)>')
LOADER_RE = re.compile(r'<tim-plugin-loader[^>]*plugin-type="(?P<type>[^"]*)"[^>]*>(?P<inner>.*?)</tim-plugin-loader>', re.S)
def parse_page(fn):
    s = pathlib.Path(fn).read_text(encoding='utf-8')
    docid = re.search(r'"src_docid": (\d+)', s).group(1)
    body = s[s.find('id="pars"'):]
    pars = []
    matches = list(PAR_RE.finditer(body))
    for i, m in enumerate(matches):
        raw = {k: (v1 or v2) for k, v1, v2 in ATTR_RE.findall(m.group('rest'))}
        end = matches[i+1].start() if i+1 < len(matches) else len(body)
        chunk = body[m.end():end]
        plugin = None
        lm = LOADER_RE.search(chunk)
        if lm:
            plugin = {'type': lm.group('type').strip('/'), 'json': None}
            jm = re.search(r'json=(?:"([^"]*)"|\'([^\']*)\')', lm.group('inner'))
            if jm:
                j = html.unescape(jm.group(1) or jm.group(2))
                try:
                    plugin['json'] = json.loads(base64.b64decode(j).decode('utf-8'))
                except Exception:
                    try: plugin['json'] = json.loads(j)
                    except Exception as e: plugin['json'] = {'err': str(e)}
        pars.append({'id': raw.get('id'), 'cls': m.group('cls').split(), 'attrs': json.loads(html.unescape(raw.get('attrs', '{}'))),
                     'preamble': 'data-from-preamble' in raw, 'plugin': plugin, 'raw': raw, 'html': chunk})
    return docid, pars
CACHE = pathlib.Path('timpars')
def get_block(docid, pid):
    f = CACHE / docid / (pid + '.json'); 
    if f.exists(): return json.loads(f.read_text(encoding='utf-8'))
    f.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(f'https://tim.jyu.fi/getBlock/{docid}/{pid}', timeout=60) as r: d = json.load(r)
    except urllib.error.HTTPError as e: d = {'error': e.code}
    f.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8'); return d
