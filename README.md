# Jypeli-ohjeet

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Jypeli-pelikirjaston käyttöohjeet aiheittain. Sivusto on katseltavissa
osoitteessa <https://ohj-perus-jy.github.io/jypelidocs/>.

Ohjeet on tuotu [TIMin Jypeli-wikistä](https://tim.jyu.fi/view/kurssit/jypeli/wiki)
(tuonti 16.9.2026, ks. [tools/tim-tuonti/](tools/tim-tuonti/)). Lähdepuu on
`src/`, ja se on samaa Markdown-murretta kuin
[Ohjelmointi 1:n materiaali](https://github.com/ohj-perus-jy/ohj1):
koodilohkot ` ```csharp,ignore ` ja ` ```csharp,feature-jypeli ` (ajonappi,
joka näyttää pelin ikkunan kuvana), piilorivit `//-`, korostukset
`// HIGHLIGHT_GREEN_BEGIN` … `_END`, huomautukset `> [!HUOMAUTUS]`,
navigaatio `src/SUMMARY.md`:ssä.

Rakenteen kehitystyön tila ja suunnitelma: [TODO.md](TODO.md).

## Sivuston kehittäminen omalla koneella

Sivusto rakennetaan **Zensicalilla** (`zensical/`, sama työkalu kuin ohj1:ssä
ja ohj2:ssa). Suositeltu tapa on mukana oleva DevContainer, joka asentaa
tarvittavan (`zensical/setup.sh`) avatessa. Ilman DevContaineria riittää
Python 3.11 ja `./zensical/setup.sh`.

Kehityspalvelin, joka seuraa `src/`-puun muutoksia:

```bash
./zensical/run.sh            # http://localhost:8001
./zensical/run.sh build      # pelkkä rakennus zensical/site/-hakemistoon
./zensical/run.sh test       # testit (pytest + Playwright)
```

**Muokattava puu on `src/`, ei `zensical/docs/`**, joka on `convert.py`:n
kertakäyttöinen kopio. Työkalun ohjeet ja perustelut: [zensical/README.md](zensical/README.md).

## Haarat ja julkaisu

`main` on tuotanto (sivuston juuri), `dev` on työhaara, jonka esikatselu
julkaistaan polkuun `/dev/`. Molemmat rakennetaan jokaisella pushilla
(`.github/workflows/pages.yml`), joten `dev`-haaran on oltava olemassa
GitHubissa ja `github-pages`-ympäristön sallittava se. Julkaisu `dev` →
`main` tehdään PR:llä merge-committina, ja heti perään `main` → `dev`.

## Tuonnin tila ja tunnetut puutteet

Tuonti (`tools/tim-tuonti/tim2md.py`) lukee TIMin sivujen kappaleet
sellaisenaan ja kääntää ne pandocilla; liitännäiset (csPlugin, showVideo,
timTable) kootaan sivun HTML-näkymän tiedoista. Tuonnin jälkeen tarkistettu:
`zensical build` ilman varoituksia, kaikki 22 ajonapillista esimerkkiä
palauttavat kuvan suorituspalvelimelta. Käsin katsottavaa jäi:

- **Vanhan trac-wikin linkit** (`trac.cc.jyu.fi`, 52 kpl) eivät vastaa; sama
  TIMissä. Tyhjät liitelinkit kuvien perässä on poistettu, mutta viisi kuvaa
  (`animaatio.md`, `pistelaskuri.md`, `ohjainten-lisays.md`) osoittaa yhä
  traciin eikä näy.
- Ajonapit on annettu vain kokonaisille ohjelmille, jotka eivät lataa
  sisältötiedostoja (`LoadImage` ym.); csPlugin-esimerkkien kehyskoodi on
  piiloriveinä (`//-`). Pong-oppaan koodilohkoihin on lisätty piilotetut
  `using`-rivit, jotta ne voi ajaa.
- TIMin sivukohtaiset `# `-otsikot on laskettu asteella alemmas, jotta
  sivulla on yksi H1; TIMissä rikki olleet ankkurit `#taustakuva` ja
  `#1wdXts95Twpe` on korjattu (`HEADING_FIXES`, `LINK_FIXES`).
- Videot ovat `images/`-kansioissa (`<video>`), YouTube-videot linkkeinä.

## Ongelmista ilmoittaminen

Avaa [issue](https://github.com/ohj-perus-jy/jypelidocs/issues/new/choose)
tai ehdota muutosta sivun alareunan "Ehdota muutosta" -linkistä.

## Lisenssi

Materiaali on lisensoitu [CC BY-SA 4.0][cc-by-sa] -lisenssillä.

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/deed.fi
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
