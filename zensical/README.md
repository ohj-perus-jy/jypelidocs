# Zensical

Sivuston rakennus **Zensicalilla** (Material for MkDocsin tekijöiden
generaattori). Lähdepuu on `../src`, samaa Markdown-murretta kuin ohj1:n ja
ohj2:n materiaalit.

Työkalut (`convert.py`, tyylit, skriptit, teeman mallit, testit) ovat
git-submodule [`tyokalut/`](https://github.com/ohj-perus-jy/kirjatyokalut),
yhteinen ohj1:n ja ohj2:n kanssa. Käyttö, asetukset, työkalujen muuttaminen ja
testit: [tyokalut/README.md](tyokalut/README.md). Ratkaisujen perustelut:
[tyokalut/PERUSTELUT.md](tyokalut/PERUSTELUT.md).

## Käynnistys

```bash
./zensical/run.sh              # http://localhost:8001, vahtii ../src:ää
./zensical/run.sh build        # pelkkä rakennus site/-hakemistoon
./zensical/run.sh test         # testit: koekirja ja tämä kirja
```

Kloonin jälkeen submodule haetaan komennolla `git submodule update --init`
(`run.sh` tekee sen itse, jos hakemisto on tyhjä). `git pull` ei päivitä
submodulea; `git config submodule.recurse true` korjaa sen tässä kloonissa.

**Muokattava puu on `../src`, ei `docs/`.**

## Tämän kirjan omat tiedostot

- `kirja.toml`: kirjan asetukset työkaluille. Täällä vain nimi: sivuja ei
  siirretä toistensa alle eikä osioita poisteta.
- `mkdocs.yml`: `site_name`, `site_url`, `copyright`, `repo_url` ja
  sivustovalikon lista (`extra.sites`). Teema, tyylit ja skriptit tulevat
  työkalujen `mkdocs-pohja.yml`:stä generoidun `nav.yml`:n kautta.
- `cache/svgbob/`: `ekstrat/konepellin-alla.md`:n kaksi bob-kaaviota ja
  `aloittaminen/pelin-rakenne.md`:n koordinaatisto (svgbob_cli 0.7.6). Kuvat
  ovat versionhallinnassa, koska julkaisu ei asenna svgbobia: uusi tai muutettu
  kaavio piirretään paikallisesti (`./zensical/run.sh build`; `convert.py`
  asentaa `svgbob_cli`:n cargolla, DevContainerissa Rust on valmiina) ja
  syntynyt tiedosto committoidaan. Julkaisun `convert.py --strict` kaatuu,
  jos kuva puuttuu.
- `run.sh`: kääre, joka kutsuu `tyokalut/run.sh`:ta.

## Työkalujen päivittäminen

```bash
git -C zensical/tyokalut pull origin main
git add zensical/tyokalut && git commit -m "Työkalut: ..."
```

`.github/workflows/pages.yml` kääntää samalla ajolla sekä `main`in että
`dev`in, joten rakennetta koskeva muutos viedään molempiin haaroihin samalla
työnnöllä.
