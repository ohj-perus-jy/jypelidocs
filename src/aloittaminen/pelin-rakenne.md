# Miten Jypeli-peli toimii

Tämä sivu kertoo, mistä osista Jypeli-peli koostuu ja mitä sanat kenttä,
kamera ja ruutu tarkoittavat. Tietoa tarvitaan lähes joka ohjeessa.

## Peli on luokka, Begin sen alku

Peli on C#-luokka, joka perii Jypelin `PhysicsGame`-luokan (tai `Game`, jos
fysiikkaa ei tarvita). Jypeli kutsuu pelin `Begin`-aliohjelmaa kerran
käynnistyksessä. Sen jälkeen Jypeli pyörittää *pelisilmukkaa* itse: se
siirtää olioita, laskee törmäykset, piirtää ruudun ja kutsuu sinun
aliohjelmiasi, kun jotain tapahtuu (näppäintä painetaan, ajastin laukeaa,
oliot törmäävät). Omaa silmukkaa ei siis kirjoiteta. Silmukan vaiheet
selitetään alempana kohdassa [Mitä konepellin alla tapahtuu](#mita-konepellin-alla-tapahtuu).

```csharp,ignore
public class Peli : PhysicsGame
{
    public override void Begin()
    {
        // Luo oliot, aseta näppäimet, käynnistä ajastimet.
    }
}
```

| Luokka | Milloin |
| --- | --- |
| `PhysicsGame` | Oliot törmäävät, putoavat ja pomppivat. Fysiikkapeli-projektimalli. Lähes kaikki ohjeet olettavat tämän. |
| `Game` | Ei fysiikkaa. Kevyempi, sopii esimerkiksi korttipeliin tai visailuun. |

## Oliot

Kaikki ruudulla näkyvä on olioita. `PhysicsObject` noudattaa fysiikkaa,
`GameObject` ei. Olio tulee näkyviin vasta, kun se on lisätty peliin
`Add`-aliohjelmalla, ja katoaa, kun sille kutsutaan `Destroy`. Tarkemmin:
[Olion luominen](../oliot/luonti.md) ja [Oliotyypit](../oliot/oliotyypit.md).

## Koordinaatisto

Kentän **origo (0, 0) on ruudun keskellä**. X kasvaa oikealle ja **y kasvaa
ylöspäin**, kuten matematiikassa (ei kuten useissa muissa
grafiikkakirjastoissa, joissa y kasvaa alaspäin). Yksikkö on pikseli, kun
kameraa ei ole zoomattu.

```text
                 y
                 ^
                 |
  (-100, 50) o   |
                 |
  ---------------+---------------> x
                 | (0, 0)
                 |
                 |     o (200, -80)
```

Sijainti annetaan `Vector`-oliona tai erikseen: `olio.Position = new
Vector(100, -50)` tai `olio.X = 100; olio.Y = -50;`. Kulmat annetaan
`Angle`-tyyppinä, esimerkiksi `Angle.FromDegrees(90)`; nolla osoittaa
oikealle ja kulma kasvaa vastapäivään.

## Kenttä, kamera ja ruutu

| Sana | Mitä se on | Tavallisia rivejä |
| --- | --- | --- |
| **Level** (kenttä) | Pelimaailma, jossa oliot ovat. Voi olla ruutua suurempi. | `Level.Width`, `Level.Left`, `Level.Top`, `Level.CreateBorders()`, `Level.Background.Color = Color.Black` |
| **Camera** (kamera) | Se osa kenttää, joka näytetään. Kameraa voi siirtää ja zoomata. | `Camera.ZoomToLevel()`, `Camera.Follow(pelaaja)`, `Camera.ZoomFactor = 2` |
| **Screen** (ruutu) | Peli-ikkuna pikseleinä. Käyttöliittymän osat, kuten pistenäyttö, asetetaan ruudun eikä kentän mukaan. | `Screen.Width`, `Screen.Top` |

Aloittelijan tavallisin hämmennys: olio on luotu ja lisätty, mutta se ei
näy. Syy on yleensä, että olio on kameran näkymän ulkopuolella. Kutsu
`Camera.ZoomToLevel()` tai tarkista sijainti.

## Fysiikan yksiköt

Fysiikka-arvot ovat pikselipohjaisia. Painovoima annetaan pikseleinä
sekunnissa toiseen, esimerkiksi `Gravity = new Vector(0, -981)` vastaa
tulkintaa "yksi pikseli on senttimetri". Nopeus on pikseliä sekunnissa.
Sopivat arvot löytyvät kokeilemalla, ks. [Painovoima](../fysiikka/painovoima.md)
ja [Fysiikan ilmiöt](../fysiikka/fysiikan-ilmiot.md).

## Tapahtumat ja käsittelijät

Peli reagoi asioihin *tapahtumankäsittelijöillä*: annat Jypelille oman
aliohjelmasi nimen, ja Jypeli kutsuu sitä, kun tapahtuma sattuu.

```csharp,ignore
Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaVasemmalle, "Liiku vasemmalle");
AddCollisionHandler(pallo, maila, PalloOsuiMailaan);
ajastin.Timeout += LisaaVihollinen;
```

Käsittelijä on tavallinen aliohjelma, jonka parametrit riippuvat tapahtumasta.
Ks. [Ohjainten lisääminen](../ohjaimet/ohjainten-lisays.md),
[Törmäysten käsittely](../tapahtumat/tormaykset.md) ja
[Ajastimet](../tapahtumat/ajastimet.md). Se, miksi aliohjelman nimi
kelpaa parametriksi, selitetään sivulla [Delegaatit](../ohjelmointi/delegaatit.md).

## Mitä konepellin alla tapahtuu

Tämän kohdan voi lukea myöhemminkin. Se selittää, mitä Jypeli tekee sinun
koodisi ympärillä, ja auttaa ymmärtämään, miksi peli reagoi juuri silloin
kuin reagoi.

### Käynnistys, silmukka ja lopetus

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

### Mitä yksi päivitys tekee

Päivityksessä Jypeli käy läpi pelin osat aina samassa järjestyksessä.
Tapahtumankäsittelijäsi kutsutaan sen osan kohdalla, johon ne kuuluvat.

| Vaihe | Mitä Jypeli tekee | Mitä omaa koodiasi kutsutaan |
| --- | --- | --- |
| 1. Fysiikka | Fysiikkamoottori siirtää `PhysicsObject`-olioita niiden nopeuden, painovoiman ja voimien mukaan 1/60 sekunnin verran ja ratkaisee törmäykset. | `AddCollisionHandler`-käsittelijät niille pareille, jotka törmäsivät. |
| 2. Ohjaimet | Lukee näppäimistön, hiiren ja peliohjainten tilan ja vertaa sitä edelliseen päivitykseen. | `Keyboard.Listen`- ja `Mouse.Listen`-käsittelijät. `ButtonState.Pressed` laukeaa sillä päivityksellä, jolla näppäin painui alas; `ButtonState.Down` joka päivityksellä, kun näppäin on pohjassa, eli 60 kertaa sekunnissa. |
| 3. Kamera | Siirtää kameraa, jos se seuraa oliota (`Camera.Follow`). | |
| 4. Oliot | Päivittää kerroksittain kaikki peliin lisätyt oliot: `GameObject`-olioiden liike, animaatioiden ruudut, tekoälyt (`Brain`), elinajan (`LifetimeLeft`) päättyminen. | Olion oma `Update`-aliohjelma, jos olet tehnyt [oman oliotyypin](../oliot/oma-oliotyyppi.md) ja korvannut sen. |
| 5. Ajastimet | Kasvattaa jokaisen käynnissä olevan `Timer`-olion laskuria ja katsoo, ylittyikö `Interval`. | `Timeout`-käsittelijät. |
| 6. Muut käsittelijät | Tarkistaa `AddCustomHandler`-ehdot ja suorittaa `Begin`-vaiheen jälkeen lykätyt toimet. | Ehtojen täyttyessä niiden käsittelijät. |

Piirrossa Jypeli tyhjentää ruudun, piirtää kentän taustan, sitten oliot
kerros kerrallaan kameran läpi katsottuna, sen päälle käyttöliittymän osat
(kuten pistenäytön), ja lopuksi kutsuu `Paint`-aliohjelmaa, jos olet
kirjoittanut sellaisen. Ks. [Piirtäminen](../grafiikka/piirtaminen.md).

### Mitä tästä seuraa käytännössä

- **`Begin` ei saa jäädä pyörimään.** Jypeli pääsee silmukkaan vasta, kun
  `Begin` palaa. Jos kirjoitat `Begin`-aliohjelmaan `while`-silmukan tai
  `Thread.Sleep`-kutsun, ikkuna ei piirry eikä reagoi mihinkään. Toistuva
  tekeminen hoidetaan ajastimella, odottaminen `Timer.SingleShot`-kutsulla.
- **Olio ei liiku heti.** Kun asetat `Velocity`-arvon tai kutsut `Push`,
  sijainti muuttuu vasta seuraavissa päivityksissä, 1/60 sekunti kerrallaan.
  Nopeus 100 tarkoittaa 100 pikseliä sekunnissa.
- **Käsittelijässä saa luoda ja tuhota olioita.** Käsittelijät ajetaan
  päivityksen sisällä, eivät sen kanssa kilpaa, joten `Add` ja `Destroy`
  ovat turvallisia missä tahansa käsittelijässä.
- **Hidas kone hidastaa peliä.** Jos päivitys ja piirto eivät ehdi valmiiksi
  1/60 sekunnissa, Jypeli ei hyppää päivityksiä yli vaan peli kulkee
  hitaammin. Yleisin syy on suuri määrä olioita tai raskas käsittelijä.
- **Tauko pysäyttää vain pelin.** `Pause()` pysäyttää fysiikan, oliot ja
  ajastimet, mutta ohjaimet ja käyttöliittymän osat toimivat yhä, joten
  valikkoa voi käyttää pelin ollessa tauolla.

### Mistä Jypeli on tehty

Jypeli on .NET-kirjasto, joka tulee projektiin NuGet-paketteina
`Jypeli.NET` ja `Jypeli.FarseerPhysics.NET`. Ikkunan, näppäimistön ja
näytönohjaimen kanssa Jypeli juttelee
[Silk.NET](https://dotnet.github.io/Silk.NET/)-kirjaston ja OpenGL:n
kautta, ja fysiikan laskee [Farseer Physics](../oliot/liitokset.md)
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

## Sisältötiedostot

Kuvat, äänet ja kenttätiedostot laitetaan projektin `Content`-kansioon ja
ladataan nimellä: `LoadImage("norsu")`, `LoadSoundEffect("pum")`. Ks.
[Kuvat ja äänet mukaan projektiin](sisallon-tuonti.md).
