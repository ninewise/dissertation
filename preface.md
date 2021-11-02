# Preface {.unnumbered}

## Summary {.unnumbered}

In shotgun metagenomics, a great number of random DNA fragments,
called reads, are sequenced from an environment sample. By identifying
for each read the organism this fragment originates from, you
can draw conclusions about the abundance of those organisms in the
environment sample. Of course, often the reads are too short to identify
a specific organism, instead indicating a complete group of evolutionary
more-or-less related organisms, called a taxon, which all contain this
read in their DNA.

In this work, we represent the Unipept Metagenomics Analysis Pipeline
(UMGAP), a set of tools for taxonomic identification of shotgun
metagenomics reads. With the UMGAP, we explore the possibility of
running taxonomic identifications of DNA reads using the proteins this
DNA codes. Unlike most taxonomic identification tools, which map DNA
reads directly to taxa, the UMGAP will first predict which (partial)
protein is coded in a DNA read and map this protein on a taxon using a
general purpose protein database. This detour adds robustness to the
identification process, as proteins are less likely to mutate than the
underlying DNA.

The UMGAP is concluded to be a valid alternative for existing
metagenomics identification tools, though it cannot equal the speed and
accuracy of all. The pipeline does offer interesting avenues towards
functional analysis (what organisms are doing in the sample - which uses
proteins anyway) and metatranscriptomics (analysing RNA reads instead of
DNA reads).

Next to the development of the UMGAP, we also introduce an alternative
implementation for FragGeneScan, called FragGeneScanRs. FragGeneScan
performs an important function in the UMGAP: the prediction of
proteins (or gene fragments) from DNA reads. However, the existing
implementation, nor any of the available alternatives, proved
sufficiently fast for our applications and contained a number of bugs.
FragGeneScanRs fixes these bugs and runs up to 20 times faster.

## Samenvatting {.unnumbered}

In *shotgun metagenomics* worden een hoog aantal willekeurige stukjes
DNA uitgelezen uit een omgevingsstaal. Door voor elk van deze stukjes,
genaamd *reads*, te bepalen uit welk organisme het afkomstig is, kan je
conclusies trekken over de aanwezigheid en verhouding van die organismen
in het omgevingsstaal. Vaak zijn *reads* echter te kort om een specifiek
organisme aan te duiden, omdat ze voorkomen in het DNA van een hele
groep aan evolutionair min-of-meer verwante organismen, genaamd een
taxon.

In dit werk wordt de *Unipept Metagenomics Analysis Pipeline* (UMGAP)
gepresenteerd, een suite van programma's voor taxonomische identificatie
van *shotgun metagenomics reads*. Met de UMGAP zoeken we uit of de
taxonomische identificatie van DNA ook kan gebeuren aan de hand van
de eiwitten die dit DNA codeert. In tegenstelling tot de meeste
gelijkaardige programma's, die *DNA reads* rechtstreeks proberen
te identificeren, zal de UMGAP eerst proberen te voorspellen welk
(gedeeltelijk) eiwit een *DNA read* omschrijft en vervolgens dat eiwit
opzoeken in een algemene eiwitdatabank. Deze extra stap voegt robustheid
toe aan het process (eiwitten gaan minder snel muteren dan DNA).

De UMGAP blijkt een waardig alternatief te vormen voor reeds
bestaande programma's, al kan het niet van allen de snelheid en
accuraatheid evenaren. De *pipeline* biedt echter wel interessante
uitbereidingsmogelijkheden betreffende functionele analyse (wat in
een omgevingsstaal gebeurt - waarvoor je sowieso naar de eiwitten wil
kijken) en metatranscriptomics (waar we vertrekken vanaf *RNA reads* in
plaats van *DNA reads*).

Naast de ontwikkeling van de UMGAP wordt ook een alternatieve
implementatie van FragGeneScan, genaamd FragGeneScanRs, voorgesteld.
Dit programma vormt een belangrijke stap in de UMGAP, namelijk de
voorspelling van eiwitten (of genfragmenten) uit *DNA reads*. De
implementatie ervan bleek echter onvoldoende snel voor onze toepassing,
en bevatten een aantal fouten. FragGeneScanRs lost deze problemen op en
voert tot 20 maal sneller uit.
