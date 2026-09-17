# Sivulle vierivä kenttä

Esim. spaceshooter-tyyppisissä peleissä pelaaja on paikallaan ja muut oliot, esimerkiksi vihollisalukset, lähestyvät pelaajaa.

Alla on ohje, jolla voidaan liikuttaa "muita olioita" pelaajan pysyessä paikallaan.

Huomaa, että tämä ei ole välttämättä hyvä tapa tehdä ns. sidescroller-pelejä. Sellaisissa peleissä (esim. Geometry Dash) on mielekkäämpää liikuttaa pelaajaa ja kameraa ja pitää muu maailma paikallaan.

Alla olevat rivit kuuluu laittaa luokan yläreunaan, ennen Begin-aliohjelmaa. Suunnalla voi säädellä olioiden liikesuuntaa ja tuhoamisX määrittää, minkä koordinaatin ylittäessään oliot tuhotaan.

```csharp,ignore
    private List<GameObject> liikutettavat = new List<GameObject>();
    private double suunta = -5;
    private double tuhoamisX;
```

Begin:iin lisätään tuhoamisX:n sijainnin määritys. Samoin luodaan uusi ajastin, jonka avulla saadaan liikutettua olioita vasemmalle. Oliot, joiden halutaan liikkuvan vasemmalle, pitää lisätä liikutettavat-listaan.

```csharp,ignore
    public override void Begin()
    {
        tuhoamisX = Level.Left;

        Timer liikutusajastin = new Timer();
        liikutusajastin.Interval = 0.05;
        liikutusajastin.Timeout += LiikutaOlioita;
        liikutusajastin.Start();

        PhysicsObject pallo = new PhysicsObject(50, 50);
        Add(pallo);
        liikutettavat.Add(pallo);
    }
```

Lisää vielä alla oleva aliohjelma koodiin. Aliohjelma siirtää listalla olevia olioita vasemmalle.

```csharp,ignore
    private void LiikutaOlioita()
    {
        for(int i = 0; i < liikutettavat.Count; i++)
        {
            GameObject olio = liikutettavat[i];
            olio.X += suunta;
            if (olio.X <= tuhoamisX)
            {
                olio.Destroy();
                liikutettavat.Remove(olio);
            }
        }
    }
```
