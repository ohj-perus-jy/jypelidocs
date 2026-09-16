# Olion käyttäminen pelissä

Oma oliotyyppi käyttäytyy pelissä kuten kantaluokkansa. Tälle sivulle on
koottu, mitä oman tyypin kanssa tehdään `Peli`-luokan puolella: luominen,
monta oliota, törmäykset ja tyypin tunnistaminen.

Tarvitset ensin: [Oman luokan periminen](luokan-periminen.md) ja
[Omat ominaisuudet ja metodit](ominaisuudet.md). Esimerkeissä käytetään
tätä luokkaa:

```csharp,ignore
class Vihu : PhysicsObject
{
    public int Elamat { get; set; }

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Elamat = 3;
        Color = Color.Red;
        Tag = "vihu";
    }

    public void OtaVahinkoa(int maara)
    {
        Elamat -= maara;
        if (Elamat <= 0)
        {
            Destroy();
        }
    }
}
```

## Luominen ja lisääminen

Olio luodaan ja lisätään kuten `PhysicsObject`, vain tyypin nimi vaihtuu.
Kantaluokan ominaisuudet ja omat ominaisuudet ovat käytössä rinnakkain.

```csharp,ignore
Vihu vihu = new Vihu(40, 40);
vihu.Position = new Vector(100, 0);   // kantaluokasta
vihu.Elamat = 5;                      // omasta luokasta
Add(vihu);
```

Kaikki, mikä ottaa parametrikseen `PhysicsObject`-olion, kelpaa myös
`Vihu`-oliolle: `Camera.Follow(vihu)`, `new FollowerBrain(vihu)`,
`AddCollisionHandler(vihu, ...)`, `vihu.Destroy()`.

Jos oliota tarvitaan useassa aliohjelmassa, siitä tehdään attribuutti samoin
kuin muistakin olioista, ks.
[Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti).

```csharp,ignore
Vihu pomo;                    // attribuutti luokan tasolla

public override void Begin()
{
    pomo = new Vihu(80, 80);  // ei "Vihu" eteen!
    Add(pomo);
}
```

## Monta samanlaista oliota

Oma luokka on hyödyllisimmillään, kun olioita on monta: jokainen vihu kantaa
omat elämänsä mukanaan, eikä `Peli`-luokkaan tarvita erillistä muuttujaa
joka vihulle.

```csharp,ignore
for (int i = 0; i < 5; i++)
{
    Vihu vihu = new Vihu(40, 40);
    vihu.Position = new Vector(-200 + i * 100, 100);
    Add(vihu);
}
```

Jos vihuja pitää myöhemmin käydä läpi, esimerkiksi laskea, montako on
jäljellä, ne kerätään listaan. Lista tarvitsee tiedoston alkuun rivin
`using System.Collections.Generic;`.

```csharp,ignore
List<Vihu> vihut = new List<Vihu>();    // attribuutti

void LuoVihut()
{
    for (int i = 0; i < 5; i++)
    {
        Vihu vihu = new Vihu(40, 40);
        vihu.Position = new Vector(-200 + i * 100, 100);
        Add(vihu);
        vihut.Add(vihu);
    }
}

int ElossaOlevia()
{
    int maara = 0;
    foreach (Vihu vihu in vihut)
    {
        if (!vihu.IsDestroyed)
        {
            maara++;
        }
    }
    return maara;
}
```

Toinen tapa on hakea oliot pelistä [tagin](../oliot/olioiden-erottaminen-toisistaan.md)
perusteella: `GetObjectsWithTag("vihu")` palauttaa listan kaikista
pelissä olevista olioista, joilla on kyseinen tagi.

## Törmäyskäsittelijä omalle tyypille

Tavallinen törmäyskäsittelijä saa parametrinsa `PhysicsObject`-tyyppisinä,
jolloin omia ominaisuuksia ei näe:

```csharp,ignore
void VihuTormasi(PhysicsObject tormaaja, PhysicsObject kohde)
{
    tormaaja.Elamat--;    // VIRHE: PhysicsObject ei tiedä elämistä
}
```

Ratkaisu on `AddCollisionHandler`-aliohjelman tyyppiparametrillinen versio,
jossa kulmasulkeissa kerrotaan törmääjän ja kohteen tyypit. Silloin
käsittelijän parametrit saavat olla omaa tyyppiä.

```csharp,ignore
AddCollisionHandler<Vihu, PhysicsObject>(vihu, VihuTormasi);

void VihuTormasi(Vihu vihu, PhysicsObject kohde)
{
    vihu.OtaVahinkoa(1);
}
```

Sama toimii toisin päin, kun pelaaja törmää vihuun. Tagillinen versio
käsittelee kaikki vihut yhdellä käsittelijällä:

```csharp,ignore
AddCollisionHandler<PhysicsObject, Vihu>(pelaaja, "vihu", PelaajaOsuiVihuun);

void PelaajaOsuiVihuun(PhysicsObject pelaaja, Vihu vihu)
{
    vihu.OtaVahinkoa(1);
}
```

Kaikkien olioiden, joilla on tagi `"vihu"`, pitää silloin olla tyyppiä
`Vihu`. Muuten peli kaatuu törmäyksessä, kun Jypeli yrittää antaa
käsittelijälle vääränlaisen olion. Ks. myös
[Törmäysten käsittely](../tapahtumat/tormaykset.md).

## Tyypin tunnistaminen

Kun pelaaja voi törmätä moneen erilaiseen olioon, käsittelijä saa kohteen
`PhysicsObject`-tyyppisenä. Sanalla `is` tarkistetaan, onko kohde vihu, ja
samalla siitä saadaan `Vihu`-tyyppinen muuttuja:

```csharp,ignore
AddCollisionHandler(pelaaja, PelaajaTormasi);

void PelaajaTormasi(PhysicsObject pelaaja, PhysicsObject kohde)
{
    if (kohde is Vihu vihu)
    {
        vihu.OtaVahinkoa(1);
    }
}
```

Toinen tapa on `as`, joka antaa `null`, jos tyyppi ei täsmää:

```csharp,ignore
Vihu vihu = kohde as Vihu;
if (vihu != null)
{
    vihu.OtaVahinkoa(1);
}
```

Oma tyyppi korvaa monessa paikassa
[Tag-ominaisuuden](../oliot/olioiden-erottaminen-toisistaan.md): tyyppi
kertoo jo, mikä olio on kyseessä. Tagia tarvitaan yhä esimerkiksi
`FollowerBrain("pelaaja")`-kutsussa ja silloin, kun samaa tyyppiä olevat
oliot pitää erottaa toisistaan.

## Oma tyyppi käsittelijän parametrina

Näppäimen tai ajastimen käsittelijälle voi antaa oman olion lisäparametrina,
ja käsittelijä saa sen omaa tyyppiä:

```csharp,ignore
Keyboard.Listen(Key.Space, ButtonState.Pressed, Vahingoita, "Vahingoita pomoa", pomo);

void Vahingoita(Vihu vihu)
{
    vihu.OtaVahinkoa(1);
}
```

## Kokonainen esimerkki

Pelaaja hyppii välilyönnillä ja vihut ottavat vahinkoa osumista. Kolmas
osuma tuhoaa vihun.

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
        Shape = Shape.Triangle;
    }

    public void OtaVahinkoa(int maara)
    {
        Elamat -= maara;
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
        Gravity = new Vector(0, -500);
        Level.CreateBorders();

        PhysicsObject pelaaja = new PhysicsObject(40, 40);
        pelaaja.Shape = Shape.Circle;
        pelaaja.Color = Color.Blue;
        pelaaja.Position = new Vector(0, -200);
        Add(pelaaja);

        for (int i = 0; i < 5; i++)
        {
            Vihu vihu = new Vihu(40, 40);
            vihu.Position = new Vector(-200 + i * 100, 150);
            Add(vihu);
        }

        AddCollisionHandler(pelaaja, PelaajaTormasi);
        Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Hyppää", pelaaja);
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, Exit, "Poistu");
    }

    void Hyppaa(PhysicsObject pelaaja)
    {
        pelaaja.Hit(new Vector(RandomGen.NextDouble(-300, 300), 800));
    }

    void PelaajaTormasi(PhysicsObject pelaaja, PhysicsObject kohde)
    {
        if (kohde is Vihu vihu)
        {
            vihu.OtaVahinkoa(1);
            MessageDisplay.Add("Vihulla on elämiä " + vihu.Elamat);
        }
    }
}
```

## Katso myös

- [Törmäysten käsittely](../tapahtumat/tormaykset.md): käsittelijät, tagit ja valmiit käsittelijät.
- [Tapahtumat omassa luokassa](tapahtumat.md): törmäyksen käsittely luokan sisällä.
- [Olioiden Tag-ominaisuus](../oliot/olioiden-erottaminen-toisistaan.md).
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti): attribuutit ja käsittelijän parametrit.
