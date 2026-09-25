# Piirtäminen Canvakselle

Yleensä kaikki pelissä näkyvä on [olioita](../oliot/index.md): olio luodaan
kerran ja lisätään peliin `Add`-kutsulla, minkä jälkeen Jypeli muistaa sen ja
huolehtii sen piirtämisestä, liikkeestä ja törmäyksistä. `Paint`-aliohjelmassa
piirretään sen sijaan suoraan ruudulle, eikä Jypeli muista piirrettyä: viiva
näkyy vain sen yhden ruudunpäivityksen ajan, jolla se piirrettiin. Siksi Jypeli
kutsuu `Paint`-aliohjelmaa jokaisella ruudunpäivityksellä, 60 kertaa
sekunnissa, ja kaikki, minkä halutaan pysyvän näkyvissä, piirretään joka kerta
uudelleen. Piirretty viiva ei törmää mihinkään, eikä sitä tarvitse tuhota: kun
sitä ei enää haluta, se jätetään piirtämättä. `Paint` sopii siis pelkkään
kuvaan, joka muuttuu koko ajan, kuten tähtäysviivaan, kahden olion välille
vedettyyn naruun tai kuvaajaan. Kaikki, mihin pitää voida törmätä tai minkä
pitää liikkua fysiikan mukaan, tehdään olioina.

Piirtämistä varten peliluokkaan lisätään `Paint`-aliohjelma. Tämä piirtää
janan pisteestä (−200, −100) pisteeseen (200, 100):

```csharp,feature-jypeli
//-using Jypeli;
//-
//-public class Peli : Game
//-{
protected override void Paint(Canvas canvas)
{
  canvas.DrawLine(-200, -100, 200, 100);
  base.Paint(canvas);
}
//-}
```

`Paint` piirtää kaikkien olioiden päälle. Koordinaatit ovat samat kuin
olioilla, ja kamera vaikuttaa piirrettyyn samoin kuin olioihin, joten
esimerkiksi `pelaaja.Position` on pelaajan keskipiste myös piirrettäessä.

## Janat ja kuvat

Piirtäminen tapahtuu parametrina saatavan `canvas`-olion metodeilla:

- `DrawLine` – piirtää janan. Parametreina alku- ja loppupisteen koordinaatit
  joko vektoreina tai luettelemalla molempien pisteiden x- ja y-koordinaatit.
- `DrawImage` – piirtää [kuvan](kuvat.md) niin, että kuvan keskipiste on
  annetussa pisteessä: `canvas.DrawImage(paikka, kuva)`. Lisäksi voi antaa
  skaalauksen ja kiertokulman: `canvas.DrawImage(paikka, kuva, new Vector(2, 1), Angle.FromDegrees(45))`
  piirtää kuvan kaksi kertaa leveämpänä ja 45 astetta kierrettynä.

Janan värin voi asettaa `BrushColor`-ominaisuuden kautta. Väri on jokaisen
`Paint`-kutsun alussa musta.

## Piirtoalueen reunat

Piirtoalueen reunat ovat samat kuin
[kentän](../aloittaminen/pelin-rakenne.md#kentta-kamera-ja-ruutu) reunat
(`Level.Left` jne.), eivät ikkunan reunat:

| Ominaisuus         | Selitys                        |
|:-------------------|--------------------------------|
| canvas.Left        | Vasemman reunan x-koordinaatti |
| canvas.Right       | Oikean reunan x-koordinaatti   |
| canvas.Bottom      | Alareunan y-koordinaatti       |
| canvas.Top         | Yläreunan y-koordinaatti       |
| canvas.TopLeft     | Vasen ylänurkka                |
| canvas.TopRight    | Oikea ylänurkka                |
| canvas.BottomLeft  | Vasen alanurkka                |
| canvas.BottomRight | Oikea alanurkka                |

## Esimerkkejä

### Rasti kentän nurkassa

Punainen rasti piirretään 100 yksikön päähän vasemmasta ylänurkasta
reunojen avulla, joten se pysyy nurkassa kentän koosta riippumatta.

```csharp,feature-jypeli
//-using Jypeli;
//-
//-public class Peli : Game
//-{
protected override void Paint(Canvas canvas)
{
  canvas.BrushColor = Color.Red;

  double x = canvas.Left + 100;
  double y = canvas.Top - 100;

  canvas.DrawLine(x - 50, y + 50, x + 50, y - 50);
  canvas.DrawLine(x + 50, y + 50, x - 50, y - 50);

  base.Paint(canvas);
}
//-}
```

### Tähtäysviiva pelaajasta hiireen

Pelaaja on olio, joka lisätään peliin kerran, mutta viiva piirretään joka
ruudunpäivityksellä uudelleen pelaajan ja hiiren senhetkisten paikkojen mukaan.

```csharp,feature-jypeli
using Jypeli;

public class Peli : PhysicsGame
{
  PhysicsObject pelaaja;

  public override void Begin()
  {
    pelaaja = new PhysicsObject(40, 40, Shape.Circle);
    pelaaja.X = -200;
    Add(pelaaja);
    Mouse.IsCursorVisible = true;
  }

  protected override void Paint(Canvas canvas)
  {
    canvas.BrushColor = Color.Red;
    canvas.DrawLine(pelaaja.Position, Mouse.PositionOnWorld);
    base.Paint(canvas);
  }
}
```

### Pyörivä jana

Koska kaikki piirretään joka kerta uudelleen, animaation saa laskemalla
koordinaatit siitä, paljonko aikaa on kulunut. Jana pyörii alkupisteensä
ympäri kierroksen 2π sekunnissa.

```csharp,ignore
protected override void Paint(Canvas canvas)
{
  canvas.BrushColor = Color.Red;

  double ajanhetki = Game.Time.SinceStartOfGame.TotalSeconds;

  Vector keskipiste = new Vector(0, 0);
  Vector reunapiste = new Vector(100 * Math.Cos(ajanhetki), 100 * Math.Sin(ajanhetki));

  canvas.DrawLine(keskipiste, keskipiste + reunapiste);

  base.Paint(canvas);
}
```
