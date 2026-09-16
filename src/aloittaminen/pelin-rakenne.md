# Miten Jypeli-peli toimii

Tämä sivu kertoo, mistä osista Jypeli-peli koostuu ja mitä sanat kenttä,
kamera ja ruutu tarkoittavat. Tietoa tarvitaan lähes joka ohjeessa.

## Peli on luokka, Begin sen alku

Peli on C#-luokka, joka perii Jypelin `PhysicsGame`-luokan (tai `Game`, jos
fysiikkaa ei tarvita). Jypeli kutsuu pelin `Begin`-aliohjelmaa kerran
käynnistyksessä. Sen jälkeen Jypeli pyörittää *pelisilmukkaa* itse: se
siirtää olioita, laskee törmäykset, piirtää ruudun ja kutsuu sinun
aliohjelmiasi, kun jotain tapahtuu (näppäintä painetaan, ajastin laukeaa,
oliot törmäävät). Omaa silmukkaa ei siis kirjoiteta.

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

## Sisältötiedostot

Kuvat, äänet ja kenttätiedostot laitetaan projektin `Content`-kansioon ja
ladataan nimellä: `LoadImage("norsu")`, `LoadSoundEffect("pum")`. Ks.
[Kuvat ja äänet mukaan projektiin](sisallon-tuonti.md).
