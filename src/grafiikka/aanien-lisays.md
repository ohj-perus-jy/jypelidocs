# Äänet ja musiikki

## Taustamusiikki

Taustamusiikin soittamista varten täytyy ihan ensimmäisenä tuoda taustamusiikiksi haluttu tiedosto mukaan projektiin. Taustamusiikin **tulee olla wav-tiedosto**. Liitä tiedostosi projektiin käyttämällä apuna ohjeita [sisällön tuomisesta](../aloittaminen/sisallon-tuonti.md).

Kun musiikkitiedosto on liitetty projektiin, saa sen soimaan seuraavalla koodilla:

```csharp,ignore
MediaPlayer.Play("taustamusiikki");
```

- Nimen taustamusiikki kohdalla on wav-tiedoston nimi, ilman wav-päätettä.

Tämä on suositeltu tapa, sillä se toimii kaikilla tuetuilla alustoilla, ja projektiin liitettynä tiedostot tulevat varmasti mukaan.

Voit soittaa myös suoraan URL-osoitteesta:

```csharp,ignore
MediaPlayer.PlayFromURL("http://joku.nettiosoite/musaa.wav");
```

Jos haluat toistaa biisiä ikuisesti, kirjoita

```csharp,ignore
MediaPlayer.IsRepeating = true;
```

## Äänitehosteet {#tehosteet}

Ihan ensimmäisenä pitää olla äänitiedosto, jota voidaan pelissä soittaa. Niiden tekemiseen on monia työkaluja tai voi hakea internetistä.

Kun äänitiedosto on olemassa, se pitää vielä liittää projektiin. Katso sitä varten ohjeet [sisällön tuomisesta](../aloittaminen/sisallon-tuonti.md). **Äänen täytyy olla .wav-tiedosto.** Kun äänitiedosto on liitetty projektiin, ääni on valmis soitettavaksi seuraavilla tavoilla:

Ääniefektien lataaminen tehdään samaan tapaan kuin kuvien lataaminen. Luokan sisällä (ei välttämättä minkään aliohjelman sisällä) ladataan ääniefekti omaan muuttujaansa:

```csharp,ignore
SoundEffect hyppyAani = LoadSoundEffect("aanitehoste");
```

Kun ääni on kerran ladattu, sitä voidaan käyttää seuraavasti:

```csharp,ignore
hyppyAani.Play();
```

`SoundEffectin` `Play`-metodista on myös parametreja vastaanottava versio, joka ottaa vastaan desimaalilukuna mm. äänen voimakkuuden ja korkeuden.

Jos ääniefektin korkeutta haluaa vaihdella, voi kuitenkin olla kätevämpää tehdä siitä ääniä. Yhdestä ääniefektistä voi luoda `CreateSound`-metodilla monta ääntä (`Sound`), jotka voivat soida yhtäaikaa. `Sound` on ääni, jonka voimakkuutta ja korkeutta voidaan muuttaa. Se voidaan myös keskeyttää ja jatkaa. Uusia ääniä voi käyttää esimerkiksi näin:

```csharp,ignore
Sound pelaaja1HyppyAani = hyppyAani.CreateSound();
Sound pelaaja2HyppyAani = hyppyAani.CreateSound();

pelaaja1HyppyAani.Pitch = 0.9;
pelaaja2HyppyAani.Pitch = 0.1;

pelaaja1HyppyAani.Play();
pelaaja2HyppyAani.Play();
```
