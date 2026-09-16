# Läpsylintu, vaihe 9: Maali

## Kentän oikeaan laitaan maaliviiva

Toteutetaan kentän oikeaan reunaan maaliviiva, johon koskettaessaan pelaaja pääsee kentän läpi.

Etsi aliohjelma `LuoKentta`. Se näyttää tässä vaiheessa seuraavalta:

```csharp,ignore
private void LuoKentta()
{
    TileMap kentta = TileMap.FromLevelAsset("kentta1");
    kentta.SetTileMethod('#', LisaaTaso);
    kentta.SetTileMethod('*', LisaaTahti);
    kentta.SetTileMethod('L', LisaaPelaaja);
    kentta.SetTileMethod('v', LisaaVihollinen);
    kentta.Execute(RUUDUN_KOKO, RUUDUN_KOKO);
    Level.CreateBorders();
    Level.Background.CreateGradient(Color.White, Color.SkyBlue);
}
```

Aliohjelmassa oleva rivi `Level.CreateBorders();` luo kentän jokaiselle reunalle reunaviivan. Voit kommentoida rivin pois, koska tarvitsemme tähän peliin erillisen oikean reunan. Kommentointimerkkinä C#-kielessä toimii kaksi kauttaviivaa, `/`-merkkiä. Kauttaviivan saat painamalla `Shift + 7`. Rivin pitäisi tämän jälkeen näyttää tältä.

```csharp,ignore
// Level.CreateBorders();
```

Lisää sitten edellisen rivin alapuolelle seuraavat koodirivit, joilla ylä- ja alarivi luodaan yhdessä ja sivut luodaan erikseen.

```csharp,ignore
Level.CreateLeftBorder();
Level.CreateVerticalBorders();
Level.CreateRightBorder();
```

Koska haluamme käyttää näistä viimeisintä hyödyksi, muokataan vielä tätä oikean reunan lisäävää riviä:

```csharp,ignore
Level.CreateRightBorder();
```

tällaiseksi:

```csharp,ignore
PhysicsObject oikeaReuna = Level.CreateRightBorder();
```

Alkuun lisättiin siis fysiikkaolio-tyyppisen muuttujan esittely, ja luodun oikean reunan viite sijoitettiin siihen talteen.

Nyt voimme lisätä oikean reunan oliolle tägin, jota voimme hyödyntää hetken kuluttua törmäystarkistuksessa:

```csharp,ignore
oikeaReuna.Tag = "oikea";
```

Kokonaisuutena aliohjelma on muutosten jälkeen seuraavanlainen (tässä lisätty myös pari tyhjää riviä selkeyttämään):

```csharp,ignore
void LuoKentta()
{
    TileMap kentta = TileMap.FromLevelAsset("kentta1");
    kentta.SetTileMethod('#', LisaaTaso);
    kentta.SetTileMethod('*', LisaaTahti);
    kentta.SetTileMethod('L', LisaaPelaaja);
    kentta.SetTileMethod('v', LisaaVihollinen);
    kentta.Execute(RUUDUN_KOKO, RUUDUN_KOKO);

    //Level.CreateBorders();
    Level.CreateLeftBorder();
    Level.CreateTopBorder();
    Level.CreateBottomBorder();
    PhysicsObject oikeaReuna = Level.CreateRightBorder();
    oikeaReuna.Tag = "oikea";

    Level.Background.CreateGradient(Color.White, Color.SkyBlue);
}
```

## Maaliviivaan törmäämisen tarkistus

Etsi aliohjelma `LisaaPelaaja`, koska se sisältää kaikki pelaajaan liittyvät törmäystarkistukset. Lisää aliohjelmaan seuraava rivi:

```csharp,ignore
AddCollisionHandler(pelaaja1, "oikea", TormaaOikeaanReunaan);
```

Ohjelmointiympäristö taas varoittaa, että aliohjelmaa `TormaaOikeaanReunaan` ei vielä ole olemassa. Luodaan se luokan `Lapsylintu` sisäpuolelle, eli ennen ihan viimeistä aaltosulkua, `TormaaTahteen`-aliohjelman jälkeen.

```csharp,ignore
void TormaaOikeaanReunaan(PhysicsObject tormaaja, PhysicsObject kohde)
{

}
```

Koska aliohjelma on törmäystarkistinta varten luotu, sen on sisällettävä esittelyrivillä parametrit törmääjälle ja törmäyksen kohteelle.

Lisätään aluksi aliohjelmaan pelkästään viesti, joka kertoo pelaajalle, että kenttä on läpäisty:

```csharp,ignore
MessageDisplay.Add("Pääsit kentän läpi!");
```

Kokeile, kuinka hyvin maaliviivaan eli kentän oikeaan laitaan törmääminen toimii! Vinkki: voit testausvaiheessa "huijata" ja siirtää linnun aloituspaikan `kentta1.txt`-tiedostossa lähemmäs oikeaa reunaa, jotta koko kenttää ei tarvitse pelata läpi.

> [!KOKEILE]

## Maaliviivan törmäyksen parantelut

Voit parannella maaliviivaan törmäämistä vielä lisäämällä seuraavia rivejä aliohjelman TormaaOikeaanReunaan sisälle:

```csharp,ignore
Gravity = Vector.Zero; // Pelaaja ei enää putoa alas
```

```csharp,ignore
StopAll(); // Pysäyttää kaikki oliot, mm. vihollisten liikkeen
```

```csharp,ignore
Keyboard.Disable(Key.Up); // Poistaa pelinäppäimen käytöstä
```

> [!KOKEILE]
