# Miten pelikentän voi aloittaa alusta?

(Jos haluat tehdä peliisi useita erilaisia kenttiä, [tsekkaa tämä ohje](../kentat/kentan-vaihtuminen.md).)

Kenttää (Level) ei oikeastaan tarvi ohjelmakoodissa luoda uudestaan, vaikka pelissä kenttä näyttäisi vaihtuvan tai alkavan alusta. Vanha kenttä on helppo tyhjentää ja alustaa taas uudestaan.

Esimerkki kentän luomisesta:

```csharp,ignore
protected override void Begin()
{
    LuoKentta();
}

void LuoKentta()
{
    PhysicsObject kissa = new PhysicsObject(40, 20, Shape.Rectangle);
    Add(kissa);
}
```

Kenttä on siis jo olemassa kun ohjelman suoritus alkaa `Begin`-aliohjelmasta. Aliohjelmassa `LuoKentta` vain lisätään olemassa olevaan kenttään kissa-niminen `PhysicsObject`-luokan olio.

Jos kentän luomisen toteuttaa tällä tavalla, nyt on helppo vaikka aloittaa kenttä aina alusta jos pelaaja epäonnistuu, siihen on kätevä `ClearAll`-aliohjelma:

```csharp,ignore
PhysicsObject kissa;
PhysicsObject vasenReuna;
PhysicsObject oikeaReuna;

protected override void Begin()
{
    LuoKentta();
    AsetaOhjaimet();
}

void LuoKentta()
{
    vasenReuna = Level.CreateLeftBorder();
    oikeaReuna = Level.CreateRightBorder();
    Level.CreateBottomBorder();
    Level.CreateTopBorder();

    kissa = new PhysicsObject(10, Shape.CreateRectangle(40, 20));
    AddCollisionHandler(kissa, KissaTormasi);
    Add(kissa);
}

void AsetaOhjaimet()
{
    //tässä asetettaisiin napit ja kissan ohjaaminen jos tämä olisi oikea peli
}

void KissaTormasi(PhysicsObject kissa, PhysicsObject kohde)
{
    if ((kohde == vasenreuna) || (kohde == oikeaReuna))
    {
         AloitaAlusta();
    }
}

void AloitaAlusta()
{
    ClearAll();
    LuoKentta();
    AsetaOhjaimet();
}
```

Esimerkissä kissan liikuttamista ei ole toteutettu, mutta pääasia onkin huomata, mitä tapahtuu kun kissa *törmää*. Tutkitaan siis kissan törmäyksenkäsittelijää, aliohjelmaa `KissaTormasi`.

If-lauseen mukaan jos kissan törmäyksen kohde on kentän vasen tai oikea reuna, kutsutaan `AloitaAlusta`-nimistä aliohjelmaa (kaksi tolppamerkkiä `||` voidaan lukea "tai", vastaavasti kuin `&&`-merkintä tarkoittaa "ja").

`AloitaAlusta` kutsuu ensin `ClearAll`-nimistä (suom. tyhjennä kaikki) aliohjelmaa. Se pyyhkii kentän tyhjäksi kaikista sinne luoduista olioista ja sille tehdyistä asetuksista. Tyhjentämisen jälkeen tilanne on kuin olisimme juuri käynnistäneet pelin, ja asetukset täytyy tehdä uudelleen. Voidaankin kutsua jälleen `LuoKentta`-aliohjelmaamme, joka tekee kentälle halutut asetukset ja oliot. Myös ohjaimet täytyy asettaa uudestaan - `ClearAll` tyhjentää nimensä mukaan kaikki asetukset.
