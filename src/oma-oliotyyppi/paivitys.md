# Oma päivitysmetodi

Jypeli päivittää pelin tilan 60 kertaa sekunnissa (ks.
[Mitä konepellin alla tapahtuu](../ekstrat/konepellin-alla.md#mita-yksi-paivitys-tekee)).
Oma luokka voi osallistua päivitykseen: sen `Update`-metodia kutsutaan joka
päivityksellä, ja siihen kirjoitetaan olion oma käyttäytyminen, esimerkiksi
kääntyminen kohti pelaajaa tai tarkistus, onko olio pudonnut kentän
ulkopuolelle.

Tarvitset ensin: [Oman luokan periminen](luokan-periminen.md).

## Kaksi asiaa

1. Rakentajassa asetetaan `IsUpdated = true`. Ilman sitä Jypeli ei kutsu
   olion `Update`-metodia lainkaan. Oletus on `false`, jotta tuhannet
   seinäpalikat eivät hidasta peliä turhilla kutsuilla.
2. Luokkaan kirjoitetaan `public override void Update(Time time)`. Se tekee
   omat asiat ja kutsuu lopuksi `base.Update(time)`.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Pyorija : GameObject
{
    public Pyorija(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Shape = Shape.Star;
        Color = Color.Yellow;
        IsUpdated = true;                        // 1. pyydä päivityksiä
    }

    public override void Update(Time time)       // 2. tehdään joka päivityksellä
    {
        double sekunteja = time.SinceLastUpdate.TotalSeconds;
        Angle += Angle.FromDegrees(90 * sekunteja);   // 90 astetta sekunnissa
        base.Update(time);
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Pyorija tahti = new Pyorija(100, 100);
        Add(tahti);
    }
}
```

Parametri `time` kertoo ajan: `time.SinceLastUpdate` on edellisestä
päivityksestä kulunut aika (normaalisti 1/60 sekuntia) ja
`time.SinceStartOfGame` pelin alusta kulunut aika. Molemmat ovat
`TimeSpan`-tyyppiä, ja `.TotalSeconds` muuntaa ne sekunneiksi
(`double`). Kun nopeus kerrotaan kuluneella ajalla, liike on yhtä nopea,
vaikka päivitysväli vaihtelisi.

Fysiikkaoliota ei yleensä siirretä suoraan `Position`-ominaisuudella eikä
pyöritetä kasvattamalla `Angle`-ominaisuutta, koska fysiikkamoottori
liikuttaa sitä samaan aikaan. Fysiikkaoliolle asetetaan `Update`-metodissa
mieluummin `Velocity` tai `AngularVelocity`. Olion saa silti suunnata
menosuuntaansa asettamalla `Angle`-ominaisuuden, kuten alla oleva ohjus
tekee.

## Esimerkki: ohjus seuraa pelaajaa

Ohjus saa kohteensa rakentajan parametrina ja suuntaa nopeutensa joka
päivityksellä kohti sitä. Nuolinäppäimet liikuttavat pelaajaa; kenttä on
kuvattu ylhäältä, joten painovoimaa ei ole.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-using Jypeli.Assets;
//-
class Ohjus : PhysicsObject
{
    public PhysicsObject Kohde { get; set; }
    public double Nopeus { get; set; }

    public Ohjus(PhysicsObject kohde)
        : base(30, 10)
    {
        Kohde = kohde;
        Nopeus = 150;
        Color = Color.Orange;
        IsUpdated = true;
    }

    public override void Update(Time time)
    {
        if (Kohde != null && !Kohde.IsDestroyed)
        {
            Vector suunta = Kohde.Position - Position;
            Velocity = Vector.FromLengthAndAngle(Nopeus, suunta.Angle);
            Angle = suunta.Angle;
        }
        base.Update(time);
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Level.CreateBorders();

        PhysicsObject pelaaja = new PhysicsObject(40, 40);
        pelaaja.Shape = Shape.Circle;
        pelaaja.Color = Color.Blue;
        Add(pelaaja);

        Ohjus ohjus = new Ohjus(pelaaja);
        ohjus.Position = new Vector(-300, 200);
        Add(ohjus);

        AddCollisionHandler<Ohjus, PhysicsObject>(ohjus, OhjusOsui);

        Keyboard.Listen(Key.Left, ButtonState.Down, Liikuta, "Vasemmalle", pelaaja, new Vector(-300, 0));
        Keyboard.Listen(Key.Right, ButtonState.Down, Liikuta, "Oikealle", pelaaja, new Vector(300, 0));
        Keyboard.Listen(Key.Up, ButtonState.Down, Liikuta, "Ylös", pelaaja, new Vector(0, 300));
        Keyboard.Listen(Key.Down, ButtonState.Down, Liikuta, "Alas", pelaaja, new Vector(0, -300));
    }

    void Liikuta(PhysicsObject olio, Vector nopeus)
    {
        olio.Velocity = nopeus;
    }

    void OhjusOsui(Ohjus ohjus, PhysicsObject kohde)
    {
        Explosion rajahdys = new Explosion(80);
        rajahdys.Position = ohjus.Position;
        Add(rajahdys);
        ohjus.Destroy();
    }
}
```

Räjähdys (`Explosion`) tarvitsee tiedoston alkuun rivin
`using Jypeli.Assets;`, ks. [Räjähdykset](../grafiikka/rajahdykset.md).

## Muista base.Update

Kantaluokan `Update` hoitaa aivot, eliniän, lapsioliot, värähtelyn ja
fysiikkaolion nopeusrajat. Jos `base.Update(time)` jää pois, ne lakkaavat
toimimasta. Kutsu sitä aina, yleensä metodin lopussa.

## Milloin Updatea kutsutaan

- Vasta kun olio on lisätty peliin `Add`-kutsulla. Rakentajassa olio ei
  vielä ole pelissä, ks.
  [Tapahtumat omassa luokassa](tapahtumat.md#addedtogame).
- Ei, kun peli on tauolla (`Pause`). Käyttöliittymän osat (`Widget`)
  päivittyvät tauollakin.
- Tuhotulle oliolle vielä kerran: olio poistuu pelistä vasta seuraavalla
  päivityksellä, ja sen `Update` ajetaan sitä ennen. Kantaluokan `Update`
  ei silloin tee mitään, mutta oma koodi ajetaan. Jos `Update` muuttaa
  jotain olion ulkopuolella, kuten laskuria, aloita se tarkistuksella
  `if (IsDestroyed) return;` (esimerkki:
  [Pelin tiedot olion sisällä](pelin-tiedot.md#1-anna-tarvittava-olio-rakentajassa)).
- `IsUpdated` menee päälle itsestään, kun oliolle annetaan aivot (`Brain`),
  elinikä (`LifetimeLeft`) tai nopeusraja (`MaxVelocity`), ja
  `PlatformCharacter`-hahmolla se on aina päällä. Omassa luokassa se
  kannattaa silti asettaa itse, niin `Update` toimii varmasti.
- `IsUpdated = false` lopettaa päivitykset, myös aivot ja eliniän.

Missä kohtaa pelin päivitystä olioiden `Update` ajetaan, näkyy sivun
[Mitä konepellin alla tapahtuu](../ekstrat/konepellin-alla.md#mita-yksi-paivitys-tekee)
taulukosta.

## Tavallisia käyttötapoja

Katkelmat kirjoitetaan `Update`-metodiin ennen `base.Update`-kutsua.

```csharp,ignore
// Tuhoudu, kun olio putoaa kentän alareunan alapuolelle
if (Y < Game.Level.Bottom - 100)
{
    Destroy();
}
```

```csharp,ignore
// Käänny menosuuntaan (jatkuvaan pyörittämiseen fysiikkaoliolla
// katso CanRotate ja AngularVelocity)
if (Velocity.Magnitude > 1)
{
    Angle = Velocity.Angle;
}
```

```csharp,ignore
// Vaihda väriä sen mukaan, onko pelaaja lähellä
double etaisyys = (Kohde.Position - Position).Magnitude;
if (etaisyys < 200)
{
    Color = Color.Red;
}
else
{
    Color = Color.Green;
}
```

```csharp,ignore
// Tee jotain kerran sekunnissa; aikaaKertynyt on luokan attribuutti (double)
aikaaKertynyt += time.SinceLastUpdate.TotalSeconds;
if (aikaaKertynyt >= 1.0)
{
    aikaaKertynyt = 0;
    Ammu();
}
```

Viimeiseen tapaukseen [ajastin](../tapahtumat/ajastimet.md) on yleensä
selkeämpi. Ajastimen käyttö omassa luokassa on sivulla
[Tapahtumat omassa luokassa](tapahtumat.md#destroy).

Katkelmissa `Game.Level` on pelin kenttä. Mitä muuta `Game`-sanan kautta
löytyy ja miten `Update` pääsee käsiksi pelin pistelaskuriin tai muuhun
`Peli`-luokkaan itse kirjoitettuun, on sivulla
[Pelin tiedot olion sisällä](pelin-tiedot.md).

## Vaihtoehto: omat aivot

Jos sama käyttäytyminen halutaan antaa monelle erityyppiselle oliolle, sen
voi kirjoittaa omiksi [aivoiksi](../oliot/tekoaly.md) (`Brain`) oman
oliotyypin sijaan. Aivoilla on oma `Update`, ja niiden omistaja löytyy
`Owner`-ominaisuudesta. `IsUpdated` menee päälle itsestään, kun aivot
annetaan oliolle.

```csharp,ignore
class Seuraajaaivot : Brain
{
    public PhysicsObject Kohde { get; set; }

    public Seuraajaaivot(PhysicsObject kohde)
    {
        Kohde = kohde;
    }

    protected override void Update(Time time)
    {
        Vector suunta = Kohde.Position - Owner.Position;
        Owner.Position += Vector.FromLengthAndAngle(2, suunta.Angle);
        base.Update(time);
    }
}
// ...
vihu.Brain = new Seuraajaaivot(pelaaja);
```

Valmiita aivoja, kuten `FollowerBrain`, kannattaa käyttää, kun ne riittävät.

## Suorituskyky

`Update` ajetaan 60 kertaa sekunnissa jokaiselle oliolle, jolla
`IsUpdated` on päällä. Pidä se kevyenä: älä lataa kuvia tai luo uusia olioita
joka päivityksellä, äläkä aseta `IsUpdated = true` olioille, jotka eivät
tarvitse sitä.

## Katso myös

- [Mitä konepellin alla tapahtuu](../ekstrat/konepellin-alla.md): päivityssilmukka ja mitä yhdessä päivityksessä tapahtuu.
- [Ajastimet](../tapahtumat/ajastimet.md): kun jotain tehdään säännöllisin väliajoin.
- [Aivot ja tekoäly](../oliot/tekoaly.md): valmiit aivot.
- [Tapahtumat omassa luokassa](tapahtumat.md): `AddedToGame`, `Destroy` ja omat tapahtumat.
- [Pelin tiedot olion sisällä](pelin-tiedot.md): `Game`-sana ja pelin laskurit `Update`-metodissa.
