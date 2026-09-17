# Kulma

Etäisyyksien lisäksi monesti on oleellista tietää kulma. Vektoreiden käyttäminen vähentää kulmien käyttöä, mutta ei poista sitä kokonaan. Esimerkiksi tankkipelissä on tärkeää tietää, missä kulmassa tykin piippu on, ennen kuin sillä ammutaan.

Kulmia varten on Jypelissä erillinen luokka Angle, joka on riippumaton käytettävästä asteikosta. Sitä käyttämällä ei tarvitse huolehtia, onko kulma asteina, radiaaneina vai jonakin erikoisempana mittayksikkönä, kuten tykistössä käytettävinä 6000-jakoisina piiruina.

## Kulman luominen

Nollakulman luominen on yksinkertaista:

```csharp,ignore
Angle kulma = Angle.Zero;
```

Kulman voi luoda myös tunnetusta aste- tai radiaaniluvusta. Seuraavassa esimerkissä luodaan kaksi suoraa kulmaa:

```csharp,ignore
Angle suora1 = Angle.FromDegrees(90);
Angle suora2 = Angle.FromRadians(Math.PI / 2);
```

## Kulman arvo

Kulman numeraalisen arvon saa

```csharp,ignore
double asteina = kulma.Degrees;
double radiaaneina = kulma.Radians;
```

Palautettu kulma on väliltä -180...180, tai -Pi...Pi.

## Laskuoperaatiot

Kulmia voi laskea yhteen, vähentää, kertoa vakioarvolla tai vaihtaa niiden merkkiä.

```csharp,ignore
Angle a = Angle.FromDegrees(90);
Angle b = Angle.FromDegrees(60);

Angle c = a + b;
Angle d = -b;
Angle e = 2 * c - d;
```

Osaatko sanoa, mitä tulee kulmaksi **e**?

## Vektorien kulmat

Vektorityypillä **Vector** on myös kulma. Vektorin `v` kulma on `v.Angle`.

## Olioiden kulmat

Myös olioilla, kuten `GameObject`- ja `PhysicsObject`-olioilla, on kulma. Olioiden kulman saa selville niiden `Angle`-ominaisuudesta:

```csharp,ignore
Angle olionKulma = olio.Angle;
```
