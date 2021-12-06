# Summary {.unnumbered}

Each organism carries its complete genetic code, the genome, in the form
of DNA in their cells. To perform functions, the DNA is transcribed to
RNA, which is translated into proteins. The complete set of potentially
transcribed RNA is called the transcriptome, and the complete set of
potentially expressed proteins is called the proteome. When studies
are performed on the genomes, transcriptomes and proteomes of multiple
organisms at once, they are called metagenomics, metatranscriptomics and
metaproteomics. This dissertation describes the development and results
of several bioinformatics tools to help with such studies.

In shotgun metagenomics, a great number of random DNA fragments, called
reads, are sequenced from an environmental sample. By identifying which
organism each read originates from, one can draw conclusions about
the organisms in the environmental sample or compare the abundance
between similar samples. Often the reads are too short to identify a
specific organism, occurring in a number of organisms. They might also
not match with any known organism, because of natural mutation in the
DNA or sequencing errors in the read; or just because there are unknown
organisms in the sample. Instead, each read is identified as coming from
a group of evolutionary more-or-less related organisms, called a taxon.

The Unipept Metagenomics Analysis Pipeline ([UMGAP][sum-umgap]),
described in chapter \ref{chapter:umgap} is a set of tools for taxonomic
identification of shotgun metagenomics reads. With UMGAP, we explore the
possibility of performing taxonomic identifications of DNA reads using
the proteins this DNA encodes. Unlike most taxonomic identification
tools, which map DNA reads directly to taxa, UMGAP will first predict
which (partial) protein (or peptide) is encoded in a DNA read and map
this peptide on a taxon using a general purpose protein database. This
detour adds robustness to the identification process, as proteins are
more conserved than the underlying DNA.

[sum-umgap]: https://github.com/unipept/umgap

UMGAP turns out to be a valid alternative for existing metagenomics
identification tools, though it cannot equal the speed and accuracy
of all. The pipeline does offer interesting avenues towards
functional analysis (what organisms are doing in the sample) and
metatranscriptomics (analyzing RNA reads instead of DNA reads).

As part of the development of UMGAP, we also introduce an
alternative implementation for FragGeneScan in Rust, called
[FragGeneScanRs][sum-fgsrs], in chapter \ref{chapter:fgsrs}.
FragGeneScan plays an important role in UMGAP: prediction of
proteins (or gene fragments) from DNA reads. However, the existing
implementation proved to be insufficiently fast. The primary
alternative, FragGeneScan-Plus, which we forked and partially debugged
as [FragGeneScanPlusPlus][sum-fgs++], is faster but contains a number of
hard-to-solve parallelization bugs. FragGeneScanRs fixes these bugs and
runs up to 22 times faster.

[sum-fgsrs]: https://github.com/unipept/FragGeneScanRs
[sum-fgs++]: https://github.com/unipept/FragGeneScanPlusPlus

Both the UMGAP and the original Unipept application (The Unipept
Metaproteomics Analysis Pipeline, or UMPAP) are, at their core,
a mapping of peptides onto taxa. This mapping is processed
from the UniProtKB, a large database of annotated proteins. In
chapter \ref{chapter:on-the-side}, we describe the [Database
creation][sum-database] repository. This repository contains the code to
parse the UniProtKB and compose the Unipept database tables. To create
the peptide-taxon mapping, it gathers for each peptide occurring in
the UniProtKB the taxa the proteins in which it occurs are annotated
with. It aggregates these taxa using a lowest common ancestor method,
resulting in a single taxon per peptide which contains all taxa in the
list. Chapter \ref{chapter:on-the-side} also describes the contributions
made to the [SPeDE][sum-spede] and [SMAP][sum-smap] projects.

[sum-database]: https://github.com/unipept/make-database
[sum-spede]: https://github.com/LM-UGent/SPeDE
[sum-smap]: https://gitlab.com/truttink/smap
[sum-smap2]: https://gitlab.com/dschaumont/smap-haplotype-window

# Samenvatting {.unnumbered}

<!-- TODO translate english summary -->

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

# Software Repositories {.unnumbered}

The focus of this PhD was the development of bioinformatics software
tools. While this dissertation decribes those tools and the results of
their application, no text can better describe software than the code
by which it is defined. As all tools contributed to are (to be) freely
available and open source, you may find a list of the relevant software
repositories below.

UMGAP
  ~ https://github.com/unipept/umgap

    The Unipept Metagenomics Analysis Pipeline is the main focus of
    this dissertation. It is a collection of tools to be composed into
    an taxonomic classifier for shotgun metagenomics reads. Given the
    DNA found in an environment sample, it explores the organisms found
    using frequency tables and interactive visualizations.

Unipept's Database Creation
  ~ https://github.com/unipept/make-database

    Both the Unipept metaproteomics and metagenomics pipelines operate
    on data found in UniProt's database. This collections of scripts
    downloads and processes that database, and others, into the actual
    database tables and indices used by Unipept.

FragGeneScan++
  ~ https://github.com/unipept/FragGeneScanPlusPlus

    FragGeneScan++ is our fork of the FragGeneScan-Plus project,
    which is a scalable high-throughput short-read gene predictor.
    Since FragGeneScan-Plus was no longer maintained, we took over
    maintainance and fixed a series of bugs. Note that FragGeneScan++
    has since been replaced by FragGeneScanRs.

FragGeneScanRs
  ~ https://github.com/unipept/FragGeneScanRs

    An better and faster implementation of the FragGeneScan gene
    prediction model for short and error-prone reads. It is a *de facto*
    replacement of both FragGeneScan and FragGeneScan-Plus.

SPeDE
  ~ https://github.com/LM-UGent/SPeDE

    Contributions were made to the Spectral Dereplication tool by the
    microbiology lab of Ghent University. SPeDE is a program used to
    dereplicate large sets of MALDI-TOF MS spectra.

SMAP
  ~ https://gitlab.com/truttink/smap

    SMAP is an analysis tool for stack-based NGS read mapping. It
    has several components, including read distribution analysis,
    comparison between two samples sets, and delineation of haplotypes.
    Contributions were made to the SMAP haplotype tool.

SMAP-Haplotype-Window
  ~ https://gitlab.com/dschaumont/smap-haplotype-window (to be published)

    SMAP-Haplotype-Window is a plugin for SMAP that allows for the
    analysis of sequencing data from CRISPR edited loci. The software
    was analyzed and advice on the development was given.

# List of Publications {.unnumbered}

**Felix Van der Jeugt**, Peter Dawyndt, Bart Mesuere. *Under review*.
"FragGeneScanRs: better and faster gene prediction for short reads."
*BMC Bioinformatics*.

**Felix Van der Jeugt**, Rien Maertens, Aranka Steyaert, Pieter
Verschaffelt, Caroline De Tender, Peter Dawyndt and Bart Mesuere. *Under
review*. "UMGAP: the Unipept MetaGenomics Analysis Pipeline." *BMC
Genomics*.

Pieter Verschaffelt, Philippe Van Thienen, Tim Van Den Bossche, **Felix
Van der Jeugt**, Caroline De Tender, Lennart Martens, Peter Dawyndt and
Bart Mesuere. 2020. "Unipept CLI 2.0: adding support for visualizations
and functional annotations." *Bioinformatics* 20 (14): 4220-4221.

Charles Dumolin, Maarten Aerts, Bart Verheyde, Simon Schellaert, Tim
Vandamme, **Felix Van der Jeugt**, Evelien De Canck, Margo Cnockaert,
Anneleen Wieme, Ilse Cleenwerck, Jindrich Peiren, Peter Dawyndt, Peter
Vandamme and Aurélien Carlier. 2019. "Introducing SPeDE: high-throughput
dereplication and accurate determination of microbial diversity from
matrix-assisted laser desorption-ionization time of flight mass
spectrometry data." *MSystems* 4 (5): e00437-19.

Caroline De Tender, Bart Mesuere, **Felix Van der Jeugt**, Annelies
Haegeman, Tom Ruttink, B Vandecasteele, Peter Dawyndt, J Debode and
EE Kuramae. 2019. "Peat substrate amended with chitin modulates the
N-cycle, siderophore and chitinase responses in the lettuce rhizobiome."
*Scientific reports* 9: 9890.

Robbert Gurdeep Singh, Alessandro Tanca, Antonio Palomba, **Felix Van
der Jeugt**, Pieter Verschaffelt, Sergio Uzzau, Lennart Martens, Peter
Dawyndt and Bart Mesuere. 2019. "Unipept 4.0: functional analysis of
metaproteome data." *Journal of Proteome Research* 18 (2): 606-615.

Bart Mesuere, **Felix Van der Jeugt**, Toon Willems, Tom Naessens, Bart
Devreese, Lennart Martens and Peter Dawyndt. 2018. "High-throughput
metaproteomics data analysis with Unipept: a tutorial." *Journal of
Proteomics* 171: 11-22.

Bart Mesuere, **Felix Van der Jeugt**, Bart Devreese, Peter Vandamme
and Peter Dawyndt. 2016. "The unique peptidome: taxon-specific tryptic
peptides as biomarkers for targeted metaproteomics." *Proteomics* 16
(17): 2313-2318.

Bart Mesuere, Toon Willems, **Felix Van der Jeugt**, Bart Devreese,
Peter Vandamme and Peter Dawyndt. 2016. "Unipept web services for
metaproteomics analysis." *Bioinformatics* 32 (11): 1746-1748.
