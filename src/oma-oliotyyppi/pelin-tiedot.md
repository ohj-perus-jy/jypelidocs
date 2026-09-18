# Pelin tiedot olion sisällä

`Peli`-luokassa voi kirjoittaa suoraan `Level.Bottom`, `Add(olio)` tai
`pisteet.Value++`, koska koodi on `Peli`-luokan sisällä. Oma oliotyyppi on
eri luokka, joten siellä nämä nimet eivät toimi sellaisenaan. Ratkaisu
riippuu siitä, onko tarvittava asia Jypelin valmis vai itse kirjoitettu.

Tarvitset ensin: [Oman luokan periminen](luokan-periminen.md). Sivun
esimerkki käyttää [omaa päivitysmetodia](paivitys.md).

## Jypelin valmiit asiat: Game

Jypelin valmiit asiat saa käyttöön kirjoittamalla eteen `Game.`. Jokaisella
pelioliolla on `Game`-ominaisuus, joka viittaa käynnissä olevaan peliin.

| `Peli`-luokassa | Omassa luokassa |
| --- | --- |
| `Level.Bottom` | `Game.Level.Bottom` |
| `Add(olio)` | `Game.Add(olio)` |
| `Keyboard.Listen(...)` | `Game.Keyboard.Listen(...)` |
| `MessageDisplay.Add("...")` | `Game.MessageDisplay.Add("...")` |
| `LoadImage("kuva")` | `Game.LoadImage("kuva")` |
| `Gravity` | `PhysicsGame.Instance.Gravity` |
| `AddCollisionHandler(...)` | `PhysicsGame.Instance.AddCollisionHandler(...)` |

Ilman `Game`-sanaa kääntäjä antaa virheen
`An object reference is required for the non-static field, method, or property 'Level.Bottom'`
tai `The name 'LoadImage' does not exist in the current context`.

Poikkeus on `Add`: omassa luokassa pelkkä `Add(olio)` kääntyy, mutta tekee
eri asian. Se lisää olion tämän olion
[lapsiolioksi](../oliot/luonti.md#olion-lisaaminen-toisen-lapsiolioksi), joka
liikkuu sen mukana. Kun luoti, räjähdys tai muu itsenäinen olio lisätään
peliin luokan sisältä, kirjoitetaan `Game.Add(olio)`.

Painovoima ja törmäyskäsittelijät ovat vain fysiikkapeleissä, joten
`Game`-sana ei tunne niitä: `Game.Gravity` antaa virheen
`'Game' does not contain a definition for 'Gravity'`. Niiden eteen
kirjoitetaan `PhysicsGame.Instance`, joka tarkoittaa käynnissä olevaa
fysiikkapeliä.

Vastaavasti `Game.Instance` tarkoittaa samaa peliä kuin olion
`Game`-ominaisuus. Oliotyypin sisällä riittää lyhyempi `Game`, mutta
luokassa, joka ei ole peliolio (esimerkiksi oma apuluokka),
`Game`-ominaisuutta ei ole, ja silloin kirjoitetaan
`Game.Instance.Add(olio)`.

`Game` on käytössä jo rakentajassa. Olion paikkaa ei silloin kuitenkaan ole
vielä asetettu, joten paikasta riippuvat asiat, kuten osien lisääminen
olion viereen, tehdään vasta
[`AddedToGame`-tapahtumassa](tapahtumat.md#addedtogame).

## Peli-luokkaan itse kirjoitetut asiat

`Peli`-luokkaan itse kirjoitetut asiat, kuten pistelaskuri `pisteet` tai
aliohjelma `PeliLoppui`, eivät löydy samalla tavalla. Rivi
`Game.pisteet.Value++` antaa käännösvirheen:

```text
error CS1061: 'Game' does not contain a definition for 'pisteet'
```

`Game`-ominaisuus lupaa vain, että kyseessä on jokin Jypeli-peli. Kääntäjä
ei tiedä, että peli on juuri sinun `Peli`-luokkasi, joten se hyväksyy vain
ne asiat, jotka ovat jokaisessa Jypeli-pelissä.

Itse kirjoitettuihin asioihin pääsee käsiksi kolmella tavalla. Kaksi
ensimmäistä sopivat useimpiin tilanteisiin.

## 1. Anna tarvittava olio rakentajassa

Laskuri, pelaaja tai muu olio, jota luokka tarvitsee, viedään sille
rakentajan parametrina ja tallennetaan attribuuttiin. Näin sai kohteensa
myös [ohjus](paivitys.md#esimerkki-ohjus-seuraa-pelaajaa). Alla pallot
vähentävät pelin elämälaskuria, kun ne putoavat kentän alareunan
alapuolelle.

```csharp,ignore
//-using System;
//-using Jypeli;
//-
class Putoaja : PhysicsObject
{
    private IntMeter elamat;

    public Putoaja(IntMeter elamat)
        : base(40, 40)
    {
        this.elamat = elamat;
        Shape = Shape.Circle;
        Color = Color.Red;
        IsUpdated = true;
    }

    public override void Update(Time time)
    {
        if (IsDestroyed)
        {
            return;                           // tuhottu, älä vähennä toista kertaa
        }
        if (Y < Game.Level.Bottom - Height)   // Jypelin oma: Game-sanan kautta
        {
            elamat.Value--;                   // pelin oma: saatu rakentajassa
            Destroy();
        }
        base.Update(time);
    }
}

public class Peli : PhysicsGame
{
    IntMeter elamat = new IntMeter(3, 0, 3);

    public override void Begin()
    {
        Gravity = new Vector(0, -800);

        Label naytto = new Label();
        naytto.Title = "Elämät: ";
        naytto.BindTo(elamat);
        naytto.Y = Screen.Top - 50;
        Add(naytto);

        elamat.LowerLimit += delegate { MessageDisplay.Add("Peli loppui"); };

        for (int i = 0; i < 3; i++)
        {
            Putoaja putoaja = new Putoaja(elamat);
            putoaja.Position = new Vector(-100 + i * 100, i * 200);
            Add(putoaja);
        }
    }
}
```

Pelissä ja jokaisessa pallossa on sama laskuriolio, joten pallon tekemä
muutos näkyy pelissä heti. Elämien loppumiseen peli reagoi laskurin omalla
`LowerLimit`-tapahtumalla (ks. [Laskurit](../kayttoliittyma/pistelaskuri.md)),
eikä pallon tarvitse tietää, mitä silloin tapahtuu. Tarkistus
`if (IsDestroyed)` tarvitaan, koska tuhotun olion `Update` ajetaan vielä
kerran (ks. [Milloin Updatea kutsutaan](paivitys.md#milloin-updatea-kutsutaan)); ilman
sitä jokainen pallo veisi kaksi elämää.

## 2. Ilmoita pelille tapahtumalla

Kun olion pitää saada peli tekemään jotain, esimerkiksi lisäämään pisteitä,
vaihtamaan kenttää tai aloittamaan alusta, olio laukaisee oman tapahtuman ja
`Peli`-luokka liittää siihen aliohjelmansa. Olio ei tiedä pelistä mitään,
joten samaa luokkaa voi käyttää monessa pelissä.

Tapahtuman kirjoittaminen ja kokonainen esimerkki ovat sivulla
[Tapahtumat omassa luokassa](tapahtumat.md#omat-tapahtumat): vihu laukaisee
`Kuoli`-tapahtuman, ja peli lisää pisteet. `Update`-metodissa tapahtuma
laukaistaan samalla tavalla, yllä olevassa esimerkissä rivin
`elamat.Value--` tilalla.

## 3. Tyyppimuunnos Peli-tyypiksi

Tyyppimuunnos `(Peli)Game` kertoo kääntäjälle, että käynnissä oleva peli on
nimenomaan `Peli`. Silloin `Peli`-luokan julkiset (`public`) attribuutit ja
aliohjelmat näkyvät. Käytä oman peliluokkasi nimeä.

```csharp,ignore
// Peli-luokassa
public IntMeter Pisteet = new IntMeter(0);

// Oman olion luokassa
Peli peli = (Peli)Game;
peli.Pisteet.Value += 10;
```

Tapa toimii, mutta se sitoo luokan yhteen peliin, eikä luokkaa voi käyttää
sellaisenaan toisessa projektissa. Lisäksi `Peli`-luokan sisältöä on
avattava julkiseksi. Käytä sitä vasta, kun kaksi ensimmäistä tapaa eivät
sovi.

## Katso myös

- [Omat ominaisuudet ja metodit](ominaisuudet.md): rakentajan parametrit ja laskuri ominaisuutena.
- [Oma päivitysmetodi](paivitys.md): `Update`, jota esimerkki käyttää.
- [Tapahtumat omassa luokassa](tapahtumat.md): `AddedToGame` ja omat tapahtumat.
- [Laskurit](../kayttoliittyma/pistelaskuri.md): `IntMeter` ja `LowerLimit`.
