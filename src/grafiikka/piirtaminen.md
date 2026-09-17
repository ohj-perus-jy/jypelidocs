# Piirtäminen

Piirtämistä varten peliluokkaan lisätään `Paint`-aliohjelma:

```csharp,ignore
protected override void Paint(Canvas canvas)
{
  // TÄHÄN VÄLIIN TULEE PIIRTÄMINEN...
  base.Paint(canvas);
}
```

Jypeli kutsuu `Paint`-aliohjelmaa jokaisella pelinpäivityksellä (60 kertaa sekunnissa) pelin ollessa käynnissä. Siinä voi siis toteuttaa animaatioita muuttamalla koordinaatteja sen mukaan, millä ajanhetkellä piirretään.

## Canvas-luokka

Itse piirtäminen tapahtuu parametrina saatavan `canvas`-olion metodeilla. Nykyisellään niitä on yksi:

- `DrawLine` – piirtää janan. Parametreina alku- ja loppupisteen koordinaatit joko vektoreina tai luettelemalla molempien pisteiden x- ja y-koordinaatit.

Värin voi asettaa `BrushColor`-ominaisuuden kautta. Lisäksi piirtoalueen reunojen koordinaatteja voi lukea samaan tapaan kuin kentänkin reunoja:

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

- Punaisen rastin piirtäminen vasempaan ylänurkkaan

```csharp,ignore
protected override void Paint(Canvas canvas)
{
  canvas.BrushColor = Color.Red;

  double x = canvas.Left + 100;
  double y = canvas.Top - 100;

  canvas.DrawLine(x - 50, y + 50, x + 50, y - 50);
  canvas.DrawLine(x + 50, y + 50, x - 50, y - 50);

  base.Paint(canvas);
}
```

- Jana, joka pyörii alkupisteensä ympäri

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
