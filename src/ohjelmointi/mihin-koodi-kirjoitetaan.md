# Mihin koodi kirjoitetaan

Ohjeissa on paljon yksittäisiä koodirivejä. Tämä sivu kertoo, mihin kohtaan
tiedostoa rivi kuuluu ja miten yksi olio saadaan näkymään useammassa
aliohjelmassa.

## Kolme paikkaa

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
  `Add(olio);`, kirjoitetaan **aliohjelman sisään**, useimmiten `Begin`-
  aliohjelmaan.
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

## Aliohjelman parametrit tulevat tapahtumasta

Tapahtumankäsittelijän parametrit määrää tapahtuma, ei sinä:

| Tapahtuma | Käsittelijän muoto |
| --- | --- |
| Näppäin, `Keyboard.Listen(..., Kasittelija, "ohje")` | `void Kasittelija()` ja omat lisäparametrit perään |
| Törmäys, `AddCollisionHandler(olio, Kasittelija)` | `void Kasittelija(PhysicsObject tormaaja, PhysicsObject kohde)` |
| Ajastin, `ajastin.Timeout += Kasittelija` | `void Kasittelija()` |
| Olion tuhoutuminen, `olio.Destroyed += Kasittelija` | `void Kasittelija()` |

Jos parametrit ovat väärät, Rider ilmoittaa virheestä `Listen`- tai
`AddCollisionHandler`-rivillä, ei aliohjelman kohdalla. Ks.
[Yleiset virheet](yleiset-virheet.md) ja [Delegaatit](delegaatit.md).
