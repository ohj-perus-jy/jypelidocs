# Satunnaisuus

Jypelin satunnaislukugeneraattorilla (`RandomGen`) voi arpoa monentyyppisiä asioita. Satunnaisen arvon voi arpoa tyypillisesti metodilla, jonka alkuosa on **Next** ja loppuosa arvottavan tyypin nimi (esimerkiksi `Double`).

<table class="wiki">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td><strong>Kokonaisluku</strong></td>
<td><strong>Desimaaliluku</strong></td>
</tr>
<tr>
<td><code>int luku = RandomGen.NextInt(100);</code> (pienempi kuin 100)<br />
<code>int luku = RandomGen.NextInt(50, 1000);</code> (väliltä 50-999)</td>
<td><code>double luku = RandomGen.NextDouble(5.0, 120.0);</code> (väliltä 5,0 - 120,0)</td>
</tr>
<tr>
<td><strong>Väri</strong></td>
<td><strong>Totuusarvo</strong></td>
</tr>
<tr>
<td><code>Color vari = RandomGen.NextColor();</code></td>
<td><code>bool totuusarvo = RandomGen.NextBool();</code></td>
</tr>
<tr>
<td><strong>Suunta</strong></td>
<td style="text-align: left;"><strong>Kulma</strong></td>
</tr>
<tr>
<td><code>Direction suunta = RandomGen.NextDirection();</code></td>
<td style="text-align: left;"><code>Angle kulma = RandomGen.NextAngle()</code></td>
</tr>
</tbody>
</table>

## Satunnaiset numerot

`RandomGen`-luokalta löytyy useita metodeja satunnaisten lukujen arvontaan.

| Metodi | Selitys |
|:---|:---|
| NextInt(max) | Satunnainen kokonaisluku, joka on pienempi kuin annettu arvo, mutta suurempi kuin nolla- |
| NextInt(min, max) | Satunnainen kokonaisluku, joka on annetulla välillä. |
| NextIntWithProbabilities(todennäköisyydet) | Palauttaa yhden satunnaisen kokonaisluvun annettujen todennäköisyyksien mukaan. |
| NextDouble(min, max) | Satunnainen desimaaliluku annetulta väliltä. |
| NextDoubleArray(min, max, size) | Taulukko satunnaisia desimaalilukuja |
| NextDoubleArray(min, max, size, maxchange) | Taulukko satunnaisia desimaalilukuja, kahden peräkkäisen luvun suurimmalla sallitulla erotuksella. |

### NextIntWithProbabilities

Funktiolle voidaan antaa niin monta todennäköisyyttä kuin halutaan, jonka pohjalta se palauttaa jonkin luvun väliltä 0...n.

Esimerkiksi:

| Parametrit | Paluuarvo                       |
|:-----------|---------------------------------|
| 0.4        | 40% todennäköisyydellä 0, 60% 1 |
| 0.6, 0.2   | 60% 0, 20% 1, 20% 2             |
| 0.6, 0.4   | 60% 0, 40% 1                    |

## Satunnaisen vektorin luominen

Esimerkiksi, vektori, jonka pituus on vähintään 500, korkeintaan 1000 ja suunta satunnainen:

```csharp,ignore
Vector voima = RandomGen.NextVector(500, 1000);
```

Satunnaisen vektorin komponentteja voidaan myös tarkemmin rajoittaa.

```csharp,ignore
RandomGen.NextVector(minX, minY, maxX, maxY);
```

## Satunnainen kulma

Satunnaisia kulmia voidaan luoda samalla tavalla kuin vektoreitakin:

```csharp,ignore
Angle korkeintaan90 = RandomGen.NextAngle(Angle.FromDegrees(90));
Angle minMax = RandomGen.NextAngle(Angle.FromDegrees(90), Angle.FromDegrees(180));
```

## Satunnainen piste pelikentältä

Jos halutaan helposti satunnainen piste pelikentältä, siihen on olemassa Jypelissä valmis keino:

```csharp,ignore
Vector kentanPiste = Level.GetRandomPosition();
```

GetRandomPosition palauttaa satunnaisen kohdan kentän reunojen sisäpuolelta Vector-oliona.

Vastaavasti pelin olioiden paikkaa voi muuttaa `Position`-ominaisuudella. Siispä olion saa satunnaiseen paikkaan kenttää seuraavasti:

```csharp,ignore
olio.Position = Level.GetRandomPosition();
```

## Satunnainen vaihtoehto

RandomGen-luokan `SelectOne`-aliohjelmalla voidaan arpoa nopeasti yksi vaihtoehto useista annetuista. 

Joitain esimerkkejä `SelectOne`n käytöstä:

```csharp,ignore
string elain = RandomGen.SelectOne("kissa", "koira", "jänis");
```

```csharp,ignore
Color vari = RandomGen.SelectOne(Color.Black, Color.Red, Color.Green, Color.Blue);
```

```csharp,ignore
PhysicsObject pelaaja = RandomGen.SelectOne(pelaaja1, pelaaja2);
```

Jos saat tällaisen virheen

- The type arguments for method 'Jypeli.RandomGen.SelectOne<T>(params T\[\])' cannot be inferred from the usage. Try specifying the type arguments explicitly.

niin sen saa pois lisäämällä `SelectOne`-metodille tyyppimäärityksen kulmasuluissa tähän tyyliin:

```csharp,ignore
Shape muoto = RandomGen.SelectOne<Shape>(Shape.Circle, Shape.Rectangle);
```
