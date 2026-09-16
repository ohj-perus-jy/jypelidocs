# Miten saan peliin aikalaskurin?

Aikalaskurin tekemiseen tarvitsee karkeasti ottaen kaksi osaa:

- Laskurin, joka laskee aikaa
- Näytön, joka näyttää ajan

Laskuri voidaan tehdä eri tavoilla eri tarkoituksiin. Tässä on esitetty muutama eri käyttötarkoitukseen sopiva tapa laskea aikaa ja näyttää ajan kuluminen ruudulla.

## Esimerkki 1

Aikalaskuri, joka laskee aikaa loputtomiin.

Loputtomiin laskevan aikalaskurin voi tehdä ajastimen eli `Timerin` ja `Label`-tyyppisen, aikalaskurin arvoa näyttävän, olion avulla.

Tehdään ajastimesta attribuutti, jotta pääsemme siihen käsiksi muuallakin koodissa.

Ajastimella on olemassa sekunteja laskeva `SecondCounter`, joka voidaan sitoa suoraan aikanäyttöön.

Luodaan ajastin ja aikanäyttö, joka näyttää aikaa yhden desimaalin tarkkuudella ja sidotaan ajastimen sekuntimittari aikanäyttöön:

```csharp,ignore
void LuoAikalaskuri()
{
    Timer aikalaskuri = new Timer();
    aikalaskuri.Start();

    Label aikanaytto = new Label();
    aikanaytto.TextColor = Color.White;
    aikanaytto.DecimalPlaces = 1;
    aikanaytto.BindTo(aikalaskuri.SecondCounter);
    Add(aikanaytto);
}
```

Ajastin pitää muistaa käynnistää ja aikanäyttö pitää muistaa lisätä peliin.

`DecimalPlaces` kertoo kuinka monen desimaalin tarkkuudella aika näytetään. Ajastimen sekuntilaskuri `aikalaskuri.SecondCounter` sidotaan aikanäyttöön `BindTo`-metodilla. Lopuksi aikanäyttökin pitää muistaa lisätä kenttään.

Nyt aikalaskurin arvoon päästään halutussa paikassa käsiksi:

```csharp,ignore
double aikaaKulunut = aikalaskuri.SecondCounter.Value;
```

## Esimerkki 2

Aikalaskuri laskee aikaa aloittaen 0:sta ja päätyen (esimerkiksi) 30 sekuntiin.

Muuten lähes samanlainen kuin ensimmäisessä esimerkissä, mutta nyt lisätään ajastimelle tapahtuma, joka suoritetaan kun haluttu aikaväli eli `Interval` on kulunut. Katso tarkemmin ajastimista ja tapahtumista [niitä koskevalta wikisivulta.](https://trac.cc.jyu.fi/projects/npo/wiki/AjastintenKaytto)

```csharp,ignore
void LuoAikalaskuri()
{
    Timer aikalaskuri = new Timer();
    aikalaskuri.Interval = 30;
    aikalaskuri.Timeout += AikaLoppui;
    aikalaskuri.Start(1);

    Label aikanaytto = new Label();
    aikanaytto.TextColor = Color.White;
    aikanaytto.DecimalPlaces = 1;
    aikanaytto.BindTo(aikalaskuri.SecondCounter);
    Add(aikanaytto);
}

void AikaLoppui()
{
    MessageDisplay.Add( "Aika loppui..." );

    // täydennä mitä tapahtuu, kun aika loppuu
}
```

Aikalaskurin `Interval`-arvosta riippuu milloin, eli monenko sekunnin kuluttua ajastimen käynnistämisestä, `AikaLoppui`-aliohjelma suoritetaan.

## Esimerkki 3

Aikalaskuri laskee aikaa aloittaen (esimerkiksi) 30 sekunnista päätyen 0 sekuntiin.

Koska ajastimen sekuntilaskuria ei saa laskemaan takaperin, joudumme toteuttamaan alaspäin laskevan laskurin itse. Tässä on esitelty yksi tapa toteuttaa se. Tarvitaan kolme osaa: desimaalilukujen laskuri, ajastin ja näyttö.

Ideana on käyttää desimaalilukuja laskevaa laskuria ja ajastinta. Laskuri alustetaan haluttuun sekuntimäärään ja ajastimen avulla vähennetään sen arvoa aina kuluneen ajan verran. Nyt aikanäyttöön sidotaan laskurin arvo, <u>ei</u> ajastimen sekuntilaskuria.

Tehdään `DoubleMeter`-tyyppisestä laskuristamme attribuutti. Annetaan sille aloitusarvoksi 30. Aina kun ajastin laukeaa, vähennetään laskurin arvoa ja tarkastetaan onko arvo nolla tai pienempi. Katso tarkemmin ajastimista ja tapahtumista [niitä koskevalta wikisivulta.](https://trac.cc.jyu.fi/projects/npo/wiki/AjastintenKaytto)

**Tärkeää** on huomata, että laskurimme arvoa vähennetään aina sen verran, mitä on ajastimen `Interval`-arvo! Muuten se ei pysy ajassa.

```csharp,ignore
DoubleMeter alaspainlaskuri;
Timer aikalaskuri;

void LuoAikalaskuri()
{
    alaspainlaskuri = new DoubleMeter(30);

    aikalaskuri = new Timer();
    aikalaskuri.Interval = 0.1;
    aikalaskuri.Timeout += LaskeAlaspain;
    aikalaskuri.Start();

    Label aikanaytto = new Label();
    aikanaytto.TextColor = Color.White;
    aikanaytto.DecimalPlaces = 1;
    aikanaytto.BindTo(alaspainlaskuri);
    Add(aikanaytto);
}

void LaskeAlaspain()
{
    alaspainlaskuri.Value -= 0.1;

    if (alaspainlaskuri.Value <= 0)
    {
        MessageDisplay.Add("Aika loppui...");
        aikalaskuri.Stop();

        // täydennä mitä tapahtuu, kun aika loppuu
    }
}
```
