# Mitä konepellin alla tapahtuu

Tämä sivu selittää, mitä Jypeli tekee sinun koodisi ympärillä, ja auttaa
ymmärtämään, miksi peli reagoi juuri silloin, kun reagoi. Perusasiat ovat
sivulla [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md).

## Käynnistys, silmukka ja lopetus

Projektissa on tiedosto `Ohjelma.cs`, jossa on ohjelman alkupiste `Main`.
Se luo peliolion ja kutsuu sen `Run`-aliohjelmaa. Kaikki muu on Jypelin
vastuulla: `Run` avaa ikkunan, alustaa grafiikan ja ohjaimet, kutsuu kerran
`Begin`-aliohjelmaasi ja jää sitten toistamaan pelisilmukkaa, kunnes ikkuna
suljetaan tai peli kutsuu `Exit`.

```bob
  Ohjelma.cs                Jypeli                          Oma peliluokka
  ==========                ======                          ==============

  kutsuu Run ---------> +----------------------+
                        | Avaa ikkunan,        |
                        | alustaa grafiikan,   |
                        | ohjaimet ja kentän   |
                        +----------+-----------+
                                   |
                                   v
                        +----------------------+
                        | Kutsuu Begin         | ---------> Begin
                        +----------+-----------+            luo oliot, asettaa
                                   |                        kuuntelijat ja ajastimet
                                   v
           .----------> +----------------------+
           |            | Päivitys             | ---------> tapahtumankäsittelijät:
           |            | fysiikka, ohjaimet,  |            törmäys, näppäin,
           |            | oliot, ajastimet     |            ajastin, ...
           |            +----------+-----------+
           |                       |
           |                       v
           |            +----------------------+
           |            | Piirto               | ---------> Paint, jos on
           |            +----------+-----------+
           |                       |
           '-----------------------'  60 kertaa sekunnissa,
                                      kunnes ikkuna suljetaan
```

Silmukan yksi kierros on *päivitys* ja *piirto*. Jypeli pyrkii tekemään
molemmat 60 kertaa sekunnissa, ja pelin aika etenee joka päivityksellä
tasan 1/60 sekuntia. Sinun koodiasi ajetaan vain, kun Jypeli kutsuu sitä:
kerran `Begin`-aliohjelmassa ja sen jälkeen tapahtumankäsittelijöissä.

## Mitä yksi päivitys tekee

Päivityksessä Jypeli käy läpi pelin osat aina samassa järjestyksessä.
Tapahtumankäsittelijöitäsi kutsutaan sen osan kohdalla, johon ne kuuluvat.

| Vaihe | Mitä Jypeli tekee | Mitä omaa koodiasi kutsutaan |
| --- | --- | --- |
| 1. Fysiikka | Fysiikkamoottori siirtää `PhysicsObject`-olioita niiden nopeuden, painovoiman ja voimien mukaan 1/60 sekunnin verran ja ratkaisee törmäykset. | `AddCollisionHandler`-käsittelijät niille pareille, jotka törmäsivät. |
| 2. Ohjaimet | Lukee näppäimistön, hiiren ja peliohjainten tilan ja vertaa sitä edelliseen päivitykseen. | `Keyboard.Listen`- ja `Mouse.Listen`-käsittelijät. `ButtonState.Pressed` laukeaa sillä päivityksellä, jolla näppäin painui alas; `ButtonState.Down` joka päivityksellä, kun näppäin on pohjassa, eli 60 kertaa sekunnissa. |
| 3. Kamera | Siirtää kameraa, jos se seuraa oliota (`Camera.Follow`). | |
| 4. Oliot | Päivittää kerroksittain kaikki peliin lisätyt oliot: `GameObject`-olioiden liike, animaatioiden ruudut, tekoälyt (`Brain`), elinajan (`LifetimeLeft`) päättyminen. | Olion oma `Update`-aliohjelma, jos olet tehnyt oman oliotyypin ja kirjoittanut sille [oman päivitysmetodin](../oma-oliotyyppi/paivitys.md). |
| 5. Ajastimet | Kasvattaa jokaisen käynnissä olevan `Timer`-olion laskuria ja katsoo, ylittyikö `Interval`. | `Timeout`-käsittelijät. |
| 6. Muut käsittelijät | Tarkistaa `AddCustomHandler`-ehdot ja suorittaa `Begin`-vaiheen jälkeen lykätyt toimet. | Ehtojen täyttyessä niiden käsittelijät. |

Piirrossa Jypeli tyhjentää ruudun, piirtää kentän taustan, sitten oliot
kerros kerrallaan kameran läpi katsottuna, sen päälle käyttöliittymän osat
(kuten pistenäytön), ja lopuksi kutsuu `Paint`-aliohjelmaa, jos olet
kirjoittanut sellaisen. Ks. [Piirtäminen Canvakselle](../grafiikka/piirtaminen.md).

## Mitä tästä seuraa käytännössä

- **`Begin` ei saa jäädä pyörimään.** Jypeli pääsee silmukkaan vasta, kun
  `Begin` palaa. Jos kirjoitat `Begin`-aliohjelmaan `while`-silmukan tai
  `Thread.Sleep`-kutsun, ikkuna ei piirry eikä reagoi mihinkään. Toistuva
  tekeminen hoidetaan ajastimella, odottaminen `Timer.SingleShot`-kutsulla.
- **Olio ei liiku heti.** Kun asetat `Velocity`-arvon tai kutsut `Push`,
  sijainti muuttuu vasta seuraavissa päivityksissä, 1/60 sekuntia kerrallaan.
  Nopeus 100 tarkoittaa 100 yksikköä sekunnissa.
- **Käsittelijässä saa luoda ja tuhota olioita.** Käsittelijät ajetaan
  päivityksen sisällä, eivät sen kanssa kilpaa, joten `Add` ja `Destroy`
  ovat turvallisia missä tahansa käsittelijässä.
- **Hidas kone hidastaa peliä.** Jos päivitys ja piirto eivät ehdi valmiiksi
  1/60 sekunnissa, Jypeli ei hyppää päivityksiä yli, vaan peli kulkee
  hitaammin. Yleisin syy on suuri määrä olioita tai raskas käsittelijä.
- **Tauko pysäyttää vain pelin.** `Pause()` pysäyttää fysiikan, oliot ja
  ajastimet, mutta ohjaimet ja käyttöliittymän osat toimivat yhä, joten
  valikkoa voi käyttää pelin ollessa tauolla.

## Mistä Jypeli on tehty

Jypeli on .NET-kirjasto, joka tulee projektiin NuGet-paketteina
`Jypeli.NET` ja `Jypeli.FarseerPhysics.NET`. Ikkunan, näppäimistön ja
näytönohjaimen kanssa Jypeli juttelee
[Silk.NET](https://dotnet.github.io/Silk.NET/)-kirjaston ja OpenGL:n
kautta, ja fysiikan laskee [Farseer Physics](../fysiikka/liitokset.md)
-moottori. Näitä ei tarvitse käyttää itse: Jypeli kääntää niiden
käsitteet omikseen (`PhysicsObject`, `Camera`, `Keyboard.Listen`), ja siksi
sama peli toimii Windowsissa, macOS:ssä, Linuxissa ja Androidissa.

```bob
  +------------------------------------------------+
  |      Oma peli: Begin ja tapahtumankäsittelijät |
  +------------------------------------------------+
  |                     Jypeli                     |
  |   oliot, kenttä, kamera, ajastimet, ohjaimet   |
  +-----------------------+------------------------+
  |  Farseer Physics      |  Silk.NET + OpenGL     |
  |  törmäykset, voimat   |  ikkuna, syöte, piirto |
  +-----------------------+------------------------+
  |                      .NET                      |
  +------------------------------------------------+
```
