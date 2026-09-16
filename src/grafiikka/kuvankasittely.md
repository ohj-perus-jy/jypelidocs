# Miten voin käsitellä kuvaa (pikselitasolla)?

`Image`-luokan kuvia voidaan muokata ja ottaa kuvasta palanen ja siirtää se toiseen kohtaan. Kuvien yksittäisiä pikseleitä on myös mahdollista manipuloida.

## Kuvan yksittäisten pikselien muokkaaminen

`Image`-oliota voidaan myös käsitellä kaksiulotteisena värimatriisina. Esimerkiksi:

```csharp,ignore
Image kuva = LoadImage("norsu.png");
kuva[36, 50] = Color.Red;
kuva[36, 70] = Color.Red;
```

asettaisi nämä kaksi pikseliä punaiseksi. Huomaa että koordinaatit menevät järjestyksessä \[y,x\] vasemmasta yläkulmasta katsottuna.

## Harmaasävykuva

Kuvasta voidaan tehdä harmaasävykuva esimerkiksi seuraavasti:

```csharp,ignore
public override void Begin()
{
    Image kuva = LoadImage("lammas");
    Harmaasavy(kuva);
    GameObject lammas = new GameObject(kuva);
    Add(lammas);
    ...
}

public static void Harmaasavy(Image kuva)
{
    for (int iy = 0; iy < kuva.Height; iy++)
        for (int ix = 0; ix < kuva.Width; ix++)
        {
            Color c = kuva[iy, ix];
            byte b = (byte)((c.RedComponent +
                             c.GreenComponent +
                             c.BlueComponent) / 3);
            kuva[iy, ix] = new Color(b, b, b);
        }
}
```

## Kuvan kloonaaminen

Joskus kuvasta voi tarvita useita erilaisia versioita. Siksi edellä olisi voitu tehdä myös

```csharp,ignore
public override void Begin()
{
    Image kuva = LoadImage("lammas");
    Image harmaaKuva = kuva.Clone();
    Harmaasavy(harmaaKuva);
    GameObject lammas = new GameObject(kuva);
    Add(lammas);
    GameObject harmaaLammas = new GameObject(harmaaKuva);
    Add(harmaaLammas);
    ...
}
```

## Kuvan käsittely Color-taulukossa

Harmaasävykuvan esimerkki toimii pienille kuville. Suora kuvan käsittely Imagessa voi olla hidasta ja siksi suurempia kuvan käsittelyjä varten kuva kannattaa ottaa Color-taulukkoon, jossa sitä käsitellään.

Esimerkkinä vaikka Harmaasävykuvan tekeminen tehokkaammin:

```csharp,ignore
public static void HarmaasavyTaulukolla(Image kuva)
{
    Color[,] bmp = kuva.GetData();
    int ny = kuva.Height;
    int nx = kuva.Width;
    for (int iy = 0; iy < ny; iy++)
        for (int ix = 0; ix < nx; ix++)
        {
            Color c = bmp[iy, ix];
            byte b = (byte)((c.RedComponent +
                             c.GreenComponent +
                             c.BlueComponent) / 3);
            bmp[iy, ix] = new Color(b, b, b);
        }
    kuva.SetData(bmp);
}
```

## Kuvan käsittely uint-taulukossa

Joskus on vielä tehokkaampaa käsitellä kuvaa kokonaislukutaulukossa. Tällöin voidaan kuvan värielementit pakata yhteen positiiviseen kokonaislukutaulukkoon niin, että

- värin alpha-arvo (läpinäkyvyyden osuus, 255=ei läpinäkyvä) vie yhden tavun värin punainen osuus (r, red) vie yhden tavun (arvo 0-255) värin vihreän osuus (g, green) vie yhden tavun (arvo 0-255) värin sinisen osuus (b, blue) vie yhden tavun (arvo 0-255)

Seuraavalla aliohjelmalla kuva voidaan muuttaa täysin punaiseksi "unohtamalla" kuvasta muut värit:

```csharp,ignore
public static void Punaiseksi(Image kuva)
{
    uint[,] bmp = kuva.GetDataUInt();
    int ny = kuva.Height;
    int nx = kuva.Width;
    for (int iy = 0; iy < ny; iy++)
        for (int ix = 0; ix < nx; ix++)
        {
            uint c = bmp[iy, ix];
            byte r = Color.GetRed(c);
            byte g = 0;
            byte b = 0;
            bmp[iy, ix] = Color.PackRGB(r, g, b);
        }
    kuva.SetData(bmp);
}
```

Taulukko voidaan ottaa myös uint\[\]\[\] muodossa, joka on vielä hieman tehokkaampaa käsittelyn kannalta C#-kielessä.

## Kuvan palan siirtäminen toiseen kohti

Käyttäen edellistä ideaa, voidaan kuvasta ottaa esimerkiksi palanen ja siirtää se saman tai toisen kuvan johonkin kohtaan, esimerkiksi:

```csharp,ignore
uint[,] pala = kuva.GetDataUInt(200, 100,100,50);
kuva.SetData(pala,200,150);
```

Tätä ideaa käyttäen voitaisiin esimerkiksi animaatio piirtää yhteen ainoaan kuvaan niin, että siinä olisi vaikka 100-pikselin leveydeltä aina kutakin hahmon asentoa. Sitten kuva voitaisiin pilkkoa useaksi pienemmäksi kuvaksi:

```csharp,ignore
Image kuva = LoadImage(kuvannimi);
int n = 5;
int korkeus = 200;
int leveys = 100;
Image[] kuvat = new Image[n];

for (int i = 0; i < n; i++)
{
    kuvat[i] = new Image(leveys, korkeus, Color.Black);
    uint[,] pala = kuva.GetDataUInt(i * leveys, 0, leveys, korkeus);
    kuvat[i].SetData(pala);
}
```

Nyt kuvat-taulukossa olisi 5 kuvaa eri tilanteissa käytettäväksi.
