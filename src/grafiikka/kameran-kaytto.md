# Miten kenttää voi zoomata (kameran käyttöohjeet)?

Pelissä tulee oletuksena aina kamera, joka näyttää pelialueen olioineen. Kameraa voi esimerkiksi zoomata lähemmäs tai kauemmas kentästä. Kameran nimi on **Camera**.

## Zoomaaminen

Kameralla voi zoomata antamalla parametriksi zoomauskertoimen.

Kun zoomauskerroin on suurempi kuin 1, niin kamera zoomaa lähemmäs:

```csharp,ignore
Camera.Zoom(1.5);
```

Jos taas zoomauskerroin on pienempi kuin 1, niin kamera zoomaa kauemmas:

```csharp,ignore
Camera.Zoom(0.5);
```

## Zoomaaminen näyttämään koko kentän kerralla

Kameran voi laittaa zoomaamaan siten, että koko kenttä näkyy kerralla näytöllä:

```csharp,ignore
Camera.ZoomToLevel();
```

Parametrina voidaan myös antaa marginaali, jos esimerkiksi halutaan nähdä hieman reunojen ulkopuolelle.

```csharp,ignore
Camera.ZoomToLevel(50);
```

Marginaali voi myös olla negatiivinen.

## Zoomaaminen näyttämään kaikki oliot

Kamera voidaan käskeä sijoittumaan niin, että kaikki peliin lisätyt oliot näkyvät ruudulla.

```csharp,ignore
Camera.ZoomToAllObjects();
```

Tälle myös voidaan antaa marginaali, jos halutaan hieman suurempi/pienempi alue näkyviin.

```csharp,ignore
Camera.ZoomToAllObject(50);
```

## Peliolion seuraaminen

Kameran voi laittaa seuraamaan tiettyä pelioliota, kuten pelaajaa:

```csharp,ignore
Camera.Follow(pelaaja1);
```

Jos halutaan seurata pelkästään vaaka- tai pystysuunnassa, voidaan Follow-aliohjelmakutsun sijasta kutsua `FollowX` tai `FollowY`.

Kamera voi seurata myös useampaaa oliota samalla kertaa. Tällöin kamera zoomaa automaattisesti niin, että kaikki oliot mahtuvat kuvaan samaan aikaan. Reunoille jäävää tilaa voi myös muuttaa erikseen pysty- ja vaakasuuntaan.

```csharp,ignore
Camera.Follow(pelaaja1, pelaaja2);
Camera.FollowXMargin = 200;
Camera.FollowYMargin = 100;
```

Kameralta voi aina pyytää olion, jota se seuraa:

```csharp,ignore
GameObject seurattuOlio = Camera.FollowedObject;
```

FollowedObject on null, jos kamera ei seuraa mitään oliota. Jos kamera seuraa useita olioita, FollowedObject on näkymätön olio seurattavien olioiden keskipisteessä.

## Seuraamisen lopettaminen

Seuraaminen voidaan lopettaa seuraavalla käskyllä:

```csharp,ignore
Camera.StopFollowing();
```

## Kameran palauttaminen alkutilaan

Kamera nollautuu takaisin alkutilaan (keskelle ruutua ja alkuperäiseen zoomauskertoimeen, lopettaa seuraamisen) seuraavasti:

```csharp,ignore
Camera.Reset();
```

Alkutilaan palauttaminen keskittää kameran koordinaatiston origoon alkuperäisellä zoomauskertoimella ja lopettaa kaikenlaisen liikkeen.

## Kameran pitäminen kentän sisällä

Jos et halua, että kamera voi näyttää aluetta kentän reunojen ulkopuolella, aseta

```csharp,ignore
Camera.StayInLevel = true;
```

## Kameran koordinaattien asettaminen

Kameralle voi myös suoraan kertoa koordinaatit, johon se halutaan keskittää. Tällöin kamera asettuu niin, että annettu piste on ruudun keskellä.

```csharp,ignore
Camera.X = Level.Right - 100;
Camera.Y = Level.Top - 400;
```

## Nopeuden asettaminen kameralle

Jos halutaan että kamera liikkuu itsekseen tietyllä nopeudella, voidaan sanoa (kuten peliolioille)

```csharp,ignore
Camera.Velocity = new Vector(200, -100);
```

Ylläolevassa esimerkissä asetettiin kamera liikkumaan 200 yksikköä sekunnissa oikealle ja 100 alaspäin.
