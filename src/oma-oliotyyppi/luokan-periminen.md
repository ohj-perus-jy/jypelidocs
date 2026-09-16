# Oman luokan periminen

Oma oliotyyppi tehdään *perimällä* uusi luokka jostakin Jypelin luokasta,
useimmiten `PhysicsObject`-luokasta. Perivä luokka saa kaikki kantaluokan
ominaisuudet (`Position`, `Color`, `Mass`, ...) ja aliohjelmat (`Push`,
`Destroy`, ...), ja niiden lisäksi siihen kirjoitetaan omat lisäykset.

## Pienin mahdollinen oma luokka

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
        Shape = Shape.Triangle;
    }
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Vihu vihu = new Vihu(50, 50);
        vihu.Position = new Vector(100, 0);
        Add(vihu);
    }
}
```

Rivi `class Vihu : PhysicsObject` tarkoittaa: `Vihu` on `PhysicsObject`.
Kaikki, mikä toimii `PhysicsObject`-oliolle, toimii myös `Vihu`-oliolle:
`Add`, `Position`, törmäykset, painovoima ja niin edelleen.

Luokan sisällä rivi `Color = Color.Red;` tarkoittaa samaa kuin
`vihu.Color = Color.Red;` pelin puolella. Luokan sisällä oliolla ei ole
nimeä, vaan sen omiin ominaisuuksiin viitataan suoraan (tai sanalla `this`).

## Rakentaja ja base

Rakentaja on aliohjelma, joka ajetaan, kun olio luodaan `new`-sanalla.
Sillä on sama nimi kuin luokalla eikä lainkaan paluutyyppiä.

Fysiikkaolio tarvitsee luotaessa leveyden ja korkeuden. Ne välitetään
kantaluokalle rivillä `: base(leveys, korkeus)`, joka kutsuu
`PhysicsObject`-luokan omaa rakentajaa. Ilman `base`-riviä kääntäjä
ilmoittaa virheen *There is no argument given that corresponds to the
required parameter 'width'*.

`base`-kutsun parametrien pitää vastata jotakin kantaluokan rakentajaa.
`PhysicsObject`-luokalla niitä on useita:

```csharp,ignore
: base(leveys, korkeus)                    // leveys ja korkeus
: base(leveys, korkeus, Shape.Circle)      // ja muoto
: base(leveys, korkeus, x, y)              // ja paikka
: base(animaatio)                          // koko kuvasta tai animaatiosta
```

Oman rakentajan parametrien ei tarvitse olla samat kuin kantaluokan. Jos
kaikki vihut ovat samankokoisia, koon voi kirjoittaa suoraan `base`-kutsuun,
jolloin oliota luotaessa ei anneta mitään:

```csharp,ignore
class Vihu : PhysicsObject
{
    public Vihu()
        : base(40, 40)
    {
    }
}
// ...
Vihu vihu = new Vihu();
```

Omia parametreja, kuten elämien määrä, voi lisätä vapaasti; ks.
[Omat ominaisuudet ja metodit](ominaisuudet.md#rakentajan-parametrit).

## Mistä luokasta peritään

| Kantaluokka | Milloin | Huomaa |
| --- | --- | --- |
| `PhysicsObject` | Olio törmää ja siihen vaikuttaa painovoima. Tavallisin valinta. | |
| `GameObject` | Olio ei tarvitse fysiikkaa: koriste, tähtäin, paikallaan pysyvä kerättävä esine. Kevyempi kuin fysiikkaolio. | Ei törmäyksiä, joten `AddCollisionHandler` ei toimi. |
| `PlatformCharacter` | Tasohyppelyn hahmo, jolla on `Walk` ja `Jump`. | Tarvitsee `using Jypeli.Assets;`. |
| `Widget` | Käyttöliittymän osa, joka piirtyy ruudun päälle. | Ks. [Omat käyttöliittymäkomponentit](../kayttoliittyma/omat-kayttoliittymakomponentit.md). |

Esimerkiksi tasohyppelyn pelaaja:

```csharp,ignore
using Jypeli.Assets;

class Pelaaja : PlatformCharacter
{
    public Pelaaja(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        Color = Color.Blue;
    }
}
```

Oman luokan voi periä myös omasta luokasta: `class Pomo : Vihu` on vihu,
jolla on jotain lisää. Mitä kantaluokat osaavat, on koottu sivulle
[Oliotyypit](../oliot/oliotyypit.md).

## Mihin luokka kirjoitetaan

Luokka kirjoitetaan **toisen luokan ulkopuolelle**, ei `Peli`-luokan eikä
minkään aliohjelman sisään. Kaksi tapaa:

1. **Oma tiedosto**, esimerkiksi `Vihu.cs` samassa projektissa. Riderissä
   klikkaa projektia hiiren oikealla, valitse **Add** › **Class** ja anna nimeksi
   `Vihu`. Rider tekee tiedoston, jonka alkuun lisätään `using Jypeli;`.
   Tämä on selkein tapa, kun luokka on pitkä.
2. **Sama tiedosto** kuin `Peli`-luokka, sen yläpuolelle tai alapuolelle.
   Riittää pienelle luokalle.

```csharp,ignore
using Jypeli;

class Vihu : PhysicsObject
{
    // vihun omat asiat
}

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        // vanha tuttu Begin
    }
}
```

Jos `Peli`-luokan tiedostossa on `namespace`-rivi, oma luokka kirjoitetaan
sen alapuolelle samaan tapaan kuin `Peli`-luokka.

## Yleisiä virheitä

- *There is no argument given that corresponds to the required parameter
  'width'*: `base`-kutsu puuttuu tai sen parametrit eivät vastaa mitään
  kantaluokan rakentajaa.
- *The type or namespace name 'PhysicsObject' could not be found*:
  tiedoston alusta puuttuu `using Jypeli;`.
- Kääntäjä valittaa aaltosuluista tai puolipisteistä luokan kohdalla:
  luokka on vahingossa aliohjelman sisällä. Siirrä se `Peli`-luokan
  ulkopuolelle.
- Olio ei näy: `Add(vihu)` puuttuu, aivan kuten muillakin olioilla.

## Katso myös

- [Omat ominaisuudet ja metodit](ominaisuudet.md): elämät, nopeus ja olion omat aliohjelmat.
- [Olion käyttäminen pelissä](kaytto.md): luominen, törmäykset ja tyypin tunnistaminen.
- [Oliotyypit](../oliot/oliotyypit.md): mitä `GameObject`, `PhysicsObject` ja `PlatformCharacter` osaavat.
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#mihin-koodi-kirjoitetaan): attribuutit, `Begin` ja omat aliohjelmat.
