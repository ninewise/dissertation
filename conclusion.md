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

In it's current state, UMGAP is unfortunately unable to better all
similar metagenomics diversity analysis tools. The roundtrip through
metaproteomics UMGAP makes carries a hit on performance with it, and it
enforces an upper limit on sensitivity because only coding regions can
be matched to a protein database. Still, UMGAP's accuracy rivals that of
the best tools around and it has a hard-to-measure advantage on unknown
genomes because it is based on database with a wide spectrum.

## Future Work

### Adaptive k-mer Length

One method to improve accuracy further would be to adapt the size of
the k-mers according to their lowest common ancestors. Currently, the
whole index consists of 9-mer peptides. Nearly 10% of those 9-mers,
however, have an LCA of rank phylum or less specific, which is near
useless in most diversity analyses. It would be interesting to see if
the 10-mers these 9-mers are subsequences of, would be more specific. If
so, the k-mer-to-LCA mapping command could, thanks to the structure of
the index, relatively easily be patched to work with k-mers of differing
length. The challenge would be in generating such an index in reasonable
time and space.

### Targeted Index Files

Another way to improve specificity would be to use targeted index files.
At the moment, two general purpose index files are provided for use
with the UMGAP: the tryptic peptide index and the 9-mer index. Both
are based on the complete UniProtKB database. While this is advantages
when analysing unknown samples, in most studies there is preliminary
knowledge about the sample or an interest in only some aspects of the
sample. Constructing an index from only the relevant data would not only
result in a more specific index, but the index would also be smaller and
as such the analysis would be faster. Of course, one should remain wary
of the bias implicit in such an index: some peptides which would match
only against a specific organism in such a database might occur in many
other organisms not included.

Such targeted index files would especially be useful for studies on
samples taken to analyse viral or fungal diversity. Both are strongly
underrepresented in the UniProtKB. Viral genomes in particular are often
included in assemblies of their host genomes, resulting in at best a
'root' identification for the whole genome (if the viral genome is also
included in UniProtKB separately) or a completely wrong identification
(if it isn't). Similarly, targeted index files could also provide a
solution for overrepresentation in the UniProtKB. Organisms with a lot
of recorded genomes tend to occur randomly in completely unrelated
samples.

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
