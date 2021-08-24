### Reading frame selection

In het geval we de UMGAP toepassen op transcriptonomics data, is vooraf
niet gekend hoe we deze reads moeten vertalen naar eiwitten. We weten
echter wel dat slechts 1 van de 6 mogelijke vertalingen de correcte zal
zijn. Daarom werd de `umgap bestof` tool ontwikkeld. Dit commando zal,
gegeven de geidentificeerde taxa voor aantal vertalingen voor eenzelfde
read, de beste identificaties (en dus de correcte vertaling) selecteren.

#### Usage

The input is given in FASTA format on standard input. Per FASTA header,
there should be multiple numbers (taxon IDs). Per 6 FASTA records (or
whichever number you specify with `-f`), the best record is selected
and written to standard output. If the input is a series of identified
taxon IDs for each of the 6 translations of a read, the output will most
likely come from the actual coding frame.

```sh
$ cat dna.fa
>header1
CGCAGAGACGGGTAGAACCTCAGTAATCCGAAAAGCCGGGATCGACCGCCCCTTGCTTGCAGCCGGGCACTACAGGACCC
$ umgap translate -n -a < dna.fa | umgap prot2kmer2lca 9mer.index | tee input.fa
>header1|1
9606 9606 2759 9606 9606 9606 9606 9606 9606 9606 8287
>header1|2
2026807 888268 186802 1598 1883
>header1|3
1883
>header1|1R
27342 2759 155619 1133106 38033 2
>header1|2R
>header1|3R
2951
$ umgap bestof < input.fa
>header1|1
9606 9606 2759 9606 9606 9606 9606 9606 9606 9606 8287
```

Taxon IDs are separated by newlines in the actual output, but are
separated by spaces in this example.

#### Options & flags

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-f / --frames f`
  ~ The number of frames of which to pick the best [default: 6]
