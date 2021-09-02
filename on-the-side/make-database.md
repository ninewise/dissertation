## Constructing the database

The core components of Unipept and the UMGAP both depend on a mapping of
peptides to taxonomic identifiers. To construct such a mapping, and to
have it be generic enough to recognize a wide variety of peptides, it
needs to be based on a vast amount of data. The UniProt Knowledgebase
[@magrane], the central hub for functional annotation on proteins, is
used for this purpose.

### Extracting the Unipept Database

To build a performant application, the data from the UniprotKB
is parsed, extracted, preprocessed and stored in a relational
database. This database is then queried by the Unipept web application
[@mesuere2012] and, more recently, the Unipept Desktop Client
[@verschaffelt2021].

TODO Tekstuele omschrijving van de verschillende stappen in de makefile, tesamen met een figuur die de structuur omschrijft.

### Creating a UMGAP index

From this complete database, only a three tables are of interest to the
UMGAP tool. First, as the UMGAP is a taxonomic identification tool,
is the processed NCBI taxonomy `taxons`. Second is the `sequence`
table, which contains the mapping of tryptic peptides unto their lowest
common ancestor. Third is the `uniprot_entries` table, which contains
amongst other columns the protein sequence and the assigned taxon of the
original Uniprot entry. The latter is used for the construction of the
*k*-mer-to-taxon mapping.

While a relational database is fast enough for a metaproteomics tool,
it does not suffice for a metagenomics tool, which is expected to
handle much larger amounts of data. This is especially true for the the
*k*-mer-to-taxon mapping, the construction of which is too slow for the
Java code used for the tryptic peptide mapping.

Three additional tools were written to construct an index file for the
`umgap pept2lca` tool, with an extra one for debugging. The first tool
is the `umgap splitkmers` command, which takes tab-separated taxon IDs
and protein sequences and outputs all *k*-mers in each protein sequence
alongside the taxon ID. The second tool is the `umgap joinkmers` tool,
which consumes an alphabetically sorted stream of peptides alongside
taxon IDs, and outputs each peptide once, together with a taxon ID
aggregated from all taxon IDs found together with this peptide. Between
the second and first tools, the GNU sort command groups together the
peptides. Finally, the `umgap buildindex` command builds a single
compressed index file which is then used by the `umgap pept2lca` tool.
The `umgap printindex` tool decompresses such an index file back to the
input of `buildindex` for debugging purposes.

TODO describe the index mechanism

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
