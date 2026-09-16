# Kirjaston liittäminen käsin

Jypelin projektimallit (Fysiikkapeli, Peli, Tasohyppelypeli) liittävät
Jypeli-kirjaston projektiin valmiiksi. Jos haluat käyttää Jypelin
aliohjelmia tavallisessa konsoliprojektissa (esimerkiksi ConsoleMain-mallista
luodussa), kirjasto pitää liittää käsin. Se tulee projektiin NuGet-pakettina
nimeltä `Jypeli.NET`.

Konsoliprojektissa toimivat esimerkiksi satunnaisluvut (`RandomGen`),
vektorit (`Vector`) ja kulmat (`Angle`). Peli-ikkunaa, olioita tai ohjaimia
ei voi käyttää, koska niitä varten tarvitaan peli, ks.
[Uuden projektin luominen](../aloittaminen/projektin-luonti.md).

## Tapa 1: projektitiedoston muokkaus

Avaa Riderin Explorer-näkymässä projektin `.csproj`-tiedosto
(kaksoisklikkaa projektin nimeä). Lisää siihen `PropertyGroup`-osan jälkeen
`ItemGroup`-osa, jolloin tiedosto näyttää tältä:

```xml
<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net10.0</TargetFramework>
        <ExternalConsole>true</ExternalConsole>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="Jypeli.NET" Version="11.*" />
    </ItemGroup>

</Project>
```

Tallenna tiedosto. Rider lataa paketin automaattisesti; se voi kestää
hetken ensimmäisellä kerralla.

## Tapa 2: Riderin NuGet-ikkuna

1. Klikkaa Explorer-näkymässä projektia hiiren oikealla painikkeella
   (Macilla Ctrl+klikkaus) ja valitse **Manage NuGet Packages**. Ikkunan
   alareunaan aukeaa NuGet-työkaluikkuna.
2. Kirjoita hakukenttään `Jypeli.NET` ja valitse listasta juuri sen niminen
   paketti. Haku löytää myös vanhoja paketteja (`Jypeli`, `Jypeli.Core`),
   älä käytä niitä.
3. Klikkaa oikeassa reunassa projektin nimen vieressä olevaa
   plus-painiketta (**Install**). Jätä versioksi uusin.

## Tapa 3: komentorivi

Avaa komentorivi projektin kansiossa (siinä, jossa `.csproj`-tiedosto on)
ja anna komento:

```bash
dotnet add package Jypeli.NET
```

## Käyttö

Kun paketti on liitetty, Jypelin aliohjelmia voi käyttää `Jypeli.`-etuliitteellä
tai lisäämällä tiedoston alkuun rivin `using Jypeli;`:

```csharp,ignore
using Jypeli;

public class ConsoleMain
{
    public static void Main()
    {
        double[] lukuja = RandomGen.NextDoubleArray(0, 20, 50);
        int noppa = RandomGen.NextInt(1, 7);
    }
}
```

## Virhe NU1202: "not compatible"

Jos paketin lataus epäonnistuu ja virheilmoituksessa lukee
`Package Jypeli.NET ... is not compatible with ...`, projekti käyttää liian
vanhaa .NET-versiota. Jypeli.NET vaatii vähintään .NET 6:n. Avaa
`.csproj`-tiedosto ja vaihda `TargetFramework`-riville `net10.0` (tai muu
koneellesi asennettu versio, ks. [Asennus](../aloittaminen/asentaminen.md)).
Tallenna, niin Rider lataa paketin uudelleen.

## Katso myös

- [Mitä konepellin alla tapahtuu](konepellin-alla.md): mistä paketeista Jypeli koostuu.
- [Satunnaisuus](../matematiikka/satunnaisuus.md): `RandomGen`-luokan käyttö.
- [Yleiset virheet](yleiset-virheet.md)
