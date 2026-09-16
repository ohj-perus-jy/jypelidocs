# Olioiden törmäysten estäminen

Joskus on toivottavaa, että jokin fysiikkaolio ei törmäile. Törmäysten estämiseen on joitakin konsteja, riippuen tilanteesta. Huomaa, että jos olion ei tarvitse koskaan liikkua tai törmäillä mihinkään, voi olla järkevämpää käyttää `GameObject`-oliota.

Katso myös [AddCollisionHandler](../tapahtumat/tormaykset.md), eli kuinka jotain saadaan tapahtumaan kun kappaleet törmäävät.

## Jos olion ei pidä törmätä mihinkään

Yksittäisen olion törmäykset kaikkiin muihin olioihin on estettävissä. Huomaa kuitenkin, että tällöin olio menee myös lattiasta läpi! Törmäyksiä voidaan kuitenkin kuunnella (`AddCollisionHandler`-kutsulla) normaalisti. Koodissa menee näin:

```csharp,ignore
haamu.IgnoresCollisionResponse = true;
```

Törmäykset saa takaisin vastaavasti:

```csharp,ignore
haamu.IgnoresCollisionResponse = false;
```

## Tiettyjen olioiden törmäysten estäminen

Joskus halutaan, että esim. tietyt kolme oliota eivät voi törmätä toisiinsa. Tätä varten voimme käyttää fysiikkaolion ominaisuutta `CollisionIgnoreGroup`, joka määrittää olion törmäysryhmän. Oliot, joilla on sama törmäysryhmä, menevät toistensa läpi.

Esimerkiksi fysiikkaoliot `hahmo1`, `hahmo2` sekä `hahmo3` saadaan välttämään törmäykset toisiinsa seuraavasti:

```csharp,ignore
hahmo1.CollisionIgnoreGroup = 1;
hahmo2.CollisionIgnoreGroup = 1;
hahmo3.CollisionIgnoreGroup = 1;
```

Jos tämän lisäksi kentällä olisi `hahmo4` ja `hahmo5`, joiden törmäysryhmät olisivat molemmilla 2, törmäilisivät oliot seuraavasti:

|        | hahmo1    | hahmo2    | hahmo3    | hahmo4    | hahmo5    |
|--------|:----------|:----------|:----------|:----------|:----------|
| hahmo1 |           | ei törmää | ei törmää | törmää    | törmää    |
| hahmo2 | ei törmää |           | ei törmää | törmää    | törmää    |
| hahmo3 | ei törmää | ei törmää |           | törmää    | törmää    |
| hahmo4 | törmää    | törmää    | törmää    |           | ei törmää |
| hahmo5 | törmää    | törmää    | törmää    | ei törmää |           |

Oletuksena `CollisionIgnoreGroup` on nolla. "Nollaryhmässä" olevat oliot törmäilevät toisiinsa siitäkin huolimatta, että niiden törmäysryhmä on sama. Jos haluttaisiin saada esimerkiksi `hahmo2` törmäämään taas muihin, tehdään seuraavasti:

```csharp,ignore
hahmo2.CollisionIgnoreGroup = 0;
```

## Oman monimutkaisemman törmäyksenvälttelylogiikan luominen

Joskus voi tulla tilanteita, että perinteiset törmäysryhmät eivät riitä. Jos meillä on esimerkiksi kolme kappaletta, `A`, `B` ja `C` ja haluaisimme että `A` ja `C` sekä `B` ja `C` voivat törmätä, mutta `A` ja `B` eivät, täytyy meidän luoda oma törmäyksenvälttelyfunktio.

```csharp,ignore
a.Tag = "a";
b.Tag = "b";

a.CollisionIgnoreFunc = Tormaako;
b.CollisionIgnoreFunc = Tormaako;

// muuta koodia

private bool Tormaako(IPhysicsObject eka, IPhysicsObject toka)
{
    if(eka.Tag == "a" && toka.Tag == "b")
        return false;
    return true;
}
```

`Tormaako`-aliohjelma ottaa parametrina törmäävät kappaleet (Huom: tyyppinä `IPhysicsObject`) ja palauttaa true jos kappaleiden pitää törmätä, false jos ei eli ne menevät toistensa läpi.

Huomaa että edellä olevassa esimerkissä ei tarvinnut ottaa kappaletta `C` mitenkään huomioon. Tämä siksi, koska senhän tulee törmätä kaikkien kanssa, se siis on tässä yhteydessä aivan "normaali" kappale. Erityiskäsittelyä tarvittiin vain kappaleiden `A` ja `B` kohdalla.

### HUOM!

Tätä funktiota voi olla houkuttelevaa käyttää myös yleiseen törmäyksen käsittelyyn, aivan kuten [AddCollisionHandlerin](../tapahtumat/tormaykset.md) kautta laitettua funktiota. Niin ei kuitenkaan tule tehdä! Tähän `CollisionIgnoreFunc`iin annetun aliohjelman tulee vain ja ainoastaan vastata kysymykseen "Pitääkö näiden kappaleiden törmätä?", eikä tehdä mitään muuta.

Jos lisäät sinne muuta toiminnallisuutta joka jotenkin vaikuttaa fysiikkaan, kuten vaikka tuhoat kappaleen, pelisi kaatuu!
