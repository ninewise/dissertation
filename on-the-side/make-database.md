## Bouwen van de index

### De algemene databank

de makefile

### De UMGAP index

umgap splitkmers, joinkmers, buildindex, printindex en het script dat
deze allemaal aan elkaar hangt.

To build an index file for the `umgap pept2lca` tool, we have four tools
working together, and one extra for debugging. The first tool is the
`umgap splitkmers` command, which takes tab-separated taxon IDs and
protein sequences and outputs the *k*-mers mapped to the taxon IDs. The
second tool isn't an UMGAP tool, but the GNU sort command. It's used
to sort the output of the previous command alphabetically. This sorted
output is can be consumed by the `umgap joinkmers` command ...

#### Usage `splitkmers` TODO

The input is given on standard input and should be a TSV formatted stream of taxon IDs and a protein sequence from this taxon. The output will be written to standard output and consists of a TSV formatted stream of k-mers mapped to the taxa in which they occur. The k-mer length is configurable with the -k option, and is 9 by default.

This output stream is ready to be grouped by K-mer by sorting and then aggregated into a searchable index, with the sort, umgap joinkmers and umgap buildindex commands.

$ cat input.tsv
654924	MNAKYDTDQGVGRMLFLGTIGLAVVVGGLMAYGYYYDGKTPSSGTSFHTASPSFSSRYRY
176652	MIKLFCVLAAFISINSACQSSHQQREEFTVATYHSSSICTTYCYSNCVVASQHKGLNVESYTCDKPDPYGRETVCKCTLIKCHDI
$ umgap splitkmers < input.tsv
MNAKYDTDQ	654924
NAKYDTDQG	654924
AKYDTDQGV	654924
KYDTDQGVG	654924
YDTDQGVGR	654924
...
SPSFSSRYR	654924
PSFSSRYRY	654924
MIKLFCVLA	176652
IKLFCVLAA	176652
KLFCVLAAF	176652
...
-h / --help
Prints help information
-V / --version
Prints version information
-k / --length k
The k-mer length [default: 9]
-p / --prefix p
Print only the (k-1)-mer suffixes of the k-mers starting with this character
