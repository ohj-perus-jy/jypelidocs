# Miten määritän oliolle eliniän?

Oliolle voi määrittää ajan, jonka se on kentällä ennen sen tuhoutumista käyttämällä sen ominaisuutta `LifetimeLeft`.

Esimerkki viiden sekunnin eliniästä:

```csharp,ignore
olio.LifetimeLeft = TimeSpan.FromSeconds( 5.0 );
```

Muita elinikään viittaavia ominaisuuksia:

- `Lifetime` kertoo olion senhetkisen eliniän
- `MaximumLifetime` kertoo ajanhetken pelin alusta jolloin olio kuolee. `LifetimeLeft`-ominaisuuden muuttaminen muuttaa myös tätä.
