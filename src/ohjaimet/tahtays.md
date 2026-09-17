# Tähtäys

Useimmissa peleissä, joissa on aseita, täytyy niillä myös tähdätä. Tässä ohjeessa neuvotaan, kuinka teet tähtäämisen hiirellä, Xbox 360 -ohjaimella sekä näppäimistöllä.

## Hiirellä tähtääminen

Kun olet luonut peliisi pelihahmon ja tälle aseen ([aseiden luonti](../fysiikka/aseiden-lisaaminen.md)), voit toteuttaa hiirellä tähtäämisen. Hiirellä tähtääminen toteutetaan kuuntelemalla hiiren liikettä ja vaihtamalla aseen kulmaa aina, kun hiiri liikkuu.

### Kuuntelijan luonti

Luodaan siis ensiksi kuuntelija hiiren liikkeelle.

```csharp,ignore
Mouse.ListenMovement(0.1, Tahtaa, "Tähtää aseella");
```

Tässä parametreina annettavat asiat ovat:

- `0.1` - Kuinka monta yksikköä hiiren täytyy liikkua, että kuuntelija aktivoituu
- `Tahtaa` - Aliohjelma, joka suoritetaan, kun kuuntelija aktivoituu
- `"Tähtää aseella"` - Teksti, joka näytetään, kun pelissä pyydetään näppäinohjeita

### Aliohjelman tekeminen

Kun kuuntelija on tehty, luodaan aliohjelma, joka suoritetaan aina, kun hiiri liikkuu.

```csharp,ignore
void Tahtaa()
{
    Vector suunta = (Mouse.PositionOnWorld - pelaaja1.Weapon.AbsolutePosition).Normalize();
    pelaaja1.Weapon.Angle = suunta.Angle;
}
```

Aliohjelmassa määritellään uusi vektori `suunta`, johon lasketaan pelaajan aseen ja hiiren välinen suunta.

Tarkemmin, `Mouse.PositionOnWorld` antaa meille hiiren paikan pelimaailmassa ja `pelaaja1.Weapon.AbsolutePosition` antaa pelaajan aseen sijainnin. Lopuksi näiden kahden vektorin erotukselle tehdään normalisointi, eli vektori muutetaan yhden yksikön pituiseksi.

Kun meillä on yhden yksikön mittainen vektori, saadaan siitä helposti kulma, `suunta.Angle`, joka asetetaan aseen kulmaksi. Näin ase saadaan osoittamaan haluttuun suuntaan.

## Näppäimistöllä tähtääminen

Mikäli hiirellä tähtääminen ei ole sopiva vaihtoehto pelillesi (esim. useamman pelaajan peli) etkä halua käyttää peliohjaimia, voi tähtäämisen toteuttaa myös näppäimistöllä. Näppäimistöllä tähtäämisen toteuttaminen on järkevää esimerkiksi kahden pelaajan tankkipelissä, jossa tankin tykkiä täytyy liikutella vain ylös ja alas.

Tässä ohjeessa toteutetaan yhdelle pelaajalle tankin tykin liikuttaminen.

### Näppäinkuuntelijoiden tekeminen

Tehdään näppäinkuuntelijat nuolinäppäimille ylös ja alas. Ylös-näppäimellä tankin piippu liikkuu ylös ja alas-näppäimellä vastaavasti alas.

```csharp,ignore
Keyboard.Listen(Key.Up, ButtonState.Down, KaannaTykkia, "Kääntää tankin tykkiä ylös",
                pelaaja1Tykki, Angle.FromDegrees(1));
Keyboard.Listen(Key.Down, ButtonState.Down, KaannaTykkia, "Kääntää tankin tykkiä alas",
                pelaaja1Tykki, Angle.FromDegrees(-1));
```

Tehdään molemmille napeille lähes identtiset kuuntelijat. Ainoat parametrit, jotka muuttuvat, ovat itse näppäimet sekä kulma, jolla tykkiä käännetään.

Kuuntelijalle annettavat parametrit ovat siis:

- `Key.Up`/`Key.Down` - Nappi, jota kuunnellaan
- `ButtonState.Down` - Napin tila. Tässä tapauksessa kuuntelija aktivoituu aina, kun nappi on alhaalla.
- `KaannaTykkia` - Aliohjelma, joka suoritetaan, kun kuuntelija aktivoituu
- `"Kääntää tankin tykkiä ylös"` - Teksti, joka näytetään, kun pelissä pyydetään näppäinohjeita
- `pelaaja1Tykki` - Tykki, jota käännetään
- `Angle.FromDegrees(1/-1)` - Kulma, jolla tykkiä käännetään

### Aliohjelman tekeminen

Seuraavaksi toteutetaan kuuntelijan yhteydessä käytettävä aliohjelma

```csharp,ignore
void KaannaTykkia(Weapon tykki, Angle kulma)
{
   tykki.Angle += kulma;
}
```

Aliohjelma on hyvin yksinkertainen. Siinä vain käännetään parametrina annetun tykin (`tykki`) kulmaa parametrina annetun kulman (`kulma`) verran.

## Tähtääminen toista hahmoa kohti

Joissain tilanteissa halutaan ampua kohti jotain tiettyä toista oliota.

Ampumista varten voidaan laskea **suuntavektori**. Suuntavektori on ikään kuin nuoli, joka osoittaa toisesta oliosta toiseen.

Tässä tilanne, jossa olion `pahis` on tarkoitus ampua oliota `hyvis`:

```csharp,ignore
Vector suunta = (hyvis.Position - pahis.Position).Normalize();
```

Suunnasta voidaan laskea kulma, jolla `pahis` osoittaa vihollista kohti:

```csharp,ignore
pahis.Angle = suunta.Angle;
```

Suuntaa voidaan käyttää hyväksi esim. kappaleiden heittämiseksi kohteen suuntaan:

```csharp,ignore
kranaatti.Hit(suunta * 1000);
```

Jos esimerkiksi lisätään ampuminen viholliselle, jota pelaaja ei itse ohjaa, apua voi olla lisäksi sivusta:

- [Ajastinten käyttö](../tapahtumat/ajastimet.md)
