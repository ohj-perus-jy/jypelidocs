# Oma oliotyyppi

Valmiissa `PhysicsObject`-oliossa on paikka, nopeus, massa ja väri, mutta ei
elämiä, pisteitä tai omaa käyttäytymistä. Kun pelihahmo tarvitsee sellaisia,
peritään oma luokka: se on kaikkea sitä, mitä `PhysicsObject` on, ja lisäksi
jotain omaa. Tämä osio käy läpi, miten oma luokka kirjoitetaan ja miten sitä
käytetään pelissä.

| Ohje | Sisältö |
| --- | --- |
| [Oman luokan periminen](luokan-periminen.md) | Luokan runko, rakentaja ja `base`, mistä luokasta peritään, mihin tiedostoon luokka kirjoitetaan. |
| [Omat ominaisuudet ja metodit](ominaisuudet.md) | Elämät ja muut ominaisuudet, rakentajan parametrit, oletusarvot, laskuri ominaisuutena, olion omat aliohjelmat. |
| [Olion käyttäminen pelissä](kaytto.md) | Luominen ja lisääminen, monta samanlaista oliota, törmäyskäsittelijä omalle tyypille, tyypin tunnistaminen. |
| [Oma päivitysmetodi](paivitys.md) | `IsUpdated = true` ja `Update`, jota Jypeli kutsuu 60 kertaa sekunnissa. |
| [Tapahtumat omassa luokassa](tapahtumat.md) | `AddedToGame`, törmäys luokan sisällä, `Destroy`-metodin korvaaminen ja omat tapahtumat. |
| [Pelin tiedot olion sisällä](pelin-tiedot.md) | `Game`-sana luokan sisällä ja kolme tapaa päästä käsiksi `Peli`-luokan laskureihin ja aliohjelmiin. |

Tarvitset ensin: [Olion luominen](../oliot/luonti.md) ja Ohjelmointi 1:n
[luennon perinnästä](https://ohjelmointi1.it.jyu.fi/luennot/luento14/).

Sama tekniikka sovellettuna käyttöliittymään on sivulla
[Omat käyttöliittymäkomponentit](../kayttoliittyma/omat-kayttoliittymakomponentit.md),
ja pidempi esimerkki omasta luokasta on auto sivulla
[Liitokset](../fysiikka/liitokset.md).
