# Olion tuhoaminen

Olio tuhoutuu, kutsumalla sen metodia `Destroy`.

Esimerkki:

```csharp,ignore
vihollinen.Destroy();
```

Jos halutaan tietää onko olio tuhottu, se onnistuu näin:

```csharp,ignore
if (vihollinen.IsDestroyed)
{
    // ...
}
```

Joskus on hyödyllistä poistaa (`Remove`) olio ruudulta vain väliaikaisesti, kuitenkaan tuhoamatta sitä. Tällöin oliota ei tarvitse luoda uudestaan kun se lisätään takaisin ruudulle, ja säästetään resursseja. Turvallisempaa on kuitenkin käyttää `Destroy`-metodia.

Esimerkki:

```csharp,ignore
Remove(vihollinen);
```
