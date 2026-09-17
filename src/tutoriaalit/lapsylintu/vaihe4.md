# Läpsylintu, vaihe 4: Seinään törmääminen

## Seinään törmääminen

Haluamme, että pelaaja ei voi enää liikuttaa lintuhahmoa, jos hän osuu seinään. Seiniä kutsutaan valmiissa tasohyppelypelin pohjassa tasoiksi, joten muokataan ensin `LisaaTaso`-aliohjelmaa.

Etsi aliohjelma `LisaaTaso`, joka vielä tässä vaiheessa näyttää tältä:

```csharp,ignore
private void LisaaTaso(Vector paikka, double leveys, double korkeus)
{
    PhysicsObject taso = PhysicsObject.CreateStaticObject(leveys, korkeus);
    taso.Position = paikka;
    taso.Color = Color.Green;
    Add(taso);
}
```

Jotta voimme lisätä törmäystarkistuksen, pitää törmättävillä asioilla, tässä tapauksessa tasoilla, olla jokin tunniste.

Lisätään rivin `taso.Color = Color.Green;` jälkeen seuraava rivi:

```csharp,ignore
taso.Tag = "seina";
```

Nyt jokaiselle kenttään lisätylle tasolle tulee käyttöön tagi "seina".

Hyödynnetään seuraavaksi tätä tagia.

Etsi aliohjelma `LisaaPelaaja`. Sen loppuosassa on seuraava rivi:

```csharp,ignore
AddCollisionHandler(pelaaja1, "tahti", TormaaTahteen);
```

Se tarkoittaa, että kun olio `pelaaja1` törmää mihin tahansa olioon, jonka tagina on "tahti", kutsutaan aliohjelmaa `TormaaTahteen`.

Haluamme tehdä vastaavanlaisen rivin, mutta niin, että aina, kun `pelaaja1` törmää olioon, jonka tagina on "seina", kutsutaan aliohjelmaa `TormaaTasoon`.

Lisää siis seuraava rivi olemassa olevan rivin alapuolelle:

```csharp,ignore
AddCollisionHandler(pelaaja1, "seina", TormaaTasoon);
```

Ohjelmointiympäristö varoittaa, että `TormaaTasoon`-nimistä aliohjelmaa ei ole vielä olemassa. Seuraavaksi lisätään uusi `TormaaTasoon`-niminen aliohjelma `LisaaPelaaja`-aliohjelman lopettavan `}`-aaltosulun alapuolelle:

```csharp,ignore
void TormaaTasoon(PhysicsObject tormaaja, PhysicsObject kohde)
{

}
```

Törmäysaliohjelma saa Jypelissä automaattisesti kaksi parametria: törmääjän, joka törmäsi, ja kohteen, johon törmättiin.

Tarkoituksenamme on vain ottaa pelaajan ylös-näppäin pois käytöstä, jotta hyppääminen ei enää olisi mahdollista, joten emme käytännössä tarvitse parametreja, mutta ne on silti esiteltävä aliohjelman esittelyrivillä.

Kirjoitetaan käyttäjälle viesti kuolemasta ja otetaan ylös-näppäin pois käytöstä aliohjelmassa `TormaaTasoon`:

```csharp,ignore
MessageDisplay.Add("Kuolit! :(");
Keyboard.Disable(Key.Up);
```

Kokeile, että pelisi toimii nyt. Törmäyksestä pitäisi tulla viesti ja näppäimistön ylös-näppäimen lakata toimimasta.

> [!KOKEILE]

## Useamman törmäämisen estäminen

Jos pelaaja osuu kattoon ja putoaa sieltä alas, saattaa ensimmäisen kuolemisen jälkeen tulla useampiakin törmäyksiä seiniin. Jokaisesta törmäämisestä pelaaja kuolee uudelleen, mitä emme halua.

Kuolemisen pitää tapahtua vain silloin, jos peli on yhä käynnissä eikä vielä kentän aikana ole kuoltu.

Esitellään `Lapsylintu`-luokan sisälle totuusarvo `peliKaynnissa`, joka saa arvon `true` aina silloin, kun peli on käynnissä, ja arvon `false` aina silloin, kun peli ei ole käynnissä. Totuusarvot esitellään C#-kielessä muuttujatyypillä `bool`.

Lisää ennen `Begin`-aliohjelmaa (eli `Begin`-aliohjelman yläpuolelle, sinne, mihin aiemmin lisättiin kuvien lataus) seuraava rivi:

```csharp,ignore
private bool peliKaynnissa = false;
```

Oletuksena `peliKaynnissa` on siis totuusarvoltaan epätosi.

Jatketaan `TormaaTasoon`-aliohjelman muokkaamista.

Lisää aliohjelmaan `TormaaTasoon` `if`-lohko seuraavasti. Huomaa, että osa riveistä on jo olemassa koodissasi. Lohkoa varten tarvitset aaltosulkumerkkejä `{` ja `}`.

```csharp,ignore
void TormaaTasoon(PhysicsObject tormaaja, PhysicsObject kohde)
{
    if (peliKaynnissa)
    {
        MessageDisplay.Add("Kuolit! :(");
        Keyboard.Disable(Key.Up);
        peliKaynnissa = false;
    }
}
```

Nyt `TormaaTasoon`-aliohjelman sisällä olevat rivit suoritetaan vain, jos `peliKaynnissa`-muuttujan arvo on tosi (eli `true`).

Jos peli on ensimmäisellä törmäyskerralla käynnissä, näytetään viesti, ja peli asetetaan jatkoa varten pois päältä, jottei törmäyksistä tapahdu enää uudestaan mitään.

Jotta `peliKaynnissa` olisi edes joskus tosi (eli totuusarvona `true`), asetetaan `Begin`-aliohjelmaan viimeiseksi riviksi ennen lopettavaa `}`-sulkua seuraava rivi:

```csharp,ignore
peliKaynnissa = true;
```

Peli siis käynnistyy siinä vaiheessa, kun `Begin`-lohko on saatu suoritetuksi. Peli on pois käynnistä sen jälkeen, kun ensimmäinen törmäys ja kuolema on tapahtunut. Kokeile, toimiiko ohjelma.

> [!KOKEILE]
