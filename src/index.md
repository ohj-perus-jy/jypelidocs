# Jypeli-ohjeet

Jypeli on Jyväskylän yliopistossa kehitetty, opetuskäyttöön suunniteltu
C#-pelikirjasto. Tällä sivustolla ovat sen käyttöohjeet.

Ohjelmoinnin perusteita opiskellaan
[Ohjelmointi 1](https://ohjelmointi1.it.jyu.fi/) -kurssilla, ja tämä
materiaali perustuu sen kurssin oppeihin.

## Aloita tästä

1. [Asenna työkalut](perusteet/asentaminen.md) ja
   [luo uusi projekti](perusteet/projektin-luonti.md).
2. Tee [ensimmäinen peli](perusteet/ensimmainen-peli.md): pallo, painovoima
   ja yksi näppäin, kymmenen riviä koodia.
3. Tee kokonainen peli [Pong-oppaan](mallit/pong/index.md) mukaan vaihe
   kerrallaan.

Sen jälkeen oma peli kasvaa aihe kerrallaan [ohjeiden](#ohjeet-kysymyksittain)
avulla. Kun etsit yhtä koodiriviä, katso [pikaohje](viite/pikaohje.md).
Kun jokin ei toimi, katso [yleiset virheet](ohjelmointi/yleiset-virheet.md).

> [!HUOMAUTUS]
> Ohjeet ovat osittain vielä työn alla, ja osa sisällöstä saattaa olla
> puutteellista. Ohjeet on tuotu [TIMin Jypeli-wikistä](https://tim.jyu.fi/view/kurssit/jypeli/wiki).
> Jokaisen sivun alareunassa on "Ehdota muutosta" -linkki.

## Ohjeet kysymyksittäin

Sama sisältö kuin vasemman reunan valikossa, samassa järjestyksessä.

### Oliot

- [Miten lisään olion?](oliot/luonti.md)
- [Millaisia olioita on olemassa?](oliot/oliotyypit.md)
- [Millaisia olioiden muotoja on olemassa?](oliot/muodot.md)
- [Miten olion ulkonäköä voi muuttaa?](oliot/ulkonako.md)
- [Miten lisään oliolle animaation?](oliot/animaatio.md)
- [Miten saan olion näkymään muiden edessä tai takana?](oliot/kerrokset.md)
- [Millä eri tavoilla olioita voi liikuttaa ja siirtää?](oliot/liikuttelu.md)
- [Miten olio tuhotaan?](oliot/tuhoaminen.md)
- [Miten määritän oliolle eliniän?](oliot/elinika.md)
- [Miten peliin saa aivot ja tekoälyn?](oliot/tekoaly.md)
- [Miten erotan erityyppiset oliot toisistaan?](oliot/olioiden-erottaminen-toisistaan.md)
- [Miten saan oliolle ominaisuuden, esimerkiksi elämät?](oliot/oma-oliotyyppi.md)

### Ohjaus

- [Miten lisään näppäimet, hiiren tai peliohjaimen?](ohjaimet/ohjainten-lisays.md)
- [Miten näppäimet toimivat vain tietyssä pelitilassa?](ohjaimet/ryhmittely.md)
- [Miten teen tähtäyksen?](ohjaimet/tahtays.md)
- [Miten ohjaimeen saa värinän?](ohjaimet/varina.md)

### Tapahtumat ja törmäykset

- [Miten peliin voi ajastaa tapahtumia?](tapahtumat/ajastimet.md)
- [Miten voin liittää törmäyksiin tapahtumia?](tapahtumat/tormaykset.md)
- [Miten voin estää olioita törmäämästä toisiinsa?](fysiikka/tormayksen-estaminen.md)
- [Mitä muita tapahtumia on?](tapahtumat/muuttapahtumat.md)
- [Mitä delegaatit ovat?](ohjelmointi/delegaatit.md)

### Fysiikka

- [Miten painovoima lisätään?](fysiikka/painovoima.md)
- [Mitä muita fysiikan ilmiöitä voin hyödyntää?](fysiikka/fysiikan-ilmiot.md)
- [Kuinka liitän fysiikkaolioita toisiinsa?](oliot/liitokset.md)

### Kentät ja kamera

- [Miten teen kentän, jossa on olioita ruudukossa?](kentat/ruutukentta.md)
- Miten vaihdan kentän [taustavärin](kentat/tausta.md#taustavari) tai [taustakuvan?](kentat/tausta.md#taustakuva)
- [Miten teen kameran mukana liikkuvan taustan?](kentat/tausta.md#liukuva)
- [Miten kentälle saa reunat tai maaston?](kentat/maasto.md)
- [Miten pelissä voi olla monta kenttää?](kentat/kentan-vaihtuminen.md)
- [Miten teen kentän, jossa oliot liikkuvat vasemmalle?](kentat/sivusuuntainen-skrollaus.md)
- [Miten teen radan autopeliin?](kentat/autorata.md)
- [Miten kenttää voi zoomata tai kamera seurata pelaajaa?](grafiikka/kameran-kaytto.md)
- [Miten saan pelin koko ruutuun tai vaihdan resoluutiota?](grafiikka/ikkunan-asettelu.md)
- [Miten pelin voi aloittaa alusta?](pelin-kulku/aloittaminen-alusta.md)
- [Miten pelin saa pauselle?](pelin-kulku/pause.md)

### Grafiikka ja äänet

- [Miten lisään omia kuvia?](grafiikka/kuvat.md)
- [Miten kuvaan tehdään läpinäkyviä osia?](grafiikka/kuvan-lapinakyvyys.md)
- [Miten peliin saa efektejä (räjähdys, savu, liekki)?](grafiikka/efektit.md)
- [Kuinka piirrän itse kuvioita?](grafiikka/piirtaminen.md)
- [Miten voin käsitellä kuvaa pikselitasolla?](grafiikka/kuvankasittely.md)
- [Miten peliin saa ääniä?](aanet/aanien-lisays.md#tehosteet)
- [Miten saan peliin taustamusiikin?](aanet/aanien-lisays.md#taustamusiikki)

### Aseet ja räjähdykset

- [Miten peliin saa aseita?](aseet/aseiden-lisaaminen.md)
- [Miten pelaaja voi heittää esineen, esim. kranaatin?](aseet/aseiden-lisaaminen.md#heitettavat)
- [Miten peliin saa räjähdyksen?](aseet/rajahdykset.md)

### Käyttöliittymä ja laskurit

- [Miten ruudulle saa näkymään tekstiä?](kayttoliittyma/teksti.md)
- [Miten muutan tekstin kokoa tai fonttia?](kayttoliittyma/fontti.md)
- [Miten teen pistelaskurin?](laskurit/pistelaskuri.md)
- [Miten teen aikalaskurin?](laskurit/aikalaskuri.md)
- [Miten teen palkin, joka näyttää laskurin arvon?](laskurit/etenemispalkki.md)
- [Miten peliin tehdään alkuvalikko?](kayttoliittyma/valikko.md)
- [Monivalintaikkuna](kayttoliittyma/valikko.md#multiselect)
- [Miten kysyn pelaajalta tekstiä?](kayttoliittyma/tekstin-kysyminen.md)
- [Parhaiden pisteiden lista](kayttoliittyma/parhaiden-pisteiden-lista.md)
- [Sommittelu](kayttoliittyma/sommittelu.md)
- [Liukusäätimen tekeminen](kayttoliittyma/liukusaatimet.md)
- [Miten teen koostettuja ikkunoita?](kayttoliittyma/koostettu-ikkuna.md)
- [Oman käyttöliittymäkomponentin tekeminen](kayttoliittyma/omat-kayttoliittymakomponentit.md)
- [Esimerkkejä](kayttoliittyma/esimerkkeja.md)

### Satunnaisuus ja kulmat

- [Miten saan peliini satunnaisuutta?](matematiikka/satunnaisuus.md)
- [Kulma](matematiikka/kulma.md)

### Ohjelmointi

- [Mihin koodi kirjoitetaan?](ohjelmointi/mihin-koodi-kirjoitetaan.md)
- [Miksi peli ei käänny tai toimi?](ohjelmointi/yleiset-virheet.md)

### Viite

| | |
| --- | --- |
| [Pikaohje](viite/pikaohje.md) | Yleisimmät koodirivit yhdellä sivulla. |
| [Jypelin API-dokumentaatio](https://kurssit.it.jyu.fi/npo/material/latest/documentation/html/index.html) | Lähdekoodista tuotettu luettelo kaikista luokista ja aliohjelmista. |
| [Lähdekoodi](https://github.com/Jypeli-JYU/Jypeli) | Jypeli GitHubissa. |
