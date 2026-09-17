# Värinä

Värinällä voi tehostaa pelikokemusta. Huomaa, että värinä toimii vain Xbox 360 -ohjaimella ja puhelimessa.

## Xbox 360

Esimerkkikoodi:

```csharp,ignore
ControllerOne.Vibrate(0.5, 0.5, 0.0, 0.0, 0.1);
```

Parametrit ovat järjestyksessä:

- Vasemman moottorin teho
- Oikean moottorin teho
- Vasemman moottorin kiihdytys
- Oikean moottorin kiihdytys
- Värinän kesto

Vastaavasti `ControllerTwo.Vibrate` kakkosohjaimelle ja niin edelleen.

## Puhelin

Esimerkkikoodi:

```csharp,ignore
Phone.Vibrate(100);
```

Parametri määrittää, montako millisekuntia puhelin tärisee.
