# TIM-tuonti

Kertaluontoinen tuonti TIMin Jypeli-wikistä (`kurssit/jypeli/*`) `src/`-puuksi.
Ajettu 16.9.2026. Skriptit olettavat välimuistihakemistot työhakemistossaan:

| Skripti          | Tekee                                                              |
| ---------------- | ------------------------------------------------------------------ |
| `fetch_html.py`  | sivujen HTML-näkymät → `timhtml/` (sivulista `tim/`-viennistä)     |
| `fetch_pars.py`  | kappaleiden raaka Markdown TIMin `getBlock`-rajapinnasta → `timpars/` |
| `fetch_files.py` | kuvat ja videot → `timfiles/`                                      |
| `tim2md.py`      | kokoaa sivut, kääntää pandocilla GFM:ksi ja kirjoittaa `src/`      |
| `timlib.py`      | HTML:n kappalelistan jäsennys ja `getBlock`-välimuisti             |

`tim2md.py` tarvitsee pandocin (`pip install pypandoc_binary` ja polku
`PANDOC`-vakioon). Sivuluettelo kerättiin wikin etusivulta seuraamalla
kaikkia `kurssit/jypeli/`-linkkejä (myös suhteelliset) sekä etusivun
timTable-taulukon linkkiä `paivitysloki`. Kun wiki muuttuu, helpoin tapa
on ajaa tuonti uudelleen tyhjään hakemistoon ja verrata `src/`-diffiä.
