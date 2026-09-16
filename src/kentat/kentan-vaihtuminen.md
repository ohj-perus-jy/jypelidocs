# Kentän vaihtaminen

Monissa peleissä on useita eri kenttiä. Tässä on yksi tapa tai periaate, miten saat omaan peliisi monta erilaista kenttää ja miten kenttiä voi vaihtaa.

Periaatteena on se, että pidetään koodissa jossain muuttujassa yllä tietoa siitä, missä kentässä ollaan menossa. Tämän tiedon perusteella valitaan, mikä kenttä luodaan.

Kun kenttä vaihtuu, edellinen kenttä täytyy ensin tyhjentää. Tämän jälkeen voidaan luoda tilalle uusi kenttä. Kannattaa muistaa, että `ClearAll` tyhjentää myös ohjainasetukset, joten kannattaa miettiä missä näppäimet luodaan.

Tässä esimerkissä kuvitellaan, että [kentät luodaan tekstitiedostosta.](ruutukentta.md) Kentän luovalle aliohjelmalle viedään parametrina sen tekstitiedoston nimi, josta kenttä luodaan.

Esimerkkikoodi (Huom! Koodi on Nuorten pelikurssia varten, Ohjelmointi 1 kurssilaisten pitää osata korvat suurin osa if-lauseita järkevämmin):

```csharp,ignore
//Pelin alussa ollaan kentässä 1
int kenttaNro = 1;

public override void Begin()
{
    SeuraavaKentta();
}

void SeuraavaKentta()
{
    ClearAll();

    if (kenttaNro == 1) LuoKentta("kentta1");
    else if (kenttaNro == 2) LuoKentta("kentta2");
    else if (kenttaNro == 3) LuoKentta("kentta3");
    else if (kenttaNro > 3) Exit();

    // Parempi olisi:
    // if (kenttaNro > 3) Exit();
    // LuoKentta($"kentta{kenttaNro}");

    AsetaOhjaimet();
}

void LuoKentta(string kenttatiedostonNimi)
{
    TileMap ruudut = TileMap.FromLevelAsset(kenttatiedostonNimi);
    //tässä luodaan kenttä tekstitiedostosta
}

void TormasiMaaliin(PhysicsObject pelaaja, PhysicsObject maali)
{
    //Kasvatetaan kenttänumeroa yhdellä ja siirrytään seuraavaan kenttään:
    kenttaNro++;
    SeuraavaKentta();
}

void TormasiPiikkiin(PhysicsObject pelaaja, PhysicsObject piikki)
{
    //Sama kenttä ladataan alusta jos kenttänumeroa ei kasvateta:
    SeuraavaKentta();
}
```

**VAROITUS:** Yllä esitetyllä tavalla on valitettavan helppo saada peli solmuun. Tämä tapa toimii parhaiten niissä tilanteissa, joissa *aivan kaikki* (myös kontrollit) tuhotaan kentän päätteeksi, ja luodaan uudelleen seuraavassa kentässä. Koska tämä ei läheskään aina ole ihanteellinen tapa toimia, niin `ClearAll`-metodin käyttöä tulisikin oikeastaan välttää ja pyrkiä tuhoamaan vain ne oliot jotka oikeasti halutaan tuhota.

Jos kuitenkin haluat käyttää ClearAll-metodia, niin on huolehdittava pelaajan toiminnasta. Jos pelaaja-olio on attribuuttina (ts. sama pelaajaolion ilmentymä jatkaa kentästä toiseen), voit käyttää kentän luonnin yhteydessä sellaista pelaajan luontimetodia joka palauttaa pelaajaolion viitteen. Tästä tulee hieman ikävän näköinen koodi, alla esimerkki:

```csharp,ignore
void LuoKentta(string kenttaTiedosto)
{
  // ...
  kentta.SetTileMethod('P', (paikka, leveys, korkeus) => { pelaaja = LisaaPelaaja(paikka, leveys, korkeus); });
}

PlatformCharacter LisaaPelaaja(Vector paikka, double leveys, double korkeus)
{
  pelaaja = new PlatformCharacter(...);
  return pelaaja;
}
```

Tämän jälkeen kontrollit pitää myös asettaa uudestaan.
