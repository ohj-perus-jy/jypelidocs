# Kahden pelaajan tasohyppely

Tässä esimerkissä tehdään kahden pelaajan tasohyppely välttäen turhaa toistoa aliohjelmissa.

Ensimmäinen osa näyttää vain, miten toinen pelaaja lisätään kentälle ilman koodin kahdentamista. Se on alku, josta voi jatkaa pidemmälle. Sen jälkeen tehdään neljä laajennusta, jotka ovat luontevia nimenomaan kahden pelaajan pelissä: kamera seuraa molempia, kilpailu, yhteistyö ja tönäisy. Sivun lopussa on lista jatkokehittelyideoita.

## Toinen pelaaja kentälle

Tehdään aluksi TasoHyppelyPeli-mallin mukainen projekti.

Poistetaan kenttätiedostosta `N`-merkki ja lisätään sinne merkit `1` ja `2` pelaajien aloituspaikoiksi.

Lisätään sitten toinen pelaaja luokkamuuttujaksi ensimmäisen pelaajan tapaan. Laitetaan tässä esimerkissä kummankin tekstuuriksi sama norsu.

```csharp,ignore
private PlatformCharacter pelaaja1;
private PlatformCharacter pelaaja2;
private Image pelaajan1Kuva = LoadImage("norsu.png");
private Image pelaajan2Kuva = LoadImage("norsu.png");
```

Muokataan sitten `LuoKentta`-aliohjelmaa. Luodaan pelaajaoliot jo tässä, jotta ne voidaan välittää argumentteina `LisaaPelaaja`-aliohjelmalle. Välitetään argumenttina myös pelaajan kuva.

```csharp,ignore
pelaaja1 = new PlatformCharacter(RUUDUN_KOKO, RUUDUN_KOKO);
pelaaja2 = new PlatformCharacter(RUUDUN_KOKO, RUUDUN_KOKO);
kentta.SetTileMethod('1', LisaaPelaaja, pelaaja1, pelaajan1Kuva);
kentta.SetTileMethod('2', LisaaPelaaja, pelaaja2, pelaajan2Kuva);
```

Nyt `LisaaPelaaja`-aliohjelma vaatii muutoksia.

```csharp,ignore
private void LisaaPelaaja(Vector paikka, double leveys, double korkeus, PlatformCharacter pelaaja, Image kuva)
{
  pelaaja.Position = paikka;
  pelaaja.Mass = 4.0;
  pelaaja.Image = kuva;
  AddCollisionHandler(pelaaja, "tahti", TormaaTahteen);
  Add(pelaaja);
}
```

Huomaa erityisesti, että tässä aliohjelmassa ei enää luoda pelaajaoliota (`new PlatformCharacter…`), vaan ainoastaan asetetaan parametrina saadun olion ominaisuuksien arvoja, ja lisätään olio lopuksi kentälle.

Tehdään lopuksi vielä kontrollit toiselle pelaajalle.

```csharp,ignore
Keyboard.Listen(Key.A, ButtonState.Down, Liikuta, "Liikkuu vasemmalle", pelaaja2, -NOPEUS);
Keyboard.Listen(Key.D, ButtonState.Down, Liikuta, "Liikkuu oikealle", pelaaja2, NOPEUS);
Keyboard.Listen(Key.W, ButtonState.Pressed, Hyppaa, "Pelaaja hyppää", pelaaja2, HYPPYNOPEUS);
```

Tämän vaiheen valmis koodi löytyy täältä:

Ks. <https://gitlab.jyu.fi/tie/ohj1/jypeli-esimerkit/kaksi-pelaajaa/-/blob/main/KaksiPelaajaa.cs?ref_type=heads>

> [!KOKEILE]
> Aja peli ja kävele hahmoilla eri suuntiin. Pelaaja 2 katoaa pian ruudulta, koska kamera seuraa vain pelaajaa 1. Se korjataan seuraavaksi.

## Kameran seuranta

Mallipohjan `Begin`-aliohjelmassa kamera laitetaan seuraamaan pelaajaa 1:

```csharp,ignore
Camera.Follow(pelaaja1);
Camera.ZoomFactor = 1.2;
Camera.StayInLevel = true;
```

Kamera osaa seurata useampaa oliota kerralla. Silloin se pitää kaikki seurattavat kuvassa ja zoomaa itse kauemmas, kun hahmot etääntyvät toisistaan. Korvaa kaksi ensimmäistä riviä näillä:

```csharp,ignore
Camera.Follow(pelaaja1, pelaaja2);
Camera.FollowXMargin = 200;
Camera.FollowYMargin = 100;
```

`FollowXMargin` ja `FollowYMargin` kertovat, paljonko tyhjää tilaa jätetään hahmojen ja ruudun reunan väliin. Oletusarvo on suuri, joten pienemmillä arvoilla hahmot näkyvät isompina. `ZoomFactor`-rivi jäi pois, koska kamera valitsee zoomauksen nyt itse. `StayInLevel`-rivi jätetään paikalleen, jotta kentän ulkopuolista tyhjää ei näytetä turhaan.

Lisää kameran käytöstä: [Kamera ja zoomaus](../kentat/kameran-kaytto.md).

> [!KOKEILE]
> Kävele hahmoilla kauas toisistaan. Kamera zoomaa kauemmas, ja molemmat pysyvät kuvassa.

## Kilpailu: kumpi kerää enemmän tähtiä

Yksinkertaisin kahden pelaajan peli on kilpailu: tähtiä on rajallinen määrä, ja enemmän kerännyt voittaa. Tarvitaan kummallekin oma pistelaskuri (ks. [Pistelaskuri](../kayttoliittyma/pistelaskuri.md)) ja tieto siitä, montako tähteä on vielä jäljellä.

Lisätään luokkamuuttujat:

```csharp,ignore
private IntMeter pisteet1;
private IntMeter pisteet2;
private int tahtiaJaljella = 0;
```

Laskuri ja sen näyttö tehdään aliohjelmassa, jota kutsutaan kahdesti eri paikoilla. Näin laskurin luontikoodia ei tarvitse kirjoittaa kahteen kertaan.

```csharp,ignore
private void LuoLaskurit()
{
    pisteet1 = LuoPistelaskuri(Screen.Left + 100, Screen.Top - 100);
    pisteet2 = LuoPistelaskuri(Screen.Right - 100, Screen.Top - 100);
}

private IntMeter LuoPistelaskuri(double x, double y)
{
    IntMeter laskuri = new IntMeter(0);

    Label naytto = new Label();
    naytto.X = x;
    naytto.Y = y;
    naytto.TextColor = Color.Black;
    naytto.BindTo(laskuri);
    Add(naytto);

    return laskuri;
}
```

Kutsu `LuoLaskurit();` `Begin`-aliohjelmassa `LuoKentta();`-kutsun jälkeen. Lisää sitten `LisaaTahti`-aliohjelman loppuun rivi, joka laskee kentän tähdet:

```csharp,ignore
tahtiaJaljella++;
```

Törmäyskäsittelijä `TormaaTahteen` saa ensimmäisenä parametrina sen hahmon, joka osui tähteen. Sen perusteella piste annetaan oikealle pelaajalle. Kun viimeinen tähti on kerätty, julistetaan voittaja.

```csharp,ignore
private void TormaaTahteen(PhysicsObject hahmo, PhysicsObject tahti)
{
    if (tahti.IsDestroyed) return;

    if (hahmo == pelaaja1) pisteet1.Value++;
    else pisteet2.Value++;

    maaliAani.Play();
    tahti.Destroy();
    tahtiaJaljella--;
    if (tahtiaJaljella == 0) JulistaVoittaja();
}

private void JulistaVoittaja()
{
    if (pisteet1.Value > pisteet2.Value) MessageDisplay.Add("Pelaaja 1 voitti!");
    else if (pisteet2.Value > pisteet1.Value) MessageDisplay.Add("Pelaaja 2 voitti!");
    else MessageDisplay.Add("Tasapeli!");
}
```

Ensimmäinen rivi on kahden pelaajan pelin erikoisuus. Jos molemmat hahmot osuvat samaan tähteen samalla hetkellä, käsittelijä suoritetaan kahdesti, ja ilman tarkistusta sama tähti antaisi pisteen molemmille. Tuhottu olio poistuu kentältä vasta päivityksen lopussa, mutta sen `IsDestroyed`-ominaisuus on jo `true`, joten toinen osuma jätetään huomiotta.

> [!KOKEILE]
> Kerätkää kaikki tähdet. Kun viimeinen tähti katoaa, ruudulle tulee voittajan nimi.

## Yhteistyö: ovi ja kytkin

Yhteistyöpelissä kenttää ei pääse läpi yksin. Tehdään ovi, joka on auki vain silloin, kun jompikumpi hahmo seisoo kytkimellä. Kun kytkin on kaukana ovesta, toisen pelaajan on jäätävä kytkimelle pitämään ovea auki, ja toinen menee ovesta. Jos oven toisella puolella on toinen kytkin, pelaajat pääsevät ovesta vuorotellen. Jos teet yhteistyöpelin, edellisen kohdan erilliset pistelaskurit voi jättää pois.

Lisätään kenttätiedostoon merkit `O` (ovi) ja `K` (kytkin). Mallipohjan hahmo hyppää noin seitsemän ruudun korkeuteen, joten ovi piirretään kentän ylälaitaan asti. Kenttätiedoston alaosa voi näyttää esimerkiksi tältä:

```text
                   O
                   O
                   O
  1   2     K      O     K      *   *
######################################
```

Oven paloja ja kytkimiä voi olla monta, joten ne kerätään listoihin:

```csharp,ignore
private List<PhysicsObject> ovet = new List<PhysicsObject>();
private List<PhysicsObject> kytkimet = new List<PhysicsObject>();
```

Lisätään merkeille käsittelijät `LuoKentta`-aliohjelmaan:

```csharp,ignore
kentta.SetTileMethod('O', LisaaOvi);
kentta.SetTileMethod('K', LisaaKytkin);
```

Ovi on tavallinen kiinteä olio. Kytkin on ohut laatta tason pinnalla, jonka läpi hahmo voi kävellä.

```csharp,ignore
private void LisaaOvi(Vector paikka, double leveys, double korkeus)
{
    PhysicsObject ovi = PhysicsObject.CreateStaticObject(leveys, korkeus);
    ovi.Position = paikka;
    ovi.Color = Color.Brown;
    Add(ovi);
    ovet.Add(ovi);
}

private void LisaaKytkin(Vector paikka, double leveys, double korkeus)
{
    PhysicsObject kytkin = PhysicsObject.CreateStaticObject(leveys, korkeus / 4);
    kytkin.Bottom = paikka.Y - korkeus / 2;
    kytkin.X = paikka.X;
    kytkin.IgnoresCollisionResponse = true;
    kytkin.Color = Color.Red;
    Add(kytkin);
    kytkimet.Add(kytkin);
}
```

Oven tilaa tarkistetaan ajastimella kymmenen kertaa sekunnissa ([Ajastimet](../tapahtumat/ajastimet.md)). Lisää `Begin`-aliohjelmaan `LuoKentta();`-kutsun jälkeen:

```csharp,ignore
Timer.CreateAndStart(0.1, TarkistaKytkimet);
```

Kun jompikumpi hahmo on kytkimellä, ovi piilotetaan ja siitä tehdään läpikuljettava samaan tapaan kuin tähdistä. Kun kytkimeltä poistutaan, ovi palaa kiinteäksi.

```csharp,ignore
private void TarkistaKytkimet()
{
    bool painettu = OnKytkimella(pelaaja1) || OnKytkimella(pelaaja2);
    foreach (PhysicsObject ovi in ovet)
    {
        ovi.IsVisible = !painettu;
        ovi.IgnoresCollisionResponse = painettu;
    }
}

private bool OnKytkimella(PlatformCharacter pelaaja)
{
    foreach (PhysicsObject kytkin in kytkimet)
    {
        if (Vector.Distance(kytkin.Position, pelaaja.Position) < RUUDUN_KOKO) return true;
    }
    return false;
}
```

Hahmo on kytkimellä, kun sen keskipiste on alle yhden ruudun päässä kytkimen keskipisteestä.

> [!KOKEILE]
> Jättäkää toinen hahmo kytkimelle ja viekää toinen ovesta. Kokeilkaa myös, mitä tapahtuu, jos kytkimeltä lähtee pois, kun toinen on vielä oviaukossa.

## Tönäisy

Hahmot törmäävät toisiinsa, mutta `PlatformCharacter` ei työnnä toista hahmoa kävelemällä, vaan pysähtyy siihen kuin seinään. Kilpailuun sopii tönäisynäppäin: painallus antaa lähellä olevalle toiselle hahmolle sysäyksen.

Lisätään vakio sysäyksen voimakkuudelle:

```csharp,ignore
private const double TONAISYVOIMA = 2000;
```

Lisätään näppäimet `LisaaNappaimet`-aliohjelmaan. Sama aliohjelma hoitaa molemmat tönäisyt, koska tönäisijä ja kohde annetaan parametreina eri järjestyksessä:

```csharp,ignore
Keyboard.Listen(Key.RightShift, ButtonState.Pressed, Tonaise, "Tönäisee toista pelaajaa", pelaaja1, pelaaja2);
Keyboard.Listen(Key.LeftShift, ButtonState.Pressed, Tonaise, "Tönäisee toista pelaajaa", pelaaja2, pelaaja1);
```

```csharp,ignore
private void Tonaise(PlatformCharacter tonaisija, PlatformCharacter kohde)
{
    if (Vector.Distance(tonaisija.Position, kohde.Position) > 2 * RUUDUN_KOKO) return;

    Vector suunta = (kohde.Position - tonaisija.Position).Normalize();
    kohde.MaintainMomentum = true;
    kohde.Hit(suunta * TONAISYVOIMA);
    Timer.SingleShot(0.5, delegate { kohde.MaintainMomentum = false; });
}
```

Tönäisy tehoaa vain, jos toinen hahmo on enintään kahden ruudun päässä. Suunta lasketaan hahmojen paikkojen erotuksesta, joten sysäys lähtee aina tönäisijästä poispäin. `Hit` antaa oliolle sysäyksen ([Fysiikan ilmiöt](../fysiikka/fysiikan-ilmiot.md)).

Tasohyppelyhahmo pysäyttää itsensä vaakasuunnassa joka päivityksessä, kun kävelynäppäintä ei paineta, joten pelkkä sysäys ei liikuttaisi sitä juuri lainkaan. `MaintainMomentum` antaa hahmon liukua, ja kertalaukeava ajastin ottaa sen puolen sekunnin päästä taas pois päältä, jotta hahmo ei jää liukkaaksi.

> [!KOKEILE]
> Tönäiskää toisianne tasanteen reunalla. Muuta `TONAISYVOIMA`-vakion arvoa ja katso, miten sysäys muuttuu.

## Jatkokehittely

Näitä ideoita varten joudut soveltamaan Jypelin muita ohjeita.

### Kilpajuoksu maaliin

Lisää kenttätiedostoon maalimerkki. Peli päättyy, kun ensimmäinen hahmo koskettaa maalia, ja törmäyskäsittelijä kertoo, kumpi ehti ([Törmäysten käsittely](../tapahtumat/tormaykset.md)).

### Aikaraja

Kilpailu kestää esimerkiksi 60 sekuntia, ja ajan loppuessa enemmän tähtiä kerännyt voittaa ([Aikalaskuri](../kayttoliittyma/aikalaskuri.md)). `JulistaVoittaja`-aliohjelma toimii sellaisenaan.

### Uudelleensyntyminen

Kaksinpelissä toisen kuolema ei voi lopettaa peliä, koska toinen jatkaa. Kun hahmo putoaa kuiluun tai osuu viholliseen, siirrä se pienen viiveen jälkeen takaisin aloituspaikkaan ([Ajastimet](../tapahtumat/ajastimet.md)). Aloituspaikan saat talteen `LisaaPelaaja`-aliohjelmassa. Kummallekin voi lisätä myös elämälaskurin, joka nollaan pudotessaan julistaa toisen voittajaksi ([Pistelaskuri](../kayttoliittyma/pistelaskuri.md), kohta laskurin rajat).

### Erilaiset hahmot

Yhteistyöpeli on kiinnostavampi, jos hahmot osaavat eri asioita. Pelaaja 2 hyppää korkeammalle, kun `Hyppaa`-kuuntelijalle annetaan parametriksi `HYPPYNOPEUS * 1.3`, ja pelaaja 1 voi olla nopeampi. Suunnittele kenttä niin, että kytkimelle pääsee vain korkeammalla hypyllä.

### Peliohjain toiselle pelaajalle

Kahdeksan näppäintä samalla näppäimistöllä käy ahtaaksi, eivätkä kaikki näppäimistöt rekisteröi montaa samanaikaista painallusta. Anna toiselle pelaajalle peliohjain ([Ohjainten lisääminen](../ohjaimet/ohjainten-lisays.md), kohta Peliohjain).

### Hahmot toistensa läpi

Jos hahmojen törmäily toisiinsa haittaa esimerkiksi ahtaissa käytävissä, estä törmäys pelaajien välillä ([Törmäysten estäminen](../tapahtumat/tormayksen-estaminen.md)).

### Uusi peli

Lisää näppäin, joka aloittaa pelin alusta ja nollaa laskurit ([Pelin aloittaminen alusta](../kentat/aloittaminen-alusta.md)).
