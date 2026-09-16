# Jypeli-ohjeiden rakenteen parantaminen

Tavoite: sivustosta aloittelijalle ystävällinen pelikirjaston dokumentaatio,
jossa on selvä polku (asennus → ensimmäinen peli → opas → ohjeet aiheittain),
vähemmän ylätason osioita ja toisiinsa linkittyvät sivut. Tausta-analyysi
alempana kohdassa "Havainnot".

Merkinnät: `[x]` tehty, `[ ]` tekemättä, `[~]` osittain.

## 1. Nopeat mekaaniset korjaukset

- [x] Nimeä tutoriaalien vaiheet valikossa ja sivujen otsikoissa
      ("Vaihe 2: Pallo liikkeelle" eikä "Vaihe 2").
- [x] Korjaa `perusteet/projektin-luonti.md`: tyhjä koodilohko, katkennut
      polku "C:", ja "takaisin pong-tutoriaaliin" -linkki, joka olettaa
      lukijan tulleen Pongista.
- [x] Poista asennus- ja projektinluontiohjeiden kopio `mallit/index.md`:stä
      ja linkitä aloitusosioon.
- [x] Pura `muut/`-hakemisto: `sisallon-tuonti.md` → `perusteet/`,
      `kuvan-lapinakyvyys.md` → `grafiikka/`. Päivitä linkit.
- [x] Korvaa trac-wikin linkit (29 kpl): sivuston omiin sivuihin, tai
      ohj1-materiaaliin (`ohjelmointi1.it.jyu.fi/luennot/...`), tai poista.
      `ohjelmointi/apua.md` kirjoitettu uusiksi ohj1-linkeillä.
- [x] Vaihda Visual Studio -maininnat Rideriin (6 sivua).
- [x] Poista päällekkäinen "Millaisia muotoja on" -osio `oliot/luonti.md`:stä
      ja linkitä `oliot/muodot.md`:hen.
- [x] Ristiinlinkitä `grafiikka/efektit.md` (partikkeliefekti) takaisin
      `aseet/rajahdykset.md`:hen (fysiikan Explosion); räjähdyssivu linkitti jo
      efekteihin, mutta ankkuri oli rikki.
- [x] Yhtenäistä valikkoteksti ja sivun H1 (valikossa substantiivi, H1 sama;
      kysymysmuoto jää etusivun hakemistoon).
- [x] Siirrä "Kirjaston liittäminen käsin" pois aloituspolusta Viite-osioon.

## 2. Rakenne

- [x] Ryhmittele `SUMMARY.md` ylätason osioihin:
      Aloittaminen · Valmiit pelit · aiheosiot (Oliot, Ohjaus, …) suoraan päävalikossa · Ohjelmointi · Viite.
- [x] Yhdistä pienet osiot: Ohjaimet+liikuttelu → Ohjaus; Tapahtumat +
      törmäyksen estäminen; Kentät + kamera + ikkuna + pelin kulku;
      Grafiikka + äänet; Käyttöliittymä + laskurit; Fysiikka + liitokset.
      Tag-ominaisuus jäi Oliot-osioon (se on olion ominaisuus); Ohjelmointi
      linkittää siihen.
- [x] Siirrä `ohjaimet/kaksi-pelaajaa.md` Oppaisiin (esimerkkipeli).
- [x] Päivitä osioiden etusivujen taulukot vastaamaan uutta ryhmittelyä ja
      poista tarpeettomat etusivut (`pelin-kulku/`, `aanet/`, `laskurit/`).
- [x] Etusivu: "Aloita tästä" -polku (3 askelta) ja aihehakemisto samassa
      järjestyksessä kuin valikko.
- [ ] Pudota valikon numerointi ohjeosioista ja säilytä se vain oppaiden
      vaiheissa. Vaatii muutoksen `zensical/convert.py`:n `build_nav`-
      funktioon (numerointi on nyt kaikilla luettelokohdilla); convert.py on
      jaettu ohj1:n ja ohj2:n kanssa, joten muutos kannattaa tehdä
      asetuksena.
- [ ] Päivitä `tools/tim-tuonti/tim2md.py`:n osiokartta (SECTION_DIRS,
      EXTRA_PAGES) uuteen rakenteeseen, jos TIMistä tuodaan vielä uudelleen.

## 3. Uudet sivut

- [x] `perusteet/ensimmainen-peli.md`: 10 rivin peli ajonapilla, ctrl-F5,
      mitä `Begin` tekee.
- [x] `perusteet/pelin-rakenne.md`: PhysicsGame vs Game, `Begin`,
      koordinaatisto (origo keskellä, y ylös), yksiköt, Level/Camera/Screen.
- [x] `ohjelmointi/mihin-koodi-kirjoitetaan.md`: paikallinen muuttuja vs
      attribuutti, oma aliohjelma, tapahtumankäsittelijä.
- [x] `ohjelmointi/yleiset-virheet.md`: punainen alleviivaus, nimeä ei
      löydy, kuva ei löydy (Content, Copy if newer), peli ei käynnisty.
- [x] `viite/pikaohje.md`: yhden sivun cheat sheet yleisimmistä riveistä.
- [ ] Tarkistuta uudet sivut Jypelin ylläpitäjällä (yksiköt, oletukset,
      projektimallien nimet). Erityisesti `perusteet/erilaisia-peleja.md`
      tarvitsee projektimallien taulukon; trac-linkki poistettu.

## 4. Sivujen sisäinen rakenne (jatkuva)

- [~] Jokaiselle ohjesivulle: lyhyt kuvaus, "Tarvitset ensin", yksi
      kokonainen esimerkki (näkyy mihin aliohjelmaan koodi kirjoitetaan),
      muunnelmat, "Katso myös". Tehty: törmäykset, ohjainten lisäys,
      ajastimet, pistelaskuri, olioiden luonti. Tekemättä: loput 44 sivua,
      joilla ei ole yhtään sisäistä linkkiä.
- [ ] Lisää ajonapillisia kokonaisia esimerkkejä (nyt 16; irrallisia
      `csharp,ignore`-katkelmia ~680). Priorisoi: ohjaimet, törmäykset,
      ajastimet, laskurit, valikko.
- [x] `ohjaimet/liikuttelu.md` alkoi TODO-huomautuksella; sivu on
      olioiden liikuttamisesta, ei ohjaimista. Siirretty `oliot/liikuttelu.md`:ksi
      ("Olioiden liikuttelu ja siirtely"), näppäimistöesimerkki siirretty
      `ohjaimet/ohjainten-lisays.md`:hen.
- [ ] Näkyvät `TODO`-merkinnät: `oliot/animaatio.md`, `grafiikka/kuvat.md`.
- [ ] Puuttuvat kuvat (trac ei vastaa): `oliot/animaatio.md`,
      `laskurit/pistelaskuri.md`, `ohjaimet/ohjainten-lisays.md`.
- [ ] Videot `kentat/`- ja `grafiikka/`-sivuilla: lisää tekstivastine tai
      kuvakaappaus.

## Havainnot (16.9.2026)

Sivusto oli aiheittain järjestetty wiki: 16 ylätason osiota (viidessä vain
1–2 sivua), kaksi tutoriaalia ja noin 80 how-to-sivua. Tyypillisestä
pelikirjaston dokumentaatiosta puuttuivat "ensimmäinen peli" -sivu,
käsitteiden selitys (miten Jypeli-peli toimii), vianetsintä ja näkyvä
API-viite. Osioiden järjestys ei seurannut oppimispolkua (Ohjaimet toiseksi
viimeisenä). Etusivu ryhmitteli sivut eri tavalla kuin valikko. 52 sivua ei
linkittänyt yhteenkään toiseen sivuun. Aloitusosio oli ohut: asennus pelkkä
linkkilista, projektinluontisivulla tyhjä lohko ja katkennut polku, ja
mallipelisivu toisti samat ohjeet. Tutoriaalien vaiheet olivat nimettömiä.
`muut/`-hakemisto oli kaatoluokka. 29 linkkiä osoitti kuolleeseen
trac-wikiin ja 6 sivua neuvoi Visual Studiota, vaikka työkalu on Rider.
