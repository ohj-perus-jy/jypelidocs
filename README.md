# Jypeli-ohjeet

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Jypeli-pelikirjaston käyttöohjeet aiheittain. Sivusto on katseltavissa
osoitteessa <https://jypeli.it.jyu.fi/>.

## Haluatko osallistua?

Jos haluat osallistua sivuston kehittämiseen, kloonaa repo submoduleineen ja
aloita muokkaus:

```bash
git clone --recurse-submodules https://github.com/ohj-perus-jy/jypelidocs.git
cd jypelidocs
git config submodule.recurse true    # git pull päivittää jatkossa myös työkalut
```

Sivusto rakennetaan **[Zensicalilla](https://zensical.org)**. Työkalut
(muunnos, tyylit, skriptit, testit) ovat git-submodule `zensical/tyokalut`, repo
[kirjatyokalut](https://github.com/ohj-perus-jy/kirjatyokalut), joka on yhteinen
Ohjelmointi 1:n ja Ohjelmointi 2:n materiaalien kanssa.

Suositeltu tapa on mukana oleva DevContainer, joka hakee työkalut ja asentaa
tarvittavan avattaessa. Ilman DevContaineria riittää Python 3.11 tai uudempi:
`run.sh` hakee submodulen ja asentaa Zensicalin ensimmäisellä ajolla.

Kehityspalvelin, joka seuraa `src/`-puun muutoksia:

```bash
./zensical/run.sh            # http://localhost:8001
./zensical/run.sh build      # pelkkä rakennus zensical/site/-hakemistoon
./zensical/run.sh test       # testit (pytest + Playwright)
```

**Muokattava sisältö on kansiossa `src/`.**

Tee pull request, kun olet valmis.

Lisää: [zensical/README.md](zensical/README.md) (tämän sivuston asetukset,
kaaviot ja työkalujen päivittäminen) ja
[kirjatyokalut/README.md](https://github.com/ohj-perus-jy/kirjatyokalut#readme)
(rakenne, merkkaus, työkalujen muuttaminen).

## Ongelmista ilmoittaminen

Avaa [issue](https://github.com/ohj-perus-jy/jypelidocs/issues/new/choose)
tai ehdota muutosta sivun alareunan "Ehdota muutosta" -linkistä.

## Lisenssi

Materiaali on lisensoitu [CC BY-SA 4.0][cc-by-sa] -lisenssillä.

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/deed.fi
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
