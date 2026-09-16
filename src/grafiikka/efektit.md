# Miten peliin saa efektejä?

Jotta saisit efektit käyttöön peliisi, tulee sinulla olla seuraava **using**-rivi kooditiedostosi alussa:

```csharp,ignore
using Jypeli.Effects;
```

## Yleistä efekteistä

Jotta ymmärtäisit kuinka efektit toimivat ja kuinka niitä luodaan Jypelissä, tulee sinun tietää muutamia seikkoja efekteistä.

- Jokainen efekti joka pelissä luodaan, kuuluu johonkin efektijärjestelmään Yksi efekti koostuu aina niin sanotuista partikkeleista.

## Räjähdys

Jokainen erilainen efekti käyttää sille tarkoitettua järjestelmää. Räjähdysefektillä tuon järjestelmän nimi on `ExplosionSystem`. Jotta voisit luoda räjähdyksiä, sinun täytyy kirjoittaa seuraavat rivit koodiin

```csharp,ignore
//-using System;
//-using System.Collections.Generic;
//-using Jypeli;
//-using Jypeli.Assets;
//-using Jypeli.Controls;
//-using Jypeli.Effects;
//-using Jypeli.Widgets;
//-
//-namespace ExplosionExample;
//-
//-public class ExplosionExample : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-        Level.BackgroundColor = Color.Black;
// Ensin alustetaan räjähdysjärjestelmä kuvalla ja
// partikkelien maksimimäärällä
        int pMaxMaara = 200;
        Image rajahdyskuva = LoadImage("Explosion.png");
        ExplosionSystem rajahdys = new ExplosionSystem(rajahdyskuva, pMaxMaara);

        rajahdys.MinVelocity = 20; // Muodostuvien hiukkasten miniminopeus
        rajahdys.MinLifetime = 1; // Muodostuvien hiukkasten minimielinaika

        rajahdys.MaxVelocity = 100; // Muodostuvien hiukkasten maksiminopeus
        rajahdys.MaxLifetime = 3; // Muodostuvien hiukkasten maksimielinaika

        // Lisätään järjestelmä peliin
        Add(rajahdys);

        double x = 0;
        double y = 0;
        int pMaara = 50;
        // "Käynnistetään" räjähdys
        rajahdys.AddEffect(x, y, pMaara);
//-    }
//-}
```

Edellä oleva koodi antaisi seuraavanlaisen räjähdyksen:

<video controls width="320" src="images/esimerkki-rajahdyksesta.mp4"></video>

*Esimerkki räjähdyksestä*

Huomaa erityisesti seuraava rivi.

```csharp,ignore
rajahdys.AddEffect(x, y, pMaara);
```

Tämä rivi lisää halutun efektin peliin, tässä tapauksessa räjähdyksen. Parametreista:

- x ja y-parametrit kertovat efektin x ja y-koordinaatit, eli paikan. pMaara-parametri kertoo kuinka monta partikkelia luotava efekti käyttää. Yhdellä järjestelmällä voidaan tehdä monta räjähdystä, ja kaikilla räjähdyksillä yhdessä on käytössä järjestelmän pMax kappaletta partikkeleita käytössään. Esim. jos tehdään ExplosionSystem rajahdys jonka partikkeleiden maksimi on 50, ja lisätään 3 räjähdystä, jossa kussakin 20 partikkelia, niin partikkelit "loppuvat kesken", ja silloin partikkeleita aletaan tuhoamaan vanhemmasta päästä. (Eli ensin luodut partikkelit tuhotaan ensin.)

[Hyvin vanhan efektejä esittelevä video](http://www.youtube.com/watch?v=jzU1a7camRo)

### Räjähdyksen mukauttaminen

Räjähdyksellä on paljon ominaisuuksia, joilla voi muokata räjähdyksen ulkonäköä haluamakseen. Tässä niistä muutama.

| Ominaisuus | Tyypp | i merkitys | Selitys |
|:---|---:|:---|---:|
| MinLifeTime | double | aika sekunteina | Efektin partikkelin lyhin mahdollinen elinaika. |
| MaxLifeTime | double | aika sekunteina | Efektin partikkelin pisin mahdollinen elinaika. |
| MinVelocity | double | Pienin nopeus, | joka efektin partikkelilla voi olla. |
| MaxVelocity | double | Suurin nopeus, | joka efektin partikkelilla voi olla. |
| MinScale | double | Pienin skaalaus | joka efektin partikkeleilla voi olla. (Luku 1 tarkoittaa että partikkelin koko on tekstuurin koko.) |
| MaxScale | double | Suurin skaalaus | joka efektin partikkeleilla voi olla. |
| MinRotationSpeed | double | Pienin pyörimisnope | us joka efektin partikkelilla voi olla. |
| MaxRotationSpeed | double | Suurin pyörimisnope | us joka efektin partikkelilla voi olla. |

### Sopivien ominaisuusarvojen etsiminen

Räjähdyksen arvoja voit kokeilla yllä olevassa esimerkissä vaihtelemalla arvoja tai lisäämällä uusia parametreja.

### Räjähdys toisella tavalla

```csharp,ignore
//-using System;
//-using System.Collections.Generic;
//-using Jypeli;
//-using Jypeli.Assets;
//-using Jypeli.Controls;
//-using Jypeli.Effects;
//-using Jypeli.Widgets;
//-
//-namespace ExplosionExample2;
//-
//-public class ExplosionExample2 : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-        Level.BackgroundColor = Color.Black;
//-        var vihu = new PhysicsObject(100, 100, Shape.Circle);
//-        vihu.Image = LoadImage("Baby");
//-        Add(vihu);
        var rajahdys = new Explosion(300);
        rajahdys.Position = new Vector(-150, -150);
        rajahdys.UseShockWave = true;
        Add(rajahdys);
//-    }
//-}
```

<video controls width="400" src="images/explosion2.mp4"></video>

*Explosion*

## Liekki

Liekkiefekti käyttää `Flame` nimistä efektijärjestelmää. Liekin voisi esimerkiksi luoda seuraavalla tavalla:

```csharp,ignore
//-using System;
//-using System.Collections.Generic;
//-using Jypeli;
//-using Jypeli.Assets;
//-using Jypeli.Controls;
//-using Jypeli.Effects;
//-using Jypeli.Widgets;
//-
//-namespace FlameExample;
//-
//-public class FlameExample : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-        Level.BackgroundColor = Color.Black;
        Image kuva = LoadImage("Explosion.png");
        Flame liekki = new Flame(kuva);
        liekki.MaxAngleChange = 30; // Kuinka leveälle liekki leviää
        Add(liekki);
//-    }
//-}
```

Kuten räjähdyksessäkin, tämä rivi alustaa uuden liekkijärjestelmän, joka huolehtii liekin piirtämisestä ja päivittämisestä.

- kuva-parametri määrittää mitä kuvaa liekin hiukkaset käyttävät.
- Huomaa että liekki on "jatkuva" efekti, joten sille ei tarvitse antaa hiukkamäärää.

```csharp,ignore
Add(liekki);
```

Kuten räjähdyksessäkin, tämä rivi lisää liekkijärjestelmän peliin, mutta toisin kuin räjähdysjärjestelmä, tämä on välittömästi toiminnassa.

<video controls width="320" src="images/liekkijarjestelman-esimerkki.mp4"></video>

*Liekkijärjestelmän esimerkki*

### Liekin mukauttaminen

Liekillä on samat muokkausmahdollisuudet kuin räjähdykselläkin. Joitain hyödyllisiä ominaisuuksia voi olla mm.

- `MaxAngleChange`, joka määrittää kuinka "leveälle" liekki leviää.
- `Min`- ja `MaxLifeTime`, kuinka korkealle liekki nousee.
- `Min`- ja `MaxVelocity`, kuinka nopeasti liekin hiukkaset liikkuvat

## Savu

Valmiin savuefektin saa luotua `Smoke`-efektin avulla.

Savu käyttäytyy hyvin samalla tavalla kuin tuli, mutta sille Jypelistä löytyy valmis kuva.

```csharp,ignore
Smoke savu = new Smoke();
Add(savu);
```

```csharp,feature-jypeli
//-using System;
//-using System.Collections.Generic;
//-using Jypeli;
//-using Jypeli.Assets;
//-using Jypeli.Controls;
//-using Jypeli.Effects;
//-using Jypeli.Widgets;
//-
//-namespace SmokeExample;
//-
//-public class SmokeExample : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-        Level.BackgroundColor = Color.Black;
        Smoke savu = new Smoke();
        Add(savu);
//-    }
//-}
```

Omasta kuvasta luotu savuefekti luodaan antamalla uudelle savulle parametrina kuva ja savun leveys.

```csharp,ignore
Smoke savu = new Smoke(savuHiukkasenKuva, 10);
```

Ulomman savuhiukkasen kuvan voi asettaa erikseen:

```csharp,ignore
savu.OuterParticleImage = ulommanSavuHiukkasenKuva;
```

Savuefektillä on lisäksi monia samoja ominaisuuksia kuin muillakin efekteillä. Ominaisuuksien arvoja muuttamalla voi savusta muokata juuri mieleisensä.

<video controls width="320" src="images/esimerkki-savuefektista.mp4"></video>

*Esimerkki savuefektistä*

## Tuuli

Efektien käyttäytymiseen voi myös vaikuttaa tuulen avulla. Tuuli vaikuttaa ainoastaan efekteihin, ei mihinkään muuhun.

Tuulen asettaminen onnistuu samalla tavalla kuin [painovoiman](../fysiikka/painovoima.md):

```csharp,ignore
//-using System;
//-using System.Collections.Generic;
//-using Jypeli;
//-using Jypeli.Assets;
//-using Jypeli.Controls;
//-using Jypeli.Effects;
//-using Jypeli.Widgets;
//-
//-namespace WindExample;
//-
//-public class WindExample : PhysicsGame
//-{
//-    public override void Begin()
//-    {
//-        Level.BackgroundColor = Color.Black;
        Image kuva = LoadImage("Explosion.png");
        Flame liekki = new Flame(kuva);
        liekki.MaxAngleChange = 30; // Kuinka leveälle liekki leviää
        Add(liekki);

        Smoke savu = new Smoke();
        Add(savu);
        savu.Position = new Vector(-150,0);

        Wind = new Vector(15, 0);
//-    }
//-}
```

Esimerkki tuulesta aiemman tuliefektin kanssa:

<video controls width="320" src="images/tuuliefekti.mp4"></video>

*Tuuliefekti*
