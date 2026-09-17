# Muita tapahtumia

Jypelissä moni asia laukaisee *tapahtuman* (event), johon voi liittää oman
aliohjelman `+=`-merkinnällä. Ajastimen `Timeout`-tapahtuma ja törmäykset on
käsitelty omilla sivuillaan: [Ajastimet](ajastimet.md) ja
[Törmäysten käsittely](tormaykset.md). Tällä sivulla on lueteltu eräitä
muita tapahtumia. Lista ei ole täydellinen: Jypelissä on tapahtumia myös
esimerkiksi aseilla, aivoilla, äänillä ja listoilla.

Käsittelijäksi annetaan aliohjelman nimi ilman sulkuja. Aliohjelman
parametrien pitää vastata tapahtuman muotoa. Useimmat tämän sivun tapahtumat
kutsuvat parametritonta `void`-aliohjelmaa; poikkeukset on mainittu erikseen.
Jos käsittelijälle pitää viedä omia parametreja, katso
[Delegaatit](delegaatit.md).

## Olion tuhoutuminen: Destroyed

Kun olio tuhotaan `Destroy`-metodilla, kutsutaan sen `Destroyed`-tapahtuman
käsittelijää. Tapahtuma on kaikilla peliolioilla, myös käyttöliittymän
komponenteilla kuten `Label`. Alla olevassa esimerkissä vihu lakkaa
heittelemästä esineitä, kun se tuhoutuu.

```csharp,ignore
{
  PhysicsObject vihu = new PhysicsObject(...);
  // ...
  Timer heittoajastin = new Timer();
  heittoajastin.Interval = 2.0;
  heittoajastin.Timeout += HeitaKappale;
  vihu.Destroyed += heittoajastin.Stop;
}
```

`Destroyed`-tapahtuman käsittelijän tulee olla parametriton `void`-aliohjelma.
Jos tuhoutumisen yhteydessä on tarvetta tehdä monimutkaisempaa logiikkaa
(esimerkiksi kutsua parametrillista aliohjelmaa), kannattaa käyttää
delegate-avainsanaa.

```csharp,ignore
vihu.Destroyed += delegate { MessageDisplay.Add("Vihu tuhoutui!"); };
```

Tapahtuma laukeaa myös silloin, kun olio tuhoutuu itsestään eliniän
päätyttyä, ks. [Elinikä](../oliot/elinika.md).

## Olion lisääminen peliin: AddedToGame

`AddedToGame` laukeaa, kun olio on lisätty peliin `Add`-aliohjelmalla. Sitä
tarvitaan lähinnä [omissa oliotyypeissä](../oma-oliotyyppi/tapahtumat.md): olion
rakentajassa olio ei ole vielä pelissä, joten esimerkiksi ohjainten
asettaminen tai muiden olioiden lisääminen peliin onnistuu vasta tässä
tapahtumassa. Alla vihu lisää itselleen kilven, kun se on lisätty peliin.

```csharp,ignore
public class Vihu : PhysicsObject
{
    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        AddedToGame += LisaaKilpi;
    }

    void LisaaKilpi()
    {
        PhysicsObject kilpi = new PhysicsObject(Width, 10);
        kilpi.Position = Position + new Vector(0, Height / 2);
        Game.Instance.Add(kilpi);
    }
}
```

Laajempia esimerkkejä: auton pyörät sivulla [Liitokset](../fysiikka/liitokset.md)
ja ohjainten asettaminen sivulla
[Omat käyttöliittymäkomponentit](../kayttoliittyma/omat-kayttoliittymakomponentit.md).

Vastaavasti `Removed` laukeaa, kun olio poistetaan pelistä. Myös `Destroy`
poistaa olion, joten oliota tuhottaessa laukeavat sekä `Destroyed` että `Removed`.

## Laskurin arvon muuttuminen: Changed

Laskurin (`IntMeter`, `DoubleMeter`) `Changed`-tapahtuma laukeaa aina, kun
laskurin arvo muuttuu. Käsittelijä saa parametreina vanhan ja uuden arvon,
`IntMeter`-laskurilla `int`-tyyppisinä ja `DoubleMeter`-laskurilla
`double`-tyyppisinä.

```csharp,ignore
IntMeter pisteet = new IntMeter(0);
pisteet.Changed += PisteetMuuttuivat;
```

```csharp,ignore
void PisteetMuuttuivat(int vanhaArvo, int uusiArvo)
{
    if (uusiArvo > vanhaArvo)
    {
        MessageDisplay.Add("Piste!");
    }
}
```

Ylä- ja alarajan saavuttamiselle on omat tapahtumat `UpperLimit` ja
`LowerLimit`, ja mille tahansa arvolle voi asettaa tapahtuman
`AddTrigger`-metodilla. Ne on kuvattu sivulla
[Pistelaskuri](../kayttoliittyma/pistelaskuri.md#laskurin-yla-ja-alarajat-seka-tapahtumat-niille).
Liukusäätimeen sidotun laskurin `Changed`-tapahtumaa käytetään sivulla
[Liukusäätimet](../kayttoliittyma/liukusaatimet.md).

## Napin painallus: Clicked

`PushButton` on painike, jonka `Clicked`-tapahtuma laukeaa, kun nappia
klikataan hiirellä. Napin paikan voi asettaa kuten muidenkin olioiden.

```csharp,ignore
PushButton aloitusnappi = new PushButton("Aloita peli");
aloitusnappi.Y = 100;
aloitusnappi.Clicked += AloitaPeli;
Add(aloitusnappi);
```

Kokonainen alkuvalikko syntyy helpommin valmiilla luokalla, ks.
[Valikot](../kayttoliittyma/valikko.md).

## Ikkunan sulkeutuminen: Closed

Kaikilla ikkunoilla (`MessageWindow`, `InputWindow`, `MultiSelectWindow`,
`YesNoWindow`, `HighScoreWindow`) on `Closed`-tapahtuma, joka laukeaa, kun
ikkuna sulkeutuu. Käsittelijä saa parametrina suljetun ikkunan. Alla
`MessageWindow`, joka on yksinkertainen ilmoitusikkuna tekstillä ja
OK-napilla, aloittaa pelin alusta sulkeuduttuaan.

```csharp,ignore
MessageWindow ilmoitus = new MessageWindow("Peli päättyi!");
ilmoitus.Closed += AloitaAlusta;
Add(ilmoitus);
```

```csharp,ignore
void AloitaAlusta(Window ikkuna)
{
    ClearAll();
    Begin();
}
```

Kyllä/ei-ikkunalla on lisäksi tapahtumat `Yes` ja `No`, joiden käsittelijät
ovat parametrittomia. Alla peli suljetaan, jos pelaaja vastaa kyllä.

```csharp,ignore
YesNoWindow kysymys = new YesNoWindow("Lopetetaanko peli?");
kysymys.Yes += Exit;
Add(kysymys);
```

Kysymysikkunan `TextEntered`-tapahtuma on sivulla
[Tekstin kysyminen pelaajalta](../kayttoliittyma/tekstin-kysyminen.md) ja
parhaiden pisteiden ikkunan `Closed`-tapahtuman käyttö sivulla
[Parhaat pisteet](../kayttoliittyma/parhaiden-pisteiden-lista.md).
Pelin aloittamisesta alusta kerrotaan sivulla
[Pelin aloittaminen alusta](../kentat/aloittaminen-alusta.md).

## Animaation loppuminen: Played

Kun animaatio on toistettu annetun määrän kertoja, laukeaa sen
`Played`-tapahtuma. Esimerkiksi räjähdysanimaation jälkeen olio voidaan
tuhota.

```csharp,ignore
vihu.Animation = new Animation(rajahdysKuvat);
vihu.Animation.Played += vihu.Destroy;
vihu.Animation.Start(1);
```

Animaation luominen ja `Start`-metodi on kuvattu sivulla
[Animaatio](../oliot/animaatio.md#animaation-asettaminen-oliolle).

## Pelin sulkeminen: Exiting

Pelin `Exiting`-tapahtuma laukeaa, kun peli suljetaan. Siihen voi liittää
esimerkiksi pisteiden tallennuksen, jolloin tallennus tapahtuu riippumatta
siitä, miten peli lopetettiin.

```csharp,ignore
public override void Begin()
{
    Exiting += TallennaPisteet;
    // ...
}
```

```csharp,ignore
void TallennaPisteet()
{
    DataStorage.Save<ScoreList>(topLista, "pisteet.xml");
}
```

## Käsittelijän poistaminen

Käsittelijän voi poistaa `-=`-merkinnällä, jolloin tapahtuma ei enää kutsu
sitä.

```csharp,ignore
vihu.Destroyed -= heittoajastin.Stop;
```

Delegaattina (`delegate { ... }`) annettua käsittelijää ei voi poistaa, koska
sillä ei ole nimeä. Jos käsittelijä pitää voida poistaa, tee siitä nimetty
aliohjelma.

## Esimerkki: pallo tuhoutuu klikkaamalla {#esimerkki}

Peli näyttää pallon, joka tuhoutuu hiirellä klikkaamalla. Tuhoutuminen
laukaisee `Destroyed`-tapahtuman, jonka käsittelijä avaa ilmoitusikkunan.
Ikkunan sulkeminen laukaisee `Closed`-tapahtuman, jonka käsittelijä aloittaa
pelin alusta. Ajonappi näyttää vain pelin alkutilanteen, joten klikkausta
kannattaa kokeilla omalla koneella.

```csharp,feature-jypeli
using Jypeli;

public class Peli : PhysicsGame
{
    public override void Begin()
    {
        Mouse.IsCursorVisible = true;

        PhysicsObject pallo = new PhysicsObject(100, 100, Shape.Circle);
        pallo.Color = Color.Red;
        pallo.Destroyed += PalloTuhoutui;
        Add(pallo);

        Mouse.ListenOn(pallo, MouseButton.Left, ButtonState.Pressed, pallo.Destroy, "Tuhoa pallo");
        MessageDisplay.Add("Klikkaa palloa.");
    }

    void PalloTuhoutui()
    {
        MessageWindow ikkuna = new MessageWindow("Pallo tuhoutui. Sulje ikkuna, niin peli alkaa alusta.");
        ikkuna.Closed += AloitaAlusta;
        Add(ikkuna);
    }

    void AloitaAlusta(Window ikkuna)
    {
        ClearAll();
        Begin();
    }
}
```

`Mouse.ListenOn` kuuntelee hiiren painallusta vain pallon päällä, ks.
[Hiiren kuunteleminen vain tietyille peliolioille](../ohjaimet/ohjainten-lisays.md#hiiren-kuunteleminen-vain-tietyille-peliolioille).
