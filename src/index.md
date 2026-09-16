# Jypeli-ohjeet

Jypeli on Jyväskylän yliopistossa kehitetty, opetuskäyttöön suunniteltu
C#-pelikirjasto. Tälle sivustolle on koottu Jypelin käyttöohjeet aiheittain.
Vasemman reunan valikko luettelee ohjeet aiheen mukaan; alla samat ohjeet
kysymyksittäin.

> [!HUOMAUTUS]
> Ohjeet ovat osittain vielä työn alla, ja osa sisällöstä saattaa olla
> puutteellista. Ohjeet on tuotu [TIMin Jypeli-wikistä](https://tim.jyu.fi/view/kurssit/jypeli/wiki).

## Aloittaminen

- [Miten teen uuden projektin (pelin)?](mallit/index.md)
- [Millaisia pelejä voin tehdä?](perusteet/erilaisia-peleja.md)
- [Kirjaston liittäminen projektiin käsin](perusteet/kirjaston-liittaminen-kasin.md)

## Olioiden luominen ja muodot

- [Miten lisään olion?](oliot/luonti.md)
- [Millaisia olioiden muotoja on olemassa?](oliot/muodot.md)
- [Millaisia olioita on olemassa?](oliot/oliotyypit.md)
- [Miten olion ulkonäköä voi muuttaa?](oliot/ulkonako.md)
- [Miten lisään oliolle animaation?](oliot/animaatio.md)
- [Miten olio tuhotaan?](oliot/tuhoaminen.md)
- [Miten määritän oliolle eliniän?](oliot/elinika.md)
- [Miten saan olion näkymään muiden edessä (tai takana)?](oliot/kerrokset.md)
- [Miten saan oliolle ominaisuuden (elämät, hitpoints, kengännumero, tms)?](oliot/oma-oliotyyppi.md)
- Katso myös: [Sisällön tuominen projektiin](muut/sisallon-tuonti.md)

## Kentät

- [Miten teen kentän, jossa on olioita ruudukossa?](kentat/ruutukentta.md) (mm. kenttien lataaminen tiedostosta)
- [Miten pelikentän voi aloittaa alusta?](pelin-kulku/aloittaminen-alusta.md)
- [Miten pelin saa pauselle?](pelin-kulku/pause.md)
- [Miten pelissä voi tehdä monta kenttää?](kentat/kentan-vaihtuminen.md)
- Miten voin vaihtaa kentän [taustavärin](kentat/tausta.md#taustavari) tai [taustakuvan?](kentat/tausta.md#taustakuva)
- [Miten kentälle saa suoria / epätasaisia reunoja tai maaston?](kentat/maasto.md)
- [Miten teen kenttään kameran mukana liikkuvan taustan?](kentat/tausta.md#liukuva)
- [Miten teen radan autopeliin?](kentat/autorata.md)
- [Miten teen kentän, jossa oliot liikkuvat vasemmalle?](kentat/sivusuuntainen-skrollaus.md)

## Laskurit

- [Miten teen pistelaskurin?](laskurit/pistelaskuri.md)
- [Miten teen aikalaskurin?](laskurit/aikalaskuri.md)
- [Miten teen palkin joka näyttää laskurin arvon?](laskurit/etenemispalkki.md)

## Ohjaimet

- [Miten lisään ohjaimet peliin?](ohjaimet/ohjainten-lisays.md)
- [Ohjaimien ryhmittely](ohjaimet/ryhmittely.md)
- [Millä eri tavoilla olioita voi liikuttaa?](ohjaimet/liikuttelu.md)
- [Tähtääminen](ohjaimet/tahtays.md)
- [Miten Xbox 360 -ohjaimeen ja puhelimeen saa värinätehosteita?](ohjaimet/varina.md)

## Ajastimet, tapahtumat

- [Miten peliin voi ajastaa tapahtumia?](tapahtumat/ajastimet.md)
- [Miten voin liittää törmäyksiin tapahtumia?](tapahtumat/tormaykset.md)

## Äänet

- [Miten peliin saa ääniä?](aanet/aanien-lisays.md#tehosteet)
- [Miten saan peliin taustamusiikin?](aanet/aanien-lisays.md#taustamusiikki)
- Katso myös: [Sisällön tuominen projektiin](muut/sisallon-tuonti.md)

## Fysiikka

- [Miten painovoima lisätään?](fysiikka/painovoima.md)
- [Mitä muita fysiikan ilmiöitä voin hyödyntää?](fysiikka/fysiikan-ilmiot.md)
- [Miten voin estää olioita törmäämästä toisiinsa?](fysiikka/tormayksen-estaminen.md)
- [Kuinka liitän fysiikkaolioita toisiinsa?](oliot/liitokset.md)

## Aseet, räjähdykset, aivot

- [Miten peliin saa aseita?](aseet/aseiden-lisaaminen.md)
- [Miten pelaaja voi heittää esineen, esim. kranaatin?](aseet/aseiden-lisaaminen.md#heitettavat)
- [Miten peliin saa räjähdyksen?](aseet/rajahdykset.md)
- [Miten peliin saa aivot ja tekoälyn?](oliot/tekoaly.md)

## Grafiikka

- [Miten peliin saa efektejä (räjähdys, savu, liekki)?](grafiikka/efektit.md)
- [Miten kenttää voi zoomata (kameran käyttöohjeet)](grafiikka/kameran-kaytto.md)
- [Miten saan pelin koko ruutuun tai vaihdan pelin resoluutiota?](grafiikka/ikkunan-asettelu.md)
- [Kuvat ja niiden käsittely](grafiikka/kuvat.md)
- [Kuinka piirrän itse kuvioita?](grafiikka/piirtaminen.md)
- [Miten voin käsitellä kuvaa (pikselitasolla)?](grafiikka/kuvankasittely.md)

## Käyttöliittymä

- [Miten peliin tehdään alkuvalikko?](kayttoliittyma/valikko.md)
- [Parhaiden pisteiden lista (topten)](kayttoliittyma/parhaiden-pisteiden-lista.md)
- [Miten ruudulle saa näkymään tekstiä?](kayttoliittyma/teksti.md)
- [Tekstin kysyminen pelaajalta](kayttoliittyma/tekstin-kysyminen.md)
- [Monivalintaikkuna](kayttoliittyma/valikko.md#multiselect)
- [Miten teen koostettuja ikkunoita?](kayttoliittyma/koostettu-ikkuna.md)
- [Miten muutan tekstin kokoa tai fonttia?](kayttoliittyma/fontti.md)
- [Sommittelu](kayttoliittyma/sommittelu.md)
- [Käyttöliittymäkomponentin tekeminen](kayttoliittyma/omat-kayttoliittymakomponentit.md)
- [Liukusäätimen tekeminen](kayttoliittyma/liukusaatimet.md)
- [Esimerkkejä](kayttoliittyma/esimerkkeja.md)

## Matematiikka

- [Miten saan peliini satunnaisuutta?](matematiikka/satunnaisuus.md)
- [Kulma](matematiikka/kulma.md)

## Ohjelmointi

- [Apuja ohjelmointiin](ohjelmointi/apua.md)
- [Delegaattien teko](ohjelmointi/delegaatit.md)
- [Miten erotan erityyppiset oliot toisistaan (olion Tag-ominaisuus)](oliot/olioiden-erottaminen-toisistaan.md)

## Muut

|  |  |
| --- | --- |
| [Jypelin dokumentaatio](https://kurssit.it.jyu.fi/npo/material/latest/documentation/html/index.html) | Lähdekoodista tuotettu dokumentaatio |
| [Jypelin päivityshistoria](paivitysloki.md) | Mitä muutoksia missäkin Jypelin ja sen fysiikkamoottorin versiossa on tullut. |
| [Jypeli lähdekoodi](https://github.com/Jypeli-JYU/Jypeli) | Lähdekoodi GitHubissa |
