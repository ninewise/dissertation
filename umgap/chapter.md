# The Unipept Metagenomics Analysis Pipeline {pageheading="UMGAP"}
\label{chapter:umgap}

Shotgun metagenomics is now commonplace to gain insights into
communities from diverse environments, but fast, memory-friendly, and
accurate tools are needed for deep taxonomic analysis of the metagenome
data. To meet this need we developed UMGAP, a highly versatile open
source command line tool implemented in Rust for taxonomic profiling of
shotgun metagenomes. It differs from state-of-the-art tools in its use
of protein code regions identified in short reads for robust taxonomic
identifications, a broad-spectrum index that can identify both archaea,
bacteria, eukaryotes and viruses, a non-monolithic design, and support
for interactive visualizations of complex biodiversities.[^foot:umgap]

[^foot:umgap]: This chapter is based on the article: Felix Van der
Jeugt, Rien Maertens, Aranka Steyaert, Pieter Verschaffelt, Caroline
De Tender, Peter Dawyndt and Bart Mesuere. *Under review*. "UMGAP: the
Unipept MetaGenomics Analysis Pipeline." *BMC Genomics*.

## [paper](paper.md){.include}

## Overview of UMGAP Tools
\label{section:tools}

A pipeline is composed of a series of command line tools. This section
contains an exhaustive list of the available tools. For each tool, it
describes the intended use, shows some examples, and finally lists the
available options to change its behavior.

### [fastq2fasta](components/fastq2fasta.md){.include}

### [translate](components/translate.md){.include}

### [fragmentation](components/fragmentation.md){.include}

### [filter](components/filter.md){.include}

### [filter](components/pept2lca.md){.include}

### [bestof](components/bestof.md){.include}

### [seedextend](components/seedextend.md){.include}

### [uniq](components/uniq.md){.include}

### [taxa2agg](components/taxa2agg.md){.include}

### [snaptaxon](components/snaptaxon.md){.include}

### [reporting](components/reporting.md){.include}

### [taxonomy](components/taxonomy.md){.include}
