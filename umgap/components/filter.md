### Filtering peptides

Tijdens de verwerking van peptiden kan het gewenst zijn om bepaalde
peptiden te schrappen. Zo zullen zeer korte peptiden heel algemeen
voorkomen, en dus geen informatie bijdragen aan de read (Figure
\ref{peptide-length}). Met `umgap filter` kunnen peptiden geschrapt
worden op basis van lengte of inbegrepen en uitgesloten aminozuren.

#### Usage

The input is given in FASTA format on standard input. Per FASTA header,
there may be multiple peptides separated by newlines. Each of these
peptides are checked against the filter criteria and written to standard
output they pass them. The criteria are specified as options:

* `-m 5` sets the minimum length of the peptides to 5.

* `-M 50` sets the maximum length of the peptides to 50.

* `-c LIK` requires the peptides to contain amino acids Leucine (L),
  Isoleucine (I) and Lysine (K).

* `-l LIK` removes the peptides containing the amino acids Leucine,
  Isoleucine or Lysine.

```sh
$ cat input.fa
>header1
AYKKAGVSGHVWQSDGITNCLLRGLTRVKEAVANRDSGNGYINKVYYWTVDKRATTRDALDAGVDGIMTNYPDVITDVLN
AYK
K
AGVSGHVWQSDGITNCLLR
GLTR
VK
EAVANR
DSGNGYINK
$ umgap filter < input.fa
>header1
AGVSGHVWQSDGITNCLLR
EAVANR
DSGNGYINK
$ umgap filter -m 0 -c R -l K < input.fa
>header1
AGVSGHVWQSDGITNCLLR
GLTR
EAVANR
```

#### Options & flags

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-c / --contains c`
  ~ Amino acid symbols that a sequence must contain [none by default]

`-l / --lacks l`
  ~ Amino acid symbols that a sequence may not contain [none by default]

`-M / --maxlen M`
  ~ Maximum length allowed [default: 50]

`-m / --minlen m`
  ~ Minimum length required [default: 5]
