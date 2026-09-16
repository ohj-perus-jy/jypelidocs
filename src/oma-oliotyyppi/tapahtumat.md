# Tapahtumat omassa luokassa

Oma luokka voi hoitaa itse asioita, jotka muuten kirjoitettaisiin
`Peli`-luokkaan: asettaa omat ohjaimensa, reagoida törmäyksiin, siivota
jälkensä tuhoutuessaan ja ilmoittaa pelille omista tapahtumistaan. Tällä
sivulla ovat tavallisimmat tavat.

Tarvitset ensin: [Oman luokan periminen](luokan-periminen.md) ja
[Muita tapahtumia](../tapahtumat/muita.md).

## Rakentajassa olio ei ole vielä pelissä: AddedToGame {#addedtogame}

Rakentaja ajetaan `new`-rivillä, ennen `Add`-kutsua. Silloin olio ei ole
vielä pelissä, joten rakentajassa ei voi lisätä peliin muita olioita,
asettaa ohjaimia tai kysyä kentän kokoa. Nämä tehdään
`AddedToGame`-tapahtuman käsittelijässä, jonka Jypeli kutsuu heti
`Add`-kutsun jälkeen.

Luokan sisällä pelin aliohjelmiin päästään käsiksi `Game`-sanan kautta:
`Game.Add(...)`, `Game.Level`, `Game.Keyboard`. Alla pelaaja asettaa itse
omat näppäimensä.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Pelaaja : PhysicsObject
{
    public Pelaaja(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Shape = Shape.Circle;
        Color = Color.Blue;
        AddedToGame += AsetaOhjaimet;
    }

    void AsetaOhjaimet()
    {
        Game.Keyboard.Listen(Key.Left, ButtonState.Down, Liiku, "Vasemmalle", -300.0);
        Game.Keyboard.Listen(Key.Right, ButtonState.Down, Liiku, "Oikealle", 300.0);
        Game.Keyboard.Listen(Key.Up, ButtonState.Pressed, Hyppaa, "Hyppää");
    }

    void Liiku(double nopeus)
    {
        Velocity = new Vector(nopeus, Velocity.Y);
    }

    void Hyppaa()
    {
        Hit(new Vector(0, 600));
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Gravity = new Vector(0, -800);
        Level.CreateBorders();

        Pelaaja pelaaja = new Pelaaja(40, 40);
        Add(pelaaja);
    }
}
```

Toinen tyypillinen käyttö on lisätä oliolle osia, kuten kilpi tai pyörät:
ks. esimerkit sivuilla [Muita tapahtumia](../tapahtumat/muita.md#olion-lisaaminen-peliin-addedtogame)
ja [Liitokset](../fysiikka/liitokset.md).

## Törmäys luokan sisällä: Collided

Törmäyskäsittelijä kirjoitetaan yleensä `Peli`-luokkaan
`AddCollisionHandler`-kutsulla (ks.
[Olion käyttäminen pelissä](kaytto.md#tormayskasittelija-omalle-tyypille)).
Jos olion halutaan hoitavan törmäyksensä itse, käytetään fysiikkaolion
`Collided`-tapahtumaa. Se laukeaa, kun olio törmää mihin tahansa.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Vihu : PhysicsObject
{
    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Color = Color.Red;
        Collided += Tormasi;
    }

    void Tormasi(IPhysicsObject vihu, IPhysicsObject kohde)
    {
        if (kohde is Vihu)
        {
            return;                          // toiseen vihuun osuminen ei haittaa
        }
        Color = Color.Darker(Color, 40);     // muuhun osuminen tummentaa
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Gravity = new Vector(0, -800);
        Level.CreateBorders();

        for (int i = 0; i < 4; i++)
        {
            Vihu vihu = new Vihu(50, 50);
            vihu.Position = new Vector(-150 + i * 100, 200);
            Add(vihu);
        }
    }
}
```

Käsittelijän parametrit ovat tyyppiä `IPhysicsObject`, joka on kaikkien
fysiikkaolioiden yhteinen rajapinta. Tyypin tarkistus `is`-sanalla toimii
sille samoin kuin `PhysicsObject`-tyypille. Ensimmäinen parametri on olio
itse, joten sitä ei yleensä tarvita.

## Tuhoutuminen: Destroy-metodin korvaaminen {#destroy}

Kun olio tuhotaan, kutsutaan sen `Destroy`-metodia. Oma luokka voi korvata
sen (`override`) ja tehdä ensin omat siivouksensa: pysäyttää ajastimen,
soittaa äänen, jättää jälkeensä räjähdyksen. Lopuksi kutsutaan
`base.Destroy()`, joka poistaa olion pelistä.

Alla vihu ampuu ajastimella kahden sekunnin välein. Ajastin on pysäytettävä
tuhoutuessa; muuten se jatkaa ampumista, vaikka vihua ei enää ole.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-using Jypeli.Assets;
//-
class Vihu : PhysicsObject
{
    private Timer ampumisajastin;

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Color = Color.Red;
        IgnoresGravity = true;

        ampumisajastin = new Timer();
        ampumisajastin.Interval = 2.0;
        ampumisajastin.Timeout += Ammu;
        AddedToGame += ampumisajastin.Start;   // käyntiin vasta pelissä
    }

    void Ammu()
    {
        PhysicsObject luoti = new PhysicsObject(10, 10);
        luoti.Position = Position + new Vector(0, -Height);
        luoti.Velocity = new Vector(0, -300);
        luoti.IgnoresGravity = true;
        luoti.LifetimeLeft = TimeSpan.FromSeconds(3);
        Game.Add(luoti);
    }

    public override void Destroy()
    {
        if (IsDestroyed)
        {
            return;                  // jo tuhottu, ei toista räjähdystä
        }
        ampumisajastin.Stop();

        Explosion rajahdys = new Explosion(Width * 2);
        rajahdys.Position = Position;
        Game.Add(rajahdys);

        base.Destroy();
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Gravity = new Vector(0, -800);
        Level.CreateBorders();

        Vihu vihu = new Vihu(50, 50);
        vihu.Position = new Vector(0, 200);
        Add(vihu);

        Keyboard.Listen(Key.Space, ButtonState.Pressed, vihu.Destroy, "Tuhoa vihu");
    }
}
```

Räjähdys (`Explosion`) tarvitsee tiedoston alkuun rivin
`using Jypeli.Assets;`. `Destroy` voidaan kutsua useamman kerran, esimerkiksi omasta koodista ja
`ClearAll`-kutsusta. Tarkistus `if (IsDestroyed) return;` estää siivouksen
toistumisen.

Jos korvaamisen sijaan halutaan vain lisätä jotain tuhoutumiseen, riittää
liittää käsittelijä rakentajassa `Destroyed`-tapahtumaan:
`Destroyed += ampumisajastin.Stop;`. Ks.
[Muita tapahtumia](../tapahtumat/muita.md#olion-tuhoutuminen-destroyed).

## Omat tapahtumat

Luokka voi ilmoittaa pelille asioista omalla tapahtumalla, samaan tapaan
kuin `Destroyed`. Tapahtuma esitellään `event`-sanalla, ja luokka laukaisee
sen kutsumalla sitä kuin aliohjelmaa. Pelin puolella siihen liitetään
käsittelijä `+=`-merkinnällä.

Alla vihu laukaisee `Kuoli`-tapahtuman, kun elämät loppuvat. `Destroyed`
ei kelpaisi samaan: se laukeaa myös silloin, kun vihu poistetaan
`ClearAll`-kutsulla kentän vaihtuessa, eikä siitä pidä saada pisteitä.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Vihu : PhysicsObject
{
    public int Elamat { get; set; }

    /// <summary>
    /// Tapahtuu, kun vihun elämät loppuvat.
    /// </summary>
    public event Action Kuoli;

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Elamat = 3;
        Color = Color.Red;
    }

    public void OtaVahinkoa(int maara)
    {
        Elamat -= maara;
        if (Elamat <= 0)
        {
            if (Kuoli != null)
            {
                Kuoli();             // laukaise tapahtuma
            }
            Destroy();
        }
    }
}

public class Peli : PhysicsGame
{
    IntMeter pisteet = new IntMeter(0);

    public override void Begin()
    {
        Vihu vihu = new Vihu(50, 50);
        vihu.Kuoli += LisaaPisteet;
        Add(vihu);

        vihu.OtaVahinkoa(3);         // kokeeksi: laukaisee Kuoli-tapahtuman
        MessageDisplay.Add("Pisteet: " + pisteet.Value);
    }

    void LisaaPisteet()
    {
        pisteet.Value += 10;
    }
}
```

Tarkistus `if (Kuoli != null)` tarvitaan, koska tapahtumaan ei ehkä ole
liitetty yhtään käsittelijää. Lyhyemmin saman voi kirjoittaa
`Kuoli?.Invoke();`.

Tapahtuma voi myös kertoa, kuka sen laukaisi. Silloin se esitellään
`Action<Vihu>`-tyyppisenä ja laukaistaan `Kuoli(this)`, ja käsittelijä saa
vihun parametrina:

```csharp,ignore
public event Action<Vihu> Kuoli;
// ...
Kuoli?.Invoke(this);

// Peli-luokassa:
vihu.Kuoli += VihuKuoli;

void VihuKuoli(Vihu vihu)
{
    MessageDisplay.Add("Vihu kuoli kohdassa " + vihu.Position);
}
```

## Katso myös

- [Muita tapahtumia](../tapahtumat/muita.md): `Destroyed`, `AddedToGame`, `Removed` ja laskurin tapahtumat.
- [Delegaatit](../ohjelmointi/delegaatit.md): parametrien vieminen käsittelijälle.
- [Ajastimet](../tapahtumat/ajastimet.md).
- [Omat käyttöliittymäkomponentit](../kayttoliittyma/omat-kayttoliittymakomponentit.md): ohjaimet `AddedToGame`-tapahtumassa ja `ListenOn`.
