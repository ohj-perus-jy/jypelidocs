# Pong, vaihe 6: Parantelua

Tässä vaiheessa parantelemme mailojen liikuttelua ja tutustumme `if`-lauseeseen.

![](images/pong-animaatio.gif)

## Rajojen tarkistus

Edellisessä oppaassa laitoimme mailat liikkumaan, mutta pieni puute mailojen liikuttamiseen jäi. Nimittäin mailaa voi liikutella ylös- ja alaspäin rajattomasti! Ei ole varmaankaan hyödyllistä eikä toivottavaa, että mailat voivat mennä pelikentän ulkopuolelle. Tämän korjaamiseksi mailaa pitäisi voida liikuttaa ylöspäin vain silloin, kun se ei ole mennyt kentän yläreunan yli. Vastaavasti alaspäin liikuttamisen pitäisi olla mahdollista vain, kun maila ei ole mennyt alarajan ali.

### Yläreunan tarkistus

Mietitään **algoritmi** eli ohje, jolla saisimme mailan pysymään kentän sisäpuolella. Käsitellään ongelmaa ensin vain kentän yläreunalle ja mietitään alareunaa myöhemmin.

Pitäisi lisätä ohjelmakoodiin ehto, jonka mukaan:

- Jos maila on yläreunan yli,
- niin pysäytetään maila.
- Muuten liikutetaan mailaa normaalisti.

Tällainen tietyllä ehdolla suoritettava koodi voidaan toteuttaa ohjelmoinnissa **`if`-lauseella**. `if`-lause muodostuu **ehdosta** ja koodiriveistä, jotka suoritetaan **vain, jos ehto on totta**. `if`-lauseen perässä olevien aaltosulkujen väliin kirjoitetaan ne koodirivit, jotka halutaan suorittaa vain, jos annettu ehto toteutuu.

**Muokkaa** `AsetaNopeus`-aliohjelmaasi seuraavanlaiseksi:

```csharp,ignore
void AsetaNopeus(PhysicsObject maila, Vector nopeus)
{
    if (maila.Top > Level.Top)
    {
        maila.Velocity = Vector.Zero;
        return;
    }

    maila.Velocity = nopeus;
}
```

Mailan ja kentän yläreunojen y-koordinaatit saadaan niiden `Top`-ominaisuudesta.

Ehdossa katsotaan, onko mailan yläreuna kentän yläreunan yläpuolella:

- Jos on, niin pysäytetään maila ja return-lauseella tullaan pois aliohjelmasta.
- Jos ei, niin `if`-lauseen perässä olevien aaltosulkujen välissä olevia koodirivejä ei suoriteta, vaan asetetaan mailalle nopeus normaaliin tapaan.

> [!KOKEILE]

Pysähtyykö maila yläreunaan? Taitaa kyllä pysähtyä, mutta...

> [!KYSYMYS]
> Miksi maila ei enää liiku, kun se kerran saavuttaa yläreunan? Mieti hetki, ennen kuin jatkat eteenpäin.

### Toinen yritys

Mailat lopettivat liikkumisen, kun ne saavuttivat kentän yläreunan. Vaikka yritämme yläreunan saavuttamisen jälkeen liikuttaa mailaa alaspäin, *mailan yläreuna on yhä kentän yläreunan yläpuolella*. `if`-lauseemme ehto siis toteutuu yhä ja maila pysäytetään.

Täytyy siis lisätä vielä yksi ehto edelliseen algoritmiimme:

- Jos nopeuden suunta on ylöspäin **ja** jos maila on yläreunan yli,
- niin pysäytetään maila.
- Muuten liikutetaan mailaa normaalisti.

Lisätään toinen ehto samaan `if`-lauseeseen `AsetaNopeus`-aliohjelmaan:

```csharp,ignore
void AsetaNopeus(PhysicsObject maila, Vector nopeus)
{
    if ((nopeus.Y > 0) && (maila.Top > Level.Top))
    {
        maila.Velocity = Vector.Zero;
        return;
    }

     maila.Velocity = nopeus;
}
```

Tässä käytettiin `if`-lauseessa merkintää `(nopeus.Y > 0) && (maila.Top > Level.Top)`. Tässä merkit `&&` voi lukea sanana "ja".

Ehdon voisi nyt lukea: "Nopeuden y-koordinaatti on suurempi kuin nolla **JA** mailan yläreunan y-koordinaatti on suurempi kuin kentän yläreunan y-koordinaatti".

> [!KOKEILE]

[Täältä lisätietoa ehtolauseisiin liittyen.](https://ohjelmointi1.it.jyu.fi/luennot/luento6/)

### Alareunan tarkistus

Nyt kun mailan liikuttelu ylöspäin on kunnossa, tee sama alaspäin liikuttamiselle.

Nyt vastaavasti tarkistetaan, onko suunta alaspäin ja onko mailan alareunan y-koordinaatti pienempi kuin kentän alareunan y-koordinaatti.

`AsetaNopeus` näyttää muutosten jälkeen tältä:

```csharp,ignore
void AsetaNopeus(PhysicsObject maila, Vector nopeus)
{
    if ((nopeus.Y < 0) && (maila.Bottom < Level.Bottom))
    {
        maila.Velocity = Vector.Zero;
        return;
    }
    if ((nopeus.Y > 0) && (maila.Top > Level.Top))
    {
        maila.Velocity = Vector.Zero;
        return;
    }

    maila.Velocity = nopeus;
}
```

> [!KOKEILE]

## 3. Xbox-ohjainten lisääminen (valinnainen)

**Jos haluat**, voit lisätä ohjauksen Xbox 360 -ohjaimille seuraavasti. Muuten voit hypätä tutoriaalin [seuraavaan vaiheeseen](vaihe7.md).

Xbox-ohjainten napit voidaan asettaa helposti käyttämällä samantapaista `Listen`-aliohjelmaa kuin näppäimistön nappien asettamisessa. Ainoa ero on, että tällä kertaa ei kutsuta `Keyboard.Listen`-aliohjelmaa vaan `ControllerX.Listen`-aliohjelmaa (X:n paikalle ohjaimen numero: `One`, `Two`, `Three` tai `Four`). Esimerkiksi `ControllerOne.Listen` kutsuu ohjainta, joka on asetettu ykkösohjaimeksi. `ControllerOne.Listen` ottaa ensimmäisenä parametrina Xbox-ohjaimen napin, jota halutaan kuunnella, esimerkiksi `Button.X` tarkoittaa ohjaimen X-nappia.

Tässä tapauksessa voidaan käyttää samaa `AsetaNopeus`-aliohjelmaa myös Xbox-ohjaimille.

Lisää Xbox-ohjainten asetus samaan `AsetaOhjaimet`-aliohjelmaan:

```csharp,ignore
void AsetaOhjaimet()
{
    Keyboard.Listen( Key.A, ButtonState.Down, AsetaNopeus, "Pelaaja 1: Liikuta mailaa ylös", maila1, nopeusYlos );
    Keyboard.Listen( Key.A, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero );
    Keyboard.Listen( Key.Z, ButtonState.Down, AsetaNopeus, "Pelaaja 1: Liikuta mailaa alas", maila1, nopeusAlas );
    Keyboard.Listen( Key.Z, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero );

    Keyboard.Listen( Key.Up, ButtonState.Down, AsetaNopeus, "Pelaaja 2: Liikuta mailaa ylös", maila2, nopeusYlos );
    Keyboard.Listen( Key.Up, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero );
    Keyboard.Listen( Key.Down, ButtonState.Down, AsetaNopeus, "Pelaaja 2: Liikuta mailaa alas", maila2, nopeusAlas );
    Keyboard.Listen( Key.Down, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero );

    Keyboard.Listen( Key.F1, ButtonState.Pressed, ShowControlHelp, "Näytä ohjeet" );
    Keyboard.Listen( Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta peli" );

    ControllerOne.Listen( Button.DPadUp, ButtonState.Down, AsetaNopeus, "Liikuta mailaa ylös", maila1, nopeusYlos );
    ControllerOne.Listen( Button.DPadUp, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero );
    ControllerOne.Listen( Button.DPadDown, ButtonState.Down, AsetaNopeus, "Liikuta mailaa alas", maila1, nopeusAlas );
    ControllerOne.Listen( Button.DPadDown, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero );

    ControllerTwo.Listen( Button.DPadUp, ButtonState.Down, AsetaNopeus, "Liikuta mailaa ylös", maila2, nopeusYlos );
    ControllerTwo.Listen( Button.DPadUp, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero );
    ControllerTwo.Listen( Button.DPadDown, ButtonState.Down, AsetaNopeus, "Liikuta mailaa alas", maila2, nopeusAlas );
    ControllerTwo.Listen( Button.DPadDown, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero );

    ControllerOne.Listen( Button.Back, ButtonState.Pressed, ConfirmExit, "Lopeta peli" );
    ControllerTwo.Listen( Button.Back, ButtonState.Pressed, ConfirmExit, "Lopeta peli" );
}
```

> [!KOKEILE]

## Lopputulos

Tähän asti pelimme näyttää tältä.

```csharp,feature-jypeli
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Jypeli;
using Jypeli.Assets;
using Jypeli.Controls;
using Jypeli.Effects;
using Jypeli.Widgets;

public class Pong : PhysicsGame
{
    Vector nopeusYlos = new Vector(0, 200);
    Vector nopeusAlas = new Vector(0, -200);

    PhysicsObject pallo;
    PhysicsObject maila1;
    PhysicsObject maila2;

    public override void Begin()
    {
        LuoKentta();
        AsetaOhjaimet();
        AloitaPeli();
    }

    void LuoKentta()
    {
        pallo = new PhysicsObject(40.0, 40.0);
        pallo.Shape = Shape.Circle;
        pallo.X = -200.0;
        pallo.Y = 0.0;
        pallo.Restitution = 1.0;
        Add(pallo);

        maila1 = LuoMaila(Level.Left + 20.0, 0.0);
        maila2 = LuoMaila(Level.Right - 20.0, 0.0);

        Level.CreateBorders(1.0, false);
        Level.Background.Color = Color.Black;

        Camera.ZoomToLevel();
    }

    PhysicsObject LuoMaila(double x, double y)
    {
        PhysicsObject maila = PhysicsObject.CreateStaticObject(20.0, 100.0);
        maila.Shape = Shape.Rectangle;
        maila.X = x;
        maila.Y = y;
        maila.Restitution = 1.0;
        Add(maila);
        return maila;
    }

    void AloitaPeli()
    {
        Vector impulssi = new Vector(500.0, 0.0);
        pallo.Hit(impulssi * pallo.Mass);
    }

    void AsetaOhjaimet()
    {
        Keyboard.Listen(Key.A, ButtonState.Down, AsetaNopeus, "Pelaaja 1: Liikuta mailaa ylös", maila1, nopeusYlos);
        Keyboard.Listen(Key.A, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero);
        Keyboard.Listen(Key.Z, ButtonState.Down, AsetaNopeus, "Pelaaja 1: Liikuta mailaa alas", maila1, nopeusAlas);
        Keyboard.Listen(Key.Z, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero);

        Keyboard.Listen(Key.Up, ButtonState.Down, AsetaNopeus, "Pelaaja 2: Liikuta mailaa ylös", maila2, nopeusYlos);
        Keyboard.Listen(Key.Up, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero);
        Keyboard.Listen(Key.Down, ButtonState.Down, AsetaNopeus, "Pelaaja 2: Liikuta mailaa alas", maila2, nopeusAlas);
        Keyboard.Listen(Key.Down, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero);

        Keyboard.Listen(Key.F1, ButtonState.Pressed, ShowControlHelp, "Näytä ohjeet");
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta peli");

        ControllerOne.Listen(Button.DPadUp, ButtonState.Down, AsetaNopeus, "Liikuta mailaa ylös", maila1, nopeusYlos);
        ControllerOne.Listen(Button.DPadUp, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero);
        ControllerOne.Listen(Button.DPadDown, ButtonState.Down, AsetaNopeus, "Liikuta mailaa alas", maila1, nopeusAlas);
        ControllerOne.Listen(Button.DPadDown, ButtonState.Released, AsetaNopeus, null, maila1, Vector.Zero);

        ControllerTwo.Listen(Button.DPadUp, ButtonState.Down, AsetaNopeus, "Liikuta mailaa ylös", maila2, nopeusYlos);
        ControllerTwo.Listen(Button.DPadUp, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero);
        ControllerTwo.Listen(Button.DPadDown, ButtonState.Down, AsetaNopeus, "Liikuta mailaa alas", maila2, nopeusAlas);
        ControllerTwo.Listen(Button.DPadDown, ButtonState.Released, AsetaNopeus, null, maila2, Vector.Zero);

        ControllerOne.Listen(Button.Back, ButtonState.Pressed, ConfirmExit, "Lopeta peli");
        ControllerTwo.Listen(Button.Back, ButtonState.Pressed, ConfirmExit, "Lopeta peli");
    }

    void AsetaNopeus(PhysicsObject maila, Vector nopeus)
    {
        if ((nopeus.Y < 0) && (maila.Bottom < Level.Bottom))
        {
            maila.Velocity = Vector.Zero;
            return;
        }
        if ((nopeus.Y > 0) && (maila.Top > Level.Top))
        {
            maila.Velocity = Vector.Zero;
            return;
        }

        maila.Velocity = nopeus;
    }
}
```
