# Olioiden Tag-ominaisuus

Jypelissä useimmilla olioilla (esimerkiksi GameObjectilla ja PhysicsObjectilla) on olemassa Tag-niminen ominaisuus. Tag on siitä erikoinen, että sen arvoksi voidaan antaa mitä vain - niin merkkijonoja kuin mitä vain olioita.

## Olioiden "tunnistaminen" ja Tag-ominaisuus

Tagia voi käyttää pelin tekemisessä hyödyksi vaikkapa erilaisten peliolioiden ja fysiikkaolioiden tunnistamisessa.

Esimerkki: pelissä on paljon fysiikkaolioita, joita käytetään kentän seininä. Halutaan tunnistaa jos pelihahmo osuu johonkin monista seinistä ja vaihtaa aina sen seinän väriä mihin pelaaja osuu.

Ratkaisu: Voidaan lisätä jokaisen seinänä toimivan fysiikkaolion Tag-ominaisuuteen jokin merkkijono, josta voimme myöhemmin tunnistaa että se on juuri seinänä toimiva olio. Tämä on järkevää tehdä seiniä tekevässä aliohjelmassa:

```csharp,ignore
void LuoSeina(double x, double y)
{
    PhysicsObject seina = PhysicsObject.CreateStaticObject(50.0, 50.0);
    seina.X = x;
    seina.Y = y;
    seina.Tag = "seina";
    Add(seina);
}
```

Pelihahmon törmäyksiä käsittelevässä aliohjelmassa voidaan aina kysyä törmäyksen kohteelta sen Tag-ominaisuutta muutettuna merkkijonoksi.

Jos merkkijono täsmää antamamme tunnisteen kanssa, tiedetään että pelihahmo on törmännyt seinään ja reagoidaan siihen haluamallamme tavalla:

```csharp,ignore
void KasittelePelaajanTormays(PhysicsObject pelaaja, PhysicsObject kohde)
{
    if (kohde.Tag.ToString() == "seina")
    {
        kohde.Color = RandomGen.NextColor();
    }
}
```

Samaa menetelmää voi käyttää jos pelissä on esimerkiksi paljon samanlaisia kerättäviä esineitä tai paljon vihollisia. Sovella esimerkkiä!

## Miten saan vihollisen kestämään useamman osuman?

*On suositeltavaa käyttää tähän ideaan ​mieluummin perintää, kuin tagien avulla "kikkailua", mutta joissain tilanteissa tällainenkin ratkaisu voi tulla kysymykseen.*

Tag-ominaisuutta voidaan käyttää myös tallentamaan vihollisen osumapisteitä, eli kuinka monta kertaa siihen pitää osua ennen kuin se kuolee. Osumapisteet voidaan lisätä tagin perään näin:

```csharp,ignore
vihollinen.Tag = "pomo5";
```

Nyt kun pelaajan ammukselle on lisätty törmäyskäsittelijä (ks. [törmäyskäsittelijöiden lisääminen](../tapahtumat/tormaykset.md)), siellä voidaan toimia seuraavasti:

```csharp,ignore
void AmmusOsuu(PhysicsObject ammus, PhysicsObject kohde)
{
   if (ammus.Tag == null) return;
   string tagi = ammus.Tag.ToString();
   string pomonTagi = "pomo";

   if (tagi.StartsWith(pomonTagi))
   {
      int osumapisteet = int.Parse(tagi, pomonTagi.Length);
      osumapisteet--;

      if (osumapisteet <= 0)
      {
         // Vihollinen kuolee
         kohde.Destroy();
      }
      else
      {
         // Vihollinen menettää terveyttä, mutta ei kuole
         vihollinen.Tag = pomonTagi + osumapisteet;
      }
   }
}
```
