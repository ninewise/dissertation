### Snap Taxa to a Named Rank

During an analysis, a researcher may be interested in identifications
only at a given rank, e.g. species, or the presence or absence of
certain specific taxa. For this, the `umgap snaptaxon` can be used. It
takes one or more taxon IDs. For each taxon, it searches among its
ancestors if any are of the specified rank (e.g., `-r species`), or are
one of the listed taxa (e.g., `-t 1598 -t 1883`). If so, the taxon is
replaced by the most specific of these matching taxa. Otherwise, it is
mapped to the root of the taxonomy.

#### Usage {#use-snaptaxon}

The input is given on standard input and may be any sequence of FASTA
headers and/or lines containing a single taxon ID. The FASTA headers (if
any) are just copied over to standard output.

The taxonomy to be used is passed as an argument to this command. This
is a preprocessed version of the NCBI taxonomy.

```shell
$ cat input.fa
>header1
888268
186802
1598
1883
$ umgap snaptaxon 2020-04-taxons.tsv -r order < ~/input.fa
>header1
38820
186802
186826
85011
$ umgap snaptaxon 2020-04-taxons.tsv -t 1239 2 < ~/input.fa
>header1
1
1239
1239
2
```

#### Options & Flags {#opts-snaptaxon}

`-h / --help`
  ~ Prints help information

`-i / --invalid`
  ~ Include the invalidated taxa from the taxonomy

`-V / --version`
  ~ Prints version information

`-r / --rank r`
  ~ The rank to snap towards [possible values: superkingdom, kingdom,
    subkingdom, superphylum, phylum, subphylum, superclass, class,
    subclass, infraclass, superorder, order, suborder, infraorder,
    parvorder, superfamily, family, subfamily, tribe, subtribe, genus,
    subgenus, species group, species subgroup, species, subspecies,
    varietas, forma]

`-t / --taxons t...`
  ~ A taxon to snap towards (allow multiple times)
