# Uuden projektin luominen

Tässä ohjeessa kerrotaan, miten aloitat uuden projektin (eli pelin)
Riderissa. Ennen tätä Rider ja Jypeli pitää olla asennettuina, ks.
[Asennus](asentaminen.md).

*Projekti* on työtila, jossa käsitellään pelin koodia ja siihen liittyviä
kuva- ja äänitiedostoja yhtenä kokonaisuutena. Jokainen peli on oma
projektinsa.

## Projektin luominen Riderissa

Käynnistä Rider. Windowsissa se löytyy Käynnistä-valikosta tai työpöydän
pikakuvakkeesta ("JetBrains Rider"), Macilla Launchpadista tai Spotlightilla
(Cmd + välilyönti, kirjoita "Rider"). Aukeavassa ikkunassa:

1. Klikkaa **New Solution**.
2. Valitse vasemmalla olevasta listasta **Fysiikkapeli** (vieritä listaa
   alaspäin). Jos Fysiikkapeliä ei näy, projektimalleja ei ole asennettu;
   katso [asennusohje](asentaminen.md#yliopiston-koneilla-jypelin-projektimallit).
3. Kirjoita **Solution name** -kohtaan pelin nimi, esimerkiksi `Pong`. Käytä
   nimessä vain englanninkielisiä kirjaimia ja numeroita, ei välilyöntejä
   eikä ääkkösiä.
4. Valitse **Solution directory** -kohtaan kansio, johon peli tallennetaan,
   esimerkiksi `C:\Users\Käyttäjänimi\Koodiprojektit` (Macilla esimerkiksi
   `/Users/käyttäjänimi/Koodiprojektit`). **Yliopiston koneilla**
   kansioksi on annettava `C:\Mytemp\Omanimi`, jossa `Omanimi` on vaikkapa
   oma etunimesi.
5. Klikkaa **Create**.

## Kokeile, että peli käynnistyy

Klikkaa Riderin ikkunan yläreunassa olevaa vihreää kolmiota (**Run**). Jos
ruudulle aukeaa vaaleansininen ikkuna, projekti on luotu oikein. Ikkunan voi
sulkea sen oikeassa yläkulmassa olevasta rastista.

Peli on nyt tyhjä. Mitä projektissa on ja mihin koodi kirjoitetaan, kerrotaan
sivulla [Ensimmäinen peli](ensimmainen-peli.md).

## Muut projektimallit

Fysiikkapeli sopii useimpiin peleihin ja sitä käyttävät myös
[oppaat](../tutoriaalit/index.md). Listassa on muitakin malleja, esimerkiksi
tavallinen Peli ilman fysiikkamoottoria. Niistä kerrotaan sivulla
[Millaisia pelejä voin tehdä?](erilaisia-peleja.md).
