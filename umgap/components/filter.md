### Peptide filtering {#peptide-filtering-component}

Some protein fragments or peptides may be useless or detrimental to the
analysis. For instance, short tryptic peptides are very common and won't
add any information to a read (Figure \ref{peptide-length}). Removing
them from consideration speeds up the pipeline. With `umgap filter`,
reads can be filtered on minimum length, maximum length, included amino
acids and excluded amino acids.

#### Usage {#use-filter}

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

```shell
$ cat input.fa
>header1
AYKKAGVSGHVWQSDGITNCLLRGLTRVKEAVANRDSGNG
YINKVYYWTVDKRATTRDALDAGVDGIMTNYPDVITDVLN
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

#### Options & flags {#opts-filter}

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
