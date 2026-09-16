# Kaksi tai useampia pelaajia tasohyppelypelissä

Tässä esimerkissä tehdään kahden pelaajan tasohyppely välttäen turhaa toistoa aliohjelmissa.

Tehdään aluksi TasoHyppelyPeli-mallin mukainen projekti.

Poistetaan kenttäkuvasta 'N'-merkki ja lisää sinne merkit '1' ja '2' pelaajien aloituspaikoiksi.

Lisätään sitten toinen pelaaja luokkamuuttujaksi ensimmäisen pelaajan tapaan. Laitetaan tässä esimerkissä kummankin tekstuuriksi sama norsu.

```csharp,ignore
private PlatformCharacter pelaaja1;
private PlatformCharacter pelaaja2;
private Image pelaajan1Kuva = LoadImage("norsu.png");
private Image pelaajan2Kuva = LoadImage("norsu.png");
```

Muokataan sitten LuoKentta-aliohjelmaa. Luodaan pelaaja-oliot jo tässä, jotta ne voidaan välittää argumentteina LisaaPelaaja-aliohjelmalle. Välitetään argumenttina myös pelaajan kuva.

```csharp,ignore
pelaaja1 = new PlatformCharacter(RUUDUN_KOKO, RUUDUN_KOKO);
pelaaja2 = new PlatformCharacter(RUUDUN_KOKO, RUUDUN_KOKO);
kentta.SetTileMethod('1', LisaaPelaaja, pelaaja1, pelaajan1Kuva);
kentta.SetTileMethod('2', LisaaPelaaja, pelaaja2, pelaajan2Kuva);
```

Nyt LisaaPelaaja-aliohjelma vaatii muutoksia.

```csharp,ignore
private void LisaaPelaaja(Vector paikka, double leveys, double korkeus, PlatformCharacter pelaaja, Image kuva)
{
  pelaaja.Position = paikka;
  pelaaja.Mass = 4.0;
  pelaaja.Image = kuva;
  AddCollisionHandler(pelaaja, "tahti", TormaaTahteen);
  Add(pelaaja);
}
```

Huomaa erityisesti, että tässä aliohjelmassa ei enää luoda pelaajaoliota (`new PlatformCharacter…`), vaan ainoastaan asetetaan parametrina saadun olion ominaisuuksien arvoja, ja lisätään olio lopuksi kentälle.

Tehdään lopuksi vielä kontrollit toiselle pelaajalle.

```csharp,ignore
Keyboard.Listen(Key.A, ButtonState.Down, Liikuta, "Liikkuu vasemmalle", pelaaja2, -NOPEUS);
Keyboard.Listen(Key.D, ButtonState.Down, Liikuta, "Liikkuu vasemmalle", pelaaja2, NOPEUS);
Keyboard.Listen(Key.W, ButtonState.Pressed, Hyppaa, "Pelaaja hyppää", pelaaja2, HYPPYNOPEUS);
```

Valmis koodi löytyy täältä:

Ks. <https://gitlab.jyu.fi/tie/ohj1/jypeli-esimerkit/kaksi-pelaajaa/-/blob/main/KaksiPelaajaa.cs?ref_type=heads>
