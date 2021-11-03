# Summary {.unnumbered}

In shotgun metagenomics, a great number of random DNA fragments, called
reads, are sequenced from an environmental sample. By identifying which
organism each read originates from, one can draw conclusions about the
abundance of organisms in the environmental sample. Often the reads
are too short to identify a specific organism, occurring in a number of
organisms. They might also not match with any known organism, because of
natural mutation in the DNA or sequencing errors in the read; or just
because there are unknown organisms in the sample. Instead, each read is
identified as coming from a group of evolutionary more-or-less related
organisms, called a taxon.

<!-- TODO abundance: gevaarlijk om te zeggen, want sequenering zorgt voor bias in organismes -->

In this work, we present the Unipept Metagenomics Analysis Pipeline
(UMGAP), a set of tools for taxonomic identification of shotgun
metagenomics reads. With the UMGAP, we explore the possibility of
performing taxonomic identifications of DNA reads using the proteins
this DNA encodes. Unlike most taxonomic identification tools, which map
DNA reads directly to taxa, the UMGAP will first predict which (partial)
protein is encoded in a DNA read and map this protein on a taxon using
a general purpose protein database. This detour adds robustness to
the identification process, as proteins are more conserved than the
underlying DNA.

The UMGAP turns out to be a valid alternative for existing metagenomics
identification tools, though it cannot equal the speed and accuracy
of all. The pipeline does offer interesting avenues towards
functional analysis (what organisms are doing in the sample) and
metatranscriptomics (analyzing RNA reads instead of DNA reads).

As part of the development of the UMGAP, we also introduce an
alternative implementation for FragGeneScan in Rust, called
FragGeneScanRs. FragGeneScan plays an important role in the UMGAP:
prediction of proteins (or gene fragments) from DNA reads. However, the
existing implementation, nor any of the available alternatives, proved
sufficiently fast for our applications and contained a number of bugs.
FragGeneScanRs fixes these bugs and runs up to 20 times faster.

# Samenvatting {.unnumbered}

Bij *shotgun metagenomics* worden een groot aantal willekeurige
stukjes DNA uitgelezen uit een omgevingsstaal. Door voor elk van deze
stukjes, *reads* genaamd, te bepalen uit welk organisme ze afkomstig
zijn, kan men conclusies trekken over de aanwezige organismen in het
omgevingsstaal. Vaak zijn *reads* echter te kort om een specifiek
organisme aan te duiden, omdat ze voorkomen in het DNA van een hele
groep aan evolutionair min-of-meer verwante organismen, genaamd een
taxon.

In dit werk stellen we de *Unipept Metagenomics Analysis Pipeline*
(UMGAP) voor, een suite van programma's voor taxonomische identificatie
van *shotgun metagenomics reads*. Met de UMGAP zoeken we uit of
taxonomische identificatie van DNA ook kan gebeuren aan de hand van de
eiwitten die DNA codeert. In tegenstelling tot de meeste gelijkaardige
programma's, die *DNA reads* rechtstreeks proberen te identificeren, zal
de UMGAP eerst proberen te voorspellen welk (gedeeltelijk) eiwit een
*DNA read* codeert en vervolgens dat eiwit (-fragment) opzoeken in een
algemene eiwitdatabank. Deze extra stap voegt robuustheid toe aan het
process (eiwitten zijn evolutionair meer geconserveerd DNA).

De UMGAP blijkt een waardig alternatief te vormen voor reeds
bestaande programma's, al kan het niet van allen de snelheid en
nauwkeurigheid evenaren. De *pipeline* biedt echter wel interessante
uitbereidingsmogelijkheden betreffende functionele analyse (welke
functies de organismen in het omgevingsstaal vervullen) en
metatranscriptomics (waar we vertrekken vanaf *RNA reads* in plaats van
*DNA reads*).

Naast de ontwikkeling van de UMGAP wordt ook een alternatieve Rust
implementatie van FragGeneScan, genaamd FragGeneScanRs, voorgesteld.
Dit programma vervult een belangrijke rol in de UMGAP, namelijk het
voorspellen van eiwitten (of genfragmenten) uit *DNA reads*. De
bestaande implementaties bleken onvoldoende snel voor onze toepassing,
en bevatten een aantal fouten. FragGeneScanRs lost deze problemen op en
werkt tot 20 maal sneller.
