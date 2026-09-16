# Muita tapahtumia

## PhysicsObject.Destroyed

Peliolion tuhoutumisen yhteydessä kutsutaan `Destroyed`-tapahtuman käsittelijää. Alla olevassa esimerkissä vihu lakkaa heittelemästä esineitä kun se tuhoutuu.

```csharp,ignore
{
  PhysicsObject vihu = new PhysicsObject(...);
  // ...
  Timer heittoajastin = new Timer();
  heittoajastin.Interval = 2.0;
  heittoajastin.Timeout += HeitaKappale;
  vihu.Destroyed += heittoajastin.Stop;
}
```

`Destroyed`-tapahtuman käsittelijä tulee olla parametriton `void`-metodi. Jos on tarvetta tehdä monimutkaisempaa logiikkaa tuhoutumisen yhteydessä (esimerkiksi kutsua parametrillista aliohjelmaa), kannattaa käyttää delegate-avainsanaa.

```csharp,ignore
vihu.Destroyed += delegate { // omaa koodia... };
```
