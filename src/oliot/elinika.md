# Elinikä

Oliolle voi määrittää ajan, jonka se on kentällä ennen tuhoutumistaan, käyttämällä sen ominaisuutta `LifetimeLeft`.

Esimerkki viiden sekunnin eliniästä:

```csharp,ignore
olio.LifetimeLeft = TimeSpan.FromSeconds( 5.0 );
```

Muita elinikään viittaavia ominaisuuksia:

- `Lifetime` kertoo olion senhetkisen iän eli ajan, joka on kulunut olion luomisesta.
- `MaximumLifetime` kertoo olion suurimman sallitun iän: olio tuhoutuu, kun `Lifetime` ylittää sen. Aika lasketaan siis olion luomisesta, ei pelin alusta. `LifetimeLeft`-ominaisuuden muuttaminen muuttaa myös tätä.
