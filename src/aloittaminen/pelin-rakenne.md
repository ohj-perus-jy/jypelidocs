# Miten Jypeli-peli toimii

Tämä sivu kertoo, mistä osista Jypeli-peli koostuu, mihin kohtaan tiedostoa
koodirivit kirjoitetaan ja mitä sanat kenttä, kamera ja ruutu tarkoittavat.
Tietoa tarvitaan lähes joka ohjeessa.

## Peli on luokka, Begin sen alku

Peli on C#-luokka, joka perii Jypelin `PhysicsGame`-luokan (tai `Game`, jos
fysiikkaa ei tarvita). Jypeli kutsuu pelin `Begin`-aliohjelmaa kerran
käynnistyksessä. Sen jälkeen Jypeli pyörittää *pelisilmukkaa* itse: se
siirtää olioita, laskee törmäykset, piirtää ruudun ja kutsuu sinun
aliohjelmiasi, kun jotain tapahtuu (näppäintä painetaan, ajastin laukeaa,
oliot törmäävät). Omaa silmukkaa ei siis kirjoiteta. Silmukan vaiheet
selitetään sivulla [Mitä konepellin alla tapahtuu](../ekstrat/konepellin-alla.md).

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

## Mihin koodi kirjoitetaan

Ohjeissa on paljon yksittäisiä koodirivejä. Peliluokassa on kolme paikkaa,
joihin ne kuuluvat.

```csharp,ignore
using Jypeli;

public class Peli : PhysicsGame
{
    // 1. ATTRIBUUTIT: luokan sisällä, aliohjelmien ulkopuolella.
    PhysicsObject pelaaja;
    IntMeter pisteet;

    // 2. BEGIN: suoritetaan kerran pelin alussa.
    public override void Begin()
    {
        pelaaja = new PhysicsObject(40, 40);
        Add(pelaaja);
        Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Hyppää");
    }

    // 3. OMAT ALIOHJELMAT: luokan sisällä, Beginin rinnalla.
    void Hyppaa()
    {
        pelaaja.Hit(new Vector(0, 500));
    }
}
```

- Yksittäiset rivit, kuten `Gravity = new Vector(0, -800);` tai
  `Add(olio);`, kirjoitetaan **aliohjelman sisään**, useimmiten
  `Begin`-aliohjelmaan.
- Kokonaiset aliohjelmat, jotka alkavat esimerkiksi `void LuoKentta()`,
  kirjoitetaan **luokan sisään mutta toisten aliohjelmien ulkopuolelle**.
  Aliohjelmaa ei voi kirjoittaa toisen aliohjelman sisään.
- Rivi `using Jypeli;` on tiedoston alussa ja tulee projektimallista.

## Paikallinen muuttuja vai attribuutti

Muuttuja, joka luodaan aliohjelman sisällä (`PhysicsObject pallo = new
...` `Begin`-aliohjelmassa), on **paikallinen**: se on olemassa vain siinä
aliohjelmassa. Jos toinen aliohjelma, vaikkapa näppäimen käsittelijä,
tarvitsee samaa oliota, on kaksi tapaa.

**Tapa 1: anna olio parametrina.** `Listen`-kutsun loppuun voi lisätä omia
parametreja, jotka Jypeli välittää käsittelijälle.

```csharp,ignore
public override void Begin()
{
    PhysicsObject pallo = new PhysicsObject(40, 40);
    Add(pallo);
    Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Hyppää", pallo);
}

void Hyppaa(PhysicsObject olio)
{
    olio.Hit(new Vector(0, 500));
}
```

Tämä on suositeltava tapa, kun se riittää: aliohjelma toimii millä tahansa
oliolla.

**Tapa 2: tee muuttujasta attribuutti.** Siirrä muuttujan esittely luokan
tasolle ja anna sille arvo `Begin`-aliohjelmassa ilman tyyppiä.

```csharp,ignore
PhysicsObject pallo;      // esittely luokan tasolla

public override void Begin()
{
    pallo = new PhysicsObject(40, 40);   // ei "PhysicsObject" eteen!
    Add(pallo);
}

void Hyppaa()
{
    pallo.Hit(new Vector(0, 500));
}
```

Tavallinen virhe on kirjoittaa `Begin`-aliohjelmaan uudestaan
`PhysicsObject pallo = new ...`. Silloin syntyy uusi paikallinen muuttuja,
joka peittää attribuutin, ja attribuutti jää tyhjäksi (`null`).

Attribuutti sopii asioille, joita on yksi ja joita moni aliohjelma tarvitsee:
pelaaja, pistelaskuri, ajastin. Ks. myös Ohjelmointi 1:n
[luento attribuuteista](https://ohjelmointi1.it.jyu.fi/luennot/luento16/).

## Oliot

Kaikki ruudulla näkyvä on olioita. `PhysicsObject` noudattaa fysiikkaa,
`GameObject` ei. Olio tulee näkyviin vasta, kun se on lisätty peliin
`Add`-aliohjelmalla, ja katoaa, kun sille kutsutaan `Destroy`-metodia. Tarkemmin:
[Olion luominen](../oliot/luonti.md) ja [Oliotyypit](../oliot/oliotyypit.md).

## Koordinaatisto

Kentän **origo (0, 0) on ruudun keskellä**. X kasvaa oikealle ja **y kasvaa
ylöspäin**, kuten matematiikassa (ei kuten useissa muissa
grafiikkakirjastoissa, joissa y kasvaa alaspäin). Koordinaatit ovat Jypelin
omia yksiköitä, eivät näytön pikseleitä. Kuinka suurena olio ruudulla
näkyy, riippuu muun muassa kamerasta.

```bob

                      ^ y
                      |
  "(-100, 50)"●       |
                      |
  --------------------+------------------------------> x
                      | "(0, 0)"
                      |
                      |               ● "(200, -80)"
                      |
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
| **Screen** (ruutu) | Peli-ikkuna. Käyttöliittymän osat, kuten pistenäyttö, asetetaan ruudun eikä kentän mukaan. | `Screen.Width`, `Screen.Top` |

Aloittelijan tavallisin hämmennys: olio on luotu ja lisätty, mutta se ei
näy. Syy on yleensä, että olio on kameran näkymän ulkopuolella. Kutsu
`Camera.ZoomToLevel()` tai tarkista sijainti.

## Fysiikan yksiköt

Fysiikka-arvot käyttävät samoja yksiköitä kuin koordinaatisto. Painovoima
annetaan yksikköinä sekunnissa toiseen, esimerkiksi `Gravity = new Vector(0,
-981)` vastaa tulkintaa "yksi yksikkö on senttimetri". Nopeus on yksikköä
sekunnissa.
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
kelpaa parametriksi, selitetään sivulla [Delegaatit](../tapahtumat/delegaatit.md).

## Aliohjelman parametrit tulevat tapahtumasta

Tapahtumankäsittelijän parametrit määrää tapahtuma, et sinä:

| Tapahtuma | Käsittelijän muoto |
| --- | --- |
| Näppäin, `Keyboard.Listen(..., Kasittelija, "ohje")` | `void Kasittelija()` ja omat lisäparametrit perään |
| Törmäys, `AddCollisionHandler(olio, Kasittelija)` | `void Kasittelija(PhysicsObject tormaaja, PhysicsObject kohde)` |
| Ajastin, `ajastin.Timeout += Kasittelija` | `void Kasittelija()` |
| Olion tuhoutuminen, `olio.Destroyed += Kasittelija` | `void Kasittelija()` |

Jos parametrit ovat väärät, Rider ilmoittaa virheestä `Listen`- tai
`AddCollisionHandler`-rivillä, ei aliohjelman kohdalla. Ks.
[Yleiset virheet](../ekstrat/yleiset-virheet.md).

## Sisältötiedostot

Kuvat, äänet ja kenttätiedostot laitetaan projektin `Content`-kansioon ja
ladataan nimellä: `LoadImage("norsu")`, `LoadSoundEffect("pum")`. Ks.
[Kuvat ja äänet mukaan projektiin](sisallon-tuonti.md).
