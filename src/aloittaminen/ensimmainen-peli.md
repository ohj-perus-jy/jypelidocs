# Ensimmäinen peli

Tällä sivulla tehdään pienin mahdollinen Jypeli-peli: pallo, joka putoaa
lattialle. Samalla nähdään, mihin kohtaan projektia koodi kirjoitetaan.
Tarvitset [luodun Fysiikkapeli-projektin](projektin-luonti.md).

## Mitä projektissa on

Riderin vasemman reunan Explorer-näkymässä on useita tiedostoja. Niistä
kiinnostava on pelin nimen mukainen tiedosto, esimerkiksi `Pong.cs`. Avaa se
tuplaklikkaamalla. Tiedostossa on suunnilleen tämä:

```csharp,ignore
using Jypeli;

public class Pong : PhysicsGame
{
    public override void Begin()
    {
        // TODO: Kirjoita ohjelmakoodisi tähän

        PhoneBackButton.Listen(ConfirmExit, "Lopeta peli");
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta peli");
    }
}
```

`Begin` on aliohjelma, jonka Jypeli suorittaa kerran, kun peli käynnistyy.
Kaikki pelin alustus, kuten hahmojen luominen ja näppäinten asettaminen,
kirjoitetaan `Begin`-aliohjelman aaltosulkujen `{` ja `}` väliin. Rivin
`PhoneBackButton` voi poistaa, sitä tarvitaan vain puhelimella.

## Pallo kentälle

Kirjoita `Begin`-aliohjelmaan kommenttirivin tilalle:

```csharp,feature-jypeli
//-using Jypeli;
//-
//-public class Pong : PhysicsGame
//-{
//-    public override void Begin()
//-    {
PhysicsObject pallo = new PhysicsObject(50, 50);
pallo.Shape = Shape.Circle;
pallo.Color = Color.Red;
Add(pallo);
//-    }
//-}
```

Riveillä tapahtuu tämä:

1. Luodaan fysiikkaolio, jonka leveys ja korkeus ovat 50 yksikköä, ja
   annetaan sille nimi `pallo`.
2. Asetetaan muodoksi ympyrä ja väriksi punainen.
3. Lisätään pallo kentälle. **Ilman `Add`-riviä olio ei näy.**

Aja peli klikkaamalla vihreää kolmiota (**Run**). Pallo on kentän keskellä,
sillä kentän origo on ruudun keskipisteessä. Ikkunan voi sulkea
sulkemispainikkeesta (Windowsissa rasti oikeassa yläkulmassa, Macilla
punainen pallo vasemmassa yläkulmassa) tai Esc-näppäimellä.

## Painovoima ja lattia

Lisää `Begin`-aliohjelmaan pallon jälkeen:

```csharp,feature-jypeli
//-using Jypeli;
//-
//-public class Pong : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-PhysicsObject pallo = new PhysicsObject(50, 50);
//-pallo.Shape = Shape.Circle;
//-pallo.Color = Color.Red;
//-Add(pallo);
//-
Gravity = new Vector(0, -800);
Level.CreateBorders();
//-    }
//-}
```

`Gravity` on painovoima: nolla sivusuunnassa ja 800 alaspäin.
`Level.CreateBorders` tekee kentän reunoille seinät, joten pallo
pysähtyy alareunaan eikä putoa ruudun ulkopuolelle.

## Näppäin, joka tönäisee palloa

Lisää vielä:

```csharp,ignore
Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Pallo hyppää", pallo);
```

Nyt Rider alleviivaa nimen `Hyppaa` punaisella, koska sen nimistä
aliohjelmaa ei ole. Kirjoita se `Begin`-aliohjelman **jälkeen**, sen
sulkevan aaltosulun alapuolelle mutta luokan sisään:

```csharp,ignore
void Hyppaa(PhysicsObject olio)
{
    olio.Hit(new Vector(0, 500));
}
```

Välilyönti antaa pallolle sysäyksen ylöspäin. Koko ohjelma on nyt tämä:

```csharp,feature-jypeli
using Jypeli;

public class Pong : PhysicsGame
{
    public override void Begin()
    {
        PhysicsObject pallo = new PhysicsObject(50, 50);
        pallo.Shape = Shape.Circle;
        pallo.Color = Color.Red;
        Add(pallo);

        Gravity = new Vector(0, -800);
        Level.CreateBorders();

        Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Pallo hyppää", pallo);
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta peli");
    }

    void Hyppaa(PhysicsObject olio)
    {
        olio.Hit(new Vector(0, 500));
    }
}
```

## Mitä seuraavaksi

- [Miten Jypeli-peli toimii](pelin-rakenne.md): mihin koodi kirjoitetaan,
  koordinaatisto, kenttä, kamera ja pelin osat.
- [Pong-opas](../tutoriaalit/pong/index.md): kokonainen peli vaihe kerrallaan.
