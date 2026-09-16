# Läpsylintu, vaihe 7: Vihollinen

Peli alkaa olla jo melko pelattava. Lisätään peliä vaikeuttamaan vielä vihollislintuja, jotta tähtien keräämisestä tulee haastavampaa!

## Vihollislintu tiedostoon

Avaa kenttätiedosto kentta1.txt ja lisää sinne merkki 'v' niinkuin vihollinen. Lisätään aluksi vain yksi vihollinen, ja kun se toimii, voidaan merkkejä lisätä enemmänkin.

Muutoksen jälkeen tiedosto voisi näyttää esimerkiksi seuraavalta:

```text
##################################################
..................................................
..............*.........................*.........
L...........................*.....................
.....*............................................
...................*..............................
..........................*................*......
................v.................................
................................*.......*.........
..................................................
..........................*.......................
##################################################
```

Vihollinen on sijainniltaan melko lähellä pelaajan lintua, jotta vihollinen näkyy jo heti pelin alkaessa ja sen ominaisuuksia on helpompi testailla.

## Vihollislintu esille pelimaailmaan

Pelkkä 'v'-kirjaimen lisääminen kenttätiedostoon ei vielä automaattisesti lisää mitään pelikentälle.

Etsi koodista kohta, jossa kerrotaan, mitä mikäkin merkki kenttätiedostossa tarkoittaa kentänlataimelle.

Oikea kohta on LuoKentta-aliohjelmassa, ja näyttää seuraavalta:

```csharp,ignore
void LuoKentta()
{
    TileMap kentta = TileMap.FromLevelAsset("kentta1");
    kentta.SetTileMethod('#', LisaaTaso);
    kentta.SetTileMethod('*', LisaaTahti);
    kentta.SetTileMethod('L', LisaaPelaaja);
    kentta.Execute(RUUDUN_KOKO, RUUDUN_KOKO);
    Level.CreateBorders();
    Level.Background.CreateGradient(Color.White, Color.SkyBlue);
}
```

Lisää rivin kentta.SetTileMethod('L', LisaaPelaaja); jälkeen seuraava rivi:

```csharp,ignore
kentta.SetTileMethod('v', LisaaVihollinen);
```

Rivi kertoo, että aina niihin kohtiin, joista löytyy merkki 'v', pitää lisätä vihollinen kutsumalla aliohjelmaa LisaaVihollinen.

Ohejelmointiympäristö valittaa, että LisaaVihollinen-aliohjelmaa ei ole olemassakaan. Sellainen täytyy siis luoda.

Lisää seuraava tyhjä aliohjelma esimerkiksi aliohjelman LisaaPelaaja jälkeen (eli päättävän }-sulun jälkeen):

```csharp,ignore
private void LisaaVihollinen(Vector paikka, double leveys, double korkeus)
{

}
```

Tämä aliohjelma saa kolme parametria:

- paikan, joka on Jypelin ns. maailmankoordinaatistossa se piste, johon olio lisätään
- leveyden, joka on Jypelin tiilielementtien leveys, tässä tapauksessa automaattisesti RUUDUN_KOKO
- korkeuden, joka on Jypelin tiilielementtien korkeus, tässä tapauksessa automaattisesti RUUDUN_KOKO

Näiden kolmen parametrin arvoja hyödyntämällä voimme lisätä vihollisen ruudulle. Lisää aliohjelman LisaaVihollinen sisällöksi seuraavat rivit:

```csharp,ignore
PhysicsObject vihollinen = new PhysicsObject(leveys, korkeus);
vihollinen.Position = paikka;
Add(vihollinen);
```

Kokeile, miten peli toimii tässä vaiheessa.

> [!KOKEILE]

## Vihollislintu pysymään ilmassa

Vihollislintumme on vielä valkoinen neliö, joka putoaa painovoiman vaikutuksesta alas maahan. **Ei välitetä vielä vihollisen ulkonäöstä**, vaan korjataan se pysymään ensin ilmassa.

Lisää rivin vihollinen.Position = paikka; jälkeen seuraava rivi:

```csharp,ignore
vihollinen.IgnoresGravity = true;
```

Kokeile, että vihollinen jää nyt ilmaan.

> [!KOKEILE]

## Vihollislintu pysymään pyörimättömänä

Jos pelaaja törmää viholliseen, vihollinen lähtee törmäyksen voimasta pyörien liikkeelle.

Lisää vihollisen luomiskohtaan seuraava rivi:

```csharp,ignore
vihollinen.CanRotate = false;
```

## Vihollislintu pysymään paikoillaan

Törmäyksen jälkeen vihollinen leijuu yhä pois paikoiltaan.

Lisää vielä seuraava rivi:

```csharp,ignore
vihollinen.IgnoresCollisionResponse = true;
```

Nyt viholliseen törmääminen ei enää vaikuta vihollisen sijaintiin mitenkään.

> [!KOKEILE]

## Vihollislintu liikkumaan ylös ja alas

Koska haluamme peliin vielä enemmän haastetta ja koska paikoillaan olevia vihollisia on helppo väistellä, lisätään vihollislintu leijumaan ylös-alas.

Se onnistuu seuraavasti:

```csharp,ignore
// Asetetaan vihollinen liikkumaan ylös-alas:
vihollinen.Oscillate(new Vector(0, 1), korkeus * 1.5, 0.3);
```

Tässä kutsutaan Oscillate-metodia, joka saa vihollisen värähtelemään. Värähtely:

- Tapahtuu suuntaan (0, 1) eli vaakasuunnassa ei mihinkään, pystysuunnassa ylöspäin.
- On korkeudeltaan vihollishahmon korkeus puolitoistakertaisena
- On taajuudeltaan 0.3 hertsiä eli tapahtuu 0.3 kertaa sekunnin aikana. Jos taajuutena olisi 1, tapahtuisi yksi kokonainen värähtely (aaltoliike) yhden sekunnin aikana.

Kokeile pelin toimivuutta! Voit lisäillä vihollisia enemmänkin vartioimaan tähtiä ja muuttaa vihollisen värähtelyasetuksia.

> [!KOKEILE]
