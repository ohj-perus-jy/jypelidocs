# Pause

Pelin saa pysäytettyä väliaikaisesti kahdella tavalla. Voit asettaa suoraan pelin ominaisuuden **IsPaused**

```csharp,ignore
IsPaused = true;
```

tai voit käyttää aliohjelmaa **Pause**

```csharp,ignore
Pause();
```

Aliohjelman kutsuminen uudelleen jatkaa peliä. Näin ollen voit tehdä esimerkiksi näppäimen, jolla pelin voi keskeyttää:

```csharp,ignore
Keyboard.Listen(Key.P, ButtonState.Pressed, Pause, "Pysäyttää pelin");
```

Pause-tilassa ollessaan pelin fysiikka, ajastimet ym. eivät päivity. Ohjaimet ja näytöt kuitenkin toimivat normaalisti.

## Pause-valikon luonti

Pause-näppäimeen voi toki liittää myös esimerkiksi valikon esiintulon:

```csharp,ignore
    pausevalikko = new MultiSelectWindow("Pause", "Aloita alusta", "Lopeta");

    // Tämän oikeanlainen toiminta vaatii hieman kikkailua, sillä
    // näppäimenkuuntelijat lakkaavat toimimasta kun peli on pausella.
    pausevalikko.Closed += (handler) => Pauseta();
    //pausevalikko.AddItemHandler(...);

    Keyboard.Listen(Key.Escape, ButtonState.Pressed, Pauseta, "Pysäyttää pelin");
}
...

private void Pauseta()
{
    if (IsPaused)
    {
        Remove(pausevalikko);
    }
    else
    {
        Add(pausevalikko);
    }
    Pause();
}
```

Katso tarkemmat ohjeet valikon luontiin siihen liittyvältä sivulta: [Valikko](../kayttoliittyma/valikko.md)
