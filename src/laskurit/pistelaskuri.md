# Pistelaskuri

<!-- kuva puuttuu (trac ei vastaa): https://trac.cc.jyu.fi/projects/npo/raw-attachment/wiki/PistelaskurinTekeminen/pisteet.jpg --> Pistelaskurin saamiseksi tarvitaan kaksi osaa:

- Laskuri, joka **laskee** pisteitä
- Olio, joka **näyttää** pisteet ruudulla

Laskuri voi olla esimerkiksi tyyppiä `IntMeter` tai `DoubleMeter`. `IntMeter` laskee kokonaislukuja ja `DoubleMeter` desimaalilukuja. Muuten niiden käyttö ei oikeastaan eroa toisistaan. Tässä esimerkissä tehdään `IntMeter`-tyyppinen laskuri ja kiinnitetään se `Label`-tyyppiseen olioon, joka osaa näyttää ruudulla laskurin arvon.

## Laskurin luominen

Tehdään ensin yksinkertainen esimerkki pistelaskurista ja sen näytöstä:

```csharp,ignore
IntMeter pistelaskuri;

void LuoPistelaskuri()
{
    pistelaskuri = new IntMeter(0);

    Label pistenaytto = new Label();
    pistenaytto.X = Screen.Left + 100;
    pistenaytto.Y = Screen.Top - 100;
    pistenaytto.TextColor = Color.Black;
    pistenaytto.Color = Color.White;

    pistenaytto.BindTo(pistelaskuri);
    Add(pistenaytto);
}
```

Ensin luodaan `IntMeter`-tyyppinen laskuri (huom. se on tässä esimerkissä attribuuttina) ja `Label`-tyyppinen tekstikenttä ja tehdään niille halutut asetukset. Tekstikentästä ei tarvitse tehdä attribuuttia, jos sen paikkaa, väriä tai muuta ominaisuutta ei muuteta sen luomisen jälkeen.

Tekstikentän tekstin väriä voi muuttaa `TextColor`-ominaisuudesta jotta se erottuu paremmin. `Color`-ominaisuus asettaa tekstikentälle taustavärin, jos sellainen halutaan. Oletustaustaväri on läpinäkyvä, eli `Color.Transparent`.

Laskurin luonnissa parametrina annetaan sen **oletusarvo**, eli mistä arvosta laskuri lähtee liikkeelle (tässä laskuri lähtee nollasta).

Lopuksi pitää muistaa **kiinnittää** laskuri tekstikenttään. Silloin tekstikenttä osaa automaattisesti näyttää laskurin arvon, vaikka arvo muuttuukin. Lopuksi vielä **lisätään** tekstikenttä ruudulle Add-kutsulla. Esimerkissä tehtiin nämä asiat riveillä:

```csharp,ignore
pistenaytto.BindTo(pistelaskuri);
Add(pistenaytto);
```

Lopuksi kutsutaan tätä kirjoittamaamme `LuoPistelaskuri`-aliohjelmaa pelin `Begin`-aliohjelmasta, jotta siinä oleva ohjelmakoodi tulee suoritetuksi.

```csharp,ignore
LuoPistelaskuri();
```

!

## Laskurin laskentaväli

Oletuksena laskuri voi saada arvoja nollasta ylöspäin niin pitkälle kuin lukualuetta riittää. Laskurin oletusarvo, eli arvo josta se aloittaa on 0. Näitä kaikkia voidaan muuttaa parametreilla haluttaessa.

Esimerkiksi jos laskurin halutaan saavan myös negatiivisia arvoja, on sille alustettaessa annettava parametrina negatiivinen minimiarvo.

### Aloittaminen arvosta 1

kokonaisluvuilla

```csharp,ignore
IntMeter laskuri = new IntMeter(1)
```

tai desimaaliluvuilla

```csharp,ignore
DoubleMeter laskuri = new DoubleMeter(1)
```

### Positiiviset ja negatiiviset kokonaisluvut

```csharp,ignore
IntMeter laskuri = new IntMeter(0, int.MinValue, int.MaxValue)
```

### Positiiviset ja negatiiviset desimaaliluvut

```csharp,ignore
DoubleMeter laskuri = new DoubleMeter(0, double.NegativeInfinity, double.PositiveInfinity)
```

### Lukuväli -100:sta 100:an oletusarvolla 10

kokonaisluvuilla

```csharp,ignore
IntMeter laskuri = new IntMeter(10, -100, 100)
```

tai desimaaliluvuilla

```csharp,ignore
DoubleMeter laskuri = new DoubleMeter(10, -100, 100)
```

## Otsikko laskurille

Usein on järkevää lisätä tekstikentällä otsikko, jotta tiedetään mitä laskuri ruudulla laskee. Tämä voidaan tehdä asettamalla teksti sen `Title`-ominaisuuteen:

```csharp,ignore
pistenaytto.Title = "Pisteet";
```

Nyt luomamme tekstikenttä näyttää tältä:

!

### Tarkempi otsikon määrittäminen

Jos haluat vaikuttaa tarkemmin siihen, miltä laskurin arvo näyttää otsikossa, voit käyttää siihen C#:n [​muotoilumerkkijonoja](http://msdn.microsoft.com/en-us/library/dwhawy9k.aspx).

```csharp,ignore
pistenaytto.IntFormatString = "Pisteitä: {0:D1}";
```

Samoin jos labelille annetaan taustaväri, voi esim formaatilla: " Pisteitä: {0:D1} " laittaa tyhjän molemmin puolin tekstiä. Muoto D3 tulostaisi laskurin aina niin, että siinä on vähintään kolme numeroa, esim 005.

Vastaavasti jos halutaan DoubleMeter, niin käytetään DoubleFormatString, esim `laskuri.DoubleFormatString = {0:N5}` näyttäisi viisi lukua desimaaliapisteen oikealla puolen.

## Laskurin arvon muuttaminen

Laskurin arvoa voidaan muuttaa sen `Value`-ominaisuudesta.

Tämä kasvattaa laskurin arvoa yhdellä:

```csharp,ignore
pistelaskuri.Value += 1;
```

Tämä vähentää laskurin arvoa yhdellä:

```csharp,ignore
pistelaskuri.Value -= 1;
```

Tämä asettaa laskurin arvoksi arvon 5:

```csharp,ignore
pistelaskuri.Value = 5;
```

## Laskurin arvon muuttaminen vähitellen

Jos halutaan, että laskuri kasvaa vaikkapa viiden sekunnin aikana kolme yksikköä, voidaan sille sanoa

```csharp,ignore
pistelaskuri.AddOverTime(3, 5);
```

Haluttaessa kolmanneksi parametriksi voidaan antaa aliohjelman nimi, joka suoritetaan kun lisäys on tehty. Näin saadaan helposti tehtyä esimerkiksi erilaisia voimamittareita.

Mittarista voidaan myös vähentää samalla periaatteella käyttämällä negatiivista arvoa.

```csharp,ignore
pistelaskuri.AddOverTime(-3, 5);
```

## Laskurin arvon nollaus

Laskuri voidaan nollata eli palauttaa oletusarvoonsa seuraavalla käskyllä:

```csharp,ignore
pistelaskuri.Reset();
```

## Laskurin ylä- ja alarajat sekä tapahtumat niille

Pistelaskuriin voi myös lisätä tapahtuman, kun se saavuttaa sille asetetun suurimman tai pienimmän arvon. Tapahtuman kuuntelu tehdään näin:

```csharp,ignore
IntMeter keratytEsineet = new IntMeter(0);
laskuri.MaxValue = 5;
laskuri.UpperLimit += KaikkiKeratty;
```

Tässä tapahtuman käsittelijän `KaikkiKeratty` suoritukseen siirrytään, kun laskuri saavuttaa suurimman arvonsa (5).

Tapahtumankäsittelijä on yksinkertainen aliohjelma ilman parametreja. Seuraava aliohjelma näyttää tekstin "Pelaaja 1 voitti pelin".

```csharp,ignore
void KaikkiKeratty()
{
    MessageDisplay.Add("Pelaaja 1 voitti pelin.");
}
```

Vastaavasti voidaan tehdä alarajalle:

```csharp,ignore
IntMeter pelaajanElamat = new IntMeter(3);
laskuri.MinValue = 0;
laskuri.LowerLimit += PelaajaHaviaa;
```

missä tapahtumankäsittelijä voi olla esimerkiksi

```csharp,ignore
void PelaajaHaviaa()
{
    MessageDisplay.Add("Pelaaja 1 hävisi pelin.");
}
```

## Muut tapahtumat

Ylä- ja alaraja eivät ole ainoita arvoja, joita voidaan tarkkailla. Mille tahansa mittarin arvolle voi asettaa tapahtumia `AddTrigger`-metodin avulla. Seuraava esimerkki soittaa äänen, kun pelaaja saa yli 9000 pistettä:

```csharp,ignore
pistelaskuri.AddTrigger(9000, TriggerDirection.Up, SoitaAani);
...

void SoitaAani()
{
   PlaySound("OVER NINE THOUSAND");
}
```

`AddTrigger`-aliohjelman ensimmäinen parametri on luonnollisesti mittarin arvo, ja kolmanneksi annetaan aliohjelma, jonka tapahtuma laukaisee.

Toinen parametri määrää, kummasta suunnasta tultaessa tapahtuma suoritetaan. Esimerkiksi ylläolevassa esimerkissä mittarin laskiessa arvon 9000 alapuolelle ääntä ei soiteta. Sallitut arvot ovat `TriggerDirection.Up` (mittarin arvo kasvaa), `TriggerDirection.Down` (mittarin arvo vähenee) ja `TriggerDirection.Irrelevant` (ei väliä, suoritetaan kummassakin tapauksessa).

## Tapahtumien poistaminen

Rajatapahtumat voidaan poistaa `-=`-operaattorilla.

```csharp,ignore
laskuri.LowerLimit -= PelaajaHaviaa;
laskuri.UpperLimit -= PelaajaVoittaa;
```

`AddTrigger`-metodilla lisätyt tapahtumat voidaan poistaa `RemoveTriggers`-metodilla antamalla parametriksi joko aliohjelman nimi tai pisteraja.

```csharp,ignore
laskuri.RemoveTriggers(9000);
```

tai

```csharp,ignore
laskuri.RemoveTriggers(SoitaAani);
```

Kaikki triggerit saa pois `ClearTriggers`-aliohjelmalla

```csharp,ignore
laskuri.ClearTriggers();
```

## Katso myös

- [Teksti ruudulla](../kayttoliittyma/teksti.md): näytön sijoittaminen ja ulkonäkö.
- [Etenemispalkki](etenemispalkki.md): laskurin arvo palkkina.
- [Törmäysten käsittely](../tapahtumat/tormaykset.md): pisteiden lisääminen törmäyksessä.
- [Parhaat pisteet](../kayttoliittyma/parhaiden-pisteiden-lista.md): pisteiden tallentaminen listaan.
