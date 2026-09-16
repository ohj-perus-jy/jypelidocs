# Läpsylintu: Vaihe 5

Edellisessä vaiheessa lisättiin peliin kuoleminen, mutta lintu jatkaa silti matkaansa oikealle. Korjataan pelaajaa liikuttava ajastin pysähtymään.

## Ajastin attribuutiksi

Jotta voimme kutsua ajastimen `Stop`-metodia, täytyy viite ajastimeen pitää tallessa sopivassa muuttujassa.

Etsi `Begin`-aliohjelmasta kohta, jossa ajastin luodaan. Se näyttää seuraavalta.

```csharp,ignore
Timer liikutusajastin = new Timer();
liikutusajastin.Interval = 0.01;
liikutusajastin.Timeout += SiirraPelaajaaOikeammalle;
liikutusajastin.Start();
```

Ensimmäisellä rivillä luodaan ajastin. Koska se on esitelty aliohjelmassa `Begin`, sitä ei voida käyttää myöhemmin muista aliohjelmista.

Siirretään ajastimen esittely `Begin`-aliohjelmasta `Lapsylintu`-luokan sisäpuolelle. Silloin ajastimeen pääsee käsiksi mistä tahansa luokan aliohjelmasta.

Poista ensin riviltä

```csharp,ignore
Timer liikutusajastin = new Timer();
```

ensimmäinen sana `Timer`, jotta jäljelle jää:

```csharp,ignore
liikutusajastin = new Timer();
```

Silloin käytetään koko luokan `liikutusajastin`-nimistä muuttujaa, jos sellainen vain on olemassa. Luokan yhteistä muuttujaa kutsutaan *attribuutiksi*.

Esitellään `liikutusajastin` luokan `Lapsylintu` attribuuttina, eli sellaisena muuttujana, johon on pääsy kaikista aliohjelmista.

Lisää ennen `Begin`-aliohjelman esittelyriviä rivi:

```csharp,ignore
private Timer liikutusajastin;
```

Tässä vaiheessa kooditiedoston yläosa näyttää jotakuinkin tältä. Kaikki `attribuutit` eivät välttämättä ole sinulla samassa järjestyksessä, mutta se ei tässä tapauksessa haittaa.

```csharp,ignore
public class Lapsylintu : PhysicsGame
{
    private const double NOPEUS = 10000;
    private const double HYPPYNOPEUS = 750;
    private const int RUUDUN_KOKO = 40;

    private PlatformCharacter pelaaja1;

    private Image pelaajanKuva = LoadImage("lintu");
    private Image[] pelaajanHyppykuvat = LoadImages("lapsy", "lintu");
    private Image tahtiKuva = LoadImage("tahti");

    private SoundEffect maaliAani = LoadSoundEffect("maali");

    private bool peliKaynnissa = false;
    private Timer liikutusajastin;

    public override void Begin()
    {
```

Testaa toimiiko ohjelma vielä.

![](images/try_to_run.png)

## Ajastimen pysäyttäminen

Etsi koodista aliohjelma `TormaaTasoon`. Se näyttää suunnilleen tältä:

```csharp,ignore
void TormaaTasoon(PhysicsObject tormaaja, PhysicsObject kohde)
{
    if (peliKaynnissa)
    {
        MessageDisplay.Add("Kuolit! :(");
        Keyboard.Disable(Key.Up);
        peliKaynnissa = false;
    }
}
```

Lisää rivin `Keyboard.Disable(Key.Up);` jälkeen rivi:

```csharp,ignore
liikutusajastin.Stop();
```

Nyt kun pelaaja törmää seinään, hän kuolee.

Koska ajastin, joka kutsui päällä ollessaan pelaajaa oikeammaksi työntävää aliohjelmaa, pysäytetään, myös pelaajan liike loppuu. Testaa koodisi.

![](images/try_to_run.png)
