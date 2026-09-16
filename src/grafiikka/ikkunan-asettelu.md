# Miten saan pelin koko ruutuun tai vaihdan pelin resoluutiota?
Oletuksena ikkunan resoluutio on 1024x768. Ikkunan todelliseen kokoon vaikuttaa kuitenkin järjestelmässä mahdollisesti käytössä oleva skaalauskerroin. Läppäreillä se on lähestulkoon aina oletuksena käytössä.

Oletuksena peli näytetään ikkunassa. Tämä sen takia, että debuggaus tuottaa ongelmia, jos peli näytetään koko ruudulla.

Resoluutio / kokoruututila kannattaa asettaa heti ensimmäisenä `Begin`-aliohjelmassa.

Pelin saa näkymään koko ruudulla (fullscreen) seuraavasti:

```csharp,ignore
public override void Begin()
{
      IsFullScreen = true;
      // muu koodi...
}
```

Jos haluaa vaihtaa pelin käyttämään tiettyä resoluutiota, tulee se tehdä hieman eri tavalla:

```csharp,ignore
public override void Begin()
{
      SetWindowSize(1024, 768, false);
      // muu koodi ...
}
```

Resoluutiota muutetaan `SetWindowSize`-kutsulla. Parametreiksi ensin leveys, sitten korkeus, ja viimeiseksi `true` tai `false` kokoruututilan tai ikkunan merkiksi (eli int leveys, int korkeus, bool kokoruutu).

## Ikkunan sijainnin muuttaminen

Peli-ikkunan sijaintia on myös mahdollista muuttaa.

```csharp,ignore
SetWindowPosition(100, 100);
```

Tämä komento asettaa ikkunan vasemman yläkulman annettuihin ruutukoordinaatteihin. Ruutukoordinaatit lasketaan näytön vasemmasta yläkulmasta, eli edellä oleva kutsu asettaa ikkunan näytön vasempaan yläkulmaan.

Oleellista on myös huomata, että Y-akseli menee "väärään suuntaan".

Useamman näytön tapauksissa on mahdollista että koordinaatit menevät myös negatiiviselle.

Windowsilla päänäytön vasen yläkulma on koordinaateissa (0,0). Jos päänäytön vasemmalla puolella on toinen näyttö, on sen x-suuntaiset koordinaatit negatiivisella puolella.
