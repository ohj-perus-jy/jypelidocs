# Painovoima

Fysiikkapeliin lisätään painovoima kirjoittamalla seuraava koodi:

```csharp,ignore
Gravity = new Vector(0.0, -981.0);
```

Painovoima siis määritetään erikseen x- ja y-suunnille. Yleensä halutaan kuitenkin, että painovoima vetää kappaleita alaspäin, jolloin x:n arvona on aina 0 ja y:n arvo on jokin negatiivinen luku.

Painovoima (kuten muutkin fysiikkaan liittyvät arvot) annetaan Jypelin omina yksikköinä, eli samoina yksikköinä kuin olioiden paikat ja koot. Ne eivät ole näytön pikseleitä. Painovoiman voimakkuus annetaan yksikössä `yksikköä/s^2`, ja voit kuvitella, että yksi yksikkö olisi yksi senttimetri oikeassa maailmassa. Eli täten Y-akselin arvo `-981` olisi vastine oikean maailman `9,81 m/s^2` putoamiskiihtyvyydelle.

Kokeile mikä arvo tuntuu hyvältä juuri sinun peliisi.
