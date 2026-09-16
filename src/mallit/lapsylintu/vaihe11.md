# Läpsylintu, vaihe 11: Pelin jatkokehittely

Tällä sivulla on lueteltu ideoita Läpsylintu-pelin jatkokehittelyä varten. Näitä ideoita varten joudut itse soveltamaan [Jypeli-kirjaston käyttöohjeita](../../index.md).

## Kenttään erilaisia esteitä

Lisää kenttään eri näköisiä kiinteitä esteitä.

Vinkki: Tee yksi LisaaEste-niminen aliohjelma, jonka esittelyrivi on:

```csharp,ignore
void LisaaEste(Vector paikka, double leveys, double korkeus, Image kuva)
```

Kutsu tätä yhtä aliohjelmaa jokaisesta eri tyyppisen esteen lisäävästä aliohjelmasta.

## Kentän aloittaminen alusta

Nykyinen kenttä pitäisi pystyä aloittamaan mahdollisimman helposti alusta. Lisää esimerkiksi näppäin `R` (niin kuin "Restart") tai `U` (kuten "Uudelleen") aloittamaan pelin nykyinen kenttä alusta!

## Enemmän kenttiä

Tee peliin myös toinen kenttä `kentta2.txt`. Lisää kentän vaihtuminen, kun oikeaan reunaan kosketetaan (eli kun kenttä päästään läpi). Kenttiä on helppo luoda, jos täyttää kentän tyhjällä esimerkiksi pisteillä. Tämän jälkeen voit painaa näppäimistöltä `insert`-näppäintä. Tämän jälkeen voit kirjoittaa pisteiden yli minkä tahansa kirjaimen.

## Pistelaskuri

Lisää peliin pistelaskuri, joka laskee kerättyjä tähtiä.

### Tarkistuskohta, jotka ohittaessa saa pisteitä

Lisää mahdollisuus lisätä kenttätiedostoon koko pystyrivin mittainen tarkistuskohta, eräänlainen "checkbox"-olio, jonka keräämällä pelaaja saa lisäpisteitä.

## Tietyn ajan kestävä kuolemattomuus

Tee superesine, jonka keräämällä pelaaja on esimerkiksi 5 sekunnin ajan kuolematon.
