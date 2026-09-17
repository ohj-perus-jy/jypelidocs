# Kuvan läpinäkyvyys

Näin saat tehtyä [Paint.NET](https://www.getpaint.net/)-ohjelmalla kuvaasi läpinäkyviä osia ja tallennettua ne PNG-formaatissa.

Luo uusi kuva. Ota heti alussa huomioon kuvan koko, eli millaisella tarkkuudella haluat kuvan olevan lopullisessa pelissä. Tässä kuvan koko on 64 × 64 pikseliä, mikä riittää pienelle pelihahmolle. Piirrä sitten haluamasi kuva.

![](images/PaintPallo.png)

Kun olet piirtänyt, aletaan poistaa kuvasta niitä osia, jotka halutaan läpinäkyviksi. Valitse taikasauvatyökalu (Magic Wand) ja klikkaa (yhden kerran) sille alueelle, jonka haluat läpinäkyväksi (tasainen väri lähtee helpoiten).

Jos haluat valita useita alueita, pidä Shift-näppäin pohjassa ja tee monta valintaa.

![](images/PaintValittu.png)

Kun valinta on valmis, klikkaa Edit → Erase selection tai paina Del-näppäintä.

![](images/PaintErase.png)

Läpinäkyvä alue näkyy nyt "shakkiruudukkona".

![](images/PaintLapinakyva.png)

Voit toki vielä jatkaa hahmon piirtämistä ruudulliselle alueellekin. Mutta edelleen – vain se alue, joka on ruudullinen, on läpinäkyvää aluetta lopullisessa kuvassa.

![](images/PaintNaama.png)

Kun olet valmis, tallenna kuva ja valitse tallennusmuodoksi PNG.

![](images/PaintTallenna.png)

Bit Depthiin on yleensä parasta laittaa 32-bit.

![](images/PaintBitDepth.png)

Seuraavaksi katso, kuinka [kuva tuodaan peliin ja lisätään oliolle](../grafiikka/kuvat.md#kuvan-lataaminen-tiedostosta-ja-asettaminen-oliolle).
