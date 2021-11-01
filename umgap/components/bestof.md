### Reading frame selection

The UMGAP, intended for metagenomics analysis, has also been
experimentally applied to transcriptomics data. While very similar
to metagenomics data, we have additional knowledge: every read will
consist completely of coding RNA. This implies we don't have to do
gene prediction, we should just translate the whole read to a protein
fragment. As the correct reading frame is unknown, the UMGAP chooses to
translate all six frames, process each, and finally pick the correct
among the six frames. This last step is performed by `umgap bestof`.
This command will, given the taxonomic identifications for any number of
translations of a read, pick the best identifications.

#### Usage {#use-bestof}

The input is given in FASTA format on standard input. Per FASTA header,
there should be multiple numbers (taxon IDs). Per 6 FASTA records (or
whichever number you specify with `-f`), the best record is selected
and written to standard output. If the input is a series of identified
taxon IDs for each of the 6 translations of a read, the output will most
likely come from the actual coding frame.

```shell
$ cat dna.fa
>header1
CGCAGAGACGGGTAGAACCTCAGTAATCCGAAAAGCCGGG
ATCGACCGCCCCTTGCTTGCAGCCGGGCACTACAGGACCC
$ umgap translate -n -a < dna.fa | \
  umgap prot2kmer2lca 9mer.index | \
  tee input.fa
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

#### Options & flags {#opts-bestof}

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-f / --frames f`
  ~ The number of frames of which to pick the best [default: 6]
