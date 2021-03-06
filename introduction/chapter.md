# Primer on Metagenomics

## Classifying Life

Upon hearing the term "Animal Kingdom", you might think of either the
jungle or the stories of Reynard the Fox, where the lion rules over the
other animals as King. Or you might be reminded of any other number of
movies, music albums or television series. Often in such stories, the
comparison is made between human and animals, either assigning animal
traits to humans or featuring anthropomorphic animals.

In evolutionary biology, the term "Animal Kingdom", or rather "Kingdom
Animalia", is a classification; a grouping of organisms. It is not the
only kingdom, but perhaps it is, for us humans, the most important
one, since we are part of it. Fortunately, despite calling it a
kingdom, there's no king we all swear fealty to. The other kingdoms are
usually the plants (Plantae), Fungi, Chromista, Protozoa, Archaea and
Bacteria. Why usually? Well, life being life, the borders between these
classifications are a rather gray area and they have been reassigned
often. In fact, the study of naming and classifying groups of organisms
is a whole branch of biology, called taxonomy. Other than discussing
about the number of kingdoms, taxonomists also subdivide kingdoms
in phyla, those in classes, those in orders, and so forth (Figure
\ref{fig:ranks}). Each group of organisms is called a taxon and may
contain any number of other taxa. Kingdom, phyla and class are called
taxonomic ranks. In this work, we use the NCBI taxonomy [@federhen],
a taxonomy with 29 named taxonomic ranks (though at the start of my
PhD, it had only 27), but in between those are many unnamed ranks.
It includes viruses as well as living organisms. The NCBI taxonomy
was chosen mostly for practical reasons, but there are many competing
taxonomies such as Species 2000 [@banki] and Encyclopedia of Life
[@parr].

![Commonly used taxonomic ranks ordered from least to most specific, with the most important for this thesis highlighted.\label{fig:ranks}](ranks.svg){ width=60% }

Each taxon is directly contained by only a single other taxon, called
its parent. All taxa together are thus structured in a tree, sometimes
called the tree of life, with the group containing all organisms as
root of the tree. The taxa containing a taxon, all the way up to the
root, are called its ancestors; and all taxa contained within a taxon
are called its descendants. Do note that this does not necessarily imply a certain
organism of which all these organisms descend (in reproductive sense),
just that they are grouped together because they are showing similar
characteristics.

![A simplified taxonomy describing some birds, both in subset representation (left) and tree representation (right).](./taxonomy.svg){ width=70% }

One of the interesting ranks of grouping organisms is the species,
near the bottom of the taxonomic tree. Whereas most taxa are assigned
subjectively by experienced taxonomists, a species is often defined as
the largest grouping in which every two organisms (of the appropriate
sexes or mating types) can reproduce, with fertile offspring [@mayden].
Still, this definition does not include organisms which reproduce only
asexually, among others.

The first real taxonomy, by Carl Linnaeus [@linnaeus], introduced the
ranked taxa and a naming system for animal and plant species. It was
based on visible characteristics, such as appearance and behavior. After
the evolutionary theory was published by Charles Darwin [@darwin],
classifications would come to reflect common evolutionary descent. In
general, the closer two organisms are to their shared precursor, the
closer they should be in a taxonomy.

The introduction of microscopic organisms into taxonomies has put a
strain on division by visible characteristics. These organisms are
more easily classified by studying their genetic material, carried by
biopolymers.

## The Central Dogma of Molecular Biology

The most well-known carrier of genetic material is without doubt DNA, or
deoxyribonucleic acid (Figure \ref{fig:dna}). A DNA molecule is a long
polymer, formed by a chain of small pairs of monomers. Each DNA monomer,
called a nucleotide, is composed of the sugar 'deoxyribose', a fixed
phosphate group and one of four nucleobases: cytosine (represented by a
C), guanine (G), adenine (A) and thymine (T). Each nucleobase pairs up
with another (cytosine with guanine and adenine with thymine) to form a
base pair, via a hydrogen bond. On the other side, the deoxyribose and
phosphate group bind respectively with the phosphate group of another
monomer, and the deoxyribose of yet another. As such, together, the
deoxyribose-phosphate alternations form two long strands, which spiral
around each other forming a double helix.

![The structure of DNA, uncoiled to two dimensions.\label{fig:dna}](dna.svg){ width=60% }

Because the deoxyribose and the phosphate group are the same for each
monomer, the genetic information in a single strand can be represented
by the sequence of the 4 bases. Furthermore, because the pairs are
fixed, the second strand can be derived from a representation of the
first. The convention is to write down a DNA strand from the end with a
phosphate group (called the 5'-end) towards the end with a deoxyribose
(called the 3'-end). The representing strand is called the forward
strand, and the redundant strand is called the reverse strand. For
example, the DNA fragment in Figure \ref{fig:dna} would be written as
`ACATGG` (with reverse complement `CCATGT` on the reverse strand).

DNA itself is just an information carrier. To perform functions, parts
of the DNA called genes are generally expressed into proteins. DNA is
called protein-coding (or just coding), or alternatively non-coding,
if it encodes for a protein. Depending on the organism, the fraction
of coding versus non-coding DNA wildly varies (for example, the
pufferfish *Takifugu* has 90% non-coding DNA, while the bladderworm
plant *Utricularia gibba* has only 3% non-coding DNA).

To perform gene expression, the DNA is first transcribed into another
polymer called ribonucleic acid (RNA). An enzyme called RNA polymerase
picks onto either strand and starts processing it in the 3' to 5'
direction, as shown in Figure \ref{fig:transcription}. For each
nucleotide, it attaches the complementary nucleotide, thus forming a
copy of the other strand in 5' to 3' direction. The only exception is
that RNA polymerase couples a uracil nucleobase (U) with the adenine
nucleobases in the DNA strand, instead of a thymine. As such, the
resulting RNA polymer is a copy of the opposing DNA strand with T
replaced by U.

![Free RNA nucleotides are complemented to a template DNA strand, forming a single RNA strand. The formed strand is identical to the coding strand, except thymine (T) is replaced by uracil (U) and the deoxyribose is a ribose. The RNA polymerase performing the splitting and matching is not included in the drawing.\label{fig:transcription}](./transcription.svg)

In eukaryotes, RNA splicing can remove some parts of the RNA sequence
(called introns) while keeping the coding regions (called exons). The
spliced parts may not always be the same for the same RNA sequence in
the same organism (called alternative splicing).

After transcription, the resulting RNA can be translated into yet
another polymer called a polypeptide, which then folds into a protein.
This translation is performed by a ribosome. It scans triplets of
nucleotides in the RNA, called codons, starting at the 5'-end, looking
for a start codon (`AUG`). Then, including the start codon, for each
codon up to but excluding a stop codon (`UAA`, `UAG` or `UGA`), it
attaches the corresponding amino acid. The translation table, the
mapping of the $4^3$ codons onto amino acids (or stop codons) as
visualized in Figure \ref{fig:translation-table}, is not the same
for every organism. The constructed protein might still undergo some
post-translational modifications before it performs its functions and
degrades.

![The standard RNA codon table used for translation. Reading a triplet from inside to outside shows the corresponding amino acid, or indicates a stop codon (\*).\label{fig:translation-table}](./translation-table.svg)

In this work, we will be using the UniProt Knowledgebase [UniProtKB,
@magrane] as reference database. UniProt, short for the Universal
Protein Resource, is a comprehensive resource for protein sequence and
annotation data. Their UniProtKB contains more than 200 million proteins
not only annotated with an NCBI taxon identifier, but also linked to EC
numbers, GO terms and InterPro entries. These point to information on
functions in respectively the EBI enzyme database [@alcantara], the Gene
Ontology [@ashburner] and the InterPro database [@blum].

For instance, Uniprot Entry Q9DF66 is the "Snake venom serine
protease 3" protein. It is annotated with Taxon ID 242841, which is
Protobothrops jerdonii or the Jerdon's pitviper. It's linked to EC
number `EC3.4.21.-`, a classifier for all serine endopeptidases (part
of enzymes acting on peptide bonds). The GO numbers are from two of
the three available types (excluding a biological process annotation).
`GO:0004252` refers to a molecular function, serine-type endopeptidase
activity, similar to the EC number. `GO:0005576` refers to a cellular
component, the location relative to cellular structures in which a
gene performs a function. This particular GO term means the function
is performed in an extracellular region (the thing the snake is
biting). `GO:0090729` is also a molecular function: the more general
"toxin activity". Finally, the cross-referenced InterPro entries
are `IPR009003` (Peptidase S1, PA clan), `IPR043504` (Peptidase
S1, PA clan, chymotrypsin-like fold), `IPR001314` (Peptidase S1A,
chymotrypsin family), `IPR001254` (Serine proteases, trypsin domain)
and `IPR018114` (Serine proteases, trypsin family, histidine active
site).

This three-form-two-step process is called the central dogma of
molecular biology. Most organisms follow these steps, but for instance
some bacteria couple the transcription and translation, and some DNA
segments don't translate to proteins but perform their function as RNA.

## Studying Biopolymers

The complete set of an organism's DNA is called its genome, and studying
genomes is called genomics. Genomics aims at a deeper understanding of
organisms by collecting and annotating all of an organism's genes, and
studying their interrelations and influence on the organism.

A genomics study traditionally consists of three parts: sequencing,
assembly and annotation. The first part, sequencing, is the conversion
of physical DNA molecules into their DNA sequence, the order of the
nucleotides in the chain. Current machinery is capable of accurately and
rapidly sequencing DNA molecules of a certain length range (Illumina 50
base pairs (bp) to 500bp, PacBIO 1kbp to several 10kbp, Oxford Nanopore
from 10kbp up to Mbp range, each with differing read error types and
rates), so the DNA fragments are randomly split into shorter fragments
according to the size range fit per instrument. The result of sequencing
is a data set of the DNA sequences of reads, along with some metadata
such as the quality of a read.

Since the DNA molecules were segmented into reads, the next step is
assembling the reads again into the complete genome sequence. When the
sequenced DNA sequence is of an organism closely related to an organism
with a known genome, comparative assembly (read mapping) can be used.
The sequenced reads are mapped onto the reference sequence to form the
new sequence. When there's no reference genome, *de novo* assembly is
used. In *de novo* assembly, an attempt is made to form the complete
genome by overlapping the short reads. As reference, the average fruit
fly, human and SARS-CoV-2 genomes are respectively 139.991 Mbp ($10^6$
base pairs), 2864.1 Mbp and 29882 bp long.

Finally the assembled sequence is annotated. Coding and non-coding
parts are identified, the genes in the coding parts are predicted, the
functions of the genes are analyzed, among other annotations. These
steps are performed manually and automatically (called *in silico*), or
a mixture of both.

Similar to a genome, the collection of an organism's proteins is
called its proteome, with the corresponding study called proteomics.
Since a protein performs a function, studying the proteome of an
organism provides insight in what this organism is doing. Large scale
proteomics studies may follow the same pattern as genomics studies: the
proteins are segmented, often with trypsin. The protein sequence of
these segments, called (tryptic) peptides, is then determined by for
example comparing the measured mass spectrum to a set of predicted mass
spectra. However, since tryptic peptides do not overlap, assembly is not
possible.

Finally, the set of an organism's RNA transcripts is called its
transcriptome, and the corresponding study is called transcriptomics.
The study of a transcriptome provides similar insights to a proteomics
study.

All of these studies are performed on individual organisms. Studying
the genomes, proteomes and transcriptomes of all organisms found in
an environment sample are called metagenomics, metaproteomics and
metatranscriptomics.

In metagenomics, rather than sequencing isolated organisms from
cultivated samples, the DNA is extracted directly from environmental
samples. This has several advantages. First, the cultivation of samples
takes time. Second, cultivation may skew the relative abundance of
organisms in the sample. When extracting DNA without cultivation, the
relative abundance of taxa in the data set is more representative
for the relative abundance of organisms in the sample. This allows
comparative studies of environments over time or location [@metabias].
Third, many organisms cannot currently be cultivated, and as such cannot
be sequenced in genomics [@locey;@rappe;@hugenholtz1998;@hoferthemi].

Metagenomics are especially useful when it comes to studying
microorganisms, since those are so hard to discover and analyse by
conventional means. Nevertheless can they still be used to track DNA of
eukaryotes.

## Targeted and Shotgun Metagenomics

Early sequencing methods for metagenomics methods were based on
(partial) 16S ribosomal RNA sequences [@phylogeny16s]. These short
sequences occur in all prokaryote cells, and contain both highly
conserved (rarely mutating) regions and variable (often mutating)
regions. The conserved regions can be used as primers (markers) to
sequence the 16S rRNA. The variable regions in between the primers
can than be used to differentiate between organisms [@primers16s].
While this makes a powerful tool to identify prokaryote species in a
sample and build phylogenetic trees of these organisms, it does not
help to assemble complete genomes, nor does this work on eukaryotes
(though there are other regions usable for subgroups of eukaryotes).
Furthermore, the short 16S sequence can be subject to horizontal
gene transfer, which makes it less reliable as identifying sequence
[@horizontal16S].

The more recent shotgun metagenomics method [@quince], on the other
hand, uses non-targeted sequencing yielding randomly located short reads
from all genomes in the complete environmental sample. Because reads
from the complete genome are sequenced, shotgun metagenomics allow not
only profiling of the taxonomic composition, but also the functional
potential.

The taxonomic profiling of shotgun metagenomics data
is approached from two angles. First, the reads are
assembled into larger contigs, which are then profiled
[@peng2011;@namiki;@peng2012;@simpson;@boisvert;@pell], often by
aligning the contigs to reference genomes to find the closest match.
To provide sufficiently complete coverage to allow assembly of all
organisms in the sample, much larger data sets are required compared to
genomics (3.3 million genes from 567.7 Gbp sequence data for the human
gut microbiome gene catalog). The amount of data and the repetitions of
DNA within and between (allowing the incorrect assembly of chimeras)
organisms make assembly a hard problem to solve.

<!-- Aurelien 1 -->

Alternatively, the reads are individually partitioned and assigned
to an individual genome [@huson;@brady;@wood2014]. This process is
called binning. By directly classifying the reads, assembly problems
are avoided, less computations are required, and low-abundance
organisms that cannot be assembled *de novo* can still be profiled
[@quince]. After binning, each bin can still be assembled as if the
reads resulted from a genomics sample. Most binning methods work by
comparing DNA properties of reads, such as CG-content (the ratio of C-
or G-nucleotides to A- and T- nucleotides), to the properties of known
genomes.

## Unipept

Unipept is a set of tools for biodiversity and functional analysis
of metaproteomics data sets. It was originally made available as
a web application with a focus on interactive data visualizations
[@mesuere2012;@mesuere2015]. It offers three services.

The **tryptic peptide analysis** service is used to gather information
about a single tryptic peptide. It searches for the proteins this
peptide occurs in and shows the taxonomic lineage for each of these
proteins in a table (Figure \ref{fig:unipept:tpa}). It also reports the
lowest common ancestor taxon (LCA) of all these proteins based on this
lineage table. Finally, since functional annotations were also added
to Unipept [@gurdeep], the tryptic peptide analysis service also lists
the GO terms, EC numbers and InterPro entries linked to the matching
proteins.

![The lineage table of some of the proteins in which the tryptic peptide 'ENFVYLAK' occurs. We call the taxon 'Magnoliopsida' the lowest common ancestor associated with the peptide 'ENFVYLAK' because it is the taxon at the lowest named rank (class for this peptide) which is the same in all lineages.\label{fig:unipept:tpa}](./unipept-lineage-table.png)

The **metaproteome analysis** service applies the tryptic peptide
analysis to a list of tryptic peptides extracted from a sample. For
each peptide, it calculates the lineage-based LCA and the lists of
functional annotations linked to the matching proteins. The LCAs are
visualized in sunbursts, tree maps, heat maps and other interactive
visualizations, giving insight in the biodiversity of the sample (Figure
\ref{fig:unipept:ma}). The lists of functional annotations are added
together and also reported.

![The sunburst visualization of a marine data set. Clicking on any of the arcs zooms in on the corresponding subset of the taxa.\label{fig:unipept:ma}](unipept-sunburst.svg)

Finally, the **peptidome analysis** service offers information about the
complete set of (tryptic) peptides encoded in the proteome of one or
multiple organisms [@peptidome]. The unique peptide finder is an aid
for targeted proteomics. It searches for the disjoint sets of tryptic
peptides that are unique to an single proteome within a list of selected
proteomes. These disjoint sets can then be used as markers for targeted
proteomics experiments. The peptidome clustering, on the other hand,
searches for similarities between the proteomes of, again, a list of
selected organisms. This makes it a very useful tool to, for instance,
detect misclassifications in a taxonomy (Figure \ref{fig:unipept:pa}).

![Peptidome clustering of all 15 *Bacillus anthracis* proteomes and the 3 *Bacillus cereus* reference proteomes of UniProt using the "union" similarity measure.\label{fig:unipept:pa}](unipept-similarity-matrix.png)

Where Unipept started out as a web application, a platform chosen
for its ease of access and user friendliness, the ecosystem has been
extended over the years. An API was added for machine interactions
with Unipept [@unipeptapi]. This has allowed for integration in other
services such as Galaxy [@galaxy] and the development of a command
line interface (CLI) for power users. Furthermore, the web application
was rewritten to be more portable, leading to the release of a desktop
client [@verschaffelt2021] that largely shares the same code base as
the web application, but also supports the use of custom reference
databases.

Running a service such a Unipept as a highly responsive web application
is only possible due to a thoughtfully designed database with proper
indexing and caching of relevant data. In fact, the lowest common
ancestor of all known tryptic peptides and the lists of functional
annotations are precomputed and stored in the database. This is
achieved by preprocessing all proteins in the UniProtKB after it
is released. More details on this process can be found in section
\ref{section:makedatabase}.

## A protein space detour

Given the success of Unipept for metaproteomics, could we reuse the
fast and accurate peptide-to-taxa mapping also for the analysis of
metagenomics data sets? By using a gene (fragment) predictor, a
metagenomics data set can be transformed *in silico* to a metaproteomics
data set. As metagenomics data sets are of much larger volume than
metaproteomics data sets, the Unipept index is wrapped in a local
command line tool to avoid the network bottlenecks of an online tool.
Thus the Unipept Metagenomics Analysis Pipeline, UMGAP for short, is
born, as an experiment to perform a metagenomics biodiversity analysis
by making a detour through a general purpose metaproteomics database.

## Existing tools

Of course, UMGAP is not the first tool for analyzing metagenomics data
sets. In fact, we will evaluate UMGAP by comparing its use, speed
and results to several state-of-the-art metagenomic tools: Kraken
[@wood2014], Kaiju [@menzel] and CLARK [@ounit].

Kraken utilizes a Jellyfish [@jellyfish] database of DNA *k*-mers
(sequences of *k* bases, with *k*=31 by default), and the taxon this
*k*-mer occurs in. This taxon is usually a single organism, but
sometimes it is the lowest common ancestor of several. For every *k*-mer
in a read, this database is queried and the taxa are structured into a
classification tree. Finally, each read is classified as the taxon on
the leaf in this tree with most *k*-mer hits on the path to the root.

Where Kraken 1 uses the concept of minimizers [@minimizers] to speed up
queries into the database, Kraken 2 [@wood2019] further improves on this
method by storing only the minimizers of the *k*-mers rather than the
complete *k*-mer. This greatly reduces storage volume of the database
and improves query speed, at the cost of some specificity and accuracy.

CLARK uses a similar approach as Kraken, but targets a predetermined
taxon rank. It stores only the discriminative *k*-mers at that rank
in the database. This reduces the size of the index, but impacts the
flexibility of the tool.

The authors of Kaiju also recognize the possibilities of protein-level
sequence classification for metagenomic samples. They translate
metagenomic sequencing reads into the six possible reading frames and
search for the number of exact *k*-mer matches in a reference protein
database. A read is classified as the taxon annotated on the protein
with the maximum number of exact matches. A Burrows-Wheeler transform of
the protein database is used for fast exact querying.

Where Kaiju chose for a complete six-frame translation of the
metagenomic reads, which is also an option in UMGAP, we will also be
using an existing gene predictor called FragGeneScan [@rho] to translate
our DNA reads to amino acid sequences. FragGeneScan uses a probabilistic
approach based on a hidden Markov model to find gene fragments in short
and error-prone DNA reads.

## Structure of this dissertation

Chapter \ref{chapter:umgap} describes UMGAP as a whole. It starts
out by describing more context and the general structure of
the pipeline (\ref{section:umgap:intro}). After this, section
\ref{section:umgap:methods} provides details on each step in the
pipeline, with variants on each step grouped together. The results of
the pipeline are evaluated in section \ref{section:umgap:results},
split into an overview of the many possible variants to find
the best configurations (\ref{section:umgap:results:tuning}),
a more in-depth benchmark of a few selected configurations
compared to other tools (\ref{section:umgap:results:benchmark})
and finally a detailed analysis of the misclassifications
UMGAP makes (\ref{section:umgap:results:analysis}). Section
\ref{section:umgap:discussion} presents short discussion on the current
and future state of the pipeline. The chapter concludes with the details
on every tool written to be part of the pipeline, their usage, and some
examples (\ref{section:umgap:tools}).

In chapter \ref{chapter:fgsrs}, we introduce a new implementation
of FragGeneScan, to be used as an improved gene predictor in the
pipeline. Section \ref{section:fgsrs:introduction} provides some
details on the inner workings of FragGeneScan and the problems emerging
in the implementation of FragGeneScan and a variant, FragGeneScan+.
Section \ref{section:fgsrs:implementation} describes our new version,
FragGeneScanRs, and the major differences with FragGeneScan. A
comparison of the results concerning processing speed and memory
footprint is made in \ref{section:fgsrs:results}. Finally, a short
side-step (\ref{section:fgsrs:complete}) discusses the accuracy and
processing speed of FragGeneScanRs on complete genomes, as compared to a
tool meant for gene prediction on complete genomes, Prodigal.

In chapter \ref{chapter:in-practice}, we include some of the metawork
on the pipeline, such as the improved construction of the Unipept (and
UMGAP) index and a few walkthroughs describing the usage of UMGAP in
other studies. Finally, in chapter \ref{chapter:related-work}, I shortly
detail some related work done during my PhD.
