# Conclusion

## History of UMGAP

* doorloping
  - Tryptische peptiden als thesis van Tom
    - oorsprong boomgebaseerde LCA
  - 9-meren als thesis van Stijn
  - seed-extend met Aranka
    - oorspronkelijk met scores
  - benchmark met Niels
    - start van FGS++

## Future Work

* adaptieve k in k-meren
  - beginnen met korte, langer maken zolang LCA hoog is
  - tijdens opbouw van databank
    - meermaals opsplitsen in k-meren
    - initieel alle houden
    - latere iteraties enkel superstrings van niet-specifieke (k-1)-meren
  - tijdens mapping
    - huidige index kan dit gewoon aan, zolang er geen prefixes zijn

* metatranscriptomics verder uitwerken
  - werken al, maar kan meer aandacht gebruiken om te specialiseren
  - momenteel thesis over bezig

* targeted databanken (virussen)
  - specifiek virussen zijn moeilijk, geen goede data in Uniprot
  - targeted databanken kunnen helpen, met caveat

* comparatieve studies
  - reeds voorzien op primitieve wijze
  - betere ondersteuning, vooral grafisch

* functionele annotaties toevoegen
  - mapping op functionele annotaties
  - probleem: geen boomstructuur -> geen eenvoudige aggregatie

* combinerende studies van meta-omics
  - samples op verschillende manieren gesequeneerd
  - gemeenschappelijke conclusies proberen nemen

* integratie in desktopapplicatie
  - ontwikkeling door Pieter
  - toegankelijker voor biologen
  - uitdagingen: linken typescript/rust
  - webassembly is optie, maar waarschijnlijk te traag
