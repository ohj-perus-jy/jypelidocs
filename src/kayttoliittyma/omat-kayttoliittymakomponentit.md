# Omat käyttöliittymäkomponentit

Jos valmiista widgeteistä ei löydy sopivaa, täytyy tehdä uusi komponentti (eli widgetti). Se tapahtuu [perimällä uusi luokka](../oma-oliotyyppi/luokan-periminen.md) jostakin widgetistä (usein `Widget`-luokasta).

## Ohjainten asettaminen

Ohjaimet tulee lisätä vasta, kun olio on lisätty peliin. Muutoin olio kuuntelee ohjaustapahtumia, vaikka sitä ei näy missään, mikä on jokseenkin hämmentävää!

```csharp,ignore
public class OmaKomponentti : Widget
{
    public OmaKomponentti(double width, double height)
        : base(width, height)
    {
        AddedToGame += AlustaOhjaimet;
    }

    private void AlustaOhjaimet()
    {
        Game.Mouse.ListenOn(this, MouseButton.Left, ButtonState.Pressed, KasitteleKlikkaus, null).InContext(this);
        // ...
    }

    private void KasitteleKlikkaus()
    {
        // Mitä haluatkaan tapahtuvan, esimerkiksi:
        this.Color = Jypeli.RandomGen.NextColor();
    }
}
```

Ohjaimet tulisi asettaa komponentin omaan kontekstiin. Tällöin ohjainten kuuntelu toimii, jos komponentti asetetaan modaaliseksi. Modaalisuudella tarkoitetaan sitä, että kun komponentti (esim. ikkuna) on lisätty ruudulle, muita ruudulla olevia komponentteja ei voi silloin käyttää. Siten esimerkiksi nuolinäppäimistä liikuteltava pelihahmo ei liiku, vaikka näppäimiä painettaisiin esim. tekstinsyöttöruudussa.

Huomaa myös, että hiiren tai kosketusnäytön kuuntelu olisi yleensä toivottavaa tehdä `ListenOn`-kutsuilla:

```csharp,ignore
Game.Mouse.ListenOn(this, MouseButton.Left, ButtonState.Pressed, KasitteleKlikkaus, null).InContext(this);
```

Näin ohjaintapahtuma tulee vain kun hiiren kursori tai käyttäjän sormi on kyseisen olion päällä. Lisätietoja ohjainten kuuntelusta löydät [täältä](../ohjaimet/ohjainten-lisays.md).
