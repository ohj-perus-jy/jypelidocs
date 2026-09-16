# Liitokset

Jypelin käyttämä Farseerphysics-fysiikkakirjasto tarjoaa erilaisia liitoksia, joilla fysiikkaolioita voi liittää toisiinsa.

Jypelissä on toistaiseksi toteutettu muutama tapa liittää fysiikkaolioita toisiinsa.

## Akseliliitos

Useimmin käytetty liitos on `AxleJoint`. Liitokselle on useita käyttötapoja.

### Kahden olion kiinnittäminen toisiinsa

Akseliliitoksella voidaan kiinnittää kaksi oliota toisiinsa niin, että kun ne liikkuvat, niiden etäisyys pysyy vakiona. Tällainen liitos voidaan luoda antamalla AxleJoint-olion rakentajalle kaksi oliota ja piste ensimmäisen kappaleen koordinaateissa, jonka läpi akseli lyödään.

```csharp,ignore
AxleJoint liitos = new AxleJoint(olio1, olio2, akselinPaikka);
```

Jos pistettä ei anneta erikseen, on se oletuksena kappaleiden välin keskipisteessä.

```csharp,ignore
AxleJoint liitos = new AxleJoint(olio1, olio2);
```

Jos lisäksi halutaan, että oliot eivät välitä toistensa törmäyksistä, voidaan ne asettaa [samaan törmäysryhmään](../fysiikka/tormayksen-estaminen.md):

```csharp,ignore
olio1.CollisionIgnoreGroup = 1;
olio2.CollisionIgnoreGroup = 1;
```

Tällä ei tietenkään ole merkitystä, jos kappaleet ovat tarpeeksi kaukana toisistaan.

Liitos pitää vielä lisätä kenttään kaikkien muiden olioiden tapaan:

```csharp,ignore
Add(liitos);
```

```csharp,feature-jypeli
using Jypeli;
using Jypeli.Assets;
using Jypeli.Controls;
using Jypeli.Widgets;
using System;
using System.Collections.Generic;

namespace Liitos2Peli;
public class Liitos2 : PhysicsGame
{
    public override void Begin()
    {
        double w = 100;
        double h = 20;
        double y = 300;

        Level.Background.Color = Color.Black;
        var osa1 = new PhysicsObject(w, h);
        osa1.Position = new Vector(-w, y);
        osa1.MakeStatic();
        osa1.AddCollisionIgnoreGroup(1);
        Add(osa1);

        var osa = osa1;

        for (int i = 0; i < 4; i++)
        {
            var osa2 = new PhysicsObject(w, h);
            osa2.AddCollisionIgnoreGroup(1);
            osa2.Position = new Vector(i*osa.Width, y);
            Add(osa2);
            var liitos = new AxleJoint(osa, osa2, new Vector(osa.Width / 2, 0));
            // liitos.Softness = 0.5;
            Add(liitos);
            osa = osa2;
        }

        Gravity = new Vector(0, -400);
    }
}
```

### Liitoksen pehmeys

Liitokselle voidaan asettaa myös pehmeys, eli kuinka paljon liitos joustaa kappaleidein liikkuessa.

```csharp,ignore
liitos.Softness = 0.5;
```

Suurempi arvo tarkoittaa pienempää joustamista. Hyvin suuren arvon käyttö voi johtaa epäfysikaalisiin ilmiöihin.

### Liitoksen tuhoaminen

Liitoksen tuhoamiseen voidaan käyttää Jypelistä tuttua `Destroy`-metodia. Kun liitos on tuhottu, oliot pääsevät liikkumaan taas vapaasti.

```csharp,ignore
liitos.Destroy();
```

## WheelJoint

Liitos joka on erityisesti tarkoitettu ajoneuvojen renkaita varten. Sisältää sisäänrakennetun moottorin pyöritystä varten.

### Kappaleiden liittäminen toisiinsa

Rengasliitos toimii melko samalla tavalla kuin akseliliitos, jonka pituudeksi olisi asetettu nolla. Liitos kiinnittää kappaleet toisiinsa niin, että liitospisteessä oleva moottori voi pyörittää niitä.

Oletuksena liitos tulee juuri siihen pisteeseen missä toisena annettu kappale on. Tässä tapauksessa renkaan keskipisteeseen:

```csharp,ignore
WheelJoint moottori = new WheelJoint(auto, rengas);
```

Liitokselle voidaan myös antaa vaihtoehtoinen sijainti, jos keskipiste ei ole haluttu:

```csharp,ignore
WheelJoint moottori = new WheelJoint(auto, rengas, new Vector(10,10));
```

Liitoksen ominaisuuksia:

| Nimi | Tyyppi | Selitys |
|:---|:---|:---|
| Axis | Vector | Akseli jonka suhteen liitos joustaa. Oletuksena `Vector.One`, eli joustaa joka suuntaan. Esimerkiksi `Vector.UnitY` tarkoittaa että joustaa ainoastaan pystysuunnassa. |
| DampingRatio | double | Liitoksen oskillaation vaimennuskerroin. |
| Softness | double | Kuinka helposti liitos joustaa. |

Liitoksen moottorille on myös muutamia ominaisuuksia:

| Nimi | Tyyppi | Selitys |
|:---|:---|:---|
| MaxMotorTorque | double | Kuinka kovaa moottori vääntää, vaikuttaa esimerkiksi auton kiihtyvyyteen. |
| MotorSpeed | double | Kuinka nopeasti moottori yrittää pyöriä, radiaaneina sekunnissa. `2 * Math.PI` = yksi kierros sekunnissa. |
| MotorEnabled | bool | Moottori päälle/pois. Pois päältä ollessa rengas pyörii vapaasti. |

Lopuksi liitos pitää muistaa lisätä peliin:

```csharp,ignore
Add(moottori);
```

### Esimerkki

Esimerkki autosta, johon on liitetty kaksi pyörää:

```csharp,feature-jypeli
using System;
using Jypeli;
using Jypeli.Controls;
using Jypeli.Widgets;
using Jypeli.Assets;

namespace AutoPeli;

/// <summary>
/// Sivusta päin kuvattu auto, jossa on kaksi pyörää.
/// </summary>
class Auto : PhysicsObject
{
    public PhysicsObject vasenPyora;
    public PhysicsObject oikeaPyora;

    public WheelJoint vasenLiitos;
    public WheelJoint oikeaLiitos;

    public Auto(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        CollisionIgnoreGroup = 100;

        LinearDamping = 0.998;
        AddedToGame += LisaaPyorat;
    }

    /// <summary>
    /// Käynnistää auton moottorin ja kiihdyttää autoa annettuun nopeuteen
    /// </summary>
    /// <param name="nopeus">Renkaiden pyörimisnopeus radiaaneina sekunnissa</param>
    public void Kaasuta(double nopeus)
    {
        vasenLiitos.MotorSpeed = nopeus;
        oikeaLiitos.MotorSpeed = nopeus;

        vasenLiitos.MotorEnabled = true;
        oikeaLiitos.MotorEnabled = true;
    }

    /// <summary>
    /// Sammuttaa auton moottorin
    /// </summary>
    public void Hidasta()
    {
        vasenLiitos.MotorEnabled = false;
        oikeaLiitos.MotorEnabled = false;
    }

    private void LisaaPyorat()
    {
        PhysicsGame fysiikkaPeli = Game as PhysicsGame;

        vasenPyora = LuoPyora();
        vasenPyora.Position = this.Position + new Vector(-Width / 4, -Height / 2);

        oikeaPyora = LuoPyora();
        oikeaPyora.Position = this.Position + new Vector(Width / 4, -Height / 2);

        vasenLiitos = new WheelJoint(this, vasenPyora);
        vasenLiitos.MaxMotorTorque = 200;
        fysiikkaPeli.Add(vasenLiitos);

        oikeaLiitos = new WheelJoint(this, oikeaPyora);
        oikeaLiitos.MaxMotorTorque = 200;
        fysiikkaPeli.Add(oikeaLiitos);
    }

    public override void Destroy()
    {
        vasenLiitos.Destroy();
        oikeaLiitos.Destroy();
        vasenPyora.Destroy();
        oikeaPyora.Destroy();
        base.Destroy();
    }

    private PhysicsObject LuoPyora()
    {
        double r = Width / 10;
        PhysicsObject pyora = new PhysicsObject(2 * r, 2 * r, Shape.Circle);
        pyora.Color = Color.Gray;
        pyora.CollisionIgnoreGroup = 100;
        pyora.AngularDamping = 0.95;
        pyora.KineticFriction = 1.0;
        Game.Add(pyora);
        return pyora;
    }
}

public class Peli : PhysicsGame
{
    Auto auto;

    public override void Begin()
    {
        LuoKentta();
        AsetaOhjaimet();
        // Kommentoi seuraava pois jos et halua heti lähteä liikkeelle
        Timer.SingleShot(0.1,delegate { auto.Kaasuta(20); });
    }

    void LuoKentta()
    {
        Gravity = new Vector(0, -400);
        Level.CreateBorders();
        Camera.ZoomToLevel();

        auto = new Auto(100, 40);
        auto.Color = Color.Red;
        auto.X = 0;
        auto.Y = Level.Bottom + 40;
        Add(auto);
    }

    void AsetaOhjaimet()
    {
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, Exit, "Poistu");
        Keyboard.Listen(Key.F1, ButtonState.Pressed, ShowControlHelp, "Näytä ohjeet");

        Keyboard.Listen(Key.Left, ButtonState.Pressed, auto.Kaasuta, "Aja vasemmalle", 20.0);
        Keyboard.Listen(Key.Right, ButtonState.Pressed, auto.Kaasuta, "Aja oikealle", -20.0);

        Keyboard.Listen(Key.Left, ButtonState.Released, auto.Hidasta, null);
        Keyboard.Listen(Key.Right, ButtonState.Released, auto.Hidasta, null);
    }
}
```

## Rakenneolio

Rakenneolio eli `PhysicsStructure` voidaan koostaa kahdesta tai useammasta oliosta. Rakenneolio vastaa kaikkien sen osaolioiden liittämistä liitoksilla toisiinsa, mutta lisäksi koko rakennetta voi käskeä esimerkiksi liikkumaan, pyörimään tai muuttamaan väriään.

### Rakenneolion luominen

Rakenteen luomiseen on kaksi vaihtoehtoa. Ensimmäinen näistä on kentällä valmiiksi olevien olioiden lisääminen siihen.

```csharp,ignore
PhysicsObject p1 = new PhysicsObject(2 * 50.0, 2 * 50.0, Shape.Circle);
p1.X = 200;
p1.Y = 200 + 50;
Add(p1);

PhysicsObject p2 = new PhysicsObject(2 * 25.0, 2 * 25.0, Shape.Circle);
p2.X = 200;
p2.Y = 200 + p1.Y + 50 + 25;
Add(p1);

PhysicsObject p3 = new PhysicsObject(2 * 15.0, 2 * 15.0, Shape.Circle);
p3.X = 200;
p3.Y = 200 + p2.Y + 25 + 15;
Add(p1);

PhysicsStructure lumiukko = new PhysicsStructure( p1, p2, p3 );
Add(lumiukko);
```

Toinen vaihtoehto on tehdä rakenne ensin ja vasta sitten lisätä fysiikkaoliot rakenteeseen. Huomaa kuitenkin, että tällä tavalla lisättäessä osaolioiden koordinaatit ovat suhteessa rakenneolion keskipisteeseen, eli esim. seuraava esimerkki vastaa täysin ylläolevaa, vaikka palloille asetetut koordinaatit poikkeavatkin edellisistä.

```csharp,ignore
PhysicsStructure lumiukko = new PhysicsStructure();
lumiukko.X = 200;
lumiukko.Y = 200;
Add(lumiukko);

PhysicsObject p1 = new PhysicsObject(2 * 50.0, 2 * 50.0, Shape.Circle);
p1.X = 0;
p1.Y = 50;
lumiukko.Add(p1);

PhysicsObject p2 = new PhysicsObject(2 * 25.0, 2 * 25.0, Shape.Circle);
p2.X = 0;
p2.Y = p1.Y + 50 + 25;
lumiukko.Add(p2);

PhysicsObject p3 = new PhysicsObject(2 * 15.0, 2 * 15.0, Shape.Circle);
p3.X = 0;
p3.Y = p2.Y + 25 + 15;
lumiukko.Add(p3);
```

### Rakenteen liitosten pehmeys

Oletuksena rakenteen olioiden välisten liitosten pehmeys (`Softness`) on 0, jolloin oliot eivät pääse liikkumaan toistensa suhteen. Arvoa voi kuitenkin muuttaa, ja se vaikuttaa koko rakenteeseen. Yksittäisten liitosten pehmeyttä ei ole mahdollista säätää.

```csharp,ignore
lumiukko.Softness = 3;
```

### Rakenteet ja törmäysten käsittely

Rakenteille on myös mahdollista asettaa törmäyskäsittelijöitä. Näin saadaan törmäystapahtuma kun mikä tahansa rakenteen osista törmää.

```csharp,ignore
void TeeLumiukko()
{
   // luodaan lumiukko...
   lumiukko.Collided += KasitteleLumiukonTormays;
}

void KasitteleLumiukonTormays(IPhysicsObject ukko, IPhysicsObject kohde)
{
   // törmäyksenkäsittelijä
}
```

### Kuuluuko fysiikkaolio rakenteeseen

Jos halutaan tietää, mihin rakenteeseen tietty fysiikkaolio kuuluu, voidaan tiedustella sen `ParentStructure`-ominaisuutta.

```csharp,ignore
if (olio.ParentStructure == ukko)
{
   // olio kuuluu ukkoon, tehdään jotain
}
```

`ParentStructure` on suora viite fysiikkarakenteeseen johon olio kuuluu. Jos olio ei kuulu mihinkään rakenteeseen, `ParentStructure` saa arvon `null`.

```csharp,ignore
if (olio.ParentStructure != null)
{
   olio.ParentStructure.Hit(new Vector(100, 0));
}
```

Ylläoleva esimerkki ensin tarkistaa, kuuluuko olio johonkin rakenteeseen ja jos kuuluu, lyö koko rakennetta suuntaan (100, 0). Jos tarkistusta ei tehdä ja olio ei kuulu mihinkään rakenteeseen, ohjelma kaatuu `NullPointerException`-poikkeukseen (koska yritetään "lyödä tyhjää").
