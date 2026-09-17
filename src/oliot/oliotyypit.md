# Oliotyypit

Tässä on esitelty tarkemmin muutama tärkeä olio pelin tekemisen kannalta. Muitakin olioita on tietysti olemassa.

## GameObject

`GameObject` on peliolio, joka ei noudata fysiikan lakeja.

Esimerkki peliolion lisäämisestä:

```csharp,ignore
GameObject kissa = new GameObject(40, 20);
kissa.Shape = Shape.Rectangle;
Add(kissa);
```

- Esimerkissä luotiin olio nimeltä kissa, jonka leveys on 40 ja korkeus 20.
- Asetettiin kissan muodoksi suorakulmio. Muoto voisi tietenkin olla myös muu kuin suorakulmio.
- Lopuksi kissa lisättiin kenttään.

### Tärkeimmät ominaisuudet

|  |  |
|:---|----|
| Angle | Kulma, jolla olioita voi kääntää. |
| Animation | Animoitu tekstuuri. |
| Brain | Aivot, jotka oliolle voi asettaa. |
| Color | Olion väri, jos tekstuuria ei ole käytössä tai tekstuuri on (osittain) läpinäkyvä. |
| Image | Olion tekstuuri. |
| IsVisible | Onko olio näkyvä vai ei. |
| Lifetime | Elinaika. |
| MaximumLifetime | Maksimielinaika. |
| Position | Sijainti koordinaateissa. |
| Size | Olion koko. |
| Shape | Olion muoto. |
| Tag | Vapaasti asetettava muuttuja. |
| X | Sijainti x-koordinaatissa. |
| Y | Sijainti y-koordinaatissa. |

### Tärkeimmät metodit

|  |  |
|:---|----|
| Move(liikevektori) | Siirtää oliota eteenpäin annetun vektorin verran. |
| MoveTo(paikkavektori, nopeus) | Aloittaa olion siirtämisen haluttuun paikkaan tietyllä nopeudella. Jos välissä on esimerkiksi seinä tai hitaampaa maastoa, olion nopeus voi olla pienempi kuin sille annettu nopeus. |
| Destroy() | Tuhoaa olion. |

## PhysicsObject

PhysicsObject on GameObjectin perillinen, joka noudattaa fysiikan lakeja, kuten painovoimaa, ja törmäilee muihin fysiikkaa noudattaviin olioihin.

Huom! PhysicsObjectilla on **lisäksi samat ominaisuudet, metodit ja tapahtumat kuin GameObjectilla**.

Esimerkki fysiikkaolion lisäämisestä:

```csharp,ignore
PhysicsObject koira = new PhysicsObject(200, 40);
koira.Shape = Shape.Rectangle;
koira.Mass = 15.0;
Add(koira);
```

- Esimerkissä luotiin aluksi koira, jonka leveys on 200 ja korkeus 40.
- Asetettiin koiran muoto suorakulmioksi.
- Annettiin koiralle massaksi 15. Katso [Fysiikan ilmiöt, Massa](../fysiikka/fysiikan-ilmiot.md#massa).
- Lopuksi koira lisättiin kenttään.

### Tärkeimmät ominaisuudet

|  |  |
|:---|:---|
| AngularDamping | Pyörimisliikkeen hidastuminen |
| CanRotate | Voiko kappale pyöriä |
| IgnoresGravity | Vaikuttaako painovoima |
| IgnoresPhysicsLogics | Vaikuttaako fysiikka |
| IgnoresCollisionResponse | Voiko kappale törmätä |
| IgnoresExplosions | Vaikuttaako räjähdysten paineaalto |
| KineticFriction | Liikekitka. Liikettä vastustava voima, joka ilmenee, kun kaksi oliota liikkuu toisiaan vasten (esim. laatikko liukuu maata pitkin). Arvot välillä 0.0 (ei kitkaa) ja 1.0 (täysi kitka). |
| LinearDamping | Liikkeen hidastuminen. Hidastaa olion vauhtia, vaikka se ei osuisi mihinkään. Vähän kuin väliaineen (esim. ilman tai veden) vastus. Oletusarvo on 1.0, jolloin hidastumista ei ole. Mitä pienempi arvo, sitä enemmän kappale hidastuu. Yleensä kannattaa käyttää arvoja, jotka ovat lähellä ykköstä, esim. 0.95. |
| Mass | Olion massa. Kuinka painava olio on. |
| MaxVelocity | Suurin nopeus, jonka olio voi saavuttaa. |
| MomentOfInertia | Olion hitausmomentti. Mitä suurempi hitausmomentti, sitä enemmän vääntöä tarvitaan olion pyörittämiseksi. Jos haluat, että olio ei pyöri lainkaan, muokkaa `CanRotate`-kentän arvoa. |
| Restitution | Olion kimmoisuus. |
| StaticFriction | Lepokitka. Liikkeen alkamista vastustava voima, joka ilmenee, kun olio yrittää lähteä liikkeelle toisen olion pinnalta (esim. laatikkoa yritetään työntää eteenpäin). |
| Velocity | Olion nopeus. |

### Tärkeimmät metodit

|  |  |
|:---|----|
| Hit() | Kohdistaa olioon impulssin, joka saa olion nopeasti liikkeeseen. |
| MakeOneWay() | Olion läpi voi mennä tietystä suunnasta. Erityisen kätevä tasohyppelypeleissä. |
| Push() | Työntää oliota annetun voimavektorin mukaisesti. |
| Stop() | Pysäyttää olion. |
| StopHorizontal() | Pysäyttää olion vaakasuunnassa. |
| StopVertical() | Pysäyttää olion pystysuunnassa. |

### Törmäyksistä

[Miten voin liittää törmäyksiin tapahtumia?](../tapahtumat/tormaykset.md)

## PlatformCharacter

Tasohyppelyhahmo eli PlatformCharacter on PhysicsObjectin perillinen, joka voi lisäksi helposti esimerkiksi kävellä pinnoilla ja hyppiä.

PlatformCharacterilla on **lisäksi samat ominaisuudet, metodit ja tapahtumat kuin PhysicsObjectilla** (ja siten myös GameObjectilla).

```csharp,ignore
PlatformCharacter rotta = new PlatformCharacter(200, 50);
Add(rotta);
```

### Tärkeimmät ominaisuudet

|                 |                                                         |
|:----------------|:--------------------------------------------------------|
| CanMoveOnAir    | Voiko liikkua ilmassa                                   |
| FacingDirection | Hahmon rintamasuunta                                    |
| AnimFall        | Animaatio tai kuva pudotessa (suunta oikealle)          |
| AnimIdle        | Animaatio tai kuva paikallaan ollessa (suunta oikealle) |
| AnimJump        | Animaatio tai kuva hypätessä (suunta oikealle)          |
| AnimWalk        | Animaatio tai kuva kävellessä (suunta oikealle)         |
| Weapon          | Hahmon ase                                              |

Animaatioita tai kuvia asetettaessa riittää asettaa oikealle osoittava kuva tai animaatio. Jypeli osaa automaattisesti kääntää sen, kun hahmo kääntyy vasemmalle.

### Tärkeimmät metodit

| Nimi | Parametrit | Metodin selitys |
|:---|:---|:---|
| ForceJump | **double** nopeus | Hyppää, vaikka olio olisi jo ilmassa. |
| Jump | **double** nopeus | Olio hyppää. Ottaa huomioon mm. sen, onko olio jo ilmassa, jolloin ei hypätä uudestaan. Parametrina otetaan desimaalilukuna vastaan nopeus, jolla olio hyppää. |
| Walk | **double** vaakanopeus | Olio kävelee. Mahdollisimman luonnollisen näköinen kävelyyn tarkoitettu metodi. Parametrina desimaaliluku, jolla ilmaistaan kävelyn nopeus vaakasuunnassa. Plusmerkkinen luku tarkoittaa oikealle päin kävelyä, miinusmerkkinen vasemmalle. |

## PlatformCharacter2

PlatformCharacter2 on myös tasohyppelyhahmo, mutta se käyttäytyy hieman eri tavalla kuin PlatformCharacter. Pähkinänkuoressa `PlatformCharacter2` käyttää liikkumiseen kiihtyvyyttä (`Acceleration`) ja maksiminopeutta (`MaxVelocity`).

### Tärkeimmät ominaisuudet (eri kuin PlatformCharacterilla)

|              |                                          |
|:-------------|:-----------------------------------------|
| Acceleration | Hahmon kiihtyvyys                        |
| MaxVelocity  | Suurin nopeus, jonka hahmo voi saavuttaa |

### Tärkeimmät ominaisuudet (samat kuin PlatformCharacterilla)

|                       |                                      |
|:----------------------|:-------------------------------------|
| CanMoveOnAir          | Voiko liikkua ilmassa                |
| FacingDirection       | Hahmon rintamasuunta                 |
| AnimFall              | Animaatio tai kuva pudotessa (suunta oikealle) |
| AnimIdle              | Animaatio tai kuva paikallaan ollessa (suunta oikealle) |
| AnimJump              | Animaatio tai kuva hypätessä (suunta oikealle) |
| AnimWalk              | Animaatio tai kuva kävellessä (suunta oikealle) |
| Weapon                | Hahmon ase                           |

### Tärkeimmät metodit

| Nimi | Parametrit | Metodin selitys |
|:---|:---|:---|
| ForceJump | **double** nopeus | Hyppää, vaikka olio olisi jo ilmassa. |
| Jump | **double** nopeus | Olio hyppää. Ottaa huomioon mm. sen, onko olio jo ilmassa, jolloin ei hypätä uudestaan. Parametrina otetaan desimaalilukuna vastaan nopeus, jolla olio hyppää. |
| Walk | **Direction** suunta | Olio kävelee. Mahdollisimman luonnollisen näköinen kävelyyn tarkoitettu metodi. Parametrina suunta, joka voi olla `Direction.Left` tai `Direction.Right`. Jos suuntaa ei anneta, käytetään nykyistä rintamasuuntaa (FacingDirection). Nopeus määräytyy `Acceleration`- ja `MaxVelocity`-ominaisuuksista. |
| StopWalking | | Lopettaa kävelyn. |

## Automobile

Auto-olio eli Automobile-tyypin olio on PhysicsObjectin perillinen, joka voi esimerkiksi kiihdyttää, jarruttaa ja käyttäytyä kuin auto.

Automobilella on siis **lisäksi samat ominaisuudet, metodit ja tapahtumat kuin GameObjectilla ja PhysicsObjectilla**.

### Tärkeimmät ominaisuudet

|                   |                      |
|:------------------|:---------------------|
| Acceleration      | Auton kiihtyvyys     |
| BrakeDeceleration | Jarrujen tehokkuus   |
| Maneuverability   | Auton ohjattavuus    |
| TopSpeed          | Auton huippunopeus   |

### Tärkeimmät metodit

|            |            |
|:-----------|:-----------|
| Accelerate | Kiihdyttää |
| Brake      | Jarruttaa  |
| Turn       | Kääntyy    |

## Tank

Tank eli tankkiolio on sivusta kuvattu tankki, joka on PhysicsObjectin perillinen ja jolla on lisäksi tankille kuuluvia ominaisuuksia, kuten osumapisteet ja tykki.

Tankilla on siis **lisäksi samat ominaisuudet, metodit ja tapahtumat kuin GameObjectilla ja PhysicsObjectilla**.

### Tärkeimmät ominaisuudet

|           |              |
|:----------|:-------------|
| Ammo      | Ammukset     |
| Cannon    | Tykki        |
| HitPoints | Osumapisteet |

### Tärkeimmät metodit

|            |                       |
|:-----------|:----------------------|
| Accelerate | Kiihdyttää.           |
| Shoot      | Ampuu tankin tykillä. |

## PhysicsStructure

PhysicsStructure on rakenne, johon voi lisätä useita PhysicsObjecteja, ja ne pysyvät tasaisen välimatkan päässä toisistaan kuin näkymättömillä kiinnikkeillä yhdistettyinä.

```csharp,ignore
PhysicsObject o1 = new PhysicsObject(20, 20);
PhysicsObject o2 = new PhysicsObject(20, 20);

o1.Position = new Vector(-100, 200);
o2.Position = new Vector(100, 150);

PhysicsStructure rakenne = new PhysicsStructure(o1, o2);
Add(rakenne);
```

Rakenteeseen kuuluvia olioita ei tarvitse erikseen lisätä peliin Add-metodilla, riittää, kun rakenteen itsessään lisää. Rakenteella on paljon samoja ominaisuuksia ja metodeita kuin PhysicsObjectilla, ja niiden käyttäminen vaikuttaa kaikkiin rakenteen osiin.

### Tärkeimmät metodit

| Nimi   | Parametrit             | Metodin selitys                 |
|:-------|:-----------------------|:--------------------------------|
| Add    | **PhysicsObject** olio | Lisää uuden olion rakenteeseen. |
| Remove | **PhysicsObject** olio | Poistaa olion rakenteesta.      |
