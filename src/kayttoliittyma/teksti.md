# Miten ruudulle saa näkymään tekstiä?

- MessageDisplay on viestinäyttö, joka tulee oletuksena pelien mukana (ks. tarkemmat ohjeet alempana).
- Label on olio, joka näyttää tekstiä kuten MessageDisplay tai erilaisten mittareiden arvoja, kuten IntMeter ja DoubleMeter. Ei tule oletuksena pelien mukana. Täytyy siis lisätä itse.

## MessageDisplay

Kaikissa Jypeli-kirjastolla tehdyissä peleissä on mukana yksi viestinäyttö nimeltään **MessageDisplay**. Se sijaitsee oletuksena näytön vasemmassa yläreunassa.

Viestin voi lisätä seuraavasti:

```csharp,ignore
MessageDisplay.Add("Moi!");
```

Viestinäytön kaikki viestit voi tyhjentää seuraavasti:

```csharp,ignore
MessageDisplay.Clear();
```

Tekstin väri on oletuksena musta, joten viestit eivät näy, jos taustakuva on hyvin tumma. Viestinäytön tekstin värin voikin vaihtaa seuraavasti:

```csharp,ignore
MessageDisplay.TextColor = Color.White;
```

Viesten kestoajan, jonka jälkeen ne häipyvät, voi asettaa MessageDisplayn `MessageTime`-ominaisuuteen. Viestien kestoaika täytyy silloin ilmaista TimeSpan-oliona. Se on olio, joka pitää sisällään erilaisia aikajaksoja. Uuden TimeSpan-olion voi luoda monella eri tavalla. Tässä MessageTimeksi asetetaan 10 sekunnin mittainen aikajakso.

```csharp,ignore
MessageDisplay.MessageTime = new TimeSpan(0, 0, 10);
```

Viestinäytölle voi myös määritellä, kuinka monta viestiä se näyttää enintään kerralla:

```csharp,ignore
MessageDisplay.MaxMessageCount = 5;
```

## Label

`Label` on tekstikenttä, jonka voi halutessaan lisätä ruudulle. Sitä voi käyttää joko **tekstin** esittämiseen tai jonkin **laskurin arvon** esittämiseen.

### Uuden tekstikentän luominen

Tyhjä tekstikenttä, koko määräytyy automaattisesti tekstin mukaan:

```csharp,ignore
Label tekstikentta = new Label();
Add(tekstikentta);
```

Tekstikenttä annetulla tekstillä, koko määräytyy tekstin mukaan:

```csharp,ignore
Label tekstikentta = new Label("teksti");
Add(tekstikentta);
```

Tyhjä tekstikenttä, parametrina leveys ja korkeus:

```csharp,ignore
Label tekstikentta = new Label(50.0, 20.0);
Add(tekstikentta);
```

Tekstikenttä annetulla tekstillä, leveys 50 ja korkeus 20:

```csharp,ignore
Label tekstikentta = new Label(50.0, 20.0, "teksti");
Add(tekstikentta);
```

Esimerkkien lopussa tekstikenttä aina lisätään ruudulle **Add**-komennolla.

Tekstikentän voi sijoittaa ruudulle haluamaansa paikkaan vaihtamalla tavalliseen tapaan sen **X**- ja **Y**-koordinaatteja:

```csharp,ignore
tekstikentta.X = Screen.Left + 100;
tekstikentta.Y = Screen.Top - 100;
```

Huomaa että Label sijaitsee ruutukoordinaateissa, eikä pelimaailman koordinaateissa. Se ei siis esimerkiksi reagoi kameran liikutteluun.

### Tekstin asettaminen

Tekstikentän tekstiä voi muuttaa sen `Text`-arvoa vaihtamalla:

```csharp,ignore
tekstikentta.Text = "kissa";
```

### Laskurin arvon näyttäminen

Katso ohjeita [pistelaskurin tekemisestä](../laskurit/pistelaskuri.md) tai [aikalaskurin tekemisestä](../laskurit/aikalaskuri.md).

### Ulkonäkö

Tekstikentän ulkonäköä voi muokata vaihtamalla sen taustan, tekstin tai reunan väriä:

```csharp,ignore
tekstikentta.Color = Color.Aqua;
tekstikentta.TextColor = Color.Red;
tekstikentta.BorderColor = Color.Black;
```
