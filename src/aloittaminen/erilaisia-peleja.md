# Millaisia pelejä voin tehdä?

Jypeli on kirjasto **kaksiulotteisten pelien** tekemiseen. Kenttä on tasainen
pinta, jota katsotaan suoraan edestä tai ylhäältä. Kolmiulotteisia pelejä
Jypelillä ei tehdä.

## Fysiikkapelit

Useimmat Jypeli-pelit käyttävät kirjaston valmista **fysiikkamoottoria**.
Oliot liikkuvat, putoavat, törmäävät ja pomppivat itsestään, eikä liikettä
tarvitse laskea itse. Tällaisia pelejä ovat esimerkiksi

- Pong ja muut pallopelit
- tasohyppelyt
- ammuskelupelit ja avaruusräiskinnät
- autopelit
- Angry Birds -tyyliset heittopelit.

Fysiikkapeli tehdään **Fysiikkapeli**-projektimallilla, jolloin peli perii
`PhysicsGame`-luokan ja oliot ovat `PhysicsObject`-tyyppisiä. Tämän oppaan
ohjeet ja [valmiit pelit](../tutoriaalit/index.md) olettavat, että käytössä on
Fysiikkapeli.

## Pelit ilman fysiikkaa

Kaikissa peleissä ei tarvita painovoimaa tai törmäyksiä. Jypelillä voi tehdä
myös pelejä, joissa oliot pysyvät paikallaan tai liikkuvat vain, kun ohjelma
niitä siirtää. Esimerkiksi

- korttipelit
- lautapelit ja ristinolla
- visailut ja muistipelit
- tekstiseikkailut
- pulmapelit, kuten Tetris tai Sokoban.

Näihin sopii **Peli**-projektimalli, jossa peli perii `Game`-luokan ja oliot
ovat `GameObject`-tyyppisiä. Peli on kevyempi kuin Fysiikkapeli, ja siinä
ohjelmoija määrää itse, milloin ja mihin oliot siirtyvät. Näppäimet, hiiri,
ajastimet, kuvat, äänet ja valikot toimivat samalla tavalla kuin
Fysiikkapelissä.

| | Fysiikkapeli | Peli |
| --- | --- | --- |
| Peliluokka | `PhysicsGame` | `Game` |
| Oliot | `PhysicsObject` | `GameObject` |
| Liike | Fysiikkamoottori laskee | Ohjelmoija siirtää |
| Törmäykset | Automaattisesti | Ei |
| Sopii | Pallo-, hyppely-, ajo- ja ammuskelupeleihin | Kortti-, lauta-, visailu- ja pulmapeleihin |

Fysiikkapelissä voi käyttää myös `GameObject`-olioita, joten fysiikkapeliin
voi lisätä esimerkiksi liikkumattomia koristeita. Toisin päin ei voi:
`Game`-luokan pelissä ei ole fysiikkaa lainkaan. Jos et ole varma, valitse
Fysiikkapeli.

Tarkemmin peliluokista ja olioista: [Miten Jypeli-peli toimii](pelin-rakenne.md)
ja [Oliotyypit](../oliot/oliotyypit.md).

## Esimerkkejä valmiista peleistä

Videoita Jypelillä tehdyistä peleistä:

- <http://youtu.be/RwmU0O7hXts>
- <http://youtu.be/sghOkrKlwmk>
