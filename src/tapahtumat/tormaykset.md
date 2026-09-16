# Törmäysten käsittely

Kun kaksi fysiikkaoliota törmää toisiinsa, syntyy *törmäystapahtuma*. Näitä tapahtumia voidaan tarkkailla *tapahtumankäsittelijöillä*, joiden avulla reagoidaan törmäykseen esimerkiksi tuhoamalla toinen olioista tai kasvattamalla pistelaskurin arvoa.

Katso myös kuinka törmäyksiä voidaan estää [täältä](tormayksen-estaminen.md).

## Törmäyksenkäsittely yhdelle tunnetulle oliolle

Aluksi tapahtumankäsittelijä täytyy asettaa seuraamaan tietyn olion törmäyksiä. Esimerkiksi jos pelissä on olio nimeltä `pelaaja` jonka törmäyksistä toisiin olioihin ollaan kiinnostuneita, voidaan `pelaajan` luomisen jälkeen asettaa *tapahtumakäsittelijä*:

importante

```csharp,ignore
AddCollisionHandler(pelaaja, PelaajaTormasi);
```

Aina kun pelaaja törmää johonkin, mihin tahansa, fysiikkaolioon pelikentällä, kutsutaan aliohjelmaa `PelaajaTormasi`.

Ennen kuin törmäyksenkäsittely toimii, tarvitaan aliohjelma joka käsittelee törmäyksen. Törmäyksen käsittelevälle aliohjelmalle tulee parametreina törmänneet kaksi oliota.

```csharp,ignore
void PelaajaTormasi(PhysicsObject tormaaja, PhysicsObject kohde)
{
   MessageDisplay.Add("Pelaaja törmäsi!");
}
```

Näin joka kerran kun `pelaaja` törmää johonkin, suoritetaan aliohjelma `PelaajaTormasi`. Parametreista `tormaaja` viittaa tässä tapauksessa pelaajaan ja `kohde` olioon johon pelaaja törmäsi.

## Törmäys kahden tunnetun olion välillä

Jos halutaan reagoida törmäykseen kahden tietyn olion välillä, voidaan *tapahtumankäsittelijälle* antaa kaksi oliota:

```csharp,ignore
AddCollisionHandler(pelaaja1, pelaaja2, PelaajatTormaavat);
```

Törmäävät oliot ovat tässä tapauksessa `pelaaja1` ja `pelaaja2`. Tapahtumankäsittelijä `pelaajatTormaavat` voidaan tehdä samaan tapaan kuin yhden tunnetun olion kanssa.

```csharp,ignore
void PelaajatTormaavat(PhysicsObject tormaaja, PhysicsObject kohde)
{
   MessageDisplay.Add("Bump!");
}
```

## Törmäys yhden tunnetun ja useamman samantyyppisen olion välillä

Usein pelissä on yksi pelaaja ja useampia erityyppisiä olioita: vihollisia, aarteita, piikkiesteitä jne. Törmäyskäsittelyyn ei enää riitäkään tieto siitä, että pelaaja törmää johonkin olioon tai pelaaja törmää tiettyyn yhteen olioon. Samantyyppisille olioille voidaan antaa yhteinen [tagi](../oliot/olioiden-erottaminen-toisistaan.md), jolla olioryhmät voidaan erottaa toisistaan. Tagi on järkevintä asettaa samalla kun olio luodaan.

```csharp,ignore
void LuoVihollinen(Vector paikka, double leveys, double korkeus)
{
   PhysicsObject vihollinen = new PhysicsObject(leveys, korkeus);
   vihollinen.Position = paikka;
   vihollinen.Tag = "pahis";
   Add(vihollinen);
}

void LuoHealthPotion(Vector paikka, double leveys, double korkeus)
{
   PhysicsObject pottu = new PhysicsObject(leveys, korkeus);
   pottu.Position = paikka;
   pottu.Tag = "health";
   Add(pottu);
}
```

Törmäyskäsittelijät voidaan luoda seuraavalla tavalla esim. pelaajan luomisen yhteydessä:

```csharp,ignore
AddCollisionHandler(pelaaja, "pahis", PelaajaOsuu);
AddCollisionHandler(pelaaja, "health", PelaajaParantuu);
```

Olion ja tagin väliset tapahtumankäsittelijät voidaan tehdä seuraavaan tapaan:

```csharp,ignore
void PelaajaOsuu(PhysicsObject pelaaja, PhysicsObject kohde)
{
   pelaajanTerveys--;

   if (pelaajanTerveys <= 0)
      pelaaja.Destroy();
}

void PelaajaParantuu(PhysicsObject pelaaja, PhysicsObject kohde)
{
   pelaajanTerveys++;
}
```

Tässä esimerkissä on oletettu, että kokonaislukumuuttuja `pelaajanTerveys` löytyy pelin attribuuteista.

```csharp,ignore
public class OmaPeli : Game
{
   int pelaajanTerveys = 5;

   public override void Begin()
   {
       // jatkuu...
```

## Törmäykset muuntyyppisiin olioihin kuin PhysicsObject

Pelissä voi olla muunkintyyppisiä olioita kuin `PhysicsObject`, esimerkiksi `PlatformCharacter`. Olion täytyy kuitenkin periytyä PhysicsObjectista, jotta sen törmäyksiä voidaan käsitellä.

Jos esimerkiksi `PlatformCharacter`-tyyppistä oliota käsitellään `PhysicsObject`:ina, esimerkiksi sen `Walk`-metodia ei voi käyttää, sillä `PhysicsObject`:illa ei ole sellaista!

`Walk`-metodin käyttämiseen on olemassa kaksi ratkaisua.

**Ensimmäinen** keino on muuttaa olion tyyppi halutuksi:

```csharp,ignore
void Tormays(PhysicsObject tormaaja, PhysicsObject kohde)
{
   PlatformCharacter hahmo = tormaaja as PlatformCharacter;
   hahmo.Walk(Direction.Right);
}
```

**Toinen** tapa on käyttää `AddCollisionHandler`-aliohjelman tyyppiparametrillista versiota:

```csharp,ignore
AddCollisionHandler<PlatformCharacter, PhysicsObject>(pelaaja, HahmonTormays);
```

Tämä kertoo, että törmäyksenkäsittelijäaliohjelman `HahmonTormays` parametrit ovat tyyppiä `PlatformCharacter` (törmääjä) ja `PhysicsObject` (kohde). Nyt voidaan kirjoittaa törmäyksenkäsittelijä suoraan muotoon

```csharp,ignore
void Tormays(PlatformCharacter tormaaja, PhysicsObject kohde)
{
   tormaaja.Walk(Direction.Right);
}
```

Huomaa, että jos yrität käyttää yo. aliohjelmaa tavalliselle, tyyppiparametrittomalle `AddCollisionHandler`-metodille, kääntäjä antaa siitä virheen.

## Valmiit törmäystapahtumat

CollisionHandler-luokka sisältää valmiita käsittelijöitä yleisimmille törmäystapahtumille.

### Olioiden tuhoaminen

`DestroyObject` tuhoaa törmäävän olion.

```csharp,ignore
AddCollisionHandler(pelaaja, vihollinen, CollisionHandler.DestroyObject);
```

`DestroyTarget` tuhoaa olion johon törmätään.

```csharp,ignore
ase.ProjectileCollision = CollisionHandler.DestroyTarget;
```

`DestroyBoth` tuhoaa molemmat.

```csharp,ignore
ase.ProjectileCollision = CollisionHandler.DestroyBoth;
```

### Räjähdykset

`ExplodeObject` räjäyttää törmäävän olion. Se ottaa parametriksi räjähdyksen säteen `(int)` ja totuusarvon `(true/false)` siitä, tuhotaanko olio samalla.

```csharp,ignore
AddCollisionHandler(pelaaja, vihollinen, CollisionHandler.ExplodeObject(100, true));
```

`ExplodeObject` toimii kuten `ExplodeTarget`, mutta se räjäyttää olion, johon törmätään.

```csharp,ignore
AddCollisionHandler(salama, CollisionHandler.ExplodeTarget(150, false));
```

`ExplodeBoth` tekee räjähdyksen olioiden törmäyskohtaan ja valinnaisesti tuhoaa kummatkin oliot samalla.

```csharp,ignore
AddCollisionHandler(salama, CollisionHandler.ExplodeBoth(200, true));
```

Jos pelissä on käytössä ExplosionSystem (ks. [Efektit](../grafiikka/efektit.md)), voidaan käyttää `AddEffect`-käsittelijää. AddEffect ottaa parametrikseen räjähdysjärjestelmän ja käytettävien partikkelien määrän. AddEffect ei tuhoa olioita automaattisesti, mutta sekin onnistuu lisäämällä erillinen DestroyObject-käsittelijä:

```csharp,ignore
AddCollisionHandler(pelaaja, vihollinen, CollisionHandler.AddEffectOnTarget(paukkupatteri, 40));
AddCollisionHandler(pelaaja, vihollinen, CollisionHandler.DestroyObject);
```

Tai

Efektit ilman olion tuhoamista:

```csharp,ignore
AddCollisionHandler(salama, CollisionHandler.AddEffectOnTarget(paukkupatteri, 80));
```

### Laskurin arvon muuttaminen

[Laskurin](../kayttoliittyma/pistelaskuri.md) arvoa voidaan kasvattaa/vähentää käyttämällä `AddMeterValue`-törmäyksenkäsittelijää. Näin voidaan esimerkiksi antaa pelaajalle pisteitä kerättävistä esineistä tai vähentää terveyttä/elämiä viholliseen osumisesta.

```csharp,ignore
AddCollisionHandler(pelaaja, "bonus", CollisionHandler.AddMeterValue(pisteet, 10));
AddCollisionHandler(pelaaja, "piikki", CollisionHandler.AddMeterValue(health, -1));
```

Tätä tapaa ei voida käyttää mikäli, pisteiden laskemisella on jotakin muita ehtoja kuin pelkkä törmääminen. Tällöin pistelaskuri pitää käsitellä normaalissa törmäystapahtumassa ja kirjoittaa sinne ehto, jonka avulla laskurin arvoa muutetaan (ks. [laskurin arvon muuttaminen](../kayttoliittyma/pistelaskuri.md#laskurin-arvon-muuttaminen)).

### Ääniefektin soittaminen

Ääniefektin soittaminen törmäyksen yhteydessä onnistuu tapahtumankäsittelijällä `PlaySound`, jolle annetaan parametriksi ääniefektin nimi. Nimi on yleensä sama kun tiedoston nimi, mutta <span class="red">ilman</span> tiedostopäätettä.

```csharp,ignore
AddCollisionHandler(pelaaja, "tuli", CollisionHandler.PlaySound("tuskan_parahdus"));
```

### Impulssi

`HitObject` lyö törmäävää oliota ja `HitTarget` oliota, johon törmätään. Molemmat ottavat parametrikseen vektorin, joka kertoo lyönnin suunnan ja voiman.

```csharp,ignore
Vector ylos = new Vector(200, 0);
AddCollisionHandler(pelaaja, "trampoliini", CollisionHandler.HitObject(ylos));
```

### Olion koon muuttaminen

Olion kokoa on mahdollista muuttaa törmäyksessä `IncreaseObjectSize` ja `IncreaseTargetSize` -käsittelijöillä. Ensimmäinen muuttaa törmääjän kokoa ja jälkimmäinen sen olion, johon törmätään. Molemmat ottavat parametrikseen leveyden ja korkeuden muutoksen (tässä järjestyksessä). Olioita voi myös pienentää käyttämällä negatiivisia arvoja.

```csharp,ignore
AddCollisionHandler(pelaaja, "nakki", CollisionHandler.IncreaseObjectSize(10, 10));
AddCollisionHandler(kirves, CollisionHandler.IncreaseTargetSize(-5, 0));
```

## Katso myös

- [Törmäysten estäminen](tormayksen-estaminen.md): olio, jonka läpi voi kulkea, ja törmäysryhmät.
- [Olioiden Tag-ominaisuus](../oliot/olioiden-erottaminen-toisistaan.md): käsittelijä vain tietyntyyppisille olioille.
- [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#aliohjelman-parametrit-tulevat-tapahtumasta): käsittelijän parametrit ja attribuutit.
- [Räjähdykset](../grafiikka/rajahdykset.md) ja [Pistelaskuri](../kayttoliittyma/pistelaskuri.md): tavallisimmat asiat, joita törmäyksessä tehdään.
