# Läpsylintu, vaihe 2: Pelaaja liikkeelle

Pelin aloittava `Begin()`-aliohjelma näyttää tällä hetkellä tältä:

```csharp,ignore
public override void Begin()
{
    Gravity = new Vector(0, -1000);

    LuoKentta();
    LisaaNappaimet();

    Camera.Follow(pelaaja1);
    Camera.ZoomFactor = 1.2;
    Camera.StayInLevel = true;

    MasterVolume = 0.5;
}
```

Lisää sen loppuun ennen `}`-merkkiä seuraavat rivit:

```csharp,ignore
Timer liikutusajastin = new Timer();
liikutusajastin.Interval = 0.01;
liikutusajastin.Timeout += SiirraPelaajaaOikeammalle;
liikutusajastin.Start();
```

Huomaat että `SiirraPelaajaaOikeammalle` alleviivaantuu punaisella, ja näytön alareunassa näkyy virheviesti. Koska meillä ei vielä ole `SiirraPelaajaaOikeammalle`-nimistä aliohjelmaa, meidän täytyy luoda sellainen. Tee uusi aliohjelma `Begin`-lohkon jälkeen (eli `}`-merkin alapuolelle):

```csharp,ignore
void SiirraPelaajaaOikeammalle()
{

}
```

Nyt aliohjelmaa kutsutaan aina 0.01 sekunnin välein eli sata kertaa sekunnissa.

Aliohjelma ei kuitenkaan tee vielä mitään, joten lisätään sen sisälle rivi, joka lisää pelaajalle sivuttaissuuntaista liikettä:

```csharp,ignore
pelaaja1.Push(new Vector(NOPEUS, 0.0) * pelaaja1.Mass);
```

Aivan ohjelman alussa on määriteltu `private const double NOPEUS = 200;`. Huomaa, että `NOPEUS` on kirjoitettu isoilla kirjaimilla, mikä tarkoittaa, että kyseessä on vakio (muuttumaton arvo). Aseta NOPEUS-vakion arvoksi 10000:

```csharp,ignore
private const double NOPEUS = 10000;
```

Emme halua, että pelaaja voi liikkua enää itse sivuille nuolinäppäimillä, varsinkaan, kun nopeutena on 10000. Muuten pelihahmo sinkoutuisi oikealle ja vasemmalle todella nopeasti.

Etsi siis aliohjelma LisaaNappaimet ja poista siitä rivit:

```csharp,ignore
Keyboard.Listen(Key.Left, ButtonState.Down, Liikuta, "Liikkuu vasemmalle", pelaaja1, -NOPEUS);
Keyboard.Listen(Key.Right, ButtonState.Down, Liikuta, "Liikkuu vasemmalle", pelaaja1, NOPEUS);
```

sekä rivit:

```csharp,ignore
ControllerOne.Listen(Button.DPadLeft, ButtonState.Down, Liikuta, "Pelaaja liikkuu vasemmalle", pelaaja1, -NOPEUS);
ControllerOne.Listen(Button.DPadRight, ButtonState.Down, Liikuta, "Pelaaja liikkuu oikealle", pelaaja1, NOPEUS);
```

> [!KOKEILE]
