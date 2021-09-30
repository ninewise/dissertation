# The Unipept Metagenomics Analysis Pipeline {pageheading="The UMGAP"}

This chapter starts with describing the intent and structure of the
pipeline (\ref{section:intent}). After, it includes a report on the
context and results (\ref{section:umgap}). Finally, it provides an
extensive list of the various tools in the pipeline, explaining their
usage and some of the algorithms they use (\ref{section:tools}).

## Intent and structure
\label{section:intent}

The analysis of shotgun metagenomics data can be subdivided in two
dimensions. First, as a sequence of individual reads to be analyzed, and
second, as a sequence of steps each read is analyzed by.

Shotgun metagenomics data is traditionally saved in FASTA and FASTQ
files. These formats are long sequences of reads, each with a header and
data. In biodiversity analysis, each of these reads can be processed
individually. After fully processing individual reads, for final
aggregation, the reads must be brought together again, for instance to
create a frequency table. This suggests subdividing the data per read.

This dimension of subdivision gives the opportunity for easy
parallelization, following a map-reduce strategy. Each
read can be processed in a separate thread, with little to no
parallelization overhead. This allows realization of the full power of
the executing machine.

The other dimension of subdivision, as a sequence of analysis steps,
allows for better optimization of each step. After all, a program
given a single task can specialize and can share the cost of a possibly
slow initialization step over all reads it will process. Parallelization
is still possible with this subdivision, though less efficient, by
running each step in a separate process, passing along reads after a
process has finished its task. However, this manner of subdivision has
the added benefit of modularity: with analysis steps as a top-level
concept, steps can easily be added, skipped and exchanged to modify the
type of analysis.

The UMGAP has chosen the second dimension of subdivision as primary
subdivision. Each analysis step was programmed as a separate subcommand
of the `umgap` executable, sharing a single source code tree. Each step
runs in a process, chained together using UNIX pipes, passing the reads
via standard output and standard input in FASTA-like formats.

## [paper](paper.md){.include}

## Analysis tools
\label{section:tools}

A pipeline is compromised of a series of tools. This section contains
an exhaustive list of the available tools. For each tool, it describes
the intended use, shows some examples, and finally lists the available
options to change its behavior.

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
