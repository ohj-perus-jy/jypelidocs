/* Sivun aloittaminen/sisallon-tuonti.md animaatiot: Content-kansion luonti
 * Riderissa ja VS Codessa (tyokalut/assets/js/walkthrough.js). Ikkunat ovat
 * yksinkertaistettuja piirroksia; Riderin näkymä on käyttäjän kuvakaappauksen
 * (2026-10) mukainen: Solution-paneeli, projekti Fysiikkapeli, tyhjä editori. */

(window.jyuWalkScenes ??= []).push((ui) => {
  const row = (html, extra = "") => `<span${extra ? ` ${extra}` : ""}>${html}</span>`;
  const cs = '<b style="margin-right:6px;color:#6aab73;font-size:10px">C#</b>';
  const dir = '<i class="jw-icon jw-icon--dir"></i>';
  const dark = "background:#2b2d30;color:#dfe1e5;box-shadow:0 10px 30px rgb(0 0 0 / 50%),0 0 0 1px #43454a";
  const hr = '<hr style="border-top-color:#43454a">';

  /* Vasemman palkin kuvakkeet viivapiirroksina (24 × 24 -ruudukko). */
  const icon = (paths, color, size = 22) =>
    `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="${color}"`
    + ` stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths}</svg>`;
  /* Puun nuoli: auki (alas) tai kiinni (oikealle), ohut viiva kuten
   * VS Coden ja Riderin puissa. Täyte nollaan, koska .jw-ide-list span
   * antaa riveille 8 px:n täytteet, jotka veisivät nuolen tilan. */
  const chevron = (open, color = "#c5c5c5", attrs = "", style = "") =>
    `<span${attrs ? ` ${attrs}` : ""} style="display:inline-flex;flex:none;width:16px;padding:0;margin-right:2px;vertical-align:-3px;color:${color};${style}">`
    + icon(open ? '<path d="M6 9l6 6 6-6"/>' : '<path d="M9 6l6 6-6 6"/>', "currentColor", 14) + "</span>";

  /* Nuoli, joka vaihtuu kiinni olevasta auki olevaksi kohdassa at. Molemmat
   * ovat päällekkäin samassa kiinteän levyisessä kehyksessä, jottei rivin
   * teksti nytkähdä vaihdon aikana (poisto tulee ennen näkyviin tuloa).
   * data-hide ja data-show ovat kääreissä, joilla ei ole omaa display-tyyliä:
   * nuolen inline-flex voittaisi .jw-gone-luokan display: nonen. */
  const chevronOpening = (at, color = "#c5c5c5") =>
    `<span style="position:relative;display:inline-flex;flex:none;width:16px;height:14px;padding:0;margin-right:2px;vertical-align:-3px">`
    + `<span data-hide="${at}" style="position:absolute;left:0;top:0;padding:0">${chevron(false, color, "", "margin:0")}</span>`
    + `<span class="jw-collapse" data-show data-order="${at}" style="position:absolute;left:0;top:0;padding:0">${chevron(true, color, "", "margin:0")}</span>`
    + "</span>";
  /* Rivin pieni kuvake tekstin edessä. */
  const small = (paths, color = "#a8abb2") =>
    `<span style="display:inline-flex;flex:none;padding:0;margin-right:6px;vertical-align:-3px">${icon(paths, color, 14)}</span>`;
  /* Riderin valikon rivi: kuvake (tai tyhjä paikka), teksti ja oikealla
   * pikanäppäin tai alivalikon nuoli. */
  const mi = (paths, label, right = "", extra = "", color = "#a8abb2") =>
    `<div${extra ? ` ${extra}` : ""} style="align-items:center;padding:3px 8px">`
    + `<span style="display:inline-flex;flex:none;width:22px">${paths ? (paths.startsWith("<b") ? paths : icon(paths, color, 14)) : ""}</span>`
    + `${label}${right ? `<span class="jw-sub" style="color:#8c8f96">${right}</span>` : ""}</div>`;
  const ICONS = {
    /* Riderin valikon kuvakkeet. */
    nuget: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>',
    build: '<path d="M4 7h16M8 7v13h8V7M10 4h4v3h-4z"/>',
    debug: '<circle cx="12" cy="13" r="5"/><path d="M12 8V5M7 13H4M20 13h-3M8 9L6 7M16 9l2-2M8 17l-2 2M16 17l2 2"/>',
    file: '<path d="M6 4h8l4 4v12H6z"/><path d="M14 4v4h4M9 12h6M9 16h6"/>',
    /* VS Code: Explorer (kaksi sivua), haku, versionhallinta, aja ja debuggaa, laajennukset. */
    files: '<path d="M9 7V4a1 1 0 0 1 1-1h6l4 4v9a1 1 0 0 1-1 1h-2"/>'
      + '<path d="M6 7h7l4 4v9a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z"/><path d="M13 7v4h4"/>',
    /* Haku kuten VS Codessa: lasi ylhäällä oikealla, kahva alas vasemmalle. */
    search: '<circle cx="14" cy="10" r="6.5"/><path d="M9.5 14.5L3.5 20.5"/>',
    git: '<circle cx="6" cy="5" r="2"/><circle cx="6" cy="19" r="2"/><circle cx="18" cy="8" r="2"/>'
      + '<path d="M6 7v10M18 10c0 5-12 2-12 7"/>',
    run: '<path d="M6 4v16l13-8z"/>',
    extensions: '<path d="M4 9h6v6H4zM10 9h6v6h-6zM4 15h6v6H4z"/><path d="M12 3h6v6h-6z"/>',
    /* Rider: Solution (kansio) ja Structure. */
    folder: '<path d="M3 6a1 1 0 0 1 1-1h5l2 2h9a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>',
    /* Riderin puun rivikuvakkeet: ratkaisu, Dependencies, Scratches and Consoles. */
    solution: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M12 9v11"/>',
    deps: '<circle cx="5" cy="12" r="2.5"/><circle cx="19" cy="12" r="2.5"/><path d="M7.5 12h9"/>',
    scratch: '<path d="M4 6h16M4 11h11M4 16h8"/><circle cx="18" cy="16" r="3"/>',
    structure: '<path d="M4 5h16M4 5v14h16M9 12h11"/>',
  };

  return {
    /* Rider: projekti hiiren oikealla (1), valikko (2), Add (3), alivalikko
     * (4), Directory (5), valikot kiinni ja nimi-ikkuna (6), nimi (7), OK (8),
     * ikkuna kiinni (8.5), Content puussa (9). */
    "rider-kansio": () => ui.window({
      title: "Fysiikkapeli",
      look: "dark",
      body: `
        <div style="display:flex;flex:none;gap:14px;padding:5px 14px;background:#2b2d30;font-size:12px">
          ${["File", "Edit", "View", "Navigate", "Code", "Refactor", "Build", "Run", "Tests", "Tools", "VCS", "Window", "Help"]
            .map((item) => `<span>${item}</span>`).join("")}
        </div>
        <div style="display:grid;flex:1;grid-template-columns:36px 250px minmax(0,1fr);min-height:0;border-top:1px solid #1e1f22">
          <div style="display:flex;flex-direction:column;align-items:center;gap:10px;padding-top:8px;background:#2b2d30;color:#8c8f96">
            <span style="display:flex;padding:4px;border-radius:5px;background:#3574f0">${icon(ICONS.folder, "#fff", 20)}</span>
            <span style="display:flex;padding:4px">${icon(ICONS.structure, "#8c8f96", 20)}</span>
            <span style="font-weight:700;letter-spacing:0.1em">···</span>
          </div>
          <div class="jw-ide-list" style="gap:1px;padding:6px 8px;border-right:1px solid #1e1f22;background:#2b2d30">
            <div style="display:flex;align-items:center;gap:6px;margin:0 0 6px;padding:2px 4px;font-size:13px;font-weight:600">
              Solution ${chevron(true, "#8c8f96")}
              <span style="margin-left:auto;color:#8c8f96;letter-spacing:0.2em">⌕ ⊕ ⋮ —</span></div>
            ${row(`${chevron(true, "#8c8f96")}${small(ICONS.solution)}Fysiikkapeli <span style="color:#8c8f96">· 1 project</span>`)}
            ${row(`${chevron(true, "#8c8f96")}${cs}Fysiikkapeli`, 'style="padding-left:20px" data-click data-wait="700" data-on="jw-sel" data-order="1"')}
            ${row(`${chevron(false, "#8c8f96")}${small(ICONS.deps)}Dependencies`, 'style="padding-left:36px"')}
            ${row(`${chevron(false, "#8c8f96")}${dir}Content`, 'style="padding-left:36px" class="jw-collapse" data-show data-order="9" data-ring')}
            ${row(`${cs}Fysiikkapeli.cs`, 'style="padding-left:48px"')}
            ${row(`${cs}Ohjelma.cs`, 'style="padding-left:48px"')}
            ${row(`${chevron(false, "#8c8f96")}${small(ICONS.scratch)}Scratches and Consoles`)}
          </div>
          <div style="display:flex;flex-direction:column;justify-content:center;gap:8px;padding:0 0 0 110px;background:#1e1f22;color:#6f737a;font-size:13px">
            <span>Search Everywhere <b style="color:#8c8f96">Double Shift</b></span>
            <span>Go to File <b style="color:#8c8f96">Ctrl+P</b></span>
            <span>Recent Files <b style="color:#8c8f96">Ctrl+E</b></span>
            <span>Navigation Bar <b style="color:#8c8f96">Alt+Home</b></span>
            <span>Drop files here to open them</span>
          </div>
        </div>
        <div class="jw-menu" style="top:150px;left:120px;width:250px;padding:6px;${dark}" data-show data-order="2" data-hide="6">
          ${mi("", "Add", "›", 'data-click data-wait="700" data-on="jw-hover" data-order="3"')}
          ${mi(ICONS.nuget, "Manage NuGet Packages")}
          ${mi("", "Unload Project")}
          ${mi("", "Reload Project")}
          ${mi("", "Entity Framework Core", "›")}
          ${hr}
          ${mi(ICONS.build, "Build Selected Projects")}
          ${mi(ICONS.run, "Run 'Fysiikkapeli'", "Ctrl+Shift+F10", "", "#5fb865")}
          ${mi(ICONS.debug, "Debug 'Fysiikkapeli'", "", "", "#5fb865")}
          ${hr}
          ${mi("", "Properties...", "Ctrl+.")}
        </div>
        <div class="jw-menu" style="top:150px;left:372px;width:230px;padding:6px;${dark}" data-show data-order="4" data-hide="6">
          ${mi(cs, "Class/Interface")}
          ${mi(ICONS.folder, "Directory", "", 'data-click data-wait="700" data-on="jw-hover" data-order="5"')}
          ${mi(ICONS.file, "File")}
          ${mi(ICONS.file, "Scratch File", "Ctrl+Alt+Shift+Insert")}
          ${mi("", "Reference...")}
          ${mi("", "Existing Item...")}
          ${hr}
          ${mi("", "More File Templates", "›")}
        </div>
        <div class="jw-dialog" style="top:170px;left:250px;width:300px;${dark}" data-show data-order="6" data-hide="8.5">
          <div class="jw-dialog-body">
            <h5 style="font-size:14px">New Directory</h5>
            <div class="jw-label" style="margin-top:8px;color:#8c8f96">Enter new directory name:</div>
            <div class="jw-input" style="border-color:#3574f0;background:#1e1f22;color:#dfe1e5" data-type data-order="7">Content</div>
            <div style="display:flex;justify-content:flex-end;gap:8px;margin-top:14px">
              <span class="jw-btn" style="border-color:#4e5157;background:#3c3f44;color:#dfe1e5">Cancel</span>
              <span class="jw-btn jw-btn--primary" style="border-color:#3574f0;background:#3574f0;color:#fff" data-click data-wait="700" data-order="8">OK</span>
            </div>
          </div>
        </div>`,
    }),

    /* VS Code (Dark Modern, käyttäjän kuvakaappaus 2026-10): työtilan
     * juuressa ratkaisun kansio Fysiikkapeli ja Fysiikkapeli.sln, projektin
     * kansio Fysiikkapeli niiden sisällä, aluksi kiinni. Kansio hiiren
     * oikealla (1), valikko (2), New Folder... (3), valikko kiinni (3.5),
     * kansio aukeaa ja nimikenttä tulee puuhun (4), nimi (5), kenttä pois ja
     * Content puussa (6). Kansiota ei avata erikseen: VS Code avaa sen itse. */
    "vscode-kansio": () => {
      const sub = 'style="padding-left:40px"';
      const file = (name, icon, extra = sub) =>
        `<span ${extra}><b style="margin-right:6px;color:${icon};font-size:10px">${
          name.endsWith(".csproj") ? "⚙" : name.endsWith(".sln") ? "≡" : "C#"}</b>${name}</span>`;
      return ui.window({
        title: "Fysiikkapeli - Visual Studio Code",
        look: "dark",
        body: `
          <div style="display:flex;flex:none;gap:14px;padding:5px 14px;background:#181818;font-size:12px;color:#ccc">
            ${["File", "Edit", "Selection", "View", "Go", "Run", "Terminal", "Help"]
              .map((item) => `<span>${item}</span>`).join("")}
          </div>
          <div style="display:grid;flex:1;grid-template-columns:40px 230px minmax(0,1fr);min-height:0;background:#1f1f1f">
            <div style="display:flex;flex-direction:column;align-items:center;gap:12px;padding-top:6px;background:#181818;border-right:1px solid #2b2b2b">
              <span style="display:flex;padding:4px 6px;border-left:2px solid #d7d7d7;margin-right:2px">${icon(ICONS.files, "#d7d7d7")}</span>
              <span style="display:flex;padding:4px 8px">${icon(ICONS.search, "#868686")}</span>
              <span style="display:flex;padding:4px 8px">${icon(ICONS.git, "#868686")}</span>
              <span style="display:flex;padding:4px 8px">${icon(ICONS.run, "#868686")}</span>
              <span style="display:flex;padding:4px 8px">${icon(ICONS.extensions, "#868686")}</span>
            </div>
            <div class="jw-ide-list" style="gap:0;padding:0;background:#181818;border-right:1px solid #2b2b2b;color:#ccc">
              <div style="display:flex;padding:8px 14px;color:#bbb;font-size:12px;font-weight:600">Explorer<span style="margin-left:auto">···</span></div>
              <span style="padding:2px 6px;font-weight:700">${chevron(true)}Fysiikkapeli</span>
              <span style="padding-left:24px" data-click data-wait="700" data-on="jw-sel" data-order="1">${chevronOpening(4)}Fysiikkapeli</span>
              <div class="jw-collapse" style="display:flex;flex-direction:column" data-show data-order="4">
              <span ${sub}>${chevron(false)}bin</span>
              <span class="jw-collapse" style="margin:2px 6px 2px 38px;padding:1px 4px;border:1px solid #0078d4;background:#313131;min-height:18px" data-show data-order="4" data-hide="6"><span data-type data-order="5">Content</span></span>
              <span class="jw-collapse" style="padding-left:40px" data-show data-order="6" data-ring>${chevron(false)}Content</span>
              <span ${sub}>${chevron(false)}obj</span>
              ${file("Fysiikkapeli.cs", "#6aab73")}
              ${file("Fysiikkapeli.csproj", "#e37933")}
              ${file("Ohjelma.cs", "#6aab73")}
              </div>
              ${file("Fysiikkapeli.sln", "#ccc", 'style="padding-left:24px"')}
            </div>
            <div style="display:flex;align-items:flex-end;justify-content:center;padding-bottom:50px;color:#5a5a5a;font-size:12px">
              <div style="text-align:right;line-height:2">Open Chat <b style="color:#888">Ctrl+Alt+I</b><br>
                Show All Commands <b style="color:#888">Ctrl+Shift+P</b><br>
                Find in Files <b style="color:#888">Ctrl+Shift+F</b></div>
            </div>
          </div>
          <div class="jw-menu" style="top:150px;left:130px;width:230px;background:#1f1f1f;color:#ccc;box-shadow:0 8px 24px rgb(0 0 0 / 50%),0 0 0 1px #454545;font-size:12px" data-show data-order="2" data-hide="3.5">
            <div>New File...</div>
            <div data-click data-wait="700" data-on="jw-hover" data-order="3">New Folder...</div>
            <hr style="border-top-color:#454545">
            <div>Reveal in File Explorer<span class="jw-sub" style="color:#888">Shift+Alt+R</span></div>
            <div>Open in Integrated Terminal</div>
            <hr style="border-top-color:#454545">
            <div>Find in Folder...<span class="jw-sub" style="color:#888">Shift+Alt+F</span></div>
            <hr style="border-top-color:#454545">
            <div>Cut<span class="jw-sub" style="color:#888">Ctrl+X</span></div>
            <div>Copy<span class="jw-sub" style="color:#888">Ctrl+C</span></div>
            <div>Paste<span class="jw-sub" style="color:#888">Ctrl+V</span></div>
            <hr style="border-top-color:#454545">
            <div>Copy Path<span class="jw-sub" style="color:#888">Shift+Alt+C</span></div>
            <div>Copy Relative Path<span class="jw-sub" style="color:#888">Ctrl+K Ctrl+Shift+C</span></div>
            <hr style="border-top-color:#454545">
            <div>Rename...<span class="jw-sub" style="color:#888">F2</span></div>
            <div>Delete<span class="jw-sub" style="color:#888">Delete</span></div>
          </div>`,
      });
    },
  };
});
