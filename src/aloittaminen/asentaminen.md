# Asennus

Tarvittavien työkalujen asentamiseksi voit seurata Jyväskylän yliopiston Ohjelmointi 1 -kurssin työkalujen asennusohjetta: <https://ohjelmointi1.it.jyu.fi/tyokalut/>

Tee ainakin seuraavat vaiheet oman käyttöjärjestelmän kohdasta em. työkalusivulta:

- [Valmistelu](https://ohjelmointi1.it.jyu.fi/tyokalut/#valmistelu)
- [.NET](https://ohjelmointi1.it.jyu.fi/tyokalut/#net)
- [JetBrains Rider](https://ohjelmointi1.it.jyu.fi/tyokalut/#jetbrains-rider)
- [Jypeli](https://ohjelmointi1.it.jyu.fi/tyokalut/#jypeli)

Jos teet Ohjelmointi 1 -kurssia, on suositeltavaa asentaa myös [Git-työkalut](https://ohjelmointi1.it.jyu.fi/tyokalut/#git), joita tarvitaan kurssin tehtävien palauttamiseen.

## Yliopiston koneilla: Jypelin projektimallit

Yliopiston koneilla Rider on jo asennettu, mutta Jypelin projektimallit
pitää asentaa kerran. Avaa komentorivi (Windowsissa Käynnistä-valikosta
*Command prompt*, Macilla *Terminal*), anna komento ja paina Enter:

```bash
dotnet new install Jypeli.Templates
```

Sen jälkeen voit sulkea komentorivin. Omalla koneella tämä on tehty jo
asennuksen yhteydessä.
