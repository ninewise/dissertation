### Joining consecutive FASTA records

The `umgap uniq` command joins consecutive FASTA records with the same
header. It can be used to join the predictions from the 2 ends of the
same read, or the 6 frames from translation, (or both) together before
they are aggregated into a single prediction. It is capable of first
stripping the header past a certain delimiter (e.g. `/` for stripping
the `/1` and `/2` for paired end reads) before comparison.

#### Usage

The input is given in a FASTA format on standard input. The content
of all consecutive records with the same FASTA header is joined under
a single header, separated by newlines (or another separated set with
`-s`).

A delimiter can be passed with the `-d` option to drop this delimiter
and everything after it from the FASTA header before comparing it.

```shell
$ cat input.fa
>header1/1
147206
240495
>header1/2
1883
1
1883
1883
$ umgap uniq -d / < input.fa
>header1
147206
240495
1883
1
1883
1883
```

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-w / --wrap`
  ~ Wrap the output sequences

`-s / --separator s`
  ~ Separator between output items [default: newline]

`-d / --delimiter d`
  ~ Strip FASTA headers after this string
