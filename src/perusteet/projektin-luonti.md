# Uuden projektin luominen

Tässä ohjeessa kerrotaan, miten aloitat uuden projektin (eli pelin)
Riderissa. Ennen tätä Rider ja Jypeli pitää olla asennettuina, ks.
[Asennus](asentaminen.md).

*Projekti* on työtila, jossa käsitellään pelin koodia ja siihen liittyviä
kuva- ja äänitiedostoja yhtenä kokonaisuutena. Jokainen peli on oma
projektinsa.

## Yliopiston koneilla: Jypelin projektimallit

Yliopiston koneilla Rider on jo asennettu, mutta Jypelin projektimallit
pitää asentaa kerran. Avaa Käynnistä-valikosta *Command prompt*, anna komento
ja paina Enter:

```bash
dotnet new install Jypeli.Templates
```

Sen jälkeen voit sulkea Command promptin. Omalla koneella tämä on tehty jo
asennuksen yhteydessä.

## Projektin luominen Riderissa

Käynnistä Rider työpöydän pikakuvakkeesta tai Käynnistä-valikosta
("JetBrains Rider"). Aukeavassa ikkunassa:

1. Klikkaa **New Solution**.
2. Valitse vasemmalla olevasta listasta **Fysiikkapeli** (vieritä listaa
   alaspäin). Jos Fysiikkapeliä ei näy, projektimalleja ei ole asennettu;
   palaa edelliseen kohtaan tai [asennusohjeeseen](asentaminen.md).
3. Kirjoita **Solution name** -kohtaan pelin nimi, esimerkiksi `Pong`. Käytä
   nimessä vain englanninkielisiä kirjaimia ja numeroita, ei välilyöntejä
   eikä ääkkösiä.
4. Valitse **Solution directory** -kohtaan kansio, johon peli tallennetaan,
   esimerkiksi `C:\Users\Käyttäjänimi\Koodiprojektit`. **Yliopiston koneilla**
   kansioksi on annettava `C:\Mytemp\Omanimi`, jossa `Omanimi` on vaikkapa
   oma etunimesi.
5. Klikkaa **Create**.

## Kokeile, että peli käynnistyy

Paina **Ctrl+F5**. Jos ruudulle aukeaa vaaleansininen ikkuna, projekti on
luotu oikein. Ikkunan voi sulkea Esc-näppäimellä.

Peli on nyt tyhjä. Mitä projektissa on ja mihin koodi kirjoitetaan, kerrotaan
sivulla [Ensimmäinen peli](ensimmainen-peli.md).

## Muut projektimallit

Fysiikkapeli sopii useimpiin peleihin ja sitä käyttävät myös
[oppaat](../mallit/index.md). Listassa on muitakin malleja, esimerkiksi
tavallinen Peli ilman fysiikkamoottoria. Niistä kerrotaan sivulla
[Millaisia pelejä voin tehdä?](erilaisia-peleja.md).
