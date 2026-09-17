# Parhaat pisteet

Jypeli sisältää valmiit luokat `EasyHighScore` ja `ScoreList` parhaiden pisteiden kirjaamiseen.

Näistä `EasyHighScore` on helppokäyttöisempi ja nopeampi toteuttaa.

`ScoreList` tarjoaa enemmän mahdollisuuksia muokata parhaiden pisteiden listaa, mutta samalla sen käyttö vaatii myös hieman enemmän työtä.

## EasyHighScore - parhaiden pisteiden lista nopeasti

`EasyHighScore`n käyttäminen on nopea tapa tehdä omaan peliin parhaiden pisteiden lista. `EasyHighScore` osaa automaattisesti tallentaa pisteet tiedostoon, jossa ne säilyvät, vaikka pelin sulkee välillä.

### EasyHighScore-listan luominen

Lista kannattaa asettaa attribuutiksi, jolloin sitä voidaan käyttää vapaasti mistä tahansa aliohjelmasta:

```csharp,ignore
public class Peli : Game
{
    private EasyHighScore topLista = new EasyHighScore();

    public override void Begin()
    {
      // alustuksia jne.
```

### EasyHighScore - pisteiden syöttäminen listalle

Kun halutaan syöttää pisteitä listalle, kutsutaan metodia `EnterAndShow`, jolle annetaan parametrina se pistemäärä, jolla listalle pyritään, esimerkiksi pistelaskurin arvo.

Parhaiden pisteiden listalle voi lisäksi kertoa, mikä aliohjelma suoritetaan, kun parhaat pisteet näyttävä ikkuna suljetaan.

```csharp,ignore
private void PelaajaKuoli()
{
    pelaaja.Destroy();
    topLista.EnterAndShow(pistelaskuri.Value);
    topLista.HighScoreWindow.Closed += AloitaPeli;
}
```

Jos pisteet riittävät listalle, pelaajalta kysytään automaattisesti nimi ja näytetään parhaiden pisteiden lista.

Kun ikkuna suljetaan, suoritetaan tässä esimerkissä aliohjelma `AloitaPeli`.

```csharp,ignore
public void AloitaPeli(Window sender)
{
    // ...
}
```

### EasyHighScore-listan näyttäminen ilman lisäämistä

Jos halutaan pelkästään näyttää lista ilman uuden pistemäärän lisäämisen mahdollisuutta, voidaan kirjoittaa:

```csharp,ignore
topLista.Show();
```

## ScoreList - muokattavamman pistelistan tekeminen

Jos `EasyHighScore` on riittämätön, voi parhaiden pisteiden tekemiseen käyttää vapaammin muokattavaa `ScoreList`iä. `ScoreList`issä joutuu itse huolehtimaan mm. siitä, milloin pisteet tallennetaan tiedostoon, mutta vastineeksi saa muokattavamman parhaiden pisteiden listan.

### ScoreList-listan luominen

Lista kannattaa asettaa attribuutiksi, jolloin sitä voidaan käyttää vapaasti mistä tahansa aliohjelmasta.

```csharp,ignore
public class Peli : Game
{
   private ScoreList topLista = new ScoreList(10, false, 0);
   // muut attribuutit

   public override void Begin()
   {
      // alustuksia jne.
```

`ScoreList`-olion rakentajan parametrit ovat järjestyksessä:

- **10** - kuinka monta nimeä listalle mahtuu
- **false** - onko järjestys takaperoinen (vähemmän pisteitä parempi), tässä tapauksessa ei.
- **0** - raja listalle pääsemiseen. Raja on eksklusiivinen, ts. pistemäärällä nolla ei pääse vielä listalle.

On syytä huomioida, että jos järjestyksen asettaa käänteiseksi, myös raja muuttuu käänteiseksi, eli ainoastaan rajaa pienemmät pisteet hyväksytään.

Listan lataaminen tiedostosta voidaan tehdä esimerkiksi `Begin`-aliohjelmassa pelin alustuksen yhteydessä. Tässä tapauksessa tiedoston nimi on `pisteet.xml`.

```csharp,ignore
public override void Begin()
{
   topLista = DataStorage.TryLoad<ScoreList>(topLista, "pisteet.xml");
   // ...
}
```

`TryLoad` yrittää ladata listan tiedostosta, jos sellainen on olemassa ja se on oikeaa muotoa. Muuten käytetään aiemmin luotua tyhjää listaa.

### ScoreList-listan näyttäminen ruudulla

Listan näyttämiseen ruudulla on olemassa luokka `HighScoreWindow`.

```csharp,ignore
HighScoreWindow topIkkuna = new HighScoreWindow(
                             "Parhaat pisteet",
                             "Onneksi olkoon, pääsit listalle pisteillä %p! Syötä nimesi:",
                             topLista, pisteet);
topIkkuna.Closed += TallennaPisteet;
Add(topIkkuna);
```

`HighScoreWindow`-olion rakentajan parametrit ovat järjestyksessä:

- **"Parhaat pisteet"** - ennen tuloksia näytettävä viesti
- **"Onneksi olkoon, pääsit listalle pisteillä %p! Syötä nimesi:"** - viesti, joka näytetään, jos pisteet oikeuttavat listasijoitukseen
- **topLista** - lista, jonka sisältö näytetään ja jolle uusi nimi lisätään tarvittaessa
- **pisteet** - edellisessä pelissä saavutettu pistemäärä

Jos pistemäärä oikeuttaa sijoitukseen listalla, kysytään pelaajan nimeä ennen listan näyttämistä.

Jos halutaan pelkästään näyttää lista ilman lisäämisen mahdollisuutta, voidaan nimensyöttöviesti ja pistemäärä jättää pois.

```csharp,ignore
HighScoreWindow topIkkuna = new HighScoreWindow(
                              "Parhaat pisteet",
                              topLista);
topIkkuna.Closed += TallennaPisteet;
Add(topIkkuna);
```

Ensimmäinen rivi luo pisteikkunan ja kiinnittää `topLista`n siihen. Toinen rivi lisää tapahtuman `TallennaPisteet` suoritettavaksi, kun ikkuna suljetaan. Tapahtuman nimi `TallennaPisteet` vastaa samannimistä aliohjelmaa pelissä, ja siihen palataan pisteiden tallennuksen yhteydessä. Kolmas rivi lisää ikkunan ruudulle.

### ScoreList-listan tallentaminen tiedostoon

Jotta nimet pysyisivät listalla, se on tallennettava tiedostoon. Edellisessä kohdassa kiinnitimme tapahtuman `TallennaPisteet` laukaistavaksi, kun ikkuna suljetaan. Tehdään sitä vastaava aliohjelma:

```csharp,ignore
private void TallennaPisteet(Window sender)
{
   DataStorage.Save<ScoreList>(topLista, "pisteet.xml");
}
```

Näin pisteet tallentuvat samaan `pisteet.xml`-tiedostoon, josta ne ladattiinkin.

## Pisteiden esitystavan muuttaminen

Oletuksena pisteet näytetään niin monen desimaalin tarkkuudella kuin ne on annettu, mutta aina näin ei haluta. Pisteiden esitystapaa voidaan muuttaa `EasyHighScore`n tapauksessa seuraavasti:

```csharp,ignore
helppoLista.HighScoreWindow.NameInputWindow.Message.Text = "Onneksi olkoon! Sait {0:0.00} pistettä!";
helppoLista.HighScoreWindow.List.ScoreFormat = "{0:0.00}";
```

Vastaavasti `HighScoreWindow`-ikkunalle:

```csharp,ignore
hsLista.NameInputWindow.Message.Text = "Onneksi olkoon! Sait {0:0.00} pistettä. Anna nimesi";
hsLista.List.ScoreFormat = "{0:0.00}";
```

Ensimmäinen rivi määrää tekstin ikkunassa, joka kysyy pelaajan nimeä, ja toinen pisteiden esitystavan itse listassa. Lisätietoja C#:n muotoilumerkkijonoista löydät esimerkiksi [täältä](http://www.csharp-examples.net/string-format-double).
