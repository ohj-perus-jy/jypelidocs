# Oman oliotyypin luominen

Peleissä käytetään yleensä `PhysicsObject`-olioita, jolla on jo paljon ominaisuuksia, kuten massa ja kimmoisuus. Omassa pelissä voi tarvita muitakin ominaisuuksia. Ne saadaan mukaan [perimällä](https://trac.cc.jyu.fi/projects/npo/wiki/Olioista#Periytyminen) oman oliotyypin:

```csharp,ignore
class Vihu : PhysicsObject
{
    private IntMeter elamalaskuri = new IntMeter(3, 0, 3);
    public  IntMeter Elamalaskuri { get { return elamalaskuri; } }

    public Vihu(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
        elamalaskuri.LowerLimit += delegate { this.Destroy(); };
    }
}
```

Tässä `Vihu` on samanlainen kuin `PhysicsObject`, mutta sillä on lisäksi ominaisuus nimeltä `Elamalaskuri`, joka on kokonaislukulaskuri (`IntMeter`). Koska fysiikkaoliota luodessa tarvitsee kertoa leveys sekä korkeus, ne täytyy kertoa fysiikkaolion rakentajalle ylläolevalla `base`-merkinnällä.

Vihu-tyyppiset oliot luodaan samoin kuin `PhysicsObject`-oliot, nyt vain vaihdetaan `PhysicsObject`-sanan tilalle `Vihu`.

```csharp,ignore
Vihu hemmo = new Vihu(20, 20);
hemmo.X = -100;
hemmo.Y = -100;
        // ...
hemmo.Elamalaskuri.Value--;  // häviää automaattisesti jos elämät menee 0:ksi.
```

## Huomioita

- Uusi luokka ei saa olla minkään aliohjelman sisällä. Se voi (ja usein kannattaakin) olla muiden luokkien ulkopuolella:

```csharp,ignore
class Vihu : PhysicsObject
{
    // vihun ominaisuuksia...
}

public class Peli : PhysicsGame
{
    // Vanha tuttu Peli-luokka...
}
```

- Oman tyypin voi periä melkein mistä tahansa luokasta. Jos et tarvitse fysiikkaominaisuuksia, on järkevää periä GameObject-luokka:

```csharp,ignore
class Pelihahmo : GameObject
{
    public int Elamat { get; set; }

    public Pelihahmo(double leveys, double korkeus, double elamia)
        : base(leveys, korkeus)
    {
        Elamat = elamia;
    }
}
...
  Pelihahmo hemmo = new Pelihahmo(20, 20, 3); // koko 20,20, elämiä 3 kpl
...
  hemmo.Elamat--;
  if (hemmo.Elamat <= 0) ... // jotakin kun elämät loppuu
```

- Uusia ominaisuuksia voi olla montakin:

```csharp,ignore
class Pelihahmo : PhysicsObject
{
    public int Elamat { get; set; }
    public bool OnHidas { get; set; }
    public int Kengannumero { get; set; }
    public int Rahat { get; set; }
    public Vector Respauskoordinaatit { get; set; }

    public Pelihahmo(double leveys, double korkeus)
        : base(leveys, korkeus)
    {
       Elamat = 3;
       OnHidas = false;
       Kengannumero = 42;
       Rahat = 1000;
       Respauskoordinaatit = Vector.Zero;
    }
}
```
