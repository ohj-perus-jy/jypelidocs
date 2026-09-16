# Mitä muita fysiikan ilmiöitä voin hyödyntää?

## Kimmoisuus

Oliosta saa kimmoisamman, jolloin se pomppii herkemmin tai vähemmän herkemmin.

```csharp,ignore
pallo.Restitution = 1.0;
```

Olion kimmoisuuden arvo on välillä `0.0 - 1.0`. Arvolla `1.0` olio säilyttää kaiken vauhtinsa törmäyksessä. Mitä pienempi arvo, sitä enemmän olion vauhti hidastuu törmäyksessä. Jos arvo on `0`, niin olio ei kimpoa ollenkaan.

Törmäyksessä lasketaan tärmänneiden kappaleiden kimmoisuuksien keskiarvo, eli esimerkiksi jos toisen kimmoisuus on `0` ja toisen `1`, on lopputulos sama kuin jos molempien kimmoisuus olisi ollut `0.5`.

## Massa

Kaikilla fysiikkakappaleilla on massa, joka riippuu kappaleen koosta.

Oletuksena kappaleiden massa on sama kuin kappaleen pinta-ala, eli esimerkiksi

```csharp,ignore
PhysicsObject palikka = new PhysicsObject(50, 50);
```

muodostaisi neliönmuotoisen kappaleen, jonka massa olisi `2500`.

Voit muttaa kappaleen massaa sen `Mass`-kentän kautta, esimerkiksi:

```csharp,ignore
palikka.Mass = 100;
```

On oleellista pitää mielessä että massa vaikuttaa kaikkeen fysiikkaan.

Jos keilapallo ja koripallo törmäävät, kuinka paljon tämä törmäys muuttaa keilapallon liikettä? Entä jos kaksi keilapalloa törmäävät?

Jos haluat kohdistaa kappaleisiin voiman, tarvittavan voiman suuruus riippuu massasta. Suurempi massa -\> tarvitaan suurempi voima jotta saadaan sama efekti kuin kevyemmälle kappaleelle.

## Voimien kohdistaminen kappaleisiin

Jypelissä on kaksi päätapaa, kuinka kappaleisiin voi kohdistaa voimia; `Hit` ja `Push`.

### Hit

`Hit` kohdistaa kappaleeseen impulssin ([Wikipedia](https://fi.wikipedia.org/wiki/Impulssi)).

Metodille annetaan parametriksi vektori, joka kuvaa impulssin suuntaa ja voimakkuutta.

Esimerkiksi:

```csharp,ignore
Vector nopeus = new Vector(100, 100);
pallo.Hit(pallo.Mass * nopeus);
```

saisi kappaleen liikkumaan yläviistoon tällä annetulla nopeudella.

Kappaleen nopeus impulssin jälkeen riippuu siis sen massasta, sekä impulssin suuruudesta.

Tässä nyt kerrottiin nopeus pallon massalla, jotta pallo saadaan liikkumaan juuri tuolla nopeudella riippumatta sen massasta.

### Push

`Push` kohdistaa kappaleeseen voiman ([Wikipedia](https://fi.wikipedia.org/wiki/Voima_(fysiikka)))

Se siis käyttäytyy melkein samalla tavalla kuin `Hit`, mutta sille annettavan vektorin suuruus on eri.

`Push` kohdistaa voiman kappaleeseen yhden pelinpäivityksen ajan (1/60s).

Esimerkiksi:

```csharp,ignore
Vector nopeus = new Vector(100, 100);
pallo.push(pallo.Mass * nopeus);
```

ei saisi kappaletta kulkemaan samalla nopeudella kuin `Hit`, vaan ainoastaan 1/60 osa siitä.

`Push`ia on suositeltavaa käyttää esimerkiksi jos halutaan sulavampi hahmon liikuttelu ylhäältäpäin kuvattuun peliin.

esimerkiksi:

```csharp,ignore
Keyboard.ListenArrows(ButtonState.Down, LiikutaPelaajaa, "Ohjaa pelaajaa");

// muuta koodia...

private void LiikutaPelaajaa(Vector suunta)
{
    double kerroin = 50; // Tämä voi olla myös esimerkiksi attribuuteissa
    pelaaja.Push(pelaaja.Mass * suunta * kerroin);
}
```

Katso myös alempaa `LinearDamping` pelaajan hidastamiseen kun näppäimestä päästetään irti.

Katso myös ohjesivu [ohjainten asettelusta](../ohjaimet/ohjainten-lisays.md).

## Painovoiman, törmäysten ja muiden fyysisten ominaisuuksien kytkeminen pois

Oliosta, joka ei noudata painovoimaa saadaan helposti esim. leijuva haamu tai taso:

```csharp,ignore
haamu.IgnoresGravity = true;
```

Tällä koodilla olio ei noudata ollenkaan fysiikan lakeja:

```csharp,ignore
haamu.IgnoresPhysicsLogics = true;
```

Jos halutaan, että olio ei törmäile eli sen läpi voi muut oliot mennä vapaasti:

```csharp,ignore
haamu.IgnoresCollisionResponse = true;
```

Huom! Vaikka `IgnoresCollisionResponse` asetetaan trueksi, törmäyksestä <u>tulee edelleen tapahtuma,</u> vaikka itse törmäystä ei tapahdukaan.

Jos halutaan, että olio ei törmää vain johonkin tiettyihin olioihin, voidaan sille lisätä `CollisionIgnoreGroup`.

Ne oliot, joilla on sama `CollisionIgnoreGroup` eivät törmää keskenään ja <u>törmäyksestä ei tule tapahtumaa</u>.

```csharp,ignore
haamu.CollisionIgnoreGroup = 1;
vampyyri.CollisionIgnoreGroup = 1;
```

Näin puolestaan olioon ei vaikuta räjähdysten paineaallot:

```csharp,ignore
haamu.IgnoresExplosions = true;
```

Oliosta voidaan tehtä läpimentävä vain yhdestä suunnasta, esimerkiksi

```csharp,ignore
este.MakeOneWay(Vector.UnitX);
```

tekee esteestä läpimentävän, jos törmääjä liikkuu vasemmalta oikealle. Jos sallittua kulkusuuntaa ei anneta, eli pelkästään

```csharp,ignore
taso.MakeOneWay();
```

on kappale läpikuljettava alhaalta ylöspäin.

## Olion liikkeen tai pyörimisliikkeen hidastaminen

Oliolla on ominaisuus, joka hidastaa sen vauhtia, vaikka se ei osuisi mihinkään. Vähän kuin väliaineen (esim. ilman tai veden) vastus. Vauhtia ja pyörimisvauhtia voi hidastaa erikseen.

Vauhdin hidastaminen tapahtuu LinearDamping-ominaisuudella:

```csharp,ignore
pallo.LinearDamping = 0.9;
```

Pyörimisen hidastaminen tapahtuu AngularDamping-ominaisuudella:

```csharp,ignore
pallo.AngularDamping = 0.95;
```

Oletusarvo molemmille on 1.0, jolloin hidastumista ei ole. Mitä pienempi arvo, sitä enemmän kappale hidastuu. Yleensä kannattaa käyttää arvoja, jotka ovat lähellä ykköstä, esimerkiksi 0.95.

## Pyöriminen päälle ja pois

Fysiikkaoliot voivat pyöriä akselinsa ympäri. Pyörimisnopeuden voi asettaa olion AngularVelocity -ominaisuudesta [ohjeen mukaisesti.](https://trac.cc.jyu.fi/projects/npo/wiki/OlioidenLiikuttaminen#a6.Py%C3%B6ritt%C3%A4minen)

Joskus ei haluta että fysiikkaolio lähtee pyörimään törmäyksistä. Tämän voi estää seuraavalla tavalla:

```csharp,ignore
pelaaja.CanRotate = false;
```

Vastaavasti pyörimisen voi taas mahdollistaa asettamalla CanRotaten arvoksi true:

```csharp,ignore
pelaaja.CanRotate = true;
```
