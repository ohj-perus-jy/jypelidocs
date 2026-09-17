# Läpsylintu, vaihe 1: Projekti ja kenttä

Tässä ohjeessa neuvotaan Läpsylintu-nimisen pelin tekeminen. Pelissä ohjataan vasemmalta oikealle lentävää lintua, jonka siipiä voi räpyttää.

## Projektin luominen

- Jos et ole vielä asentanut tarvittavia työvälineitä, asenna ne nyt.
- Avaa Rider tai jokin muu C#-kielellä toimiva ohjelmointiympäristö ja klikkaa New Solution.
- Valitse pohjaksi **Tasohyppelypeli** klikkaamalla yhden kerran **Tasohyppelypeli**-pohjan nimeä.
- Anna solutionille nimeksi esimerkiksi Lapsylintu. Älä vielä paina Createa. (Nimissä ei kannata käyttää välilyöntejä tai erikoismerkkejä!)
- Valitse **Solution directory** -kohtaan kansio, johon peli tallennetaan, esimerkiksi `C:\Users\Käyttäjänimi\Koodiprojektit` (Macilla esimerkiksi `/Users/käyttäjänimi/Koodiprojektit`). **Yliopiston koneilla** kansioksi on annettava `C:\MyTemp\Omanimi`, ei Omat tiedostot -kansiota.
- Paina Create.

Kokeile ajaa projektimallista luotu pelisi klikkaamalla yläpalkista vihreää kolmiota <span class="green">▶</span> (**Run**).

> [!KOKEILE]

## Kenttätiedoston muokkaaminen

Avaa Riderin vasemman reunan Explorer-näkymästä löytyvästä `Content`-kansiosta tiedosto `kentta1.txt`. Korvaa sen sisältö kokonaan seuraavalla tekstillä:

```text
##################################################
..................................................
..............*.........................*.........
N...........................*.....................
.....*............................................
...................*..............................
..........................*................*......
..................................................
................................*.......*.........
..................................................
..................................................
##################################################
```

## Pelaaja hyppäämään myös ilmassa

Avaa tiedosto `Lapsylintu.cs`.

Muokataan pelaajan hyppäämistä siten, että hypyn voi suorittaa myös ilmassa. Etsi aliohjelma `Hyppaa()` ja sen sisältä rivi:

```csharp,ignore
hahmo.Jump(nopeus);
```

Ja muokkaa metodi `Jump()` muotoon `ForceJump()`:

```csharp,ignore
hahmo.ForceJump(nopeus);
```

## Tutki!

> [!KYSYMYS]
> Osaatko etsiä koodista, mitä mikäkin näppäin tekee?

## Kokeile!

Kokeile, kuinka peli toimii! Siirry sen jälkeen ohjeessa eteenpäin.

> [!KOKEILE]
