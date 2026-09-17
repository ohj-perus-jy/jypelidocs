# Kerrokset

Olioita voidaan lisätä eri kerroksiin. Taaemmille kerroksille lisätyt oliot näkyvät etummaisten kerrosten takana (ja päinvastoin). Jypeli tarjoaa 7 kerrosta. Niiden numerot ovat välillä `-3`–`3`, oletus on `0`.

Jos olio halutaan näkymään muiden edessä, se lisätään kerrokseen, joka on isompi kuin `0`:

```csharp,ignore
Add(olio, 1);
```

Vastaavasti, jos olio halutaan muiden taakse, onnistuu se näin:

```csharp,ignore
Add(olio, -1);
```

## Huomioita

Kerrokset ovat ainoastaan visuaalisia, eli ne eivät vaikuta törmäyksiin millään tapaa.
