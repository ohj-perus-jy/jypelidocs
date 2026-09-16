# Aivot ja tekoäly

Joskus olioita halutaan saada liikkumaan pelissä automaattisesti ilman ihmisen ohjaamista. Tätä varten Jypelissä on olemassa muutamia erilaisia yksinkertaisia tekoälyjä.

Tekoälyn saa käyttöön antamalla halutulle oliolle aivot.

## Aivojen luominen ja käyttöönotto

Kaikkien aivojen käyttäminen toimii periaatteessa samalla tavalla:

- Ensin täytyy luoda halutunlaiset aivot.

- Sen jälkeen aivojen ominaisuuksia voi muokata juuri omaan peliin sopiviksi.

- Lopuksi aivot voidaan antaa olion käyttöön.

Esimerkki, satunnaisesti liikkuvat aivot:

```csharp,ignore
PhysicsObject randomOlio = new PhysicsObject(20.0, 20.0);
Add(randomOlio);

//Tehdään uudet satunnaisaivot, jotka liikkuvat nopeudella 200
RandomMoverBrain satunnaisaivot = new RandomMoverBrain(200);

//Ominaisuuksien muokkaaminen
satunnaisaivot.ChangeMovementSeconds = 3;

//Aivot käyttöön oliolle
randomOlio.Brain = satunnaisaivot;
```

## Erilaiset aivot

Tarkastellaan lähemmin mitä eri aivotyypeillä voi tehdä.

### Yleisiä ominaisuuksia kaikille aivoille

**Speed** säätää nopeutta, jolla aivojen omistaja liikkuu.

```csharp,ignore
aivot.Speed = 100;
```

Aivot päälle:

```csharp,ignore
aivot.Active = true;
```

Aivot pois päältä:

```csharp,ignore
aivot.Active = false;
```

**TurnWhileMoving** käskee aivoja kääntää pelaajaa menosuuntaan.

```csharp,ignore
aivot.TurnWhileMoving = true;
```

### FollowerBrain

Seuraajaolion aivot saavat olion seuraamaan yhtä tai useampaa oliota. Aivojen luonnin yhteydessä niille annetaan kohde, jota seurata:

```csharp,ignore
FollowerBrain seuraajanAivot = new FollowerBrain(pelaaja);
```

Useampien olioiden tapauksessa seurattavat oliot erotetaan pilkulla.

```csharp,ignore
FollowerBrain seuraajanAivot = new FollowerBrain(pelaaja1, pelaaja2);
```

Voit antaa aivoille myös merkkijonon (lainausmerkeissä), jolloin aivojen omistaja seuraa kaikkia olioita, joilla on kyseinen [Tag](olioiden-erottaminen-toisistaan.md)-arvo.

```csharp,ignore
FollowerBrain seuraajanAivot = new FollowerBrain("pelaaja");
```

Seuraajaolion aivoilla on muita aivoja enemmän muuttujia jotka vaikuttavat sen toimintaan.

```csharp,ignore
seuraajanAivot.Speed = 300;                 // Millä nopeudella kohdetta seurataan
seuraajanAivot.DistanceFar = 600;           // Etäisyys jolla aletaan seurata kohdetta
seuraajanAivot.DistanceClose = 200;         // Etäisyys jolloin ollaan lähellä kohdetta
seuraajanAivot.StopWhenTargetClose = true;  // Pysähdytään kun ollaan lähellä kohdetta
seuraajanAivot.FarBrain = satunnaisaivot;   // Käytetään satunnaisaivoja kun ollaan kaukana

// Tapahtuma, joka tapahtuu kun ollaan lähellä kohdetta
seuraajanAivot.TargetClose += MitaTapahtuuKunOllaanLahella;
...

// Aliohjelma joka ajetaan kun olio on tarpeeksi lähellä kohdetta.
void MitaTapahtuuKunOllaanLahella()
{
    pallo.Color = Color.Red;
}
```

FollowerBrainilta voi kysyä myös, mitä oliota se seuraa (`seuraajanAivot.CurrentTarget`), ja miten kaukana seurattava olio tällä hetkellä on (`seuraajanAivot.TargetDistance`). Jälkimmäinen on mittari (`DoubleMeter`), joten sille voi esimerkiksi lisätä tapahtuman kun on päästy tietyn matkan päähän kohteesta.

```csharp,ignore
FollowerBrain seuraajanAivot = new FollowerBrain("pelaaja");
seuraajanAivot.DistanceToTarget.AddTrigger(30, TriggerDirection.Down, Huuda);
zombi.Brain = seuraajanAivot;
...

// Aliohjelma joka ajetaan kun olio on tarpeeksi lähellä kohdetta.
void Huuda()
{
    PlaySound("Braaiins");
}
```

### RandomMoverBrain

Satunnaisesti liikkuvan olion aivot laittavat olion liikkumaan satunnaisesti (leijuen) kentässä. Satunnaisaivoille voi kertoa sekunneissa miten usein se vaihtaa liikesuuntaa:

```csharp,ignore
satunnaisaivot.ChangeMovementSeconds = 3;
```

Satunnaisaivoille voi myös antaa säteen, jonka ulkopuolelle se ei voi lähteä harhailemaan:

```csharp,ignore
satunnaisaivot.WanderRadius = 200;
```

Harhailuympyrän keskipisteen pitäisi määräytyä automaattisesti, mutta sen voi myös asettaa itse.

```csharp,ignore
satunnaisaivot.WanderPosition = new Vector(200, 300);
```

### PathFollowerBrain

Polkua seuraavat aivot kulkevat pitkin sille annettua reittiä tasaisella nopeudella.

Polku, jota aivot seuraavat annetaan vektorilistana. Listan käyttöä varten ohjelmakoodin alkuun tulee lisätä seuraava using-lause jos se sieltä puuttuu. Näin saadaan käyttöömme `List`-tyyppi.

```csharp,ignore
using System.Collections.Generic;
```

Tehdään uusi lista joka pitää sisällään vektoreita ja lisätään siihen ne vektorit, joiden kautta haluamme polun kulkevan.

```csharp,ignore
List<Vector> polku = new List<Vector>();
polku.Add(new Vector(-50, -100));
polku.Add(new Vector(-100, 50));
polku.Add(new Vector(-250, -200));
```

Sen jälkeen polku täytyy lisätä aivoille:

```csharp,ignore
polkuaivot.Path = polku;
```

Asetetaan aivot kiertämään reittiä jatkuvasti, viimeisen pisteen jälkeen palataan takaisin ensimmäiseen.

```csharp,ignore
polkuaivot.Loop = true;
```

Aivoille täytyy määrittää nopeus, jolla liikutaan:

```csharp,ignore
polkuaivot.Speed = 100;
```

### PlatformWandererBrain

Tasoa pitkin kulkevat aivot voi lisätä ainoastaan PlatformCharacter -tyyppisille olioille.

Esimerkki:

```csharp,ignore
PlatformCharacter rotta = new PlatformCharacter(20.0, 20.0);
Add(rotta);

PlatformWandererBrain tasoaivot = new PlatformWandererBrain();
tasoaivot.Speed = 100;

rotta.Brain = tasoaivot;
```

Jos haluaa, että aivoilla kävelevä hahmo voi tippua alas tasoilta:

```csharp,ignore
tasoaivot.FallsOffPlatforms = true;
```

Jos haluaa, että aivot yrittävät hyppiä ylemmälle tasolle törmätessään seinään:

```csharp,ignore
tasoaivot.JumpSpeed = 700;
tasoaivot.TriesToJump = true;
```

Hyppimisen laatua voi parantaa yrittämällä muuttamalla kävelynopeutta ja hyppynopeutta sopivassa suhteeseen keskenään.

### LabyrinthWandererBrain

Labyrintissä vaeltelevat aivot voi lisätä PhysicsObject-tyyppisille olioille.

Aivot käyttävät liikkumisessa hyväkseen tietoa labyrintin/kentän yhden "ruudun" koosta, joten ruudun koko on annettava uusia aivoja luotaessa. Aivoille on mahdollista antaa seinien tagin, jolloin aivot väistelevät ainoastaan seiniä. Jos tagia ei anneta, aivot väistelevät kaikkia muitakin olioita.

Esimerkki:

```csharp,ignore
//Kentän yhden "ruudun" koko, käytä samaa lukua kuin jos kenttä luotu esimerkiksi ColorTileMapilla.
const int RUUDUN_KOKO = 40;

PhysicsObject rotta = new PhysicsObject(RUUDUN_KOKO / 2, RUUDUN_KOKO / 2);
Add(rotta);

LabyrinthWandererBrain labyrinttiaivot = new LabyrinthWandererBrain(RUUDUN_KOKO);
labyrinttiaivot.Speed = 100.0;
labyrinttiaivot.LabyrinthWallTag = "seina";

rotta.Brain = labyrinttiaivot;
```
