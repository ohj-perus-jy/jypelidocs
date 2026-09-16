# Sommittelu

Sommitteluilla (layout) asemoidaan käyttöliittymän elementtejä automaattisesti. Sommitteluiden avulla välttyy itse kirjoittamasta koodia, joilla komponentit sijoitetaan paikoilleen. Näin käyttöliittymä on myös helppo saada toimimaan erikokoisilla ruuduilla.

Jypelissä on valmiina seuraavat sommittelut:

- `HorizontalLayout` sommittelee widgetit vierekkäin vaakasuunnassa.
- `VerticalLayout` sommittelee widgetit päällekkäin pystysuunnassa.

Sommittelua varten tarvitaan aina joku emo-widgetti, jonka sisälle asemoitavat oliot lisätään. Sommittelun voi antaa suoraan rakentajassa tai käyttämällä ominaisuutta `Layout`. Tällöin emo-widgettiin lisätyt oliot asemoidaan sommittelun mukaan:

```csharp,ignore
Widget alusta = new Widget(new HorizontalLayout());
Add(alusta);

Widget lapsiolio = new Widget(kuva);
alusta.Add(lapsiolio);

// ...
```

## Sommiteltavista olioista

Sommittelu tapahtuu seuraavien sommiteltavien olioiden ominaisuuksien perusteella:

- `PreferredSize` - Kuinka suuri olio haluaisi olla
- `HorizontalSizing` - Kuinka olio käyttäytyy jos käytössä oleva leveys on eri kuin toivottu (PreferredSize.X)
- `VerticalSizing` - Kuinka olio käyttäytyy jos käytössä oleva korkeus on eri kuin toivottu

**HUOM!** Olion koon muuttaminen ei saa muuttaa `PreferredSize`-ominaisuutta! (koska jos layout asettaa koon, mikä muuttaa toivottua kokoa, mikä aiheuttaa uuden koon muutoksen, mikä muuttaa toivottua kokoa, mikä taas...)

## Automaattinen koko

Esimerkki yksinkertaisesta pystysuuntaisesta asettelusta. Tässä emo-widget (muuttujassa `lista`) asettaa kokonsa automaattisesti sellaiseksi, että lapsioliot mahtuvat sen sisälle.

```csharp,ignore
Widget lista = new Widget(new VerticalLayout());
lista.BorderColor = Color.Black;
lista.Color = Color.Transparent;
Add(lista);

lista.Add(new Label("kissa"));

Widget laatikko = new Widget(100, 20);
laatikko.Color = Color.Blue;
lista.Add(laatikko);

lista.Add(new Widget(taulunKuva));

lista.Add(new Label("koira"));
```

Jos jonkin asemoitavan olion kokoa halutaan muuttaa, tulee se tehdä asettamalla sen `PreferredSize`. Huomaa, että koon asettaminen suoraan ei toimi, sillä sommittelu vastaa koon asettamisesta. Tässä esimerkissä kuvan koko asetetaan pienemmäksi lauseella

```csharp,ignore
taulu.PreferredSize = new Vector(100, 100);
```

```csharp,ignore
Widget lista = new Widget(new VerticalLayout());
lista.BorderColor = Color.Black;
lista.Color = Color.Transparent;
Add(lista);

lista.Add(new Label("kissa"));

Widget laatikko = new Widget(100, 20);
laatikko.Color = Color.Blue;
lista.Add(laatikko);

Widget taulu = new Widget(taulunKuva);
taulu.PreferredSize = new Vector(100, 100);
lista.Add(taulu);

lista.Add(new Label("koira"));
```

Olioiden asettelua saa "väljemmäksi" muuttamalla sommittelun ominaisuuksia. `Spacing`-ominaisuus vaikuttaa olioiden väliin jäävään tyhjään tilaan. Huomaa, että sitä ei ole määritelty `ILayout`-rajapinnassa, vaan `VerticalLayout`-luokassa. `Padding`-ominaisuudet asettavat reunoille jäävän tilan.

```csharp,ignore
VerticalLayout sommittelu = new VerticalLayout();
sommittelu.Spacing = 20;
sommittelu.TopPadding = 30;
sommittelu.BottomPadding = 10;
sommittelu.LeftPadding = 10;
sommittelu.RightPadding = 30;
```

```csharp,ignore
VerticalLayout sommittelu = new VerticalLayout();
sommittelu.Spacing = 20;
sommittelu.TopPadding = 30;
sommittelu.BottomPadding = 10;
sommittelu.LeftPadding = 10;
sommittelu.RightPadding = 30;

Widget lista = new Widget(sommittelu);
lista.BorderColor = Color.Black;
lista.Color = Color.Transparent;
Add(lista);

lista.Add(new Label("kissa"));

Widget laatikko = new Widget(100, 20);
laatikko.Color = Color.Blue;
lista.Add(laatikko);

lista.Add(new Widget(taulunKuva));

lista.Add(new Label("koira"));
```

## Kiinteä koko

Emo-oliolle voidaan asettaa kiinteä koko:

```csharp,ignore
Widget lista = new Widget(400, 400);
lista.SizingByLayout = false;
lista.Layout = new VerticalLayout();
```

Jos koko on pienempi kuin mitä lapsiolioiden toivoma koko (`PreferredSize`) yhteensä, niin lapsiolioita kutistetaan jotta ne mahtuvat emon sisälle. Tässä esimerkissä koko on suurempi, kuin mitä tarvitaan. Tällöin jää tyhjää tilaa:

```csharp,ignore
Widget lista = new Widget(400, 400);
lista.SizingByLayout = false;
lista.Layout = new VerticalLayout();
lista.BorderColor = Color.Black;
lista.Color = Color.Transparent;
Add(lista);

lista.Add(new Label("kissa"));

Widget laatikko = new Widget(100, 20);
laatikko.Color = Color.Blue;
lista.Add(laatikko);

lista.Add(new Widget(taulunKuva));

lista.Add(new Label("koira"));
```

Oliot voidaan asettaa täyttämään ylijäävä tila. Tämän voi tehdä erikseen pysty- ja vaakasuunnassa:

```csharp,ignore
laatikko.HorizontalSizing = Sizing.Expanding;
laatikko.VerticalSizing = Sizing.Expanding;
```

Tässä esimerkissä sininen `laatikko` laajenee sekä pysty- että vaakasuunnassa. `taulu` laajenee vain vaakasuunnassa.

```csharp,ignore
Widget lista = new Widget(400, 400);
lista.SizingByLayout = false;
lista.Layout = new VerticalLayout();
lista.BorderColor = Color.Black;
lista.Color = Color.Transparent;
Add(lista);

lista.Add(new Label("kissa"));

Widget laatikko = new Widget(100, 20);
laatikko.Color = Color.Blue;
laatikko.HorizontalSizing = Sizing.Expanding;
laatikko.VerticalSizing = Sizing.Expanding;
lista.Add(laatikko);

Widget taulu = new Widget(taulunKuva);
taulu.HorizontalSizing = Sizing.Expanding;
lista.Add(taulu);

lista.Add(new Label("koira"));
```
