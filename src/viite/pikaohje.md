# Pikaohje

Yleisimmät rivit yhdellä sivulla. Rivit kirjoitetaan `Begin`-aliohjelmaan,
ellei toisin sanota. Linkki vie tarkempaan ohjeeseen.

## Oliot

```csharp,ignore
PhysicsObject pallo = new PhysicsObject(40, 40);   // leveys, korkeus
pallo.Shape = Shape.Circle;
pallo.Color = Color.Red;
pallo.Image = LoadImage("pallo");                  // Content-kansiosta
pallo.Position = new Vector(100, -50);
pallo.Mass = 10;
pallo.Restitution = 0.8;                           // kimmoisuus 0..1
pallo.Tag = "pallo";
Add(pallo);
pallo.Destroy();
pallo.MakeStatic();                                // ei liiku, esim. seinä
```

[Olion luominen](../oliot/luonti.md) · [Muodot](../oliot/muodot.md) ·
[Ulkonäkö](../oliot/ulkonako.md) · [Oliotyypit](../oliot/oliotyypit.md)

## Kenttä ja kamera

```csharp,ignore
Gravity = new Vector(0, -800);
Level.CreateBorders();
Level.Background.Color = Color.Black;
Level.Background.CreateStars();
Camera.ZoomToLevel();
Camera.Follow(pelaaja);
ClearAll();          // tyhjentää kaiken, esim. uuden kentän alussa
```

[Kentät ja kamera](../kentat/index.md) · [Painovoima](../fysiikka/painovoima.md)

## Näppäimet ja hiiri

```csharp,ignore
Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaVasemmalle, "Liiku vasemmalle");
Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Hyppää", pelaaja);
Keyboard.Listen(Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta");
Keyboard.Listen(Key.F1, ButtonState.Pressed, ShowControlHelp, "Näytä ohjeet");
Mouse.Listen(MouseButton.Left, ButtonState.Pressed, Ammu, "Ammu");
ControllerOne.Listen(Button.A, ButtonState.Pressed, Hyppaa, "Hyppää");
```

Käsittelijä: `void Hyppaa(PhysicsObject olio) { olio.Hit(new Vector(0, 500)); }`

[Ohjainten lisääminen](../ohjaimet/ohjainten-lisays.md) ·
[Olioiden liikuttelu ja siirtely](../oliot/liikuttelu.md)

## Liike

```csharp,ignore
pelaaja.Push(new Vector(500, 0));      // voima
pelaaja.Hit(new Vector(0, 500));       // sysäys
pelaaja.Velocity = new Vector(200, 0); // nopeus suoraan
pelaaja.Walk(200);                     // PlatformCharacter
pelaaja.Jump(600);                     // PlatformCharacter
```

## Törmäykset

```csharp,ignore
AddCollisionHandler(pallo, PalloTormasi);            // mihin tahansa
AddCollisionHandler(pallo, maila, PalloOsuiMailaan); // tiettyyn olioon
AddCollisionHandler(pallo, "tahti", PalloOsuiTahteen); // tagilla
```

Käsittelijä: `void PalloTormasi(PhysicsObject pallo, PhysicsObject kohde) { ... }`

[Törmäysten käsittely](../tapahtumat/tormaykset.md) ·
[Törmäysten estäminen](../fysiikka/tormayksen-estaminen.md)

## Ajastimet

```csharp,ignore
Timer ajastin = new Timer();
ajastin.Interval = 2.0;              // sekuntia
ajastin.Timeout += LuoVihollinen;    // void LuoVihollinen()
ajastin.Start();
Timer.SingleShot(3.0, PeliOhi);      // kerran 3 s kuluttua
```

[Ajastimet](../tapahtumat/ajastimet.md)

## Laskurit ja teksti

```csharp,ignore
IntMeter pisteet = new IntMeter(0);
Label pisteNaytto = new Label();
pisteNaytto.BindTo(pisteet);
pisteNaytto.X = Screen.Left + 100;
pisteNaytto.Y = Screen.Top - 100;
Add(pisteNaytto);
pisteet.Value += 1;
MessageDisplay.Add("Osuma!");
```

[Pistelaskuri](../laskurit/pistelaskuri.md) · [Teksti ruudulla](../kayttoliittyma/teksti.md) ·
[Valikot](../kayttoliittyma/valikko.md)

## Äänet

```csharp,ignore
SoundEffect pum = LoadSoundEffect("pum");
pum.Play();
MediaPlayer.Play("musiikki");
MediaPlayer.IsRepeating = true;
```

[Äänet ja musiikki](../aanet/aanien-lisays.md) ·
[Kuvat ja äänet mukaan projektiin](../perusteet/sisallon-tuonti.md)

## Satunnaisuus

```csharp,ignore
int arpa = RandomGen.NextInt(1, 7);          // 1..6
double d = RandomGen.NextDouble(0, 100);
Vector v = RandomGen.NextVector(100, 200);   // pituus 100..200
Color c = RandomGen.NextColor();
```

[Satunnaisuus](../matematiikka/satunnaisuus.md)

## Pelin kulku

```csharp,ignore
Pause();            // tauko päälle/pois
IsPaused = true;
ClearAll(); Begin(); // alusta
Exit();
```

[Pelin aloittaminen alusta](../pelin-kulku/aloittaminen-alusta.md) ·
[Pause](../pelin-kulku/pause.md)
