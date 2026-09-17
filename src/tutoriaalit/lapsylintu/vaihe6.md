# Läpsylintu, vaihe 6: Ikkunan koko ja kuolema

## Ikkunan koon vaihtaminen

Jos haluat vaihtaa peli-ikkunan kokoa, voit tehdä sen lisäämällä aivan `Begin`-aliohjelman alkuun rivin:

```csharp,ignore
SetWindowSize(1280, 720);
```

Numerot kertovat ikkunan leveyden ja korkeuden. Kokeile, millä luvuilla ikkuna on hyvänkokoinen. Ikkunaa ei kuitenkaan kannata laittaa suuremmaksi kuin näyttösi. :)

Useimmiten kannettavissa on myös näytönskaalaus käytössä, jolloin ikkunan resoluutio ei täysin vastaa näytön todellista resoluutiota. Kokeile ja muokkaa arvoja. Oman näyttösi resoluution näet koneesi näyttöasetuksista.

## Kuolemiseen erilainen kuva

Jotta peliä pelaavalle tulee varmasti selväksi, että pelihahmo on kuollut seinään osumisen jälkeen, vaihdetaan kuolleelle hahmolle erilainen kuva.

Lataa oheinen kuva omalle tietokoneellesi kuten aiemmatkin kuvat. Yliopiston koneilla tallenna se `C:\MyTemp\Omanimi`-kansioon, ei Omat tiedostot -kansioon, sillä se täyttää käyttäjäprofiilin levytilan.

![](images/kuollut.png)

Tallenna kuva nimellä `kuollut.png`.

Muistatko vielä, miten tiedosto lisättiin projektiin? Katso mallia [vaiheesta 3](vaihe3.md).

Koodissa on attribuutteina esitelty muun muassa seuraavat kuvat.

```csharp,ignore
private Image pelaajanKuva = LoadImage("lintu.png");
private Image[] pelaajanHyppykuvat = LoadImages("lapsy.png", "lintu.png");
```

Lisää näiden rivien perään `kuollut.png` seuraavasti:

```csharp,ignore
private Image pelaajanKuolemakuva = LoadImage("kuollut.png");
```

Jotta kuolemisen jälkeen tulisi käyttöön uusi kuva, se täytyy lisätä `TormaaTasoon`-aliohjelmassa.

Etsi `TormaaTasoon`-aliohjelma ja sen sisältämä `if (peliKaynnissa)`-lohko. Lisää tämän lohkon sisälle seuraavat rivit.

```csharp,ignore
// Asetetaan pelaajan normaali kuva kuolemiskuvaksi:
pelaaja1.Image = pelaajanKuolemakuva;

// Asetetaan pelaajan animaatiot kuolemisen animaatioksi (voi sisältää useammankin kuvan):
Animation kuolemisanimaatio = new Animation(pelaajanKuolemakuva);
pelaaja1.AnimFall = kuolemisanimaatio;
pelaaja1.AnimJump = kuolemisanimaatio;
```

Pelihahmon kuolemisanimaatio voisi olla myös useamman kuvan sisältävä, mutta tässä esimerkissä käytetään vain yksittäistä kuvaa, jossa linnun silmät ovat sarjakuvamaisesti ristissä.

> [!KOKEILE]
