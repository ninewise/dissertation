### Fragmentation of proteins

De UMGAP maakt gebruik van *exact matching* op korte eiwitfragmenten
om delen van *reads* te kunnen identificeren en zodoende een conclusie
te trekken over de volledige *read*. Hiervoor worden de tools `umgap
prot2tryp` en `umgap prot2kmer` voorzien. De eerste voorziet een *in
silico tryptic digest* om de eiwitten op te splitsen in fragmenten van
variabele lengte, op basis van een vast patroon. De tweede zal alle
(overlappende) fragmenten van een vaste lengte opbrengen.

#### Usage

The input is given in a FASTA format on standard input with a single
peptide per FASTA header, which may be hardwrapped with newlines. The
peptides resulting from the fragmentation are written in FASTA format to
standard output, with multiple peptides per FASTA header, separated by
newlines.

```sh
$ cat long.fa
>header1
AYKKAGVSGHVWQSDGITNCLLRGLTRVKEAVANRDSGNGYINKVYYWTVDKRATTRDALDAGVDGIMTNYPDVITDVLN
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

#### Options & flags for `prot2tryp`

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

#### Options & flags for `prot2kmer`

The *k*-mer length is configurable with the `-k` option, and is 9 by
default.

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-k / --length k`
  ~ The *k*-mer length [default: 9]

