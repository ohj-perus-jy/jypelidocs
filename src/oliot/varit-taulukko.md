<!-- Jypelin valmiit värit (Jypeli/Graphics/Color.cs). Ei oma sivu
     (kirja.toml: ei_sivuja), vaan liitetään {{#include}}-makrolla sivuille
     oliot/ulkonako.md ja kentat/ruutukentta.md. -->

<style>
/* Solut eivät rivity: kapealla näytöllä taulukkoa vieritetään vaakasuunnassa.
 * Keskitys pystysuunnassa, jotta suurennettu näyte ylittää rivirajat tasaisesti. */
.varit td { white-space: nowrap; vertical-align: middle; }
/* Näytesarakkeeseen tilaa suurennukselle, ettei se peitä nimeä. */
.varit td:has(> .varinayte) { padding-right: 2.8rem; }
/* Värinäyte; väri tulee muuttujasta --c. */
.varinayte {
  display: inline-block;
  position: relative;
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  background: var(--c);
  border: 1px solid color-mix(in srgb, var(--md-default-fg-color) 35%, transparent);
  border-radius: .2em;
  transform-origin: left center;
  transition: transform .2s ease-out, box-shadow .2s ease-out;
}
.varinayte-lapi {
  background: repeating-conic-gradient(#bbb 0 25%, #fff 0 50%) 0 0 / .75em .75em;
}
/* Hiiri näytteen tai sen nimen päällä: näyte ponnahtaa kolminkertaiseksi
 * rivirajojen yli. Kasvu lähtee vasemmasta reunasta, jotta se ei työnny
 * taulukon reunan yli. Varjo on neutraali, ei värin hehku. */
.varit td:hover > .varinayte,
.varit td:has(+ td:hover) > .varinayte {
  transform: scale(3);
  z-index: 1;
  border-color: color-mix(in srgb, var(--md-default-fg-color) 60%, transparent);
  box-shadow: 0 .15em .5em rgba(0, 0, 0, .35);
}
@media (prefers-reduced-motion: reduce) {
  .varinayte { transition: none; }
}
/* Klikkaus kopioi nimen (skripti alla); osoitin kertoo sen. */
.varit-kopioi td:has(> .varinayte), .varit-kopioi td:has(> code) { cursor: pointer; }
/* Kuittaus nimisolun sisään nimen yläpuolelle, jotta se vierii sivun mukana:
 * aksenttivärinen pilleri kuten koodilohkon kopiointinapilla
 * (tyokalut/assets/css/copy.css). */
.varit td { position: relative; }
.varit-kuittaus {
  position: absolute;
  left: .6rem;
  bottom: calc(100% - .5rem);
  z-index: 2;
  padding: .3em .8em;
  font-family: var(--md-text-font-family);
  font-size: .8rem;
  line-height: 1.4;
  color: var(--md-default-bg-color);
  white-space: nowrap;
  pointer-events: none;
  background-color: var(--md-accent-fg-color);
  border-radius: 1em;
  box-shadow: 0 .15rem .35rem #00000029;
  visibility: hidden;
  opacity: 0;
  transition: opacity .25s, visibility 0s .25s;
}
.varit-kuittaus--shown {
  visibility: visible;
  opacity: 1;
  transition: opacity .25s, visibility 0s;
}
</style>

<details>
<summary>Jypelin valmiit värit</summary>

<div class="varit" markdown="1">

| | Nimi ja RGB-arvo | | Nimi ja RGB-arvo |
| --- | --- | --- | --- |
| <span class="varinayte" style="--c:#00ffff" aria-hidden="true"></span> | `Aqua`<br><small>0, 255, 255</small> | <span class="varinayte" style="--c:#e0ffff" aria-hidden="true"></span> | `LightCyan`<br><small>224, 255, 255</small> |
| <span class="varinayte" style="--c:#7fffd4" aria-hidden="true"></span> | `Aquamarine`<br><small>127, 255, 212</small> | <span class="varinayte" style="--c:#d3d3d3" aria-hidden="true"></span> | `LightGray`<br><small>211, 211, 211</small> |
| <span class="varinayte" style="--c:#b2beb5" aria-hidden="true"></span> | `AshGray`<br><small>178, 190, 181</small> | <span class="varinayte" style="--c:#90ee90" aria-hidden="true"></span> | `LightGreen`<br><small>144, 238, 144</small> |
| <span class="varinayte" style="--c:#0094ff" aria-hidden="true"></span> | `Azure`<br><small>0, 148, 255</small> | <span class="varinayte" style="--c:#ffb6c1" aria-hidden="true"></span> | `LightPink`<br><small>255, 182, 193</small> |
| <span class="varinayte" style="--c:#f5f5dc" aria-hidden="true"></span> | `Beige`<br><small>245, 245, 220</small> | <span class="varinayte" style="--c:#ffffe0" aria-hidden="true"></span> | `LightYellow`<br><small>255, 255, 224</small> |
| <span class="varinayte" style="--c:#000000" aria-hidden="true"></span> | `Black`<br><small>0, 0, 0</small> | <span class="varinayte" style="--c:#00ff00" aria-hidden="true"></span> | `Lime`<br><small>0, 255, 0</small> |
| <span class="varinayte" style="--c:#7f0037" aria-hidden="true"></span> | `BloodRed`<br><small>127, 0, 55</small> | <span class="varinayte" style="--c:#32cd32" aria-hidden="true"></span> | `LimeGreen`<br><small>50, 205, 50</small> |
| <span class="varinayte" style="--c:#0000ff" aria-hidden="true"></span> | `Blue`<br><small>0, 0, 255</small> | <span class="varinayte" style="--c:#ff00ff" aria-hidden="true"></span> | `Magenta`<br><small>255, 0, 255</small> |
| <span class="varinayte" style="--c:#6699cc" aria-hidden="true"></span> | `BlueGray`<br><small>102, 153, 204</small> | <span class="varinayte" style="--c:#800000" aria-hidden="true"></span> | `Maroon`<br><small>128, 0, 0</small> |
| <span class="varinayte" style="--c:#00ff21" aria-hidden="true"></span> | `BrightGreen`<br><small>0, 255, 33</small> | <span class="varinayte" style="--c:#0000cd" aria-hidden="true"></span> | `MediumBlue`<br><small>0, 0, 205</small> |
| <span class="varinayte" style="--c:#7f3300" aria-hidden="true"></span> | `Brown`<br><small>127, 51, 0</small> | <span class="varinayte" style="--c:#9370db" aria-hidden="true"></span> | `MediumPurple`<br><small>147, 112, 219</small> |
| <span class="varinayte" style="--c:#5b7f00" aria-hidden="true"></span> | `BrownGreen`<br><small>91, 127, 0</small> | <span class="varinayte" style="--c:#48d1cc" aria-hidden="true"></span> | `MediumTurquoise`<br><small>72, 209, 204</small> |
| <span class="varinayte" style="--c:#36454f" aria-hidden="true"></span> | `Charcoal`<br><small>54, 69, 79</small> | <span class="varinayte" style="--c:#c71585" aria-hidden="true"></span> | `MediumVioletRed`<br><small>199, 21, 133</small> |
| <span class="varinayte" style="--c:#dc143c" aria-hidden="true"></span> | `Crimson`<br><small>220, 20, 60</small> | <span class="varinayte" style="--c:#21007f" aria-hidden="true"></span> | `MidnightBlue`<br><small>33, 0, 127</small> |
| <span class="varinayte" style="--c:#00ffff" aria-hidden="true"></span> | `Cyan`<br><small>0, 255, 255</small> | <span class="varinayte" style="--c:#3eb489" aria-hidden="true"></span> | `Mint`<br><small>62, 180, 137</small> |
| <span class="varinayte" style="--c:#004a7f" aria-hidden="true"></span> | `DarkAzure`<br><small>0, 74, 127</small> | <span class="varinayte" style="--c:#000080" aria-hidden="true"></span> | `Navy`<br><small>0, 0, 128</small> |
| <span class="varinayte" style="--c:#00137f" aria-hidden="true"></span> | `DarkBlue`<br><small>0, 19, 127</small> | <span class="varinayte" style="--c:#7f6a00" aria-hidden="true"></span> | `Olive`<br><small>127, 106, 0</small> |
| <span class="varinayte" style="--c:#5c4033" aria-hidden="true"></span> | `DarkBrown`<br><small>92, 64, 51</small> | <span class="varinayte" style="--c:#ff6a00" aria-hidden="true"></span> | `Orange`<br><small>255, 106, 0</small> |
| <span class="varinayte" style="--c:#007f7f" aria-hidden="true"></span> | `DarkCyan`<br><small>0, 127, 127</small> | <span class="varinayte" style="--c:#ff4500" aria-hidden="true"></span> | `OrangeRed`<br><small>255, 69, 0</small> |
| <span class="varinayte" style="--c:#007f0e" aria-hidden="true"></span> | `DarkForestGreen`<br><small>0, 127, 14</small> | <span class="varinayte" style="--c:#0026ff" aria-hidden="true"></span> | `PaintDotNetBlue`<br><small>0, 38, 255</small> |
| <span class="varinayte" style="--c:#404040" aria-hidden="true"></span> | `DarkGray`<br><small>64, 64, 64</small> | <span class="varinayte" style="--c:#ff00dc" aria-hidden="true"></span> | `PaintDotNetMagenta`<br><small>255, 0, 220</small> |
| <span class="varinayte" style="--c:#006400" aria-hidden="true"></span> | `DarkGreen`<br><small>0, 100, 0</small> | <span class="varinayte" style="--c:#ffc0cb" aria-hidden="true"></span> | `Pink`<br><small>255, 192, 203</small> |
| <span class="varinayte" style="--c:#007f46" aria-hidden="true"></span> | `DarkJungleGreen`<br><small>0, 127, 70</small> | <span class="varinayte" style="--c:#7f006e" aria-hidden="true"></span> | `Purple`<br><small>127, 0, 110</small> |
| <span class="varinayte" style="--c:#7f006e" aria-hidden="true"></span> | `DarkMagenta`<br><small>127, 0, 110 (= Purple)</small> | <span class="varinayte" style="--c:#ff0000" aria-hidden="true"></span> | `Red`<br><small>255, 0, 0</small> |
| <span class="varinayte" style="--c:#7f3300" aria-hidden="true"></span> | `DarkOrange`<br><small>127, 51, 0 (= Brown)</small> | <span class="varinayte" style="--c:#ff006e" aria-hidden="true"></span> | `Rose`<br><small>255, 0, 110</small> |
| <span class="varinayte" style="--c:#7f0000" aria-hidden="true"></span> | `DarkRed`<br><small>127, 0, 0</small> | <span class="varinayte" style="--c:#fbcce7" aria-hidden="true"></span> | `RosePink`<br><small>251, 204, 231</small> |
| <span class="varinayte" style="--c:#00ced1" aria-hidden="true"></span> | `DarkTurquoise`<br><small>0, 206, 209</small> | <span class="varinayte" style="--c:#e0115f" aria-hidden="true"></span> | `Ruby`<br><small>224, 17, 95</small> |
| <span class="varinayte" style="--c:#57007f" aria-hidden="true"></span> | `DarkViolet`<br><small>87, 0, 127</small> | <span class="varinayte" style="--c:#fa8072" aria-hidden="true"></span> | `Salmon`<br><small>250, 128, 114</small> |
| <span class="varinayte" style="--c:#7f6a00" aria-hidden="true"></span> | `DarkYellow`<br><small>127, 106, 0 (= Olive)</small> | <span class="varinayte" style="--c:#2e8b57" aria-hidden="true"></span> | `SeaGreen`<br><small>46, 139, 87</small> |
| <span class="varinayte" style="--c:#5b7f00" aria-hidden="true"></span> | `DarkYellowGreen`<br><small>91, 127, 0 (= BrownGreen)</small> | <span class="varinayte" style="--c:#c0c0c0" aria-hidden="true"></span> | `Silver`<br><small>192, 192, 192</small> |
| <span class="varinayte" style="--c:#50c878" aria-hidden="true"></span> | `Emerald`<br><small>80, 200, 120</small> | <span class="varinayte" style="--c:#87ceeb" aria-hidden="true"></span> | `SkyBlue`<br><small>135, 206, 235</small> |
| <span class="varinayte" style="--c:#267f00" aria-hidden="true"></span> | `ForestGreen`<br><small>38, 127, 0</small> | <span class="varinayte" style="--c:#6a5acd" aria-hidden="true"></span> | `SlateBlue`<br><small>106, 90, 205</small> |
| <span class="varinayte" style="--c:#ff00ff" aria-hidden="true"></span> | `Fuchsia`<br><small>255, 0, 255</small> | <span class="varinayte" style="--c:#708090" aria-hidden="true"></span> | `SlateGray`<br><small>112, 128, 144</small> |
| <span class="varinayte" style="--c:#ffd800" aria-hidden="true"></span> | `Gold`<br><small>255, 216, 0</small> | <span class="varinayte" style="--c:#fffafa" aria-hidden="true"></span> | `Snow`<br><small>255, 250, 250</small> |
| <span class="varinayte" style="--c:#808080" aria-hidden="true"></span> | `Gray`<br><small>128, 128, 128</small> | <span class="varinayte" style="--c:#00ff90" aria-hidden="true"></span> | `SpringGreen`<br><small>0, 255, 144</small> |
| <span class="varinayte" style="--c:#008000" aria-hidden="true"></span> | `Green`<br><small>0, 128, 0</small> | <span class="varinayte" style="--c:#008080" aria-hidden="true"></span> | `Teal`<br><small>0, 128, 128</small> |
| <span class="varinayte" style="--c:#adff2f" aria-hidden="true"></span> | `GreenYellow`<br><small>173, 255, 47</small> | <span class="varinayte varinayte-lapi" aria-hidden="true"></span> | `Transparent`<br><small>läpinäkyvä</small> |
| <span class="varinayte" style="--c:#4800ff" aria-hidden="true"></span> | `HanPurple`<br><small>72, 0, 255</small> | <span class="varinayte" style="--c:#40e0d0" aria-hidden="true"></span> | `Turquoise`<br><small>64, 224, 208</small> |
| <span class="varinayte" style="--c:#4cff00" aria-hidden="true"></span> | `Harlequin`<br><small>76, 255, 0</small> | <span class="varinayte" style="--c:#120a8f" aria-hidden="true"></span> | `Ultramarine`<br><small>18, 10, 143</small> |
| <span class="varinayte" style="--c:#ff69b4" aria-hidden="true"></span> | `HotPink`<br><small>255, 105, 180</small> | <span class="varinayte" style="--c:#b200ff" aria-hidden="true"></span> | `Violet`<br><small>178, 0, 255</small> |
| <span class="varinayte" style="--c:#fffff0" aria-hidden="true"></span> | `Ivory`<br><small>255, 255, 240</small> | <span class="varinayte" style="--c:#f5deb3" aria-hidden="true"></span> | `Wheat`<br><small>245, 222, 179</small> |
| <span class="varinayte" style="--c:#29ab87" aria-hidden="true"></span> | `JungleGreen`<br><small>41, 171, 135</small> | <span class="varinayte" style="--c:#ffffff" aria-hidden="true"></span> | `White`<br><small>255, 255, 255</small> |
| <span class="varinayte" style="--c:#dcd0ff" aria-hidden="true"></span> | `Lavender`<br><small>220, 208, 255</small> | <span class="varinayte" style="--c:#ffff00" aria-hidden="true"></span> | `Yellow`<br><small>255, 255, 0</small> |
| <span class="varinayte" style="--c:#add8e6" aria-hidden="true"></span> | `LightBlue`<br><small>173, 216, 230</small> | <span class="varinayte" style="--c:#b6ff00" aria-hidden="true"></span> | `YellowGreen`<br><small>182, 255, 0</small> |

</div>

</details>

<script>
/* Värin nimen kopiointi: näytteen tai nimen klikkaus kopioi "Color.Nimi"
 * leikepöydälle ja kuittaa sen pillerillä klikkauskohdan vieressä. Ilman
 * leikepöytärajapintaa (http muualla kuin localhostissa) ei tehdä mitään. */
(() => {
  "use strict";
  if (!navigator.clipboard?.writeText) return;
  const SHOWN_MS = 2000;
  let note;
  /* Pilleri siirretään klikatun nimen soluun, joten se vierii sivun mukana. */
  const notify = (cell, message) => {
    if (!note) {
      note = document.createElement("div");
      note.className = "varit-kuittaus";
      note.setAttribute("role", "status");
    }
    cell.append(note);
    note.textContent = message;
    note.classList.add("varit-kuittaus--shown");
    clearTimeout(note.timer);
    note.timer = setTimeout(
      () => note.classList.remove("varit-kuittaus--shown"), SHOWN_MS);
  };
  document.querySelectorAll(".varit").forEach((table) => {
    table.classList.add("varit-kopioi");
    table.addEventListener("click", async (event) => {
      const cell = event.target.closest("td");
      if (!cell) return;
      const code = cell.querySelector(":scope > code")
        ?? cell.nextElementSibling?.querySelector(":scope > code");
      if (!code) return;
      const name = "Color." + code.textContent.trim();
      try {
        await navigator.clipboard.writeText(name);
        notify(code.parentElement, "Kopioitu " + name);
      } catch {
        notify(code.parentElement, "Kopiointi ei onnistunut");
      }
    });
  });
})();
</script>
