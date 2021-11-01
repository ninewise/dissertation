### DNA sequence translation

The `umgap translate` command takes one or more DNA sequences and
translates them into amino acid sequences. It allows the selection of
the reading frame and a translation table to use. Most notably, it is
also capable of translating all frames, so the rest of the pipeline can
execute on each frame and decide which to keep.

#### Usage {#use-translate}

The DNA sequences are expected in a FASTA format on standard input.

```shell
$ cat input.fa
>header1
GATTACAAA
$ umgap translate -f1 < input.fa
>header1
DYK
```

The `-f` flag allows you to add reading frames to the translation. If
you want to translate multiple frames and care to keep them apart, the
`-n` flag adds the name of the frame to the end of the FASTA header.

```shell
$ umgap translate -f1 -f1R < input.fa
>header1|1
DYK
>header1|1R
FVI
```

The `-a` flag can be used as a shortcut to translate all 6 reading
frames.

With the `-t` flag, you can select a specific translation table, for
instance `-t11` for the bacterial, archaeal and plant plastid code.

##### Options & Flags {#opts-translate}

`-a / --all-frames`
  ~ Read and output all six frames

`-n / --append-name`
  ~ Append a bar (|) and the name of the frame to the FASTA header

`-h / --help`
  ~ Prints help information

`-m / --methionine`
  ~ Replace each start-codon with methionine

`-s / --show-table`
  ~ Instead of normal use, print the selected table and exit

`-V / --version`
  ~ Prints version information

`-f / --frame f...`
  ~ Adds a reading frame (1, 2, 3, 1R, 2R or 3R)

`-t / --table t`
  ~ Translation table to use [default: 1]
