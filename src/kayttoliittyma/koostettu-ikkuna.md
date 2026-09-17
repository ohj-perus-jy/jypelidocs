# Koostetut ikkunat

Peliin on mahdollista koostaa erilaisia ruutuja tai ikkunoita, joihin voi lisätä *tekstiä*, *kuvia*, *nappeja*, *laskureiden arvoja* ja niin edelleen.

Tämä tapahtuu `Widget`-olion avulla. `Widget` on käyttöliittymien rakentamiseen tarkoitettu komponentti, jolla on monta käyttötarkoitusta. Tässä ohjeessa näytetään, miten `Widget`ille voi lisätä lapsiolioita ja sillä tavalla koostaa erilaisia ruutuja tai ikkunoita peliin.

Oikeastaan lapsiolioita voi lisätä muillekin olioille kuin pelkästään `Widget`eille. `Widget` on kuitenkin erilaisten ikkunoiden ja ruutujen koostamiseen hyvä väline.

## Uuden `Widget`in luominen

`Widget`ille voi antaa leveyden, korkeuden ja muodon:

```csharp,ignore
Widget ruutu1 = new Widget(100.0, 50.0);
Widget ruutu2 = new Widget(100.0, 50.0, Shape.Circle);
```

`Widget`ille voi antaa käyttöön [sommittelusta](sommittelu.md) vastaavan olion, joka laittaa `Widget`in lapsioliot järjestykseen sommittelusta riippuen:

Sommittelu vaakasuunnassa:

```csharp,ignore
Widget ruutu1 = new Widget(100.0, 50.0);
ruutu1.Layout = new HorizontalLayout();

//tai

Widget ruutu2 = new Widget(new HorizontalLayout());
```

Sommittelu pystysuunnassa vastaavasti:

```csharp,ignore
Widget ruutu = new Widget(100.0, 50.0);
ruutu.Layout = new VerticalLayout();
```

`Widget`in voi sijoittaa ruudulle sen X- ja Y-koordinaateista. Se pitää muistaa myös **lisätä ruudulle**:

```csharp,ignore
Widget ruutu = new Widget(100.0, 50.0);
ruutu.X = Screen.LeftSafe + 150;
ruutu.Y = Screen.TopSafe - 100;
Add(ruutu);
```

`Widget`ille voi vaihtaa taustavärin ja reunavärin tai asettaa kuvan.

```csharp,ignore
ruutu.Color = Color.White;
ruutu.BorderColor = Color.Black;

ruutu.Image = LoadImage("kuvannimi");
```

Kuvan lisäämistä varten muista ohje [sisällön tuomisesta projektiin](../aloittaminen/sisallon-tuonti.md).

## Lapsiolioiden lisääminen

`Widget`ille voi lisätä lapsiolioita, esimerkiksi tekstikenttiä. Tällöin lapsiolion paikka ilmoitetaan suhteessa sen vanhempaan, eli siihen olioon, jolle lapsi lisättiin. Jos `Widget` käyttää [sommittelua](sommittelu.md), se järjestää oliot automaattisesti sen mukaisesti.

```csharp,ignore
Widget ruutu = new Widget(150.0, 100.0);

Label tekstikentta1 = new Label("tekstiä");
ruutu.Add(tekstikentta1);
tekstikentta1.Y = 50.0;

Add(ruutu);
```

Tässä tehty Label `tekstikentta1` sijoittuisi 50 yksikköä `ruutu`-Widgetin keskipisteestä ylöspäin.

## Esimerkki: laskuri ohjetekstillä

Tässä on koostettu yksi ruutu pistelaskurista ja tekstikentästä.

```csharp,ignore
IntMeter laskuri;

public override void Begin()
{
    laskuri = new IntMeter(0);

    Widget pisteruutu = new Widget( 100, 50 );
    pisteruutu.Layout = new VerticalLayout();
    pisteruutu.X = Screen.LeftSafe + 150;
    pisteruutu.Y = Screen.TopSafe - 100;
    Add(pisteruutu);

    Label pisteteksti = new Label("Pisteitä: ");
    pisteruutu.Add(pisteteksti);

    Label pistenaytto = new Label();
    pistenaytto.BindTo(laskuri);
    pisteruutu.Add(pistenaytto);
}
```
