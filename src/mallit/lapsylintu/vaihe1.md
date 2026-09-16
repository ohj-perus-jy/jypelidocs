# Läpsylintu: Vaihe 1

Tässä ohjeessa neuvotaan Läpsylintu-nimisen pelin tekeminen. Pelissä ohjataan vasemmalta oikealle lentävää lintua, jonka siipiä voi räpyttää.

## Projektin luominen

- Jos et ole vielä asentanut tarvittavia työvälineitä, asenna ne nyt.
- Avaa Rider tai joku muu C#-kielellä toimiva ohjelmointiympäristö ja klikkaa New Solution.
- Valitse pohjaksi **Tasohyppelypeli** klikkaamalla yhden kerran **Tasohyppelypeli**-pohjan nimeä.
- Anna solutionille nimeksi esimerkiksi Lapsylintu. Älä vielä paina Createa. (Nimissä ei kannata käyttää välilyöntejä tai erikoismerkkejä!)
- **Jos** teet peliä yliopiston mikroluokassa, muista tallentaa hakemistoon `C:\MyTemp\omanimi`, ei Windowsin Omat tiedostot -hakemistoon! Omalla tietokoneella voit tallentaa projektin mihin haluat.
- Paina Create.

Kokeile ajaa projektimallista luotu pelisi painamalla ctrl-F5 (joillakin laitteilla pitää painaa fn-näppäintä ctrl ja F5 kanssa), tai yläpalkista klikkaamalla <span class="green">▶</span>.

%%kokeile%%

## Kenttätiedoston muokkaaminen

Avaa näytön oikeassa reunassa näkyvästä `Solution Explorer:sta` löytyvästä `Content`-kansiosta tiedosto `kentta1.txt`. Korvaa sen sisältö kokonaan seuraavalla tekstillä:

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

Ja muokkaa metodi `Jump()` muotoon `ForceJump()`

```csharp,ignore
hahmo.ForceJump(nopeus);
```

## Tutki!

%%kysymys%% Osaatko etsiä koodista mitä mikäkin näppäin tekee?

## Kokeile!

Kokeile, kuinka peli toimii! Siirry sen jälkeen ohjeessa eteenpäin.

%%kokeile%%
