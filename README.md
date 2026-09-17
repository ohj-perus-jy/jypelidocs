# Jypeli-ohjeet

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Jypeli-pelikirjaston käyttöohjeet aiheittain. Sivusto on katseltavissa
osoitteessa <https://ohj-perus-jy.github.io/jypelidocs/>.

## Haluatko osallistua?

Jos haluat osallistua sivuston kehittämiseen, kloonaa repo ja aloita muokkaus.

Sivusto rakennetaan **Zensicalilla**. Suositeltu tapa on mukana oleva
DevContainer, joka asentaa tarvittavat työkalut (`zensical/setup.sh`) avattaessa. Ilman
DevContaineria riittää Python 3.11 ja `./zensical/setup.sh`.

Kehityspalvelin, joka seuraa `src/`-puun muutoksia:

```bash
./zensical/run.sh            # http://localhost:8001
./zensical/run.sh build      # pelkkä rakennus zensical/site/-hakemistoon
./zensical/run.sh test       # testit (pytest + Playwright)
```

**Muokattava sisältö on kansiossa `src/`.**

Tee pull request, kun olet valmis.

## Ongelmista ilmoittaminen

Avaa [issue](https://github.com/ohj-perus-jy/jypelidocs/issues/new/choose)
tai ehdota muutosta sivun alareunan "Ehdota muutosta" -linkistä.

## Lisenssi

Materiaali on lisensoitu [CC BY-SA 4.0][cc-by-sa] -lisenssillä.

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/deed.fi
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
