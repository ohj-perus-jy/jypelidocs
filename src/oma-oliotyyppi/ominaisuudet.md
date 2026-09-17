# Omat ominaisuudet ja metodit

Oma luokka on hyödyllinen vasta, kun siinä on jotain, mitä kantaluokassa ei
ole: elämät, pisteet, nopeus tai tieto siitä, onko olio vihainen. Tällä
sivulla luokkaan lisätään omia *ominaisuuksia* (tietoja) ja *metodeja*
(olion omia aliohjelmia).

Tarvitset ensin: [Oman luokan periminen](luokan-periminen.md).

## Ominaisuus

Ominaisuus kirjoitetaan luokan sisään, rakentajan ulkopuolelle:

```csharp,ignore
class Vihu : PhysicsObject
{
    public int Elamat { get; set; }

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Elamat = 3;
    }
}
```

Rivi `public int Elamat { get; set; }` tekee kokonaislukuominaisuuden, jota
voi lukea ja muuttaa pelin puolella aivan kuten `Position`-ominaisuutta:

```csharp,ignore
vihu.Elamat--;
if (vihu.Elamat <= 0)
{
    vihu.Destroy();
}
```

Alkuarvo annetaan rakentajassa. Ilman sitä ominaisuus on nolla
(luvuilla), `false` (totuusarvolla) tai `null` (olioilla).
Ominaisuuksia voi olla monta, ja ne voivat olla mitä tyyppiä tahansa:

```csharp,ignore
class Pelihahmo : PhysicsObject
{
    public int Elamat { get; set; }
    public bool OnHidas { get; set; }
    public double Nopeus { get; set; }
    public Vector Aloituspaikka { get; set; }
    public PhysicsObject Kohde { get; set; }

    public Pelihahmo(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Elamat = 3;
        OnHidas = false;
        Nopeus = 200;
        Aloituspaikka = Vector.Zero;
    }
}
```

`public` tarkoittaa, että ominaisuutta saa käyttää luokan ulkopuolelta,
esimerkiksi `Peli`-luokasta. Tieto, jota tarvitaan vain luokan sisällä,
kirjoitetaan attribuutiksi ilman `public`-sanaa, samoin kuin `Peli`-luokan
attribuutit (ks.
[Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#mihin-koodi-kirjoitetaan)):

```csharp,ignore
class Vihu : PhysicsObject
{
    private Timer ampumisajastin;   // näkyy vain Vihu-luokan sisällä
    // ...
}
```

## Rakentajan parametrit

Jos ominaisuuden arvo halutaan antaa oliota luotaessa, rakentajaan lisätään
parametri:

```csharp,ignore
class Vihu : PhysicsObject
{
    public int Elamat { get; set; }

    public Vihu(double leveys, double korkeus, int elamia)
        : base(leveys, korkeus)
    {
        Elamat = elamia;
    }
}
// ...
Vihu heikko = new Vihu(30, 30, 1);
Vihu vahva = new Vihu(60, 60, 10);
```

Kantaluokan rakentaja tarvitsee aina omat arvonsa `base`-kutsussa, mutta ne voi joko ottaa oman rakentajan parametreina, kuten tässä, tai kirjoittaa suoraan `base`-kutsuun (ks. [Oman luokan periminen](luokan-periminen.md)). Omia parametreja voi lisätä vapaasti.

## Oletusarvot rakentajassa

Rakentaja on hyvä paikka asettaa myös kantaluokan ominaisuuksia, jotka ovat
kaikilla saman tyypin olioilla samat. Silloin niitä ei tarvitse toistaa joka
kerta, kun olio luodaan.

```csharp,ignore
class Vihu : PhysicsObject
{
    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Shape = Shape.Circle;
        Color = Color.Red;
        Tag = "vihu";
        Restitution = 0.5;
        Image = Game.LoadImage("vihu");   // kuva Content-kansiosta
    }
}
```

Luokan sisällä kuva ladataan `Game.LoadImage`-kutsulla, koska `LoadImage`
kuuluu peliin eikä olioon. Samoin muut Jypelin valmiit pelin aliohjelmat ja
ominaisuudet löytyvät `Game`-sanan takaa: `Game.Level`, `Game.Add(...)`,
`Game.Keyboard`. `Peli`-luokkaan itse kirjoitetut attribuutit ja aliohjelmat
eivät löydy, ks. [Kun olio tarvitsee jotain pelistä](paivitys.md#peli).

## Laskuri ominaisuutena

Elämät voi tehdä myös [laskurina](../kayttoliittyma/pistelaskuri.md) (`IntMeter`).
Laskurilla on ala- ja yläraja, ja se laukaisee tapahtuman, kun raja
saavutetaan. Alla vihu tuhoaa itsensä, kun elämät loppuvat, eikä pelin
puolella tarvitse tarkistaa mitään.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Vihu : PhysicsObject
{
    public IntMeter Elamat { get; private set; }

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Color = Color.Red;
        Elamat = new IntMeter(3, 0, 3);   // alkuarvo, pienin, suurin
        Elamat.LowerLimit += Destroy;     // kun elämät menevät nollaan
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Vihu terve = new Vihu(50, 50);
        terve.Position = new Vector(-100, 0);
        Add(terve);

        Vihu haavoittunut = new Vihu(50, 50);
        haavoittunut.Position = new Vector(100, 0);
        Add(haavoittunut);

        haavoittunut.Elamat.Value -= 3;   // vihu tuhoutuu itsestään
        MessageDisplay.Add("Oikea vihu tuhoutui: " + haavoittunut.IsDestroyed);
    }
}
```

`private set` tarkoittaa, että laskurin arvoa saa muuttaa pelin puolella
(`vihu.Elamat.Value--`), mutta itse laskuria ei voi vaihtaa toiseen.
Laskurin saa näkyviin ruudulle palkkina, ks.
[Etenemispalkki](../kayttoliittyma/etenemispalkki.md).

## Omat metodit

Toistuva toimenpide kannattaa kirjoittaa luokan omaksi aliohjelmaksi eli
*metodiksi*. Silloin pelin puolella lukee `vihu.OtaVahinkoa(1)` eikä kolmea
riviä elämien vähentämistä ja tarkistamista, ja vihun sisäiset asiat pysyvät
vihun sisällä.

```csharp,feature-jypeli
//-using System;
//-using Jypeli;
//-
class Vihu : PhysicsObject
{
    public int Elamat { get; set; }

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Elamat = 3;
        Color = Color.Red;
    }

    /// <summary>
    /// Vähentää vihun elämiä. Kun elämät loppuvat, vihu tuhoutuu.
    /// </summary>
    /// <param name="maara">Kuinka monta elämää menetetään.</param>
    public void OtaVahinkoa(int maara)
    {
        Elamat -= maara;
        Color = Color.Darker(Color, 60);   // tummenee joka osumasta
        if (Elamat <= 0)
        {
            Destroy();
        }
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Vihu vihu = new Vihu(50, 50);
        Add(vihu);

        vihu.OtaVahinkoa(1);
        MessageDisplay.Add("Elämiä jäljellä: " + vihu.Elamat);
    }
}
```

Luokan sisällä kantaluokan aliohjelmia (`Destroy`, `Hit`, `Push`) kutsutaan
suoraan ilman olion nimeä. Metodi voi myös palauttaa arvon tai käyttää
parametrinaan toista oliota:

```csharp,ignore
/// <summary>
/// Onko vihulla enää yksi elämä jäljellä.
/// </summary>
public bool OnKuolemaisillaan()
{
    return Elamat == 1;
}

/// <summary>
/// Antaa vihulle sysäyksen kohti annettua oliota.
/// </summary>
public void SyoksyKohti(PhysicsObject kohde, double voima)
{
    Vector suunta = kohde.Position - Position;
    Hit(Vector.FromLengthAndAngle(voima, suunta.Angle));
}
```

## Katso myös

- [Olion käyttäminen pelissä](kaytto.md): ominaisuudet ja metodit törmäyskäsittelijässä.
- [Tapahtumat omassa luokassa](tapahtumat.md): kun elämien loppumisesta pitää kertoa pelille.
- [Pistelaskuri](../kayttoliittyma/pistelaskuri.md) ja [Etenemispalkki](../kayttoliittyma/etenemispalkki.md): laskurin näyttäminen.
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti): attribuutti vai paikallinen muuttuja.
