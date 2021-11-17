### Analysis Result Reports

At the end of running the analysis, the results need to be gotten
into a format ready for interpreting. The `umgap taxa2freq` tool
creates a frequency table on a given target rank (species by default).
This frequency table is in a CSV-format, so it can be loaded into a
spreadsheet program to start working on visualizations. Alternatively,
the `umgap taxa2tree` command will directly create interactive
visualizations to view in the browser. Note that it does contact the
Unipept API server to create these.

#### Usage {#use-report}

The input is given on standard input, or (for the `taxa2freq` command)
in multiple file arguments, a single taxon ID on each line. Each taxon
that is more specific than the target rank is counted towards its
ancestor on the target rank. Each taxon less specific than the target
rank is counted towards root. The `taxa2freq` command outputs a CSV
table of counts, taxon IDs and their names. The `taxa2tree` command
outputs an HTML file or, given the `-u` flag, a URL to this HTML file
hosted online.

The `taxa2freq` command needs a taxonomy to be used passed as an
argument to this command. This is a preprocessed version of the NCBI
taxonomy. The `taxa2tree` command uses a taxonomy stored on the Unipept
API server.

```shell
$ cat input1.txt
9606
9606
2759
9606
9606
9606
9606
9606
9606
9606
8287
$ umgap taxa2freq taxons.tsv < input1.txt
taxon id,taxon name,stdin
1,root,2
9606,Homo sapiens,9
$ umgap taxa2freq taxons.tsv input1.txt input1.txt
taxon id,taxon name,input1.txt,input1.txt
1,root,2,2
9606,Homo sapiens,9,9
$ cat input2.txt
>header1
817
329854
1099853
$ umgap taxa2tree < input2.txt > output.html
$ umgap taxa2tree --url < input2.txt
https://bl.ocks.org/a686a37e1dcd43dd4ec7d467487bd6a1
```

#### Options & Flags {#opts-report}

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

#### Options & Flags for `taxa2freq`

`-f / --frequency f`
  ~ The minimum frequency to be reported [default: 1]

`-r / --rank r`
  ~ The rank to show [default: species]

#### Options & Flags for `taxa2tree`

`-u / --url`
  ~ Host the result online and return the URL
