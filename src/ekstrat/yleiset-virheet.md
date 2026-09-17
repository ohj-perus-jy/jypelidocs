# Yleiset virheet

Tavallisimmat tilanteet, joissa peli ei käänny tai ei toimi odotetusti, ja
mitä niille tehdään. Virheilmoitukset ovat englanniksi, ja ne näkyvät
Riderissa punaisella alleviivauksella koodissa sekä alareunan
Problems-välilehdellä.

## Peli ei käänny

| Ilmoitus | Syy | Korjaus |
| --- | --- | --- |
| `; expected` | Rivin lopusta puuttuu puolipiste. | Lisää `;` rivin loppuun. |
| `} expected` | Aaltosulku on jäänyt sulkematta. | Tarkista, että jokaisella `{` on pari. Rider korostaa parin, kun kursori on sulun vieressä. |
| `The name 'X' does not exist in the current context` | Muuttujaa tai aliohjelmaa `X` ei ole, tai se on paikallinen toisessa aliohjelmassa, tai nimi on kirjoitettu eri tavalla (isot ja pienet kirjaimet ovat eri kirjaimia). | Tarkista kirjoitusasu. Jos muuttujaa tarvitaan toisessa aliohjelmassa, ks. [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti). |
| `No overload for 'X' matches delegate ...` | Tapahtumankäsittelijän parametrit eivät vastaa tapahtumaa. Esimerkiksi törmäyskäsittelijällä pitää olla kaksi `PhysicsObject`-parametria. | Katso oikea muoto sivulta [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#aliohjelman-parametrit-tulevat-tapahtumasta). |
| `Cannot implicitly convert type 'double' to 'int'` | Desimaaliluku on sijoitettu kokonaislukumuuttujaan. | Käytä `double`-tyyppiä tai pyöristä. |
| `A local variable named 'X' is already defined in this scope` | Sama muuttuja on esitelty kahdesti samassa aliohjelmassa. | Poista toinen esittely; jos tarkoitus oli antaa attribuutille arvo, jätä tyyppi pois rivin alusta. |
| `'X' is a type, which is not valid in the given context` | Luokan nimeä on käytetty kuin muuttujaa (esim. `PhysicsObject.Shape`). | Käytä muuttujan nimeä, esim. `pallo.Shape`. |

Punainen alleviivaus näkyy usein jo kesken kirjoittamisen. Kirjoita rivi
loppuun, ennen kuin huolestut.

## Peli käynnistyy, mutta jotain puuttuu

| Oire | Syy | Korjaus |
| --- | --- | --- |
| Olio ei näy. | `Add(olio)` puuttuu, tai olio on kameran näkymän ulkopuolella, tai se on toisen olion takana. | Lisää `Add`. Kutsu `Camera.ZoomToLevel()`. Ks. [Kerrokset](../oliot/kerrokset.md). |
| Peli kaatuu heti ja ilmoituksessa lukee `Could not find file ... Content\...` tai `FileNotFoundException`. | Kuva- tai äänitiedosto ei ole `Content`-kansiossa, tai sen *Copy to Output Directory* -asetus ei ole *Copy if newer*, tai nimi on eri. | Ks. [Kuvat ja äänet mukaan projektiin](../aloittaminen/sisallon-tuonti.md). |
| `NullReferenceException` | Attribuutille ei ole annettu arvoa, tai `Begin`-aliohjelmassa on luotu samanniminen paikallinen muuttuja. | Ks. [Miten Jypeli-peli toimii](../aloittaminen/pelin-rakenne.md#paikallinen-muuttuja-vai-attribuutti). |
| Näppäin ei tee mitään. | `Listen`-rivi puuttuu tai on toisessa aliohjelmassa, jota ei kutsuta, tai tilana on `Pressed`, vaikka tarkoitus oli pitää pohjassa (`Down`). | Ks. [Ohjainten lisääminen](../ohjaimet/ohjainten-lisays.md). |
| Törmäystä ei huomata. | Toinen olioista on `GameObject` eikä `PhysicsObject`, tai käsittelijä on lisätty, ennen kuin olio on luotu, tai oliot ovat samassa `CollisionIgnoreGroup`-ryhmässä. | Ks. [Törmäysten käsittely](../tapahtumat/tormaykset.md). |
| Oliot valuvat kentän ulkopuolelle. | Kentällä ei ole reunoja. | `Level.CreateBorders();` |
| Ääni ei kuulu. | Tiedostomuoto ei kelpaa tai tiedosto ei ole `Content`-kansiossa. | Ks. [Äänet ja musiikki](../grafiikka/aanien-lisays.md). |

## Kun mikään ei auta

- Aja peli debuggerilla klikkaamalla Run-kolmion vieressä olevaa vihreää
  ötökkäkuvaketta (**Debug**). Rider pysähtyy virheen kohdalle ja näyttää
  muuttujien arvot.
- Ohjelmointi 1:n [usein kysytyt kysymykset](https://ohjelmointi1.it.jyu.fi/ukk/).
- Jypelin [lähdekoodi ja issue-seuranta GitHubissa](https://github.com/Jypeli-JYU/Jypeli).
