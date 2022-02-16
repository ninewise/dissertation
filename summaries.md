# Summary (English) {.unnumbered}
\markboth{Summary (English)}

Each organism carries its complete genetic code, the genome, in
its cells, in the form of DNA. To perform functions, the DNA is
transcribed to RNA, which is translated into proteins. The complete
set of potentially transcribed RNA is called the transcriptome, and
the complete set of potentially expressed proteins is called the
proteome. When studies are performed on the genomes, transcriptomes and
proteomes of multiple organisms at once, they are called metagenomics,
metatranscriptomics and metaproteomics. This dissertation describes the
development and results of several bioinformatics tools to help with
such studies.

<!-- TODO Carolien 1 -->

In shotgun metagenomics, a great number of random DNA fragments, called
reads, are sequenced from an environmental sample. By identifying which
organism each read originates from, one can draw conclusions about
the organisms in the environmental sample or compare the abundance
between samples. Often the reads are too short to identify a single
organism, because they occur in a number of organisms. They might also
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
which (partial) proteins (or peptide) are encoded in a DNA read and map
these peptides on a taxon using a general purpose protein database. This
detour adds robustness to the identification process, as proteins are
more conserved than the underlying DNA.

[sum-umgap]: https://github.com/unipept/umgap

UMGAP turns out to be a valid alternative for existing metagenomics
identification tools, though it cannot equal the speed and accuracy
of all. The pipeline does offer interesting avenues towards
functional analysis (what organisms in the sample could do) and even
metatranscriptomics (what organisms in the sample are doing, by
analyzing RNA reads instead of DNA reads).

As part of the development of UMGAP, we also introduce an
alternative implementation for FragGeneScan in Rust, called
[FragGeneScanRs][sum-fgsrs] (chapter \ref{chapter:fgsrs}). FragGeneScan
plays an important role in UMGAP: prediction of proteins (or gene
fragments) from DNA reads. However, the existing implementations proved
to be insufficiently in terms of speed. The primary alternative,
FragGeneScan-Plus, which we forked and partially debugged as
[FragGeneScanPlusPlus][sum-fgs++], is faster but contains a number
of hard-to-solve parallelization bugs. FragGeneScanRs fixes these
bugs and runs up to 22 times faster than the original FragGeneScan
implementation.

[sum-fgsrs]: https://github.com/unipept/FragGeneScanRs
[sum-fgs++]: https://github.com/unipept/FragGeneScanPlusPlus

Both UMGAP and the original Unipept application (The Unipept
Metaproteomics Analysis Pipeline, or UMPAP) are, at their core,
a mapping of peptides onto taxa. This mapping is processed
from the UniProtKB, a large database of annotated proteins. In
chapter \ref{chapter:on-the-side}, we describe the [database
creation][sum-database] repository. This repository contains the code
to parse the UniProtKB and compose the Unipept database tables. The
peptide-taxon mapping is given an entry for each peptide occurring in
the UniProtKB. For each of these peptides, it gathers all proteins it
occurs in, and the taxa they are annotated with. It aggregates this list
of taxa using a lowest common ancestor method, resulting in a single
taxon per peptide. Chapter \ref{chapter:on-the-side} also describes
the contributions made to the [SPeDE][sum-spede] and [SMAP][sum-smap]
projects.

[sum-database]: https://github.com/unipept/make-database
[sum-spede]: https://github.com/LM-UGent/SPeDE
[sum-smap]: https://gitlab.com/truttink/smap
[sum-smap2]: https://gitlab.com/dschaumont/smap-haplotype-window

# Summary (Dutch) {.unnumbered}
\markboth{Summary (Dutch)}

::: {lang=nl}
\hyphenation{Frag-Gene-Scan-Rs}

Elk organisme draagt zijn volledige genetische code (het genoom) in
zijn cellen, opgeslagen als DNA. DNA wordt overgeschreven naar RNA
in een proces genaamd transcriptie, wat op zijn beurt vertaald wordt
naar eiwitten in een proces genaamd translatie. Die eiwitten voeren
vervolgende functies uit voor het organisme. De volledige verzameling
aan potentieel overgeschreven RNA noemt met het transcriptoom van
een organisme, de volledige verzameling aan potentieel vertaalde
eiwitten het proteoom. Wanneer studies gemaakt worden van de genomen,
transcriptomen en proteomen van meerdere organismen tesamen, noemt
men dit metagenomics, metatranscriptomics en metaproteomics. Dit
proefschrift beschrijft de ontwikkeling en de resultaten van enkele
bioinformaticatools ontworpen om te helpen met zulke studies.

Bij *shotgun metagenomics* worden een groot aantal willekeurige
stukjes DNA uitgelezen uit een omgevingsstaal. Door voor elk van deze
stukjes, *reads* genaamd, te bepalen uit welk organisme ze afkomstig
zijn, kan men conclusies trekken over de aanwezige organismen in het
omgevingsstaal. Vaak zijn *reads* echter te kort om een enkel organisme
aan te duiden, omdat ze voorkomen in het DNA van meerdere organismen.
Bovendien kan het ook gebeuren dat sommige *reads* niet terug te vinden
in enig gekend organisme. Daarom wordt elke *read* geïdentificeerd als
komende uit een groep aan organismen, genaamd een taxon.

De *Unipept Metagenomics Analysis Pipeline* ([UMGAP][sam-umgap]), die
we beschrijven in hoofdstuk \ref{chapter:umgap}, is een suite van
programma's voor taxonomische identificatie van *shotgun metagenomics
reads*. Met de UMGAP zoeken we uit of taxonomische identificatie van
*DNA reads* ook kan gebeuren aan de hand van de eiwitten die het DNA
codeert. In tegenstelling tot de meeste gelijkaardige programma's, die
*DNA reads* rechtstreeks proberen te identificeren, zal de UMGAP eerst
proberen te voorspellen welk (gedeeltelijk) eiwit een *DNA read* codeert
en vervolgens dat eiwitfragment opzoeken in een algemene eiwitdatabank.
Deze extra stap voegt robuustheid toe aan het process (eiwitten zijn
evolutionair meer geconserveerd dan DNA).

[sam-umgap]: https://github.com/unipept/umgap

De UMGAP blijkt een waardig alternatief te vormen voor reeds
bestaande programma's, al kan het niet van allen de snelheid en
nauwkeurigheid evenaren. De *pipeline* biedt echter wel interessante
uitbereidingsmogelijkheden betreffende functionele analyse (welke
functies de organismen in het omgevingsstaal kunnen vervullen) en
metatranscriptomics (welke functies de organismen momenteel vervullen,
waarvoor we vertrekken vanaf *RNA reads* in plaats van *DNA reads*).

Als deel van de ontwikkeling van de UMGAP wordt ook een
alternatieve Rust implementatie van FragGeneScan, genaamd
[FragGeneScanRs][sam-fgsrs], voorgesteld. Dit programma vervult een
belangrijke rol in de UMGAP, namelijk het voorspellen van eiwitten (of
genfragmenten) uit *DNA reads*. De bestaande implementaties bleken
onvoldoende snel voor onze toepassing. Het meest gebruikte alternatief,
FragGeneScan-Plus, dat we gedeeltelijk verbeterden in een *fork* genaamd
[FragGeneScan-PlusPlus][sam-fgs++], bevat een aantal moeilijk op te
lossen fouten in de parallellisatie. FragGeneScanRs lost deze problemen
op en werkt tot 22 maal sneller dan de originale implementatie.

[sam-fgsrs]: https://github.com/unipept/FragGeneScanRs
[sam-fgs++]: https://github.com/unipept/FragGeneScanPlusPlus

De UMGAP en de oorspronkelijke Unipept applicatie (de *Unipept
Metaproteomics Analysis Pipeline*, of UMPAP) steunen beide op een
afbeelding van eiwitfragmenten op taxa. Deze afbeelding wordt
berekend uit de UniprotKB, een grote databank van geannoteerde
eiwitten. In hoofdstuk \ref{chapter:on-the-side} omschrijven we
het [proces][sam-database] dat de UniProtKB inleest en de Unipept
databanktabellen opstelt. Om de eiwitfragment-naar-taxonafbeelding
op te stellen, verzamelt het alle taxa waarmee alle eiwitten waarin
elk eiwitfragment voorkomt in de UniProtKB. Het aggregeert elke lijst
van taxa tot een enkel taxon per eiwitfragment via een *lowest common
ancestor*-method: het meest specifieke taxon dat alle taxa uit die lijst
omvat. Hoofdstuk \ref{chapter:on-the-side} omschrijft verder ook nog
bijdragen aan de [SPeDE][sam-spede] en [SMAP][sam-smap] projecten.

[sam-database]: https://github.com/unipept/make-database
[sam-spede]: https://github.com/LM-UGent/SPeDE
[sam-smap]: https://gitlab.com/truttink/smap
[sam-smap2]: https://gitlab.com/dschaumont/smap-haplotype-window
:::

# Software Artefacts {.unnumbered}
\markboth{Software Artefacts}

The focus of this PhD was the development and improvement of
bioinformatics software tools. While this dissertation decribes those
tools and the results of their application, no text can better describe
software than the code by which it is defined. As all tools contributed
to are (to be) freely available and open source, here's a list of the
relevant software repositories.

UMGAP
  ~ https://github.com/unipept/umgap

    The Unipept Metagenomics Analysis Pipeline a collection of tools
    to be composed into a fast and accurate taxonomic identifier for
    shotgun metagenomics reads. Given the DNA found in an environment
    sample, it identifies the organisms found in the sample using
    frequency tables and interactive visualizations.

Unipept's Database Creation
  ~ &nbsp;
  
    https://github.com/unipept/make-database

    Both the Unipept metaproteomics and metagenomics pipelines operate
    on data found in UniProt's database. This collections of scripts
    downloads and processes that database, and others, into the actual
    database tables and indices used by Unipept.

FragGeneScan++
  ~ &nbsp;
  
    https://github.com/unipept/FragGeneScanPlusPlus

    FragGeneScan++ is our fork of the FragGeneScan-Plus project, a
    scalable high-throughput short-read gene predictor implemented in
    C. Since FragGeneScan-Plus was no longer maintained, we took over
    maintainance and fixed a series of bugs. Note that FragGeneScan++
    has since been replaced by FragGeneScanRs.

FragGeneScanRs
  ~ https://github.com/unipept/FragGeneScanRs

    A better and faster implementation of the FragGeneScan gene
    prediction model for short and error-prone reads. It is a *de facto*
    replacement of both FragGeneScan and FragGeneScan-Plus.

SPeDE
  ~ https://github.com/LM-UGent/SPeDE

    A Spectral Dereplication tool developed by the microbiology lab of
    Ghent University. SPeDE can be used to dereplicate large sets of
    MALDI-TOF MS spectra.

SMAP
  ~ https://gitlab.com/truttink/smap

    SMAP is an analysis tool for stack-based NGS read mapping. It
    has several components, including read distribution analysis,
    comparison between two samples sets, and delineation of haplotypes.
    Contributions were made to the SMAP haplotype tool.

SMAP-Haplotype-Window
  ~ (to be published)
  
    https://gitlab.com/dschaumont/smap-haplotype-window

    SMAP-Haplotype-Window is a plugin for SMAP that allows for the
    analysis of sequencing data from CRISPR edited loci. The software
    was analyzed and advice on the development was given.

# List of Publications {.unnumbered}
\markboth{List of Publications}

**Felix Van der Jeugt**, Peter Dawyndt, Bart Mesuere. (submitted).
"FragGeneScanRs: better and faster gene prediction for short reads."
*BMC Bioinformatics*.

**Felix Van der Jeugt**, Rien Maertens, Aranka Steyaert, Pieter
Verschaffelt, Caroline De Tender, Peter Dawyndt and Bart Mesuere.
(submitted). "UMGAP: the Unipept MetaGenomics Analysis Pipeline." *BMC
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
