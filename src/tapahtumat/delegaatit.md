# Delegaatit

Moni Jypelin ominaisuus perustuu *tapahtumiin* (event), joita käytetään antamalla uusi metodi tapahtumalle. Esimerkiksi uusi tapahtuma ajastimelle luodaan näin:

```csharp,ignore
ajastin.Timeout += TapahtumanKasittelevaMetodi;
```

Nyt saimme kivan tapahtuman syntymään silloin, kun ajastin saavuttaa annetun intervallin. Mutta entä jos haluaisimme vaikka nollata ajastimen Timeoutissa tai kutsua aliohjelmaa, jolle annetaan parametrina fysiikkaolio?

```csharp,ignore
PhysicsObject morko = new PhysicsObject(20,20);
ajastin.Timeout += TapahtumanKasittelevaMetodi(morko);
// Tämä koodi aiheuttaa virheen eikä toimi.
```

Ratkaisu tähän pulmaan on C#:iin sisäänrakennettu ominaisuus nimeltä *delegaatti*. Delegaatti on lyhyesti sanottuna anonyymi, eli nimetön, aliohjelma. Kirjoitetaan tuon aliohjelman koodi, eli käytännössä toisen aliohjelman kutsu.

```csharp,ignore
//aiempi ohjelman koodi
ajastin.Timeout += delegate { TapahtumanKasittelevaMetodi(morko); };
}

void TapahtumanKasittelevaMetodi(PhysicsObject morko)
{
  //tee jotain mörölle
}
```

Delegaatin voidaan ajatella olevan lyhyempi tapa kirjoittaa seuraavanlainen koodi:

```csharp,ignore
ajastin.Timeout += Avustajametodi;
}

void Avustajametodi()
{
    TapahtumanKasittelevaMetodi(morko);
}

void TapahtumanKasittelevaMetodi(PhysicsObject morko)
{
  //tee jotain mörölle
}
```

Delegaatin avulla voimme siis kutsua toista aliohjelmaa halutulla tavalla, joka ei käynyt ajastimen `Timeout`-tapahtumalle.

Delegaatin kanssa tulee muistaa laittaa puolipiste sekä aaltosulkujen että jokaisen lauseen jälkeen delegaatissa. Delegaattiin voi siis syöttää useammankin asian esimerkiksi näin:

```csharp,ignore
ajastin.Timeout += delegate { TapahtumanKasittelevaMetodi(morko);
                              luku++;
                              ajastin.Reset(); };
```

Delegaattia kannattaa käyttää ohjelman helppolukuisuuden säilyttämiseksi sekä parametrien välittämiseksi eteenpäin, tuolla tavoin ei tarvitse jokaisesta luvusta tehdä attribuuttia.

## Delegaatin käyttöesimerkkejä

Joskus voi tuntua hieman tarpeettomalta kirjoittaa aliohjelma, jossa on vain yksi rivi ja jota kutsutaan vain yhdestä paikasta. Esimerkiksi vaikka pelaajan ohjausta käsittelevät aliohjelmat:

```csharp,ignore
Keyboard.Listen(Key.Space, ButtonState.Pressed, Hyppaa, "Pelaaja hyppää");

...

private void Hyppaa()
{
    pelaaja.Jump(HYPPYVOIMA);
}
```

Voitaisiin yhtä hyvin kirjoittaa:

```csharp,ignore
Keyboard.Listen(Key.Space, ButtonState.Pressed, delegate{ pelaaja.Jump(HYPPYVOIMA); }, "Pelaaja hyppää");
```

Mutta entä jos tarvitaan parametreja?

Katsotaanpa siihen esimerkkiä:

```csharp,ignore
Keyboard.Listen(Key.Space, ButtonState.Pressed, delegate(double voima)
                                                {
                                                    pelaaja.Jump(voima);
                                                }, "Pelaaja hyppää", 50.0);
```

Sisennykset ja rivinvaihdot on lisätty tähän selkeyden vuoksi.

Sehän muistuttaa aika paljon tavallisen aliohjelman esittelyriviä.
