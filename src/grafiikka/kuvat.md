# Kuvat

Jypelissä kaikilla ruudulla näkyvillä olioilla (esimerkiksi GameObjectilla ja PhysicsObjectilla) on ominaisuus `Image`, joka kertoo, minkä näköinen olio on.

## Kuvan lataaminen tiedostosta ja asettaminen oliolle

Yksinkertaisimmillaan kuva voidaan ladata sellaisenaan pelin `LoadImage`-aliohjelmalla, kun se on ensin [lisätty](https://tim.jyu.fi/view/kurssit/tie/ohj1/tyokalut/sisallon-tuominen-peliin) projektiin.

```csharp,ignore
public class Peli : PhysicsGame
{
  Image olionKuva = LoadImage("kuvanNimi");

  public override void Begin()
  {
     //...
  }
}
```

Huomaa, että png-tunnistetta *ei* tarvitse laittaa kuvan nimen perään.

## Kuvan lataaminen internetistä

Peli voi ladata kuvansa myös internetistä. Yksinkertaisimmillaan kuva voidaan asettaa oliolle seuraavasti:

```csharp,ignore
DataStorage.DoWithURL("http://bit.ly/nl9BOr", olio.SetImage);
```

`olio.SetImage` on aliohjelma, jonka viite annetaan tässä toiselle aliohjelmalle `DataStorage.DoWithURL`. `SetImage` toimii tapahtumankäsittelijänä, joka suoritetaan, kun kuva on ladattu. Toisin sanoen kuva ei ole ladattuna vielä tämän rivin (tai aliohjelman) suorituksen jälkeen, vaan Jypeli hoitaa sen taustalla, samalla kun muuta pelin koodia suoritetaan.

Pidemmässä muodossa (ilman valmista `SetImage`-aliohjelmaa) kirjoitettuna sama olisi

```csharp,ignore
DataStorage.DoWithURL("http://bit.ly/nl9BOr", AsetaKuva);
```

```csharp,ignore
void AsetaKuva(StorageFile kuvaTiedosto)
{
   olio.Image = Image.FromFile(kuvaTiedosto);
}
```

Jos kuvalle halutaan tehdä muuta(kin) kuin asettaa se oliolle, kannattaa käyttää tätä muotoa.

Jypeli antaa oletuksena kuvalle 15 sekuntia aikaa ladata. Joissain tapauksissa tämä voi olla liikaa tai liian vähän, jolloin latausajan ylärajan voi antaa itse parametrina.

```csharp,ignore
DataStorage.DoWithURL("http://bit.ly/nl9BOr", TimeSpan.FromSeconds(5), AsetaKuva);
```

Jos halutaan ladata useita kuvia netistä ja tehdä jotain vasta sen jälkeen, kun kaikki kuvat on ladattu, se on mahdollista tehdä `TriggerOnComplete`-aliohjelmaa käyttäen.

```csharp,ignore
DataStorage.TriggerOnComplete(
   JatkaLatausta,
   DataStorage.DoWithURL("http://images4.wikia.nocookie.net/__cb20101205222241/disney/images/0/07/Dewey.jpg", tupu.SetImage),
   DataStorage.DoWithURL("http://images2.wikia.nocookie.net/__cb20101205222431/disney/images/8/85/Huey.jpg", hupu.SetImage),
   DataStorage.DoWithURL("http://images2.wikia.nocookie.net/__cb20101205222760/disney/images/b/b7/Louie.jpg", lupu.SetImage)
);
```

```csharp,ignore
void JatkaLatausta()
{
   // täällä oleva koodi suoritetaan kun kuvat on ladattu
}
```

Myös tässä tapauksessa on mahdollista säätää parametrilla, kuinka kauan odotetaan yksittäisen kuvan latautumista.

```csharp,ignore
DataStorage.TriggerOnComplete(
   JatkaLatausta,
   TimeSpan.FromSeconds(5),
   DataStorage.DoWithURL("http://images4.wikia.nocookie.net/__cb20101205222241/disney/images/0/07/Dewey.jpg", tupu.SetImage),
   DataStorage.DoWithURL("http://images2.wikia.nocookie.net/__cb20101205222431/disney/images/8/85/Huey.jpg", hupu.SetImage),
   DataStorage.DoWithURL("http://images2.wikia.nocookie.net/__cb20101205222760/disney/images/b/b7/Louie.jpg", lupu.SetImage)
);
```

## Projektiin liittämättömän kuvan lataaminen

Joskus voi tulla tarve ladata kuvia, joita ei ole lisätty mukaan projektiin. Tähän soveltuu kutsu:

Windowsissa:

```csharp,ignore
Image kuva = Image.FromFile("C:\\Users\\Mikko\\Kuvat\\kissa.png");
```

Macilla:

```csharp,ignore
Image kuva = Image.FromFile("/Users/mikko/Kuvat/kissa.png");
```

Huomaa, että Windows-polussa kansioiden välissä on kaksi `\\`-merkkiä, Macilla yksi `/`-merkki. Kuva voi olla png-, jpeg- tai bmp-muotoinen.

Kannattaa kuitenkin huomioida, että tämän käyttö vaikeuttaa pelin jakamista muille ja että polkujen oikeellisuudesta tulee pitää enemmän huolta. Tätä ei siis kannata käyttää, ellei ole aivan varma, mitä on tekemässä.

## Yksivärisen kuvan luominen

Yleensä kun halutaan tehdä oliosta yksivärinen, voidaan sen `Color`-ominaisuuteen asettaa tietty väriarvo. Joissain tapauksissa kuitenkin voidaan haluta tehdä tietyn kokoinen kuva, joka on vain yhtä väriä esimerkiksi pohjaksi muulle grafiikalle. Se onnistuu `Image`-luokan rakentajalla:

```csharp,ignore
Image punainenKuva = new Image(200, 100, Color.Red);
```

## Kahden tai useamman kuvan liittäminen yhdeksi

Kaksi erillistä kuvaa on mahdollista liittää yhteen joko vaaka- tai pystysuunnassa käyttämällä `Image`-luokan staattisia aliohjelmia `TileHorizontal` ja `TileVertical`.

```csharp,ignore
Image valkoinen = new Image(80, 27, Color.White);
Image punainen = new Image(80, 27, Color.Red);
Image puolanLippu = Image.TileVertical(valkoinen, punainen);
```

Huomaa, että vaakasuunnassa liitettäessä kuvien korkeuden ja pystysuunnassa kuvien leveyden on oltava samat.

Kuvia on myös mahdollista liittää peräkkäin useampia kuin kaksi, mutta se vaatii useamman aliohjelmakutsun.

```csharp,ignore
Image sininen = new Image(80, 18, Color.Blue);
Image valkoinen = new Image(80, 18, Color.White);
Image punainen = new Image(80, 18, Color.Red);

Image sinivalkoinen = Image.TileHorizontal(sininen, valkoinen);
Image ranskanLippu = Image.TileHorizontal(sinivalkoinen, punainen);
```

## Yksittäisten pikselien asettaminen

Kuvan pikselidataan päästään käsiksi hakasulku- eli indeksointioperaattorin avulla. Yksittäisen pikselin väri saadaan kuvasta seuraavalla tavalla

```csharp,ignore
Color pikselinVari = kuva[rivi, sarake];
```

Indekseistä `rivi` on pikselin paikka pysty- eli Y-suunnassa ja `sarake` vaaka- eli X-suunnassa. Toisin kuin pelimaailman koordinaateissa, *tekstuurikoordinaateissa* origo sijaitsee kuvan vasemmassa yläreunassa ja y-koordinaatti kasvaa alaspäin. Koordinaatit ovat positiivisia kokonaislukuja (rivi vähintään 0, enintään kuva.Height - 1 ja sarake vähintään 0 ja enintään kuva.Width - 1).

Pikselin värin voi asettaa seuraavanlaisella sijoituksella

```csharp,ignore
kuva[rivi, sarake] = Color.Fuchsia;
```

tai mikä tahansa väri, joka halutaan pikselille antaa.

Lisää pikselitason kuvankäsittelystä löytyy [Kuvankäsittely-sivulta](kuvankasittely.md).

## Kuvan rajaaminen

Kuvasta voidaan rajata pienempi osa toiseen (tai samaan) muuttujaan käyttämällä sen `Area`-aliohjelmaa.

```csharp,ignore
Image kuvanOsa = kuva.Area(10, 10, 20, 20);
```

Parametrit ovat järjestyksessä vasen reuna, yläreuna, oikea reuna ja alareuna. On huomattava, että **alkuperäisen kuvan sisältö muuttuu, jos rajattua kuvaa muutetaan!** Jos tätä ei haluta, voidaan rajatusta kuvasta ottaa kopio

```csharp,ignore
Image kuvanOsa = kuva.Area(10, 10, 20, 20).Clone();
```

## Kuvan tai sen osien täyttäminen värillä

`Image`-luokka sisältää aliohjelman `Fill` kuvan täyttämiseen yksittäisellä värillä.

```csharp,ignore
kuva.Fill(Color.Green);
```

Koko kuvan täyttäminen on harvemmin mielekästä, mutta `Area`-aliohjelman kanssa yhdistettynä kuvasta voidaan täyttää helposti suorakulmion muotoisia alueita.

```csharp,ignore
Image suomenLippu = new Image(80, 54, Color.White);
suomenLippu.Area(0, 18, 79, 36).Fill( Color.Blue);
suomenLippu.Area(18, 0, 36, 53).Fill( Color.Blue);
```

## Värin korvaaminen toisella värillä kuvassa

Kuvan valkoisten kohtien muuttaminen vihreiksi:

```csharp,ignore
kuva.ReplaceColor(Color.White, Color.Green);
```

## Kuvan tallentaminen tiedostoon

Kuva voidaan myös tallentaa tiedostoon tarvittaessa joko jpeg- tai png-muodossa.

```csharp,ignore
DataStorage.Export(kuva.AsJpeg(), "kuva.jpg");
```

```csharp,ignore
DataStorage.Export(kuva.AsPng(), "kuva.png");
```

Kuva tallentuu pelihakemiston (projektihakemiston alla yleensä bin) alle Data-alihakemistoon.

## Miksi kuvani näyttää suttuiselta pelissä?

Käytät mahdollisesti liian pientä kuvaa. Jypeli skaalaa kuvan olion kokoiseksi, mutta se ei osaa tehdä siitä tarkempaa kuin se jo on. Kuvan skaalauskäytökseen voit vaikuttaa asettamalla

```csharp,ignore
kuva.Scaling = ImageScaling.Nearest
```

tai

```csharp,ignore
kuva.Scaling = ImageScaling.Linear
```

`Nearest`-asetus on sopiva, jos halutaan pikseligrafiikkaa, `Linear` taas, kun halutaan, että kuva mieluummin "sumenee". Kannattaa kokeilla, kumpi näyttää omassa pelissä paremmalta.

<!-- TODO: Tähän voisi laittaa esimerkit molemmista. -->

## Miten saan muokattua pelin kuvaketta (ikonia)?

- Pelin hakemistossa on tiedosto Game.ico
- Avaa tiedosto vaikka Paint.NETillä tai ihan Paintilla
- Muokkaa ikoni mieleiseksi
- Tallenna `Game.png`-tiedostoksi
