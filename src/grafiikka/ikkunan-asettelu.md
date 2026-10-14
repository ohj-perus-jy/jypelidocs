# Peli-ikkuna ja resoluutio
Oletuksena ikkunan resoluutio on 1024x768. Ikkunan todelliseen kokoon vaikuttaa kuitenkin järjestelmässä mahdollisesti käytössä oleva skaalauskerroin. Läppäreillä se on lähestulkoon aina oletuksena käytössä.

Oletuksena peli näytetään ikkunassa. 

Peli-ikkunan saa koko ruudun kokoiseksi seuraavasti:

```csharp,ignore
IsMaximized = true;
```

Jos haluaa vaihtaa pelin käyttämään tiettyä resoluutiota, tulee se tehdä hieman eri tavalla:

```csharp,ignore
public override void Begin()
{
      SetWindowSize(1024, 768, false);
      // muu koodi ...
}
```

Parametrit ovat ensin leveys, korkeus ja viimeiseksi se, käytetäänkö
kokoruututilaa vai ei. Jos haluat, että peli näkyy tavallisena ikkunana, valitse
`false`. 

Myös reunaton kokoruututila on mahdollista asettaa:

```csharp,ignore
IsFullScreen = true;
```

Emme kuitenkaan suosittele kokoruututilaa, koska se aiheuttaa ongelmia debuggaamisessa. 

## Ikkunan sijainnin muuttaminen

Peli-ikkunan sijaintia on myös mahdollista muuttaa.

```csharp,ignore
SetWindowPosition(100, 100);
```

Tämä komento asettaa ikkunan vasemman yläkulman annettuihin ruutukoordinaatteihin. Ruutukoordinaatit lasketaan näytön vasemmasta yläkulmasta, eli edellä oleva kutsu asettaa ikkunan 100 oikealle ja 100 alaspäin näytön vasemmasta yläkulmasta.

Oleellista on myös huomata, että Y-akseli menee "väärään suuntaan".

Useamman näytön tapauksissa on mahdollista, että koordinaatit menevät myös negatiiviselle.

Päänäytön vasen yläkulma on koordinaateissa (0,0). Jos päänäytön vasemmalla puolella on toinen näyttö, ovat sen x-suuntaiset koordinaatit negatiivisella puolella.
