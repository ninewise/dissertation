### Identifying peptides

De kerntaak van de UMGAP is het identificeren van peptiden. Desondanks
is dit een ogenschijnlijk eenvoudige stap. Het `umgap pept2lca` commando
zal, gegeven een indexbestand, peptiden opzoeken in dit bestand en het
overeenkomstige taxon-ID (standaard de lowerst common ancestor van
alle eiwitte in de brondatabank waar we dit peptide in terugvinden)
teruggeven.

Het opzoeken van peptiden in de index is echter de traagste stap van
de hele *pipeline*. Dit commando voorziet dan ook vlaggen om de index
in het geheugen te laden (om er sneller toegang toe te hebben) en
is intern geparallelliseerd. Daarnaast zijn er ook 2 gecombineerde
commando's, `umgap prot2tryp2lca` en `umgap prot2kmer2lca` die dit
commando samenvoegen met de `umgap prot2pept` en `umgap prot2kmer`
commando's om de *overhead* komende bij het uitschrijven van de peptiden
te vermijden.

#### Usage

For all three commands, the input is given in a FASTA format on
*standard input*. The `pept2lca` command accepts multiple sequences
(peptides) per FASTA header, each on a line. In the following example
we match tryptic peptides on their lowest common ancestor in the NCBI
taxonomy.

```sh
$ cat input.fa
>header1
AAALTER
ENFVYLAK
$ umgap pept2lca tryptic-peptides.index < input.fa
>header1
2
3398
```

This selfsame result could come from the combined `prot2tryp2lca`
command, which accepts only a single sequence per FASTA header. This
sequence in split in tryptic peptides before index lookup.

```sh
$ cat input.fa
>header1
AAALTERENFVYLAK
$ umgap prot2tryp2lca tryptic-peptides.index < input.fa
>header1
2
3398
```

By default, sequences not found in the index are ignored. Using the -o
(--on-on-one) flag, they are mapped to 0, instead.

```sh
$ cat input.fa
>header1
NOTATRYPTICPEPTIDE
ENFVYLAK
$ umgap pept2lca -o tryptic-peptides.index < input.fa
>header1
0
3398
```

The `prot2kmer2lca` command follows a similar interface to the
`prot2tryp2lca` command, but uses the overlapping *k*-mers from the
`prot2kmer` command.

```
$ cat input.fa
>header1
DAIGDVAKAYKKAG*S
$ umgap prot2kmer2lca -k9 uniprot-2020-04-9mer.index < input.fa
>header1
571525
571525
6920
6920
1
6920
```

Because the index files for the `prot2kmer2lca` command are of
considerable size, searching them can be slow. When memory mapped, it
can take some time for the index to be searched. With the -m flag,
the complete index will be loaded in memory before operation. This,
too, takes some time, but for a single large analysis, this impact is
irrelevant compared to the time of analysis. When processing many short
files, the index would need to be loaded again and again. Instead of
using this command as part of a pipeline, `... | umgap prot2kmer2lca
index | ...`, it can run in a separate (and persistent) process, reusing
the same loaded index. Run `umgap prot2kmer2lca -m -s umgap-socket
index` as a service, and when the index is loaded, change your original
pipeline(s) to communicate with the socket using OpenBSD's netcat: `...
| nc -NU /path/to/umgap-socket | ...`.

#### Options & flags for `pept2lca`

`-m / --in-memory`
  ~ Load index in memory instead of memory mapping the file contents.
    This makes querying significantly faster, but requires some
    initialization time.

`-h / --help`
  ~ Prints help information

`-o / --one-on-one`
  ~ Map unknown sequences to 0 instead of ignoring them

`-V / --version`
  ~ Prints version information

`-c / --chunksize c`
  ~ Number of reads grouped into one chunk. Bigger chunks decrease the
    overhead caused by multithreading. Because the output order is
    not necessarily the same as the input order, having a chunk size
    which is a multiple of 12 (all 6 translations multiplied by the two
    paired-end reads) will keep FASTA records that originate from the
    same reads together [default: 240]


#### Additional options & flags for `prot2tryp2lca`

`-k / --keep k`
  ~ Amino acid symbols that a peptide must contain to be processed [none
    by default]

`-d / --drop d`
  ~ Amino acid symbols that a peptide may not contain to be processed
    [none by default]

`-L / --maxlen L`
  ~ Maximum length allowed [default: 50]

`-l / --minlen l`
  ~ Minimum length required [default: 5]

`-p / --pattern p`
  ~ The cleavage-pattern (regex), i.e. the pattern after which the
    next peptide will be cleaved for tryptic peptides) [default:
    `([KR])([^P])`]


#### Additional options & flags for `prot2kmer2lca`

`-l / --length l`
  ~ The length of the k-mers in the index [default: 9]

`-s / --socket socket`
  ~ Instead of reading from stdin and writing to stdout, create a Unix
    socket to communicate with using OpenBSD's netcat (`nc -NU socket`).
    This is especially useful in combination with the `--in-memory`
    flag: you only have to load the index in memory once, after which
    you can query it without having the loading time overhead each time