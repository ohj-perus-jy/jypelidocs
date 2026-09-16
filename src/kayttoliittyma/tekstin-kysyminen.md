# Tekstin kysyminen pelaajalta

Jypeli sisältää valmiin luokan `InputWindow` tekstin kysymiseen pelaajalta. Luokkaa voidaan käyttää esimerkiksi pelaajan nimen tai oven salasanan syöttämiseen. Huomaa, että parhaiden pisteiden listaa varten on oma luokka: [HighScoreWindow](parhaiden-pisteiden-lista.md).

## Ikkunan luominen

Kysymysikkuna luodaan antamalla sille otsikko ja kysymys. Tapahtumalle `TextEntered` annetaan tapahtumankäsittelijä joka suoritetaan kun teksti on syötetty. Lopuksi ikkuna näytetään ruudulla lisäämällä se peliin.

```csharp,ignore
InputWindow kysymysikkuna = new InputWindow("Vastaa kysymykseen");
kysymysikkuna.TextEntered += KasitteleSyote;
Add(kysymysikkuna);
```

Ikkunan värejä voi muuttaa seuraavasti:

```csharp,ignore
InputWindow kysymysikkuna = new InputWindow("Otsikko tähän");

// Ikkunan taustaväri
kysymysikkuna.ActiveColor = Color.DarkGray;

// Otsikon värit
kysymysikkuna.Message.Color = Color.DarkGray; // Tausta
kysymysikkuna.Message.TextColor = Color.White; // Teksti

// Kirjoituslaatikon värit
kysymysikkuna.InputBox.Color = Color.DarkGray; // Tausta
kysymysikkuna.InputBox.TextColor = Color.White; // Teksti

// Napin värit
kysymysikkuna.OKButton.Color = Color.DarkGray; // Tausta
kysymysikkuna.OKButton.TextColor = Color.White; // Teksti

Add(kysymysikkuna);
```

## Tapahtumankäsittelijä

Tapahtumankäsittelijäaliohjelma on seuraavaa muotoa:

```csharp,ignore
void KasitteleSyote(InputWindow ikkuna)
{
    string vastaus = ikkuna.InputBox.Text;
    // tehdään jotain vastauksella
}
```
