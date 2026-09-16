# Miten voin ryhmitellä ohjaimia

Jos pelissä on esimerkiksi useita pelaajia tai pelitilanteita, voi olla järkevää jaotella ohjaimia omiin ryhmiinsä. Ryhmiteltyjä ohjaimia voidaan ottaa käyttöön ja poistaa käytöstä (tai kokonaan pelistä) yhdellä koodirivillä.

## Ohjainryhmä (ListenContext) ja sen luominen

Ohjainryhmä on tyypiltään `ListenContext`. Yleensä ryhmä on hyvä asettaa peliin attribuutiksi (class-sanan ja aaltosulun jälkeen) jotta siihen pääsee kiinni kaikista aliohjelmista.

```csharp,ignore
public class Peli : PhysicsGame
{
   ListenContext ohjaimet;
```

Ryhmä voidaan alustaa ennen ohjainten kuuntelua (aliohjelman sisällä!) seuraavasti

```csharp,ignore
ohjaimet = ControlContext.CreateSubcontext();
```

Sen jälkeen ohjaimet voidaan lisätä kirjoittamalla kuuntelurivin perään `.InContext` ja sille parametriksi luotu ryhmän nimi. Esimerkiksi

```csharp,ignore
pelaajan1Kontrollit = this.ControlContext.CreateSubcontext();
Keyboard.Listen(...).InContext(pelaajan1Kontrollit);
Keyboard.Listen(...).InContext(pelaajan1Kontrollit);
Mouse.Listen(...).InContext(pelaajan1Kontrollit);
```

## Ohjainten poistaminen käytöstä

Ohjainryhmän voi poistaa väliaikaisesti käytöstä sen `Disable`-metodilla.

```csharp,ignore
// poistaa pelaajan 1 kontrollit käytöstä
pelaajan1Kontrollit.Disable();
```

Kontrollit saa vastaavasti takaisin käyttöön `Enable`-metodilla.

```csharp,ignore
// pelaajan 1 kontrollit takaisin käyttöön
pelaajan1Kontrollit.Enable();
```

Jos kontrollit halutaan poistaa kokonaan (esimerkiksi jos ne halutaan luoda uudelleen), voidaan sanoa

```csharp,ignore
// pelaajan 1 kontrollit pois kokonaan
pelaajan1Kontrollit.Destroy();
```

Huomaa, että tuhottua kontekstia (ryhmää) ei voi enää käyttää uudelleen ennen kuin se on alustettu uudelleen (CreateSubcontext)!

## Aliryhmien luominen

Kontrolliryhmiä on myös mahdollista luoda toistensa sisälle.

```csharp,ignore
pelaajienKontrollit = ControlContext.CreateSubcontext();
pelaajan1Kontrollit = pelaajienKontrollit.CreateSubcontext();
pelaajan2Kontrollit = pelaajienKontrollit.CreateSubcontext();
pelaajan1Ampuminen = pelaajan1Kontrollit.CreateSubcontext();
pelaajan2Ampuminen = pelaajan2Kontrollit.CreateSubcontext();
```

Jos ryhmät piirrettäisiin nyt puurakenteeksi (hierarkia), se näyttäisi tältä:

![](images/kontekstihierarkia.png)

Huomaa, että `ControlContext` on aina hierarkiassa ylimpänä. Se on pelin ns. pääkonteksti. Metodit vaikuttavat aina alaspäin puussa, eli esimerkiksi

```csharp,ignore
pelaajan1Kontrollit.Disable();
```

poistaa käytöstä myös ryhmän `pelaajan1Ampuminen`.

## Ikkunoihin liittyvät ohjainryhmät

Jokaisella ikkunalla on myös `ControlContext` niin kuin pelilläkin. Näin vain päällimmäisellä ikkunalla on ns. fokus eli sen alla olevien ikkunoiden (tai pelin) ohjaimet eivät toimi ennen kuin ikkuna on suljettu.

Ikkunalle voi lisätä vastaavasti ohjaimia joko yksitellen

```csharp,ignore
Keyboard.Listen(...).InContext(ikkuna);
```

tai uutena ryhmänä

```csharp,ignore
ListenContext ryhma = ikkuna.ContolContext.CreateSubcontext();
Keyboard.Listen(...).InContext(ryhma);
Keyboard.Listen(...).InContext(ryhma);
```
