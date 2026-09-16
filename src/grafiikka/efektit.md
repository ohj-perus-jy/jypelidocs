# Efektit

Jypelin efektit ovat *partikkeliefektejä*: yksi efekti koostuu suuresta joukosta pieniä kuvia eli *partikkeleita*, jotka syntyvät, liikkuvat ja häviävät kukin omaan tahtiinsa. Partikkeleita hallitsee *efektijärjestelmä* (`ParticleSystem`), jolle annetaan partikkelin kuva ja partikkelien enimmäismäärä. Jokainen efektityyppi on oma järjestelmänsä:

- `ExplosionSystem` tekee räjähdyksiä.
- `Flame` tekee liekin.
- `Smoke` tekee savua.

Kaikilla järjestelmillä on samat ominaisuudet, joilla partikkelien elinaikaa, nopeutta, kokoa ja pyörimistä säädetään. Ominaisuudet on lueteltu kohdassa [Räjähdyksen mukauttaminen](#rajahdyksen-mukauttaminen), ja ne toimivat samalla tavalla kaikissa efekteissä.

Efektijärjestelmä lisätään peliin `Add`-metodilla kuten muutkin oliot. Räjähdyksen kaltainen kertaluonteinen efekti käynnistetään sen jälkeen erikseen `AddEffect`-metodilla. Liekki ja savu ovat sen sijaan jatkuvia efektejä, jotka alkavat näkyä heti, kun ne on lisätty peliin.

Kaikki efektit ovat nimiavaruudessa `Jypeli.Effects`, joten lisää kooditiedostosi alkuun seuraava **using**-rivi:

```csharp,ignore
using Jypeli.Effects;
```

## Räjähdys

> [!HUOMAUTUS]
> Tämä on pelkkä näkyvä efekti. Jos räjähdyksen halutaan myös vaikuttavan fysiikkaan, käytä fysiikkaräjähdystä, ks. [Räjähdykset](../aseet/rajahdykset.md).

Räjähdykset tehdään `ExplosionSystem`-järjestelmällä. Alla oleva koodi luo järjestelmän ja käynnistää sillä yhden räjähdyksen:

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

Huomaa erityisesti seuraava rivi.

```csharp,ignore
rajahdys.AddEffect(x, y, pMaara);
```

Tämä rivi lisää halutun efektin peliin, tässä tapauksessa räjähdyksen. Parametreista:

- x ja y-parametrit kertovat efektin x ja y-koordinaatit, eli paikan. pMaara-parametri kertoo kuinka monta partikkelia luotava efekti käyttää. Yhdellä järjestelmällä voidaan tehdä monta räjähdystä, ja kaikilla räjähdyksillä yhdessä on käytössä järjestelmän pMax kappaletta partikkeleita käytössään. Esim. jos tehdään ExplosionSystem rajahdys jonka partikkeleiden maksimi on 50, ja lisätään 3 räjähdystä, jossa kussakin 20 partikkelia, niin partikkelit "loppuvat kesken", ja silloin partikkeleita aletaan tuhoamaan vanhemmasta päästä. (Eli ensin luodut partikkelit tuhotaan ensin.)

### Räjähdyksen mukauttaminen

Räjähdyksellä on paljon ominaisuuksia, joilla voi muokata räjähdyksen ulkonäköä haluamakseen. Tässä niistä muutama.

| Ominaisuus | Tyyppi | Selitys |
|:---|:---|:---|
| `MinLifetime` | double | Partikkelin lyhin mahdollinen elinaika sekunteina. |
| `MaxLifetime` | double | Partikkelin pisin mahdollinen elinaika sekunteina. |
| `MinVelocity` | double | Pienin nopeus, joka partikkelilla voi olla. |
| `MaxVelocity` | double | Suurin nopeus, joka partikkelilla voi olla. |
| `MinScale` | double | Pienin skaalaus, joka partikkelilla voi olla. Arvo 1 tarkoittaa, että partikkeli on kuvan kokoinen. |
| `MaxScale` | double | Suurin skaalaus, joka partikkelilla voi olla. |
| `MinRotationSpeed` | double | Pienin pyörimisnopeus, joka partikkelilla voi olla. |
| `MaxRotationSpeed` | double | Suurin pyörimisnopeus, joka partikkelilla voi olla. |
| `AlphaAmount` | double | Partikkelien läpinäkyvyys välillä 0.0–1.0. |
| `IgnoreWind` | bool | Jos `true`, [tuuli](#tuuli) ei vaikuta efektiin. |


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

`Flame` saa parametrinaan vain partikkelin kuvan. Partikkelien määrää ei anneta, eikä liekkiä käynnistetä erikseen `AddEffect`-metodilla, koska liekki on jatkuva efekti: se palaa heti, kun se on lisätty peliin.

<video controls width="320" src="images/liekkijarjestelman-esimerkki.mp4"></video>

Liekillä on samat muokkausmahdollisuudet kuin räjähdykselläkin. Joitain hyödyllisiä ominaisuuksia voi olla mm.

- `MaxAngleChange`, joka määrittää kuinka "leveälle" liekki leviää.
- `MinLifetime` ja `MaxLifetime`, kuinka korkealle liekki nousee.
- `MinVelocity` ja `MaxVelocity`, kuinka nopeasti liekin hiukkaset liikkuvat.

## Savu

Valmiin savuefektin saa luotua `Smoke`-efektin avulla.

Savu käyttäytyy hyvin samalla tavalla kuin tuli, mutta sille Jypelistä löytyy valmis kuva.

```csharp,ignore
Smoke savu = new Smoke();
Add(savu);
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
