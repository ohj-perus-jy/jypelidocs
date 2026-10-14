# Kuvat ja äänet mukaan projektiin

Jos haluat käyttää pelissä omia kuvia, ääniä tai tekstitiedostoja, ne täytyy
ensin liittää mukaan projektiin, jotta ohjelmointiympäristö tietää, mistä
kuva- ja äänitiedostot löytyvät. Tiedostot laitetaan projektin
`Content`-kansioon, josta ne kopioidaan pelin mukaan.

<details closed><summary>Mikäli peliprojektissasi ei ole vielä Content-kansiota, voit luoda sen näillä ohjeilla</summary>

Valitse käyttämäsi ohjelmointiympäristö. 

### [Rider](#tab/rider)

Napsauta *Explorer*-näkymässä (vasen reuna) projektia hiiren oikealla
painikkeella (Macilla Ctrl + napsautus) ja valitse *Add* › *Directory*. Anna
kansion nimeksi `Content` ja paina Enter. Kansio tulee näkyviin projektin
alle.

<animation scenes="images/sisallon-tuonti.js" scene="rider-kansio">

Riderin Explorer-näkymässä projektia napsautetaan hiiren oikealla, valitaan
*Add* › *Directory*, kirjoitetaan nimeksi `Content` ja painetaan OK. Kansio
ilmestyy projektin alle.

</animation>

***

### [VS Code](#tab/vscode)

Etsi *Explorer*-näkymästä (vasen reuna) pelin kansio eli se, jossa
`.csproj`-tiedosto on. Jos kansio on kiinni eikä sen sisältö näy, avaa se
napsauttamalla kansion nimeä. Napsauta sitten kansiota hiiren oikealla
painikkeella ja valitse *New Folder…*. Kirjoita kansion nimeksi `Content` ja
paina Enter.

<animation scenes="images/sisallon-tuonti.js" scene="vscode-kansio">

VS Coden Explorer-näkymässä pelin kansiota napsautetaan hiiren oikealla,
valitaan *New Folder…*, kirjoitetaan nimeksi `Content` ja painetaan Enter.
Kansio ilmestyy muiden kansioiden joukkoon.

</animation>

***

</details>

## Tiedostojen tuominen

### [Rider](#tab/rider)

Tallenna haluamasi kuva-, ääni- tai tekstitiedosto `Content`-kansioon
    Resurssienhallinnassa / Finderissa. Voit lisätä tiedoston myös Riderista
    käsin klikkaamalla `Content`-kansiota hiiren oikealla ja valitsemalla *Add*
    › *Existing Item*.

***

### [VS Code](#tab/vscode)

Tallenna haluamasi kuva-, ääni- tai tekstitiedosto `Content`-kansioon
    Resurssienhallinnassa / Finderissa. Voit myös vetää tiedoston
    *Explorer*-näkymässä `Content`-kansion päälle, jolloin VS Code kopioi
    sen sinne.

Jos saat virheilmoituksen, että tiedostoa ei löydy, avaa pelin projektitiedosto
(`.csproj`). Katso, että siinä on tällainen kohta:

```xml
<ItemGroup>
    <Content Include="Content/*.*">
        <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </Content>
</ItemGroup>
```

Jos kohtaa ei ole, lisää se ennen viimeistä riviä `</Project>`. Jos tiedostossa
    on sen sijaan rivejä `<None Update="Content\...">`, ne kopioivat vain pohjan
    omat tiedostot; korvaa ne yllä olevalla kohdalla.

***

## Tiedoston käyttö koodissa

Nyt voit käyttää lisäämääsi tiedostoa koodissasi, esimerkiksi
`norsu.Image = LoadImage("norsu");`. `LoadImage`-funktio hakee tiedostoja
automaattisesti `Content`-kansion sisältä.

`LoadImage`- ja `LoadSoundEffect`-funktioille ei tarvitse antaa
tiedostopäätettä, mutta se saa myös olla. Eli äskeisessä esimerkissä olisi
yhtä hyvin voitu kirjoittaa `LoadImage("norsu.png");`.
