# Ajastimet

Ajastimilla voi saada peliin tapahtumia esimerkiksi, että uusia vihollisia ilmestyy aina 10 sekunnin välein. Jos sen sijaan haluat pelissäsi mitata aikaa, katso ohjetta [aikalaskurin tekemisestä](../kayttoliittyma/aikalaskuri.md).

## Ajastimen käyttö

Ajastimen voi luoda seuraavalla tavalla:

```csharp,ignore
Timer ajastin = new Timer();
ajastin.Interval = 1.5;
ajastin.Timeout += LisaaAsteroideja;
ajastin.Start();
```

- `Interval` on aika sekunneissa, jonka välein ajastimeen liitetty tapahtuma suoritetaan.
- `Timeout` on tapahtuma, joka suoritetaan.
- Ajastin pitää muistaa käynnistää `Start`-funktiolla.

Tämän voi myös tehdä lyhyemmin ja nätimmin yhdellä rivillä käyttäen `CreateAndStart`-funktiota:

```csharp,ignore
Timer.CreateAndStart(1.5, LisaaAsteroideja);
```

Jos ajastimen haluaa talteen myöhempää käyttöä varten, `CreateAndStart` palauttaa luomansa ajastimen, jotta sen voi ottaa kiinni muuttujaan.

Ajastimeen liitetyn tapahtuman runko:

```csharp,ignore
void LisaaAsteroideja()
{
    // lisätään asteroideja tässä
}
```

Ajastimen voi halutessaan pysäyttää:

```csharp,ignore
ajastin.Stop();
```

## Ajastimen suorittaminen useita kertoja

Muuten samoin kuin edellä, mutta ajastinta käynnistettäessä kerrotaan kuinka monta kertaa ajastintapahtuma suoritetaan:

```csharp,ignore
ajastin.Start(3);
```

## Ajastimen suorittaminen vain kerran

Jos tarvitsee vain kerran laukeavaa ajastinta, voi käyttää `Timer`-luokan `SingleShot`-metodia. Sille annetaan parametrina (`double`) sekuntimäärä ja aliohjelma, joka suoritetaan annetun ajan kuluttua.

```csharp,ignore
Timer.SingleShot(5.0, LisaaAsteroidi);
```

Yllä `LisaaAsteroidi` on valmis aliohjelma, joka ei ota parametreja. Jos haluat tehdä jotain vähän "erikoisempaa", voit käyttää delegaatteja ([Lisätietoa delegaateista](../ohjelmointi/delegaatit.md)). Alla esimerkki hahmon paikan muuttamisesta.

```csharp,ignore
Timer.SingleShot(5.0,
  delegate { hahmo.Position = hahmo.Aloituspaikka; }
);
```

## Parametrin vieminen aliohjelmalle

Joskus aliohjelmalle tarvitsee viedä jokin olio. Otetaan esimerkiksi tilanne, jossa jokaisen vihollisen pitäisi ampua tietyn ajan välein. Jos vihollisia on monta, oman käsittelijä-aliohjelman kirjoittaminen jokaiselle viholliselle olisi työlästä. Tämähän voitaisiin ratkaista siten, että ampumisen hoitava aliohjelma ottaa vihollisen parametrina. Tälläinen aliohjelma ei kuitenkaan kelpaa ajastimelle suoraan, joten tarvitaan **delegaattia**:

```csharp,ignore
void LuoVihollinen()
{
    PhysicsObject vihollinen = new PhysicsObject(50, 100);
    Add(vihollinen);

    Timer ajastin = new Timer();
    ajastin.Interval = 3.5; // Kuinka usein ajastin "laukeaa" sekunneissa
    ajastin.Timeout += delegate { VihollinenAmpuu(vihollinen); }; // Aliohjelma, jota kutsutaan 3.5 sekunnin välein
    ajastin.Start(); // Ajastin pitää aina muistaa käynnistää
}
```

Ajastimen tapahtumankäsittelijä:

```csharp,ignore
void VihollinenAmpuu(PhysicsObject vihu)
{
    // Tässä ohjelmoidaan vihollisen ampuminen...
}
```

Huomaa:

- Vaikka aliohjelmissa on viholliselle erinimiset muuttujat (`vihollinen` ja `vihu`), ne voivat silti viitata samaan olioon.
- Muuttujaa vihollinen voi käyttää ainoastaan aliohjelman `LuoVihollinen`
- sisällä (koska se on määritelty siellä!). Vastaavasti muuttuja vihu näkyy ainoastaan aliohjelman `VihollinenAmpuu` sisällä. Tämän takia tarvittiin delegaattia vihollis-olion välittämiseen.

## Ajastimen nopeuttaminen

Joskus on tarpeen nopeuttaa tai hidastaa ajastimen aikaväliä kesken pelin. Tällöin ajastinolio tulee viedä parametrina sitä käsittelevälle aliohjelmalle (tai delegaatille). Alla esimerkki, miten aikaväliä voi nopeuttaa välilyöntiä painamalla. Ota huomioon, että `Interval`-välin täytyy olla positiivinen luku.

```csharp,feature-jypeli
using System;
using System.Collections.Generic;
using Jypeli;
using Jypeli.Assets;
using Jypeli.Controls;
using Jypeli.Effects;
using Jypeli.Widgets;

public class AjastinEsimerkki : PhysicsGame
{
    public override void Begin()
    {
        SetWindowSize(1024, 768);
        Level.Background.Image = Image.FromGradient(1024, 768,
                                                    new Color(20, 20, 60),
                                                    new Color(60, 60, 90));
        Timer synnytaOlioita = new Timer();
        synnytaOlioita.Interval = 1.0;
        synnytaOlioita.Timeout += LuoSatunnainenPallo;
        synnytaOlioita.Start();

        Keyboard.Listen(Key.Space, ButtonState.Pressed, MuutaAjastinta, "Nopeuta", synnytaOlioita, -0.1);
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, Exit, "Poistu");
    }

    void MuutaAjastinta(Timer muutettavaAjastin, double muutos)
    {
        if (muutettavaAjastin.Interval + muutos < 0) return;
        muutettavaAjastin.Interval += muutos;
    }

    void LuoSatunnainenPallo()
    {
        PhysicsObject p = new PhysicsObject(10, 10, Shape.Circle);
        p.Position = RandomGen.NextVector(Level.BoundingRect);
        p.Color = RandomGen.NextColor();
        Add(p);
    }
}
```

Vastaavasti jos haluat, että ajastin `a` nopeuttaa ajastimen `b` `Interval`:ia, on tehtävä tässä tapauksessa `a`:lle `Timeout`-delegaatti. Alla oleva koodi tulisi esimerkissämme `Begin`-aliohjelmaan.

```csharp,ignore
Timer olioidenSynnyttamisenNopeutin = new Timer();
olioidenSynnyttamisenNopeutin.Interval = 1.0;
olioidenSynnyttamisenNopeutin.Timeout += delegate
{
    if (synnytaOlioita.Interval - 0.1 <= 0) return;
    synnytaOlioita.Interval -= 0.1;
};
olioidenSynnyttamisenNopeutin.Start();
```

## Katso myös

- [Aikalaskuri](../kayttoliittyma/aikalaskuri.md): ajastin ja laskuri yhdessä.
- [Elinikä](../oliot/elinika.md): olio tuhoutuu itsestään ilman ajastinta.
- [Delegaatit](../ohjelmointi/delegaatit.md): miksi `Timeout += Aliohjelma` toimii.
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti): ajastin attribuutiksi, jotta sen voi pysäyttää toisesta aliohjelmasta.
