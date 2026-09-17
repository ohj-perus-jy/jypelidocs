# Ohjainten lisääminen

Peli voi ottaa vastaan näppäimistön ja hiiren ohjausta. Ohjainten liikettä ”kuunnellaan” ja voidaankin määrittää erikseen, mitä mistäkin tapahtuu. Ohjaimelle on tehty oma `Listen`-aliohjelma, jolla kuuntelun asettaminen onnistuu.

Esimerkki näppäimistön kuuntelusta:

```csharp,ignore
Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaPelaajaaVasemmalle, "Pelaaja liikkuu vasemmalle");
```

- Kun vasen (`Key.Left`) näppäin on painettuna alhaalla (`ButtonState.Down`), niin liikutetaan pelaajaa suorittamalla metodi `LiikutaPelaajaaVasemmalle`. Viimeisenä parametrina on ohjeteksti.

## Yleisesti

Jokainen `Listen`-kutsu on muodoltaan samanlainen riippumatta siitä, mitä ohjainta kuunnellaan.

**Ensimmäinen parametri** kertoo, mitä näppäintä kuunnellaan, esimerkiksi:

- Näppäimistö: `Key.Up`
- Hiiri: `MouseButton.Left`

Riderin kirjoitusapu auttaa löytämään, mitä erilaisia näppäinvaihtoehtoja kullakin ohjaimella on.

**Toinen parametri** määrittää, minkälaisia näppäinten tapahtumia halutaan kuunnella, ja sillä on neljä mahdollista arvoa:

- `ButtonState.Released`: Näppäin on juuri vapautettu
- `ButtonState.Pressed`: Näppäin on juuri painettu alas
- `ButtonState.Up`: Näppäin on ylhäällä (vapautettuna)
- `ButtonState.Down`: Näppäin on alaspainettuna

**Kolmas parametri** kertoo, mitä tehdään, kun näppäin sitten on painettuna. Tähän tulee *tapahtumankäsittelijä*, eli sen aliohjelman nimi, jonka suoritukseen haluamme siirtyä näppäimen tapahtuman sattuessa.

**Neljäs parametri** on ohjeteksti, joka voidaan näyttää pelaajalle pelin alussa. Tässä tarvitsee vain kertoa, mitä tapahtuu, kun näppäintä painetaan. Ohjetekstin tyyppi on string eli merkkijono. Jos ohjetta ei halua tai tarvitse laittaa, neljännen parametrin arvoksi voi antaa `null`, jolloin se jää tyhjäksi.

Parametreja voi antaa enemmänkin sen mukaan, mitä pelissä tarvitsee. Omat (eli valinnaiset) parametrit laitetaan edellä mainittujen pakollisten parametrien jälkeen ja ne viedään automaattisesti `Listen`-kutsussa annetulle käsittelijälle. Esimerkki on alla kohdassa [Näppäimistö](#nappaimisto).

### Lopetuspainike ja näppäinohjepainike

Pelin lopettamiselle ja näppäinohjeen näyttämiselle ruudulla on Jypelissä olemassa valmiit aliohjelmat. Ne voidaan asettaa näppäimiin seuraavasti:

```csharp,ignore
Keyboard.Listen(Key.Escape, ButtonState.Pressed, Exit, "Poistu");
Keyboard.Listen(Key.F1, ButtonState.Pressed, ShowControlHelp, "Näytä ohjeet");
```

Tässä näppäimistön Esc-painike lopettaa pelin ja F1-painike näyttää ohjeet.

`ShowControlHelp` näyttää peliruudulla pelissä käytetyt näppäimet ja niille asetetut ohjetekstit. Ohjeteksti on `Listen`-kutsun neljäntenä parametrina annettu merkkijono.

## Näppäimistö

Tässä esimerkissä asetetaan näppäimistön nuolinäppäimet liikuttamaan pelaajaa. Viimeinen parametri (vektori) on ns. valinnainen parametri:

```csharp,ignore
public override void Begin()
{
    pelaaja1 = new PhysicsObject(40, 40);
    Add(pelaaja1);

    Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaPelaajaa, null, new Vector(-1000, 0));
    Keyboard.Listen(Key.Right, ButtonState.Down, LiikutaPelaajaa, null, new Vector(1000, 0));
    Keyboard.Listen(Key.Up, ButtonState.Down, LiikutaPelaajaa, null, new Vector(0, 1000));
    Keyboard.Listen(Key.Down, ButtonState.Down, LiikutaPelaajaa, null, new Vector(0, -1000));
}

void LiikutaPelaajaa(Vector vektori)
{
    pelaaja1.Push(vektori);
}
```

`Listen`-aliohjelmassa pystyy antamaan omia parametreja, kuten tässä on annettu vektori. Käsittelijä `LiikutaPelaajaa` ottaa vastaan vastaavan parametrin.

Ohjetekstin arvo on `null` eli tyhjä.

Jatketaan vielä edellistä esimerkkiä asettamalla kuuntelija näppäinyhdistelmälle. Näppäimet voidaan antaa esim. taulukossa tai listassa ja kuuntelijaan voi myös antaa valinnaisia parametreja, kuten yhden näppäimen kuuntelijassa:

```csharp,ignore
public override void Begin()
{
    pelaaja1 = new PhysicsObject(40, 40);
    Add(pelaaja1);

    Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaPelaajaa, null, new Vector(-1000, 0));
    Keyboard.Listen(Key.Right, ButtonState.Down, LiikutaPelaajaa, null, new Vector(1000, 0));
    Keyboard.Listen(Key.Up, ButtonState.Down, LiikutaPelaajaa, null, new Vector(0, 1000));
    Keyboard.Listen(Key.Down, ButtonState.Down, LiikutaPelaajaa, null, new Vector(0, -1000));

    Keyboard.ListenMultiple(new Key[] {Key.C, Key.H}, ButtonState.Pressed, ActivateCheats, null);
}

void LiikutaPelaajaa(Vector vektori)
{
    pelaaja1.Push(vektori);
}

void ActivateCheats()
{
    Console.WriteLine("Cheat codes activated");
    pelaaja1.IgnoresCollisionResponse = true;
    pelaaja1.IgnoresGravity = true;
}
```

### Tasainen nopeus nuolinäppäimillä

Edellä `Push` kiihdyttää pelaajaa, kun näppäin on pohjassa. Jos pelaajan halutaan liikkuvan tasaisella nopeudella ja pysähtyvän heti, kun näppäin vapautetaan, kuunnellaan jokaiselle näppäimelle kahta tapahtumaa: `ButtonState.Down` asettaa nopeuden ja `ButtonState.Released` nollaa sen. Tämä sopii esimerkiksi ylhäältäpäin kuvattuun labyrinttipeliin.

```csharp,feature-jypeli
using System;
using System.Collections.Generic;
using Jypeli;
using Jypeli.Assets;
using Jypeli.Controls;
using Jypeli.Effects;
using Jypeli.Widgets;

public class FysiikkaPeli1 : PhysicsGame
{
    private double liikkumisnopeus = 300;

    public override void Begin()
    {
        PhysicsObject pelaaja = new PhysicsObject(100, 100, Shape.Circle);
        Add(pelaaja);

        Keyboard.Listen(Key.Left, ButtonState.Down, Liikuta, null, pelaaja, new Vector(-liikkumisnopeus, 0));
        Keyboard.Listen(Key.Left, ButtonState.Released, Liikuta, null, pelaaja, Vector.Zero);
        Keyboard.Listen(Key.Right, ButtonState.Down, Liikuta, null, pelaaja, new Vector(liikkumisnopeus, 0));
        Keyboard.Listen(Key.Right, ButtonState.Released, Liikuta, null, pelaaja, Vector.Zero);
        Keyboard.Listen(Key.Down, ButtonState.Down, Liikuta, null, pelaaja, new Vector(0, -liikkumisnopeus));
        Keyboard.Listen(Key.Down, ButtonState.Released, Liikuta, null, pelaaja, Vector.Zero);
        Keyboard.Listen(Key.Up, ButtonState.Down, Liikuta, null, pelaaja, new Vector(0, liikkumisnopeus));
        Keyboard.Listen(Key.Up, ButtonState.Released, Liikuta, null, pelaaja, Vector.Zero);

        PhoneBackButton.Listen(ConfirmExit, "Lopeta peli");
        Keyboard.Listen(Key.Escape, ButtonState.Pressed, ConfirmExit, "Lopeta peli");
    }

    void Liikuta(PhysicsObject pelaaja, Vector suunta)
    {
        pelaaja.Velocity = suunta;
    }
}
```

Tässä pelaaja annetaan käsittelijälle parametrina, jolloin sen ei tarvitse olla attribuutti. Eri tavat liikuttaa oliota (`Push`, `Hit`, `Velocity`, `Position`, `Walk` ja `Jump`) on koottu sivulle [Olioiden liikuttelu ja siirtely](../oliot/liikuttelu.md).

## Peliohjain

Sama esimerkki kahden pelaajan versiona peliohjaimia käyttäen:

```csharp,ignore
PhysicsObject pelaaja1;
PhysicsObject pelaaja2;

public override void Begin()
{
    pelaaja1 = new PhysicsObject(40, 40);
    Add(pelaaja1);
    pelaaja2 = new PhysicsObject(40, 40);
    Add(pelaaja2);

    ControllerOne.Listen(Button.DPadLeft, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(-1000, 0), pelaaja1);
    ControllerOne.Listen(Button.DPadRight, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(1000, 0), pelaaja1);
    ControllerOne.Listen(Button.DPadUp, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(0, 1000), pelaaja1);
    ControllerOne.Listen(Button.DPadDown, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(0, -1000 ), pelaaja1);

    ControllerTwo.Listen(Button.DPadLeft, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(-1000, 0), pelaaja2);
    ControllerTwo.Listen(Button.DPadRight, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(1000, 0), pelaaja2);
    ControllerTwo.Listen(Button.DPadUp, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(0, 1000), pelaaja2);
    ControllerTwo.Listen(Button.DPadDown, ButtonState.Down, LiikutaPelaajaa,
                        null, new Vector(0, -1000), pelaaja2);
}

void LiikutaPelaajaa(Vector vektori, PhysicsObject pelaaja)
{
    pelaaja.Push(vektori);
}
```

Tässä esimerkissä käsittelijälle `LiikutaPelaajaa` annettiin parametrina vielä se pelaaja, jota liikutetaan.

### Tatti

Jos halutaan kuunnella ohjaimen tattien liikettä, käytetään `ListenAnalog`-kutsua.

```csharp,ignore
ControllerOne.ListenAnalog(AnalogControl.LeftStick, 0.1, LiikutaPelaajaa,
                            "Liikuta pelaajaa tattia pyörittämällä.");
```

Kuunnellaan vasenta tattia (`AnalogControl.LeftStick`). Luku `0.1` kuvaa sitä, miten herkästä liikkeestä tattia kuunteleva aliohjelma suoritetaan. Kuuntelua käsittelee aliohjelma `LiikutaPelaajaa`.

Nyt sitten `LiikutaPelaajaa`-aliohjelman tulee ottaa vastaan seuraavanlainen parametri:

```csharp,ignore
void LiikutaPelaajaa(AnalogState tatinTila)
{

}
```

Tatin asento saadaan selville parametrina vastaan otettavasta `AnalogState`-tyyppisestä muuttujasta:

```csharp,ignore
void LiikutaPelaajaa(AnalogState tatinTila)
{
    Vector tatinAsento = tatinTila.StateVector;
}
```

`StateVector` antaa siis vektorin, joka kertoo, mihin suuntaan tatti osoittaa. Vektorin X- ja Y-koordinaattien arvot ovat molemmat väliltä miinus yhdestä yhteen (−1…1) tatin suunnasta riippuen. Tämän vektorin avulla voidaan esimerkiksi kertoa pelaajalle, mihin suuntaan sen kuuluu liikkua.

<!-- kuva puuttuu (trac ei vastaa): https://trac.cc.jyu.fi/projects/npo/raw-attachment/wiki/OhjaintenLisays/yksikkoympyra.png -->

Tatin asennon tietyllä hetkellä saa selville myös ilman jatkuvaa tatin kuuntelua kirjoittamalla:

```csharp,ignore
Vector tatinAsento = ControllerOne.LeftThumbDirection;
```

Tämä palauttaa samoin vektorin tatin senhetkisestä asennosta (X ja Y väliltä −1…1).

### Liipasin

Liipasinten kuuntelu toimii lähes samalla tavalla kuin tattien kuuntelu. Käytetään `ListenAnalog`-kutsua:

```csharp,ignore
ControllerOne.ListenAnalog(AnalogControl.RightTrigger, 0.1, KaasutaAutolla,
                           "Käytä oikeaa liipasinta kaasupolkimen tavoin.");
```

Kuunnellaan oikeaa liipasinta (`AnalogControl.RightTrigger`). Luku `0.1` kuvaa sitä, miten herkästä liikkeestä liipasinta kuunteleva aliohjelma suoritetaan. Kuuntelua käsittelee aliohjelma `KaasutaAutolla`.

Liipasimen kuuntelusta vastaavan aliohjelman, tässä `KaasutaAutolla`, tulee olla seuraavanlainen:

```csharp,ignore
void KaasutaAutolla(AnalogState liipasimenTila)
{

}
```

Aliohjelman täytyy ottaa vastaan `AnalogState`-tyyppinen parametri. Parametrista saadaan selville liipasimen asento:

```csharp,ignore
void KaasutaAutolla(AnalogState liipasimenTila)
{
    double liipasimenAsento = liipasimenTila.State;
}
```

`State` antaa desimaaliluvun väliltä 0–1. Arvo 0 tarkoittaa, että liipasinta ei paineta yhtään. Vastaavasti 1 tarkoittaa, että liipasin on painettu aivan pohjaan saakka.

Liipasimen tila tietyllä hetkellä saadaan tarvittaessa selville myös ilman jatkuvaa liipasimen kuuntelua kirjoittamalla:

```csharp,ignore
double vasemmanLiipasimenTila = ControllerOne.LeftTriggerState;
```

Tässä esimerkissä otetaan ykkösohjaimen vasemman liipasimen tila tietyltä hetkeltä. Arvot ovat jälleen väliltä 0–1.

### Useampi ohjainvaihtoehto

Jos pelissä pelaajalla voi olla ohjain lisättynä ja samaan aikaan näppäimistö käytössä ja näppäimistö kuuntelee näppäinten ylhäällä oloa, kannattaa asettaa vain joko näppäimistölle tai ohjaimelle kuuntelijat.

```csharp,ignore
if (ControllerOne.IsConnected)
{
    ControllerOne.Listen(Button.DPadLeft,  ButtonState.Down, LiikutaPelaajaa,
                         null, new Vector( -1000, 0 ), pelaaja1);
}
else
{
    Keyboard.Listen(Key.Left, ButtonState.Down, LiikutaPelaajaa,
                   "Liikuttaa pelaajaa", new Vector(-1000, 0), pelaaja1);
}
```

## Hiiri

### Näppäimet

Hiiren näppäimiä voi kuunnella aivan samaan tapaan kuin näppäimistön.

```csharp,ignore
Mouse.Listen(MouseButton.Left, ButtonState.Pressed, Ammu, "Ammu aseella.");
```

Tässä esimerkissä painettaessa hiiren vasenta näppäintä kutsutaan `Ammu`-nimistä aliohjelmaa. Tuo aliohjelma pitää tietenkin erikseen tehdä:

```csharp,ignore
void Ammu()
{
    // Kirjoita tähän Ammu()-aliohjelman koodi.
}
```

### Hiiren liike

Hiirellä ohjauksessa on kuitenkin usein oleellista tietää jotain kursorin sijainnista. Hiiren kursori ei ole oletuksena näkyvä peliruudulla, mutta sen saa halutessaan helposti näkyviin, kun kirjoittaa koodiin seuraavan rivin vaikkapa kentän luomisen yhteydessä:

```csharp,ignore
Mouse.IsCursorVisible = true;
```

Hiiren paikan ruudulla saadaan *vektorina* kirjoittamalla:

```csharp,ignore
Vector paikkaRuudulla = Mouse.PositionOnScreen;
```

Tämä kertoo kursorin paikan näyttökoordinaateissa, ts. origo keskellä. Y-akseli kasvaa ylöspäin.

Hiiren paikan pelimaailmassa (peli- ja fysiikkaolioiden koordinaatistossa) voi saada kirjoittamalla

```csharp,ignore
Vector paikkaKentalla = Mouse.PositionOnWorld;
```

Tämä kertoo kursorin paikan maailmankoordinaateissa. Origo on keskellä ja Y-akseli kasvaa ylöspäin.

Hiiren liikettä voidaan kuunnella aliohjelmalla `Mouse.ListenMovement`. Sille annetaan parametrina kuuntelun herkkyyttä kuvaava `double`, käsittelijä sekä ohjeteksti. Näiden lisäksi voidaan antaa myös omia parametreja. Esimerkki hiiren kuuntelusta:

```csharp,ignore
PhysicsObject pallo;

public override void Begin()
{
    pallo = new PhysicsObject(30.0, 30.0, Shape.Circle);
    Add(pallo);
    Mouse.IsCursorVisible = true;
    Mouse.ListenMovement(0.1, KuunteleLiiketta, null);
}

void KuunteleLiiketta()
{
    pallo.X = Mouse.PositionOnWorld.X;
    pallo.Y = Mouse.PositionOnWorld.Y;

    Vector hiirenLiike = Mouse.MovementOnWorld; // tai Mouse.MovementOnScreen
    // tähän hiiren liikevektorin hyödyntäminen
}
```

Tässä esimerkissä luomamme fysiikkaolio nimeltä `pallo` seuraa hiiren kursoria. Käsittelijää kutsutaan aina, kun hiirtä liikuttaa.

`ListenMovement`:in parametreissa herkkyys tarkoittaa sitä, miten pieni hiiren liike aiheuttaa tapahtuman.

Hiiren liikkeestä saa tietoa `Mouse`-luokan metodeilla. Esimerkiksi `MovementOnWorld` ja `MovementOnScreen` antavat hiiren liikevektorin, joka kertoo, mihin suuntaan ja miten voimakkaasti kursori on liikkunut (hiiren ollessa paikoillaan se on nollavektori!).

### Hiiren kuunteleminen vain tietyille peliolioille

Jos hiiren painalluksia halutaan kuunnella vain tietyn peliolion (tai fysiikkaolion) kohdalla, voidaan käyttää apuna `Mouse.ListenOn`-aliohjelmaa:

```csharp,ignore
Mouse.ListenOn(pallo, MouseButton.Left, ButtonState.Down, TuhoaPallo, null, pallo);
```

Parametrina annetaan se olio, jonka päällä hiiren painalluksia halutaan kuunnella. Seuraavat parametrit ovat kuin normaalissa `Listen`-kutsussa, ja viimeiseksi voidaan antaa käsittelijän parametrina saama olio. Käsittelijää `TuhoaPallo` kutsutaan tässä esimerkissä silloin, kun hiiren kursori on pallo-nimisen olion päällä ja hiiren vasen nappi on painettuna pohjaan. Käsittelijä olisi nyt seuraavan esimerkin mukainen:

```csharp,ignore
void TuhoaPallo(PhysicsObject klikattuPallo)
{
    klikattuPallo.Destroy();
}
```

Hiirellä on olemassa myös esimerkiksi seuraavanlainen metodi:

```csharp,ignore
PhysicsObject kappale = new PhysicsObject(50.0, 50.0);
bool onkoPaalla = Mouse.IsCursorOn(kappale);
```

`Mouse.IsCursorOn` palauttaa totuusarvon true tai false riippuen siitä, onko kursori sille annetun olion (peli-, fysiikka- tai näyttöolion) päällä.

## Puhelimen kiihtyvyysanturi

Kiihtyvyysanturin kuunteleminen tapahtuu samaan tapaan kuin muillakin ohjaimilla.

### Kallistus

Kiihtyvyysanturia voi kuunnella tietyn suunnan suhteen:

```csharp,ignore
Accelerometer.Listen(AccelerometerDirection.Left,
                     AccelerometerSensitivity.High,
                     TeeJotain, "Tekee jotain");

void TeeJotain()
{
    // jotain...
}
```

On olemassa myös versio, johon ei tarvitse antaa parametrina herkkyyttä. Tällöin käytetään oletusherkkyyttä.

```csharp,ignore
Accelerometer.Listen(AccelerometerDirection.Any, TeeJotain, "Tekee jotain");
Accelerometer.ListenAnalog(TeeJotainMuuta, "Tekee jotain muuta");
```

Oletusherkkyyden vakioarvot ovat:

- `DefaultSensitivity = 0.2` (High)
- `DefaultAnalogSensitivity = 0.01` (Realtime)

Oletusherkkyyden arvoa voi muuttaa seuraavasti:

```csharp,ignore
// Suunnat
Accelerometer.SetDefaultSensitivity(AccelerometerSensitivity.Realtime);
// Tai
Accelerometer.SetDefaultSensitivity(0.1);

// Analoginen
Accelerometer.SetDefaultAnalogSensitivity(AccelerometerSensitivity.Low);
// Tai
Accelerometer.SetDefaultAnalogSensitivity(0.3);
```

### Eleet

Kiihtyvyysanturilla voi myös kuunnella puhelimella tehtäviä eleitä. Sillä voi tunnistaa puhelimen **tärähdyksen/näpäytyksen** tai puhelimen **ravistuksen**. Eleitä kuunnellaan seuraavasti:

```csharp,ignore
// Oletusherkkyydellä
Accelerometer.Listen(AccelerometerDirection.Shake, Ravistettu, "");
Accelerometer.Listen(AccelerometerDirection.Tap, Täräytetty, "");

// Jos haluaa antaa parametrina herkkyyden
Accelerometer.Listen(AccelerometerDirection.Shake, 0.4, Ravistettu, "");
Accelerometer.Listen(AccelerometerDirection.Tap, 0.5, Täräytetty, "");
```

Eleiden välillä on minimiaika millisekunteina, jonka pitää kulua, ennen kuin uusi ele tunnistetaan. Oletusarvot ovat:

- `TimeBetweenTaps = 300`
- `TimeBetweenShakes = 500`

Aikaa voi muuttaa seuraavasti:

```csharp,ignore
Accelerometer.TimeBetweenTaps = 200;
Accelerometer.TimeBetweenShakes = 700;
```

### Kalibrointi

Erilaisissa peleissä puhelinta pidetään eri lailla kädessä. Tämän takia kiihtyvyysanturin nollakohtaa (eli sitä kohtaa, jossa puhelinta ei ole kallistettu mihinkään päin) voi joutua muuttamaan. Tämä onnistuu seuraavasti:

```csharp,ignore
// Nollakohta = puhelin makaa tasaisella, näyttö ylöspäin
Accelerometer.Calibration = AccelerometerCalibration.ZeroAngle;

// Nollakohta = puhelin on 90 asteen kulmassa
Accelerometer.Calibration = AccelerometerCalibration.RightAngle;

// Nollakohta = puhelin on 45 asteen kulmassa
Accelerometer.Calibration = AccelerometerCalibration.HalfRightAngle;
```

Kiihtyvyysanturin lukeman saa selville seuraavasti:

```csharp,ignore
Vector suunta = Accelerometer.Reading;
```

Kiihtyvyysanturin kaikkien akselien (x, y, z) lukemat saa seuraavalla kutsulla (lukemat ja suunnat eivät tässä vektorissa riipu näytön orientaatiosta eikä kalibroinnista, joten sen käyttöä ei suositella):

```csharp,ignore
Vector3 tilaVektori = Accelerometer.State;
```

### Muuta

Kiihtyvyysanturin voi pysäyttää hetkeksi seuraavasti (parametri tarkoittaa, montako sekuntia kiihtyvyysanturi on pois päältä):

```csharp,ignore
Accelerometer.PauseForDuration(1);
```

Eleet saa pois päältä ja päälle seuraavasti (oletuksena päällä):

```csharp,ignore
Accelerometer.GesturesEnabled = false;
Accelerometer.GesturesEnabled = true;
```

## Puhelimen takaisin-näppäin {#puhelimentakaisinnappain}

Oletuksena puhelimen takaisin-näppäimelle ei ole kuuntelijaa. Usein halutaan käyttää näppäintä esimerkiksi palaamaan päävalikkoon tai yksinkertaisesti lopettamaan peli. Jälkimmäisessä tapauksessa riittää rivi

```csharp,ignore
PhoneBackButton.Listen(Exit, "Lopeta peli");
```

Jos halutaan, että nappulasta tapahtuu jotain muuta, voidaan `Exit`-aliohjelmakutsu korvata oman aliohjelman kutsulla. Aliohjelmalle ei tule parametreja.

```csharp,ignore
public void AsetaOhjaimet()
{
   // muita ohjainasetuksia...
   PhoneBackButton.Listen(MeneValikkoon, "Palaa päävalikkoon");
}

void MeneValikkoon()
{
   // valikkokoodi tähän
}
```

## Puhelimen kosketusnäyttö

Puhelimen kosketusnäyttöä voidaan kuunnella aliohjelmalla `TouchPanel.Listen`. Parametrit ovat muuten samat kuin muillakin kuuntelijoilla, mutta koska kosketuksen voi tehdä vain yhdellä tavalla, kuuntelija ei tarvitse parametria, joka määrittäisi, mitä näppäintä halutaan kuunnella.

Esimerkki pelaajan liikuttamisesta kosketusnäytöllä:

```csharp,ignore
TouchPanel.Listen(ButtonState.Down, LiikutaPelaajaa, "Liikuttaa pelaajaa", pelaaja);
```

Tapahtumankäsittelijä ottaa annettujen parametrien lisäksi `Touch`-tyyppisen parametrin, joka kertoo tarkemmat tiedot kosketuksesta. Näitä tietoja ovat:

- PositionOnScreen - kosketuksen paikka näyttökoordinaateissa (mittareille ym. widgeteille)
- PositionOnWorld - kosketuksen paikka maailmankoordinaateissa (tavallisille peliolioille)
- MovementOnScreen - kosketuksen paikan muutos näyttökoordinaateissa
- MovementOnWorld - kosketuksen paikan muutos maailmankoordinaateissa

```csharp,ignore
void LiikutaPelaajaa(Touch kosketus, PhysicsObject pelaaja)
{
    pelaaja.Velocity = kosketus.MovementOnWorld;
}
```

Huomaa, että `Touch`-tilaparametri tulee aina ensimmäisenä!

Windows Phone 7:n kosketusnäyttö pystyy seuraamaan maksimissaan viittä kosketusta ruudulla samaan aikaan. Kosketukset voidaan erottaa toisistaan vertailemalla tilaparametrin viitteitä.

```csharp,ignore
Touch aktiivinenKosketus = null;

public override void Begin()
{
    TouchPanel.Listen(ButtonState.Down, LiikutaPelaajaa, "Liikuttaa pelaajaa", pelaaja);
    TouchPanel.Listen(ButtonState.Released, Irroita, null);
}

void LiikutaPelaajaa(Touch kosketus, PhysicsObject pelaaja)
{
    if (aktiivinenKosketus == null)
    {
        // Ei edellistä kosketusta, tehdään tästä nykyinen
        aktiivinenKosketus = kosketus;
    }
    else if (kosketus != aktiivinenKosketus)
    {
        // Kosketus eri sormella
        MessageDisplay.Add("Yksi kerrallaan, kiitos!");
        return;
    }

    pelaaja.Velocity = kosketus.MovementOnWorld;
}

void Irroita(Touch kosketus)
{
    if (kosketus == aktiivinenKosketus)
    aktiivinenKosketus = null;
}
```

## Katso myös

- [Olioiden liikuttelu ja siirtely](../oliot/liikuttelu.md): mitä käsittelijässä tehdään, jotta olio liikkuu.
- [Ohjainten ryhmittely](ryhmittely.md): näppäimet toimivat vain tietyssä pelitilassa.
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti): olio käsittelijälle parametrina tai attribuuttina.
- [Yleiset virheet](../ekstrat/yleiset-virheet.md): näppäin ei tee mitään.
