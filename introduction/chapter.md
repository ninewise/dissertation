# Introduction

(10 pagina's bare minimum)

## Taxonomies - Classifying life

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
kingdom, phyla and class are called taxonomic ranks. In this work, we
will be using a taxonomy with 29 named taxonomic ranks (though at the
start of my PhD, it had only 27), but in between those are many unnamed
ranks. The used taxonomy includes viruses as well as organisms.

Each taxon is directly contained by only a single other taxon, called
its parent. All taxa together are thus structured in a tree, sometimes
called the tree of life, with the group containing all organisms as
root of the tree. The taxa containing a taxon, all the way up to the
root, are called its ancestors; and all taxa contained within a taxon
are called its descendants. Do note that this does not imply a certain
organism of which all these organisms descend (in reproductive sense),
just that they are grouped together because they are showing similar
characteristics.

<!-- TODO tekening tree of life? -->

One of the interesting ranks of grouping organisms is the species,
near the bottom of the taxonomic tree. Whereas most taxa are assigned
subjectively by experienced taxonomists, a species is often defined as
the largest grouping in which every two organisms (of the appropriate
sexes or mating types) can reproduce, with fertile offspring. Still,
this definition does not include organisms which reproduce only
asexually, among others.

The first real taxonomy, by Carl Linnaeus (TODO ref), introduced the
ranked taxa and a naming system for animal and plant species. It was
based on visible characteristics, such as appearance and behavior. After
the evolutionary theory was published by Charles Darwin (TODO ref),
classifications would come to reflect common evolutionary descend. In
general, the closer two organisms are to their shared precursor, the
more grouped they are in a taxonomy.

The introduction of microscopic organisms into taxonomies puts a strain
on division by visible characteristics. These organisms are more easily
classified by studying their genetic material, carried by biopolymers.

## The Central Dogma of molecular biology

The most well-known carrier of genetic material is without doubt DNA, or
Deoxyribonucleic acid (Figure \ref{fig:dna}). A DNA molecule is a long
polymer, formed by a chain of small pairs of monomers. Each DNA monomer,
called a nucleotide, is composed of the sugar 'deoxyribose', a fixed
phosphate group and one of four nucleobases: cytosine (represented by a
C), guanine (G), adenine (A) and thymine (T). Each nucleobase pairs up
with another (cytosine with guanine and adenine with thymine) to form a
base pair, via a hydrogen bond. On the other side, the deoxyribose and
phosphate group bond respectively with the phosphate group of another
monomer, and the deoxyribose of yet another. As such, together, the
deoxyribose-phosphate alternations form two long strands, which spiral
around each other forming a double helix.

![The structure of DNA, flattened to two dimensions.\label{fig:dna}](dna.svg){ width=50% }

Because the deoxyribose and the phosphate group are the same for each
monomer, the genetic information in a single strand can be represented
by the sequence of the 4 bases. Furthermore, because the pairs are
fixed, the second strand can be derived from a representation of the
first. The convention is to write down a DNA strand at the end with a
phosphate group (called the 5'-end) towards the end with a deoxyribose
(called the 3'-end). The representing strand is called the forward
strand, and the redundant strand is called the reverse strand. For
example, the DNA fragment in Figure \ref{fig:dna} would be written as
`ACATGG` (with reverse complement `CCATGT` on the reverse strand).

DNA itself is just a carrier of information. To perform functions,
parts of the DNA called genes are generally expressed into proteins.
DNA is called protein-coding (or just coding), or alternatively
non-coding, if it encodes a protein. Depending on the organism, the
fraction of coding versus non-coding DNA wildly varies (for example,
the pufferfish *Takifugu* has 90% non-coding DNA, while the bladderworm
plant *Utricularia gibba* as only 3% non-coding DNA).

To perform gene expression, the DNA is first transcribed into another
polymer called Ribonucleic Acid (RNA). An enzyme called RNA polymerase
picks onto either strand and starts processing it in the 3' to
5' direction. For each nucleotide, it attaches the complementary
nucleotide, thus forming a copy of the other strand in 5' to 3'
direction. The only exception is that RNA polymerase couples a uracil
nucleobase (U) with the adenine nucleobases in the DNA strand, instead
of a thymine. As such, the resulting RNA polymer is copy of the opposing
DNA strand with T replaced by U.

After transcription, the resulting RNA can be translated into yet
another polymer called a polypeptide, which then folds into a protein.
This translation is performed by a ribosome. It scans triplets of
nucleotides in the RNA, called a codon, starting at the 5'-end, looking
for a start codon. Then, for each codon up to a stop codon, it attaches
the corresponding amino acid. The translation table, the mapping of the
$4^3$ codons onto amino acids, is not the same for every organism.

## Studying genetic codes

* Studies regarding DNA/RNA/proteins
  - genomics & metagenomics
  - scanproblemen -> shotgun metagenomics (concept read) (oplijsting machines, volumes)
  - proteomics & metaproteomics
  - scanproblemen -> I/L equation
  - transcriptomics & metatranscriptomics

## Existing Metagenomics Tools

* Existing metagenomics methods/tools
  - assembly: binning werkt niet goed met meer soorten
  - meest gangbare methoden

Conclusie: er zijn veel strategiën, ze werken allemaal op DNA.

## Unipept

*  Unipept

## Metagenomics via eiwitten

Unipept werkt heel goed via eiwitten, we gaan de Unipept strategie proberen toepassen op reads.

(outline thesis)

* umgap als nog een tool + test of we kunnen de omweg nemen
* er is een prediction step, fraggenescan was te traag
* een paar case studies om te gebruiken in de praktijk
* andere dingen
