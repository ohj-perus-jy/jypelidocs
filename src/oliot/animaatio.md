# Animaatio

Jypelissä pelin olioille voi lisätä animaatioita eli liikkuvaa kuvaa. Oikeastaan animaatio koostuu useasta yksittäisestä kuvasta, jotka näytetään peräkkäin.

Aluksi täytyy siis piirtää animaatio piirto-ohjelmaa (esimerkiksi Paint.NET) käyttäen.

<!-- kuva puuttuu -->

<!-- TODO: TIMIIN -->

## Animaation lataaminen

Kuvat on ensin liitettävä projektiin yksitellen (lue [Sisällön tuominen peliin](https://tim.jyu.fi/view/kurssit/tie/ohj1/tyokalut/sisallon-tuominen-peliin)). Sen jälkeen kuvat ladataan koodissa taulukkoon, jonka jälkeen niistä voidaan koostaa animaatio.

```csharp,ignore
public class Peli : PhysicsGame
{
    private Image[] ukkelinKavely = LoadImages("uk2anoik1", "uk2anoik2", "uk2anoik3");

    public override void Begin()
    {
         //...
    }
```

Rivi

```csharp,ignore
private Image[] ukkelinKavely = LoadImages("uk2anoik1", "uk2anoik2", "uk2anoik3");
```

siis lataa kuvat taulukkoon. Kuvien nimet laitetaan lainausmerkkeihin ja erotetaan pilkulla, huomaa, että tiedostopäätettä (esim. .png) ei tarvitse kirjoittaa.

## Animaation asettaminen oliolle

Kun animaatio on ladattu jommallakummalla yo. tavoista, se voidaan asettaa oliolle missä vaiheessa halutaan. Yleensä animaatio asetetaan heti olion luonnin jälkeen.

```csharp,ignore
pelaaja.Animation = new Animation(ukkelinKavely);
pelaaja2.Animation = new Animation(ukkelinKavely);
```

- Jos asetat animaation suoraan ilman new Animation -kutsua (ja ukkelinKavely on tyyppiä Animation), niin animaatio on kirjaimellisesti sama, eli jos pysäytät toisen, myös toinen pysähtyy!

Lisäämisen jälkeen animaatio täytyy käynnistää:

```csharp,ignore
pelaaja.Animation.Start();
```

Animaation saa lopetettua vastaavasti:

```csharp,ignore
pelaaja.Animation.Stop();
```

Jos halutaan toistaa animaatio esimerkiksi vain kerran, `Start` voi ottaa parametrina toistojen määrän:

```csharp,ignore
pelaaja.Animation.Start(1);
```

Animaation nopeutta voi vaihdella muuttamalla sen FPS-arvoa (frames per second). Sen arvo tarkoittaa, montako ruutua animaatiosta näytetään sekunnin aikana.

```csharp,ignore
pelaaja.Animation.FPS = 10;
```

### Animaation peilaaminen pysty- tai vaakasuunnassa

Animaatio voidaan **peilata** (Mirror) tai **kääntää ylösalaisin** (Flip) koodissa, jolloin saadaan sama animaatio eri suuntiin, esimerkiksi eri suuntiin liikkumista varten.

```csharp,ignore
Animation ukkeliPeilattu = Animation.Mirror(ukkeli);
Animation ukkeliYlosalaisin = Animation.Flip(ukkeli);
```

## Animaatiot PlatformCharacter-tasohyppelyhahmolle

**PlatformCharacter** (ja **PlatformCharacter2**) -tyypille voidaan antaa erikseen

- kävelyanimaatio,

- paikallaan olon animaatio,

- hyppyanimaatio ja

- putoamisanimaatio.

Kuvat kannattaa piirtää niin, että niissä **pelaajan rintamasuunta on oikealle**. Silloin animaatiot **kääntyvät automaattisesti vasemmalle ja oikealle**, jos liikuttamiseen käyttää hahmon **Walk**-metodia.

Kuvat kannattaa ladata muuttujiin pelin alussa. Katso tämän ohjeen alusta, jos et muista, miten se tehdään.

Kun kuvat on ladattu mukaan peliin, asetetaan kuvista uudet animaatiot `PlatformCharacter`-oliolle `pelaaja1`:

```csharp,ignore
pelaaja1.AnimWalk = new Animation(kavelyAnimaatio);
pelaaja1.AnimIdle = new Animation(paikallaanAnimaatio);
pelaaja1.AnimJump = new Animation(hyppyAnimaatio);
pelaaja1.AnimFall = new Animation(laskeutumisAnimaatio);
```

Animaatioiden nopeutta voi säätää niiden FPS-ominaisuudesta:

```csharp,ignore
pelaaja1.AnimWalk.FPS = 5;
```

Animaatioiden hienosäätöön tarkoitettuja ominaisuuksia:

|  |  |
|:---|----|
| LoopJumpAnim | Toistetaanko hyppyanimaatiota useammin kuin kerran per hyppy (oletus ei). |
| LoopFallAnim | Toistetaanko putoamisanimaatiota useammin kuin kerran per putoaminen (oletus ei). |
| WalkOnAir | Toistetaanko kävelyanimaatiota ilmassa (oletus ei). |

## Muun animaation lisääminen PlatformCharacterille

PlatformCharacterille voi asettaa myös muita animaatioita kuin edellä mainittuja. Esimerkiksi `hyokkaysAnimaatio`-muuttujaan tallennettu animaatio voidaan toistaa kirjoittamalla

```csharp,ignore
pelaaja.PlayAnimation(hyokkaysAnimaatio);
```
