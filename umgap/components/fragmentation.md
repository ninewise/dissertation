### Protein Fragmentation {#protein-fragmentation-component}

UMGAP uses exact string matching on short protein fragments to identify
parts of reads and aggregate those into a conclusion for the whole read.
The `umgap prot2tryp` and `umgap prot2kmer` provide such fragmentation.

The first splits protein sequence into variable length peptides, based
on a pattern in the sequence. The default pattern is an *in silico*
tryptic digest, as UMGAP originates in a metaproteomics context, where
trypsin is *de facto* standard. The latter yields all overlapping
peptides of a fixed length, called *k*-mers.

#### Usage {#use-fragmentation}

The input is given in a FASTA format on standard input with a single
peptide per FASTA header, which may be hard wrapped with newlines. The
peptides resulting from the fragmentation are written in FASTA format to
standard output, with multiple peptides per FASTA header, separated by
newlines.

```shell
$ cat long.fa
>header1
AYKKAGVSGHVWQSDGITNCLLRGLTRVKEAVANRDSGNG
YINKVYYWTVDKRATTRDALDAGVDGIMTNYPDVITDVLN
$ umgap prot2tryp tryptic-lca.index < long.fa
>header1
AYK
K
AGVSGHVWQSDGITNCLLR
GLTR
VK
EAVANR
DSGNGYINK
VYYWTVDK
R
ATTR
DALDAGVDGIMTNYPDVITDVLN
$ cat short.fa
>header1
DAIGDVAKAYKKAG*S
$ umgap prot2kmer < short.fa
>header1
DAIGDVAKA
AIGDVAKAY
IGDVAKAYK
GDVAKAYKK
DVAKAYKKA
VAKAYKKAG
AKAYKKAG*
KAYKKAG*S
```

#### Options & Flags for `prot2tryp`

Using the `-p` flag, you can change the splitting pattern. The default
pattern `([KR])([^P])` splits between any Lysine (K) or Arginine (R),
followed by any amino acid that is not Proline (P).

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-p / --pattern p`
  ~ The cleavage-pattern (regex), i.e. the pattern after which the
    next peptide will be cleaved for tryptic peptides) [default:
    `([KR])([^P])`]

#### Options & Flags for `prot2kmer`

The *k*-mer length is configurable with the `-k` option, and is 9 by
default.

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-k / --length k`
  ~ The *k*-mer length [default: 9]
