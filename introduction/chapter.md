# Introduction

## Classifying life

<!-- TODO rename primer on metagenomics? 
start with definition of metagenomics, close in on terms -->

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
kingdom, there's no king we all are fealty to. The other kingdoms are
usually the plants (Plantae), Fungi, Chromista, Protozoa, Archaea and
Bacteria. Why usually? Well, life being life, the borders between these
classifications are a rather gray area and they have been reassigned
often. In fact, the study of naming and classifying groups of organisms
is a whole branch of biology, called taxonomy. Other than discussing
about the number of kingdoms, taxonomists also subdivide kingdoms in
phyla, those in classes, those in orders, and so forth. Each group of
organisms is called a taxon and may contain any number of other taxa.
Kingdom, phyla and class are called taxonomic ranks. In this work, we
use the NCBI taxonomy [@federhen], a taxonomy with 29 named taxonomic
ranks (though at the start of my PhD, it had only 27), but in between
those are many unnamed ranks. It includes viruses as well as living
organisms. The NCBI taxonomy was chosen mostly for practical reasons,
but there are many competing taxonomies such as the Species 2000
[@banki] and Encyclopedia of Life [@parr] taxonomies.

Each taxon is directly contained by only a single other taxon, called
its parent. All taxa together are thus structured in a tree, sometimes
called the tree of life, with the group containing all organisms as
root of the tree. The taxa containing a taxon, all the way up to the
root, are called its ancestors; and all taxa contained within a taxon
are called its descendants. Do note that this does not imply a certain
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
classifications would come to reflect common evolutionary descend. In
general, the closer two organisms are to their shared precursor, the
closer they should be in a taxonomy.

The introduction of microscopic organisms into taxonomies has put a
strain on division by visible characteristics. These organisms are
more easily classified by studying their genetic material, carried by
biopolymers.

## The central dogma of molecular biology

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

![The structure of DNA, uncoiled to two dimensions.\label{fig:dna}](dna.svg){ width=50% }

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
if it encodes a protein. Depending on the organism, the fraction
of coding versus non-coding DNA wildly varies (for example, the
pufferfish *Takifugu* has 90% non-coding DNA, while the bladderworm
plant *Utricularia gibba* as only 3% non-coding DNA).

<!-- TODO image coding density, include genome size -->

To perform gene expression, the DNA is first transcribed into another
polymer called ribonucleic acid (RNA). An enzyme called RNA polymerase
picks onto either strand and starts processing it in the 3' to
5' direction. For each nucleotide, it attaches the complementary
nucleotide, thus forming a copy of the other strand in 5' to 3'
direction. The only exception is that RNA polymerase couples a uracil
nucleobase (U) with the adenine nucleobases in the DNA strand, instead
of a thymine. As such, the resulting RNA polymer is copy of the opposing
DNA strand with T replaced by U.

<!-- TODO mRNA? but it's not all mRNA? ask Caroline to check -->

![Free RNA nucleotides are complemented to a template DNA strand, forming a single RNA strand. The formed strand is identical to the coding strand, except thymine (T) is replaced by uracil (U) and the deoxyribose is a ribose. The RNA polymerase performing the splitting and matching is not included in the drawing.](./transcription.svg)

After transcription, the resulting RNA can be translated into yet
another polymer called a polypeptide, which then folds into a protein.
This translation is performed by a ribosome. It scans triplets of
nucleotides in the RNA, called a codon, starting at the 5'-end, looking
for a start codon. Then, for each codon up to a stop codon, it attaches
the corresponding amino acid. The translation table, the mapping of the
$4^3$ codons onto amino acids (or stop codons), is not the same for
every organism.

![The standard RNA codon table used to translation. Reading a triplet from inside to outside shows the corresponding amino acid, or indicates a stop codon (\*).\label{fig:translation-table}](./translation-table.svg)

This three-form-two-step process is called the central dogma of
molecular biology. Most organisms follow these steps, but for instance
some bacteria blend the transciption and translation into a single step,
and some DNA segments don't translate to proteins but perform their
function as RNA.

<!-- TODO? image central dogma -->

## Studying biopolymers

The complete set of an organism's DNA is called its genome, and studying
genomes is called genomics. A genomics study traditionally consists
of three parts: sequencing, assembly and annotation. The first part,
sequencing, is the conversion of physical DNA molecules into their DNA
sequence, the order of the nucleotides in the chain. Current machinery
is incapable of accurately and rapidly sequencing complete molecules.
The DNA molecules are first split into shorter segments, called reads.
These reads can vary in length from 100 base pairs up to a few 10.000
base pairs, depending on the used sequencing technology, with various
read error types and rates. The result of sequencing is a data set of
the DNA sequences of reads, along with some metadata such as the quality
of a read.

<!-- TODO mention genome / read set size -->

Since the DNA molecules were segmented into reads, the next step is
assembling the reads again into the complete genome sequence. When the
sequenced DNA sequence is of an organism closely related to an organism
with a known genome, comparative assembly (read mapping) can be used.
The sequenced reads are mapped onto the reference sequence to form the
new sequence. When there's no reference genome, *de novo* assembly is
used. In *de novo* assembly, an attempt is made to form the complete
genome by overlapping the short reads.

Finally the assembled sequence is annotated. Coding and non-coding
parts are identified, the genes in the coding parts are predicted, the
functions of the genes are analyzed, among other annotations. These
steps are performed manually and automatically (called *in silico*), or
a mixture of both.

Similar to a genome, the collection of an organism's proteins is
called its proteome, with the corresponding study called proteomics.
Large scale proteomics studies may follow the same pattern as genomics
studies: the proteins are segmented, often with trypsin. The protein
sequence of these segments, called (tryptic) peptides, is then
determined by for example comparing the measured mass spectrum to a
set of predicted mass spectra. However, since tryptic peptides do not
overlap, assembly is not possible.

Finally, the set of an organism's RNA is called its transcriptome, and
the corresponding study is called transcriptomics.

All of these studies are performed on individual organisms. Studying
the genomes, proteomes and transcriptomes of all organisms found in
an environment sample are called metagenomics, metaproteomics and
metatranscriptomics.

In metagenomics, rather than sequencing isolated organisms from
cultivated samples, the DNA is extracted directly from environmental
samples. This has several advantages. First, the cultivation of samples
takes time. Second, cultivation may skew the relative abundance of
organisms in the sample. When extracting DNA without cultivation, the
relative abundance of taxa in the data set is representative for the
relative abundance of organisms in the sample. This allows comparative
studies of environments over time or location. Third, many organisms
cannot currently be cultivated, and as such cannot be sequenced in
genomics [@locey;@rappe;@hugenholtz1998;@hoferthemi].

<!-- TODO afbeelding who what 3-pijl-cirkel meta-omics -->

## Existing metagenomics methods

Early metagenomics methods were based on the 16S ribosomal RNA
sequences. These short sequences occuring in prokaryote cells contain
both highly conversative (rarely mutating) regions and often mutating
regions. The conserved regions can be used as primers (markers) to find
and sequence the 16S rRNA. While this serves to identify prokaryote
species in a sample, it does not help to assemble complete genomes, nor
does this work on eukaryotes.

The more recent shotgun metagenomics, on the other hand, use sequencers
yielding randomly located short reads from the complete environmental
sample. To provide sufficiently complete coverage to allow assembly of
all organisms in the sample, much larger (TODO numbers) data sets are
required compared to genomics. The amount of data and the repetitions
of DNA within and between (allowing the incorrect assembly of chimeras)
organisms make assembly a hard problem to solve.

To simplify assembly, reads are partioned and assigned to an individual
genome. This process is called binning. Afterwards, each bin can be
assembled as if the reads resulted from a genomics sample. Most binning
methods work by comparing DNA properties of reads, such as CG-content
(the ratio of C- or G-nucleotides to A- and T- nucleotides), to the
properties of known genomes.

## Unipept

<!-- TODO references, you can list the references you coauthored at the start of this chapter -->

Unipept is an set of tools for the biodiversity and functional analysis
of metaproteomics data sets. It is based on a mapping of tryptic
peptides, the most common protein fragment used in metaproteomics,
onto the smallest taxon grouping all organisms the tryptic peptide is
found in, called the lowest common ancestor. This mapping is created by
processing an extensive list of organisms and their proteome.

Using such a mapping, Unipept can quickly construct ranked frequency
tables of taxa for all tryptic peptides uploaded. These tables are
presented in clear visualizations, providing insight in the biodiversity
of the sample.

<!-- TODO vermelden dat functional analysis ook kan (of volgende sectie) maar enkel potential toont, zeggen dat wij enkel biodiversity doen -->

<!-- TODO minder highlevel -->

<!-- TODO overlopen van web/cli/desktop -->

<!-- TODO stuk over uniprot (volledige databank ipv selectie) -->

## Metagenomics via metaproteomics

Given the success of Unipept for metaproteomics, could its analysing
strategies prove useful for metagenomics as well? By using a gene
predictor, a metagenomics sample can be transformed *in silico* to a
metaproteomics data set. As metagenomics data sets are of much larger
volume than metaproteomics data sets, the Unipept index is wrapped in a
local command line tool to avoid the network bottlenecks of an online
tool. Thus the Unipept Metagenomics Analysis Pipeline is born.

In chapter \ref{chapter:umgap}, we describe the complete pipeline
and evaluate it as an alternative method of metagenomics analysis.
In chapter \ref{chapter:fgsrs}, we introduce a new implementation of
FragGeneScan, to be used as an improved gene predictor in the pipeline.
In chapter \ref{chapter:on-the-side}, we include some of the metawork
on the pipeline, such as the improved construction of the Unipept (and
UMGAP) index and a few walkthroughs describing the usage of the UMGAP in
other studies.

<!-- TODO more active phrasing -->
