# Conclusion

<!-- TODO hoeft niet volgens Bart en Peter
## History of UMGAP

* doorloping
  - Tryptische peptiden als thesis van Tom
    - oorsprong boomgebaseerde LCA
  initieel: puur uitgegaan van metaproteomics strategie; met filterstap beter; dan kmeren
  - 9-meren als thesis van Stijn
  - seed-extend met Aranka
    - oorspronkelijk met scores
  - benchmark met Niels
    - start van FGS++

Peter: eventueel iets over Rust, waarom dat comfortable is en er potentieel in zit
-->

## Current State

* kunnen we de roundtrip doen?
  - ja
  - we verliezen snelheid door de roundtrip
  - we verliezen accuraatheid door de coding stukken
  - qua specificiteit dicht bij de state of the art
  - voordelen: breed spectrum (in praktijk niet altijd in genomics vanwege referentiegenomen) (bij ons in de praktijk geen nadeel)

## Future Work

* adaptieve k in k-meren
  - beginnen met korte, langer maken zolang LCA hoog is
  - tijdens opbouw van databank
    - meermaals opsplitsen in k-meren
    - initieel alle houden
    - latere iteraties enkel superstrings van niet-specifieke (k-1)-meren
  - tijdens mapping
    - huidige index kan dit gewoon aan, zolang er geen prefixes zijn

* targeted databanken (virussen)
  - vermijden sample bias in referentiedatabanken
  - specifiek virussen (ook schimmels) zijn moeilijk, geen goede data in Uniprot
  - targeted databanken kunnen helpen, met caveat

* functionele annotaties toevoegen
  - mapping op functionele annotaties
  - probleem: geen boomstructuur -> geen eenvoudige aggregatie
  - doen we al voor metaproteomics
  - metagenomics is sowieso enkel functional potential

* metatranscriptomics verder uitwerken
  - werken al, maar kan meer aandacht gebruiken om te specialiseren
  - momenteel thesis over bezig

* integratie in desktopapplicatie
  - ontwikkeling door Pieter
  - toegankelijker voor biologen
  - uitdagingen: linken typescript/rust
  - webassembly is optie, maar waarschijnlijk te traag

* comparatieve studies
  - reeds voorzien op primitieve wijze
  - betere ondersteuning, vooral grafisch

* combinerende studies van meta-omics
  - samples op verschillende manieren gesequeneerd
  - gemeenschappelijke conclusies proberen nemen
  - (we zien een bias tussen 16S en shotgun in metagenomics ook)
