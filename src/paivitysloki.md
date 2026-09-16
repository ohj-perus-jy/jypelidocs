# Jypelin päivityshistoria

Alla on eritelty Jypelin ja fysiikkamoottorien päivitykset erikseen, sillä ne (useimmiten) voidaan päivittää toisistaan riippumatta.

Kaikkia muutoksia ei ole välttämättä lueteltu, jos ne ovat käyttäjälle suoraan näkymättömiä.

Vanhempienkin päivitysten muutoslista tulee kun se jaksetaan tänne naputella :)

## Jypeli

### 11.3.7 (13.4.2023)

- Korjattu `ClearAll` kaatoi pelin jos fysiikkakappaleella oli toinen fysiikkakappale lapsioliona.
- Korjattu Android projektin kaatuminen puutteellisen käyttöoikeuden takia joillain uusilla Android versiolla.
- Korjattu `Touch.PreviousPositionOnWorld` & `PreviousPositionOnScreen`.
- Tekstin piirto toteutettu erilailla, suorituskyvyn pitäisi olla huomattavasti parempi erityisesti mobiililaitteilla.
- Päivitetty Jypelin alla käytettyjä kirjastoja.

### 11.3.6 (14.3.2023)

- Korjattu samat ääniongelmat Androidille.
- Korjattu joissain tilanteissa kosketusnäytön tapahtumat eivät toimineet oikein.

### 11.3.5 ( 10.11.2022)

- Korjattu Joissain harvinaisissa tilanteissa wav-tiedoston toiston alussa kuuluva naksahdus.
- Lisätty `MediaPlayer.Play(SoundEffect)`

### 11.3.4 (28.10.2022)

- Korjattu `Image.GetDataUInt` ja `GetDataUintAA` antama väärä tavujärjestys.

### 11.3.3 (26.10.2022)

- Korjattu `ParticleSystem.AddEffect` kulman väärä käyttäytyminen.
- Otettu käyttöön reunojenpehmennys `Canvas.DrawLine`n piirtämälle viivalle.

### 11.3.2 (10.10.2022)

- Korjattu pelin kaatuminen joskus PlatformCharacterin tuhoamisen jälkeen.
- Korjattu `Level.BackgroundImage` ei päivittynyt jos sen sisältöä muokattiin esim. `SetData`n avulla.
- Lisätty `Image.Rescale`

### 11.3.1 (18.9.2022)

- Korjattu kaatuminen TIMissä ajettaessa, jos yritettiin toistaa ääntä.

### 11.3.0 (30.8.2022)

- Korjattu `PhysicsObjectin` koon muuttaminen ei toiminut jos kappaletta ei oltu vielä lisätty peliin.
- Päivitetty Silk.NET (kirjasto joka hoitaa mm. peli-ikkunan luonnin) versioon 2.16

### 11.2.2 (7.6.2022)

- Korjattu `Slider`in toiminta.

### 11.2.1 (6.6.2022)

- Korjattu `Canvas.DrawImage`
- Korjattu Android projektin kääntäminen Release-moodissa ei aina onnistunut.

#### 11.2.0 (25.5.2022)

- Korjattu `PhoneBackButton`
- Korjattu `Mouse.IsCursorOn`
- Korjattu käyttöoikeuksien kysyminen Androidilla.
- Korjattu kaatuminen jos kiihtyvyysanturia yritettiin käynnistää kun se oli jo päällä.
- Korjattu `ClearAll` ei poistanut `Keyboard.TextInput` -tapahtumakuuntelijoita.
- Korjattu Debug-näkymän elementtien väärä sijainti, jos näkymä avattiin muuttamalla `DebugScreenVisible`-muuttujan arvoa.
- Korjattu `Touch.PositionOnScreen`
- Korjattu `Slider` ja `PushButton` ei toiminut oikein kosketusnäytöllä.
- Korjattu `MessageDisplay`n viestien poistuminen ei toiminut joissain äärimmäisen harvinaisissa tilanteissa.
- Korjattu `Camera.ScreenToWorld` ja `WorldToScreen` evät toimineeet Jypelin ruutukoordinaattijärjestelmässä.
- Korjattu `Color.Mix`
- Lisätty `GameObject.FadeColorTo`.
- Lisätty `UpdatesPerSecond`-kenttä.
- Lisätty äänen toistaminen Androidilla
- Lisätty monen samanaikaisen kosketuksen tuki Androidilla.
- `Shape.FromImage` luo nyt muotoja jotka voidaan täyttää värillä.
- Muutettu Android projektien rakennetta.
- Asetettu `FixedTimeStep` oletuksena päälle.

### 11.1.5 (25.3.2022)

- Korjattu lapsiolioiden sijaintien päivittyminen joissain erikoistapauksissa.
- Korjattu kappaleen piirtyminen väärin jos sen muodon oli normalisoimaton.

### 11.1.4 (8.3.2022)

- Korjattu kaatuminen joissain tilanteissa, kun pelialueella oli hyvin paljon samanlaisia kappaleita.
- Korjattu `GetObjectsAt` oli hyvin epätarkka sijaintien suhteen.
- Korjattu `GetObjects*`-metodit eivät ottaneet huomioon kappaleita jotka ollaan juuri lisäämässä kentälle.
  - Korjaa samalla mm. `Level.GetRandomFreePosition` toiminnan luotaessa silmukassa useita kappaleita.
- Korjattu `PlatformCharacterin` ase ei kääntynyt oikein hahmon kääntyessä.
- Korjattu `PlatformCharacterin` tila ei joissain tilanteissa päivittynyt tippumisen jälkeen.
- Korjattu `Image.CreateStarSky` kaatuminen jos pyydetty kuva ei ollut neliö.
- Korjattu `Image.DrawTextOnImage`.
- Lisätty `PlatformCharacter.Visualise` näyttämään hahmon tilan ja törmäykset debuggausta varten.

### 11.1.3 (2.3.2022)

- Lisätty mahdollisuus palauttaa oskilloiva kappale sen alkuperäiseen sijaintiin, sekä lopettaa oskillointi viiveellä vasta kun kappale on sen alkuperäisellä paikalla.
  - `ClearOscillations(returnToOriginalPosition, stopGradually)`
- Lisätty mahdollisuus kysyä suurinta näytönohjaimen sallimaa tekstuurin kokoa, `GraphicsDevice.GetMaxTextureSize();`.
- Pieni suorituskykyparannus lapsiolioiden sijainnin päivitykseen.

### 11.1.2 (22.2.2022)

- Korjattu `MasterVolume` oli oletuksena 0.
- Korjattu Fysiikkakappaleiden lapsioliot lisättiin kahdesti moottorille
- Pieniä suorituskykyoptimointeja.

### 11.1.1 (18.2.2022)

- Korjattu `Mouse.PositionOnScreen`.
- Korjattu `SoundEffect` ei noudattunut `MasterVolume`-asetusta.
- Korjattu omien fonttien lataaminen ja niiden efektien muuttaminen.
- Korjattu Tilemapin lataus tekstitiedostosta Androidilla.
- Korjattu fysiikkakappaleen ominaisuuksien muuttaminen sen jälkeen, kun se oli poistettu pelistä.
- Korjattu fysiikkakappaleiden lisääminen takaisin peliin poistamisen jälkeen.
- Lisätty `WindowSizeChanged`-tapahtuma.
- Lisätty `Keyboard.IsKeyDown`.

### 11.1.0 (7.2.2022)

- Korjattu kaatuminen jos räjähdys laitettiin tismalleen samaan paikkaan kuin kappale.
- Useampia lapsiolioihin liittyviä korjauksia
- Korjattu `ProgressBar`in ja `BarGauge`n piirto jos niitä oli pyöritetty.
- Korjattu `Level.Background.TileToLevel`.
- Korjattu tankin toiminta
- Korjattu äänien hajoaminen jos niitä oli toistettu paljon.
- `MathHelper` käyttää nyt kaikkialla doubleja floattien sijaan.
- Lisättiin takaisin `Color.NextColor(object)`.
- Lisätty jonkin verran puuttuvaa dokumentaatiota.

### 11.0.6 (27.1.2022)

- Korjattu nullPointer jos ääniä yritettiin ladata ennen Beginin kutsumista.

### 11.0.5 (27.1.2022)

- Korjattu useita komentoriviajamiseen liittyviä ongelmia.
  - Disabloidaan äänet headless-moodissa.
  - Korjattu `--framesToRun` asetus ei laskenut ensimmäistä framea.
- Korjattu ikkunan virheellinen koko suuren DPI:n näytöillä.
- Korjattu äänien disabloituminen, jos Jypelin kirjastoissa ei ollut mukana laitteelle soveltuvaa OpenAL-kirjastoa, mutta laitteella oli OpenAL asennettuna.
- M1 koneilla Jypelin pitäisi nyt toimia.

### 11.0.4 (21.1.2022)

- Lisätty mahdollisuus muuttaa hiiren kuvaa ja tyyliä. `Mouse.SetCursorImage`, sekä `Mouse.MouseCursor`.
- Päivitetty Silk.NET, korjaa mm. kaatumisen jos projektin nimessä (eli siten myös ikkunan otsikkopalkissa) oli ääkkösiä.

### 11.0.3 (18.1.2022)

- Lisätty takaisin muutamat puuttuvat näppäinkontrollit joiltain widgeteiltä, kuten `MultiSelectWindow`in käyttö nuolilla.

### 11.0.2 (14.1.2022)

- Heitetään poikkeus jos kappaleen koko asetetaan negatiiviseksi.
- `Controller.Listen` toimii nyt myös analogisille liipaisinkytkimille. Painallus rekisteröityy kun liipaisin on puolivälissä.
- Korjattu dokumentaation puuttuminen julkaistusta paketista.

### 11.0.1 (6.1.2022)

- Korjattu kaatuminen, jos ääntä yritettiin ladata ennen `Begin`in kutsumista.

### 11.0.0 (6.1.2022)

- Huomattava päivitys. Jypeli ei enää rakennu MonoGamen päälle, vaan alustana on Silk.NET ja OpenGL.
- Päivitetty käyttämään `.NET 6`
- Jypeli käännetään nyt myös `.NET6-Android`ille, joten samaa pakettia voidaan käyttää myös mobiiliprojekteissa.
- Alustava toteutus uudelle `MathHelper`-luokalle.

### 10.1.6 (1.11.2021)

- Korjattu virheellinen merkkijonovertailu `GetObjects*`-metodeissa.
- Debug näkymä (F12) piirtää nyt myös liitoksien sijainnit.

### 10.1.5 (15.10.2021)

- Korjattu ensimmäisen framen tallentamattomuus ruutua kuvatessa.
- Lisätty fysiikkakappaleille `CollisionIgnoreFunc`, jolla voidaan päättää tapahtuuko törmäystä.

### 10.1.4 (27.9.2021)

- Korjattu NullPointer sisäisistä resursseista ääntä toistettaessa.

### 10.1.3 (27.9.2021)

- Korjattu kuvan lataamiseen TIM-ympäristössä liittyvä käyttöoikeusbugi
- Korjattu Jypelin sisäisistä resursseista ääntä toistettaessa aiheutunut kaatuminen, jos äänilaitetta ei ollut saatavilla.

### 10.1.2 (14.9.2021)

- Korjattu pelin pyöriminen yhden päivityksen verran liian vähän, jos pyörimisaika oli asetettu.
- Lisätty vaihtoehto kuvan tallennukseen standarditulosteeseen.

### 10.1.1 (9.9.2021)

- Korjattu Lapsiolioiden sijantien päivitys joissain tietyissä tilanteissa.
- Korjattu olion lisääminen itsensä lapseksi aiheuttama ikuinen silmukka.
- Päivitetty MonoGame uudempaan versioon.
- Lisätty `AbsolutePosition`, `-Angle`, -`X` ja `-Y` synonyymeiksi tavallisille ei `Absolute` etuliitteisille kentille.
- Lisätty komentoriviargumenttien lukeminen ruudun tallennusta varten.

### 10.1.0 (14.7.2021)

- Korjattu `MediaPlayer.IsPlaying`.
- Korjattu `PhysicsStructuren` joidenkin kenttien asettaminen.
- Korjattu `AxleJointin` `AxlePosition` asetus sen muodostajassa.
- Korjattu Debug-näkymän (F12) ikkunoiden sijainti.
- Korjattu lapsiolioiden käytöstä.
- Korjattu `PhysicsObject.Oscillate`.
- `Shape.FromImage` tuottaa nyt hieman tehokkaammin muotoja.
- Lisättiin `IMotorJoint`-rajapinta moottorin sisältäviä liitoksia varten.
- Päivitettiin `Tank` käyttämään tätä `IMotorJoint`ia sen renkaissa.
  - Lisättiin tankille `MotorTorque`-kenttä.
  - `Accelerate` toimii nyt paremmin, ottaa vastaan halutun tankin nopeuden eikä renkaiden pyörimisnopeutta.
- Poistettiin vanhentuneet `MouseAnalogState`-metodit.
- `InputBox`issa on nyt mahdollista liikuttaa kursoria nuolinäppäimillä.
- `InputWindow`n fonttia voi nyt muuttaa
- Yhdistettiin `WindowsFileManager`-luokan toiminta `FileManager` -luokkaan.
- Metodeja `JypeliContentManager`-luokkaan Jypelin sisäisten resurssien helpompaan lataamiseen.
  - `LoadInternalSoundEffect`, `LoadInternalImage`, `StreamInternalFont`
  - `InternalResources` -kenttä joka kertoo mitä kaikkea on saatavilla.
- Lisätty hyvin paljon puuttunutta dokumentaatiota.

### 10.0.9 (29.3.2021)

- Korjattu `Slider`in toiminta mikäli sijaintina oli X != 0.
- Korjattu `Slider`in arvon päivttyminen peliin lisäämisen yhteydessä.
- Korjattu `Label.Title` toimimattomuus `DecimalPlaces` asetuksen kanssa.
- Korjattiin jostain dokumentaatiosta rikkinäisiä ääkkösiä ja muotoiluvirheitä.
- Selkeytettiin `ClearAll`in dokumentaatiota.
- Toteutettiin `GameObject.RelativeLeft`, `Right`, `Top` ja `Bottom`.

#### 10.0.8 (18.3.2021)

- Päivitetty tekstinkäsittelykirjasto uudempaan.
- Konversiot Jypelin `Vector` ja `System.Numerics.Vector` välille.
- Korjattu hyvin nopean ajastimen suoritus liian monta kertaa, jos sille oli asetettu maksimisuorituskerrat.
- Korjattu `RelativePosition`in asetus.
- Korjattu kaatuminen jos `PhysicsObject`ille ajettiin päivitys sen tuhoamisen jälkeen.
- Mahdollisuus estää `Window`in raahaaminen hiirellä, `CapturesMouse`.

### 10.0.7 (4.3.2021)

- `Flame` ja `Smoke` -efektit käyttäytyvät nyt paremmin.
- Lisätty efekteille `MaxAngleChange` -kenttä.
- Lisätty `Volume` -kenttä räjähdykselle ja aseille.
- Lisätty `MasterVolume` peliluokkaan.

### 10.0.6 (24.2.2021)

- Päivitetty MonoGame uudempaan versioon, hieman parempi suorituskyky grafiikan piirrossa.
- Korjattu lisää lapsiolioiden sijaintien asettelua.

### 10.0.5 (17.2.2021)

- Korjattu joidenkin käyttöliittymäelementtien vilkkuminen ja joidenkin lapsiolioiden omituinen käytös.

### 10.0.4 (9.2.2021)

- Korjattu `Camera.ZoomToAllObjects` zoomasi äärettömään tyhjällä kentällä.
- Korjattu `PhysicsStructure`n kaatuminen.
- Korjattu Debug-näkymä `PhysicsStructure`ille
- Fysiikkaobjektien lapsioliot ovat nyt oikeasti yksi ja sama kappale -\> liitos ei jousta.

### 10.0.3 (17.1.2021)

- Korjattu `Layout`tien antama virheellinen sijainti.
- Korjattu debug-näkymän (F12) virheellisesti piirretyt ääriviivat
- Korjattu suurten kappaleiden näkymttömyys jos kameraa oli zoomattu paljon ja ne olivat ruudun reunalla.
- Lisätty piirtovaihtoehtoja debug-näkymään (`DebugViewSettings`).
- `MakeOneWay`lle voi antaa suunnan.

### 10.0.2 (13.1.2021)

- Korjattu lapsiolioita sisältävien `Widget`ien renderöityminen väärin, jos niiden sijainti ei ollut origossa.

### 10.0.1 (11.1.2021)

- Korjattu `Tank`-olion totaalinen hajoaminen.

### 10.0.0 (6.1.2021)

- Vaihtoehtoinen fysiikkamoottori (Farseer)
- Fysiikkaolioita voi lisätä lapsiolioiksi (vain Farseerilla)
- Lapsiolioiden `Position` ja `Angle` on nyt aina absoluuttinen maailmassa.
  - Poistettu `AbsolutePosition` ja `AbsoluteAngle`.
  - Lisätty `RelativePosition` ja `RelativeAngle`.
- `SetTileMethod` voi nyt vastaanottaa jopa 6 ylimääräistä parametria aiemman kolmen sijasta.
- Päivitetty käyttämään .NET 5.0
- Mahdollisuus lisätä toiminto jos käyttäjä vastaa `No` `ConfirmExit`issä.
- Lukuisia muita sisäisiä muutoksia joita Farseer ja em. muutokset vaativat.

## Farseer

### 2.0.5 (26.10.2022)

- Korjattu `IgnoresCollisionResponse` asetuksen nollaantuminen jos hahmon muotoa tai kokoa muokattiin.

### 2.0.4 (14.9.2022)

- Korjattu painovoiman muuttaminen ei vaikuttanut kappaleisiin jotka olivat lepotilassa.

### 2.0.3 (22.2.2022)

- Korjattu fysiikkakappaleiden lapsioliot lisättiin kahdesti.
- Pieniä suorituskykyoptimointeja.

### 2.0.2 (18.2.2022)

- Korjattu fysiikkakappaleen ominaisuuksien muuttaminen sen jälkeen, kun se oli poistettu pelistä.
- Korjattu fysiikkakappaleiden lisääminen takaisin peliin poistamisen jälkeen.

### 2.0.1 (7.2.2022)

- Korjattu lapsiolioiden käyttäytymistä.

### 2.0.0 (6.1.2022)

- Päivitetty käyttämään .NET 6

### 1.0.11 (1.11.2021)

- Säädetty `AxleJoint`in liitoksen sijaintia loogisemmaksi.
- Säädetty fysiikkamoottorin asetuksia jotta kappaleiden törmäykset olisivat hieman parempia.

### 1.0.10 (15.10.2021)

- Lisätty `CollisionIgnoreFunc`in tarkistus törmäyksiin.

### 1.0.9 (27.9.2021)

- Päivitetty pohjana käytetty fysiikkamoottori uudempaan versioon.
- Korjattu nullPointer törmäyksenkäsittelijässä, jos törmäyksessä mukana ollutta kappaletta oli saman päivityksen aikana muokattu.

### 1.0.8 (3.8.2021)

- Korjattu CollisionHandlerien aiheuttama kaatuminen joissain tilanteissa.

### 1.0.7 (14.7.2021)

- Taustalla oleva fysiikkamoottori päivitetty uudempaan versioon.
- Korjattu ympyrämuodon asettaminen `PhysicsObject`in muodostajassa.
- Korjattu lapsiolioiden käytöstä.
- Korjattu `AxleJoint.AxlePosition` asetus sen muodostajassa.
- Korjattu `RaySegment`in virheellinen pituus fysiikkamoottorissa.
- Muutettu kappaleiden oletustiheys olemaan 1/1000 aiemmasta.
- Lisätty `WheelJoint` käyttämään `IMotorJoint` -rajapintaa
- Lisätty `AxleJoint`ille `Softness` ja `DampingRatio`-kentät.
- Vaihdettiin fysiikkamuotojen muodostamiseen käytettyä algoritmia.

### 1.0.6 (28.3.2021)

- Vaihdettiin käyttämään sisäisessä toiminnassa `System.Numerics`-kirjaston vektoreita ja matriiseja. Tämä vaikutti parantavan suorituskykyä joissain tilanteissa.

### 1.0.5 (24.2.2021)

- Korjattu lisää lapsiolioiden sijantien päivittymistä.

### 1.0.4 (9.2.2021)

- Korjattu `IgnoresCollisionResponse`.
- Korjattu `Hit` ja `Push` -funktioiden liian suuri voimakkuus.
- Korjattu `WeldJoint`in muodostuminen
- Parannettu `MakeOneWay`n toimintalogiikkaa.
- Fysiikkaobjektien lapsioliot ovat nyt oikeasti yksi ja sama kappale -\> liitos ei jousta.

### 1.0.3 (17.1.2021)

- Korjattu `ClearAll` kaatoi pelin.
- Korjattu kappaleiden virheellinen massa joissain tilanteissa.
- Ympyrät ovat nyt oikeasti ympyröitä.
- Lisättiin `PhysicsBody`lle `Vertices` kenttä.

### 1.0.2 (11.1.2021)

- Korjattu `Surface`-olion tuottama huomattava lagi.
- Korjattu painovoiman muutoksen vaikuttamattomuus jos kappale oli paikallaan.
- Korjattu massan asetus
- Korjattu hitausmomentin muuttumattomuus massan asetuksen yhteydessä.

### 1.0.1 (7.1.2021)

- Korjattu törmäykset jos kappaleelle ei oltu asetettu `ObjectIgnorer`ia.
- `WheelJoint`, esimerkiksi auton renkaita varten.

### 1.0.0 (6.1.2021)

- Ensimmäinen julkaisu, suurimmilta osin vastaavat ominaisuudet vanhaan Physics2d moottoriin nähden.

## Physics2d
