### Filtering van taxanomische identificaties op basis van hun omgeving

Bij het opzoeken van peptiden kunnen, door mutaties of
read-errors, toevalstreffers op foute taxa vallen. Deze zouden de
aggregatie in latere fasen van de UMGAP kunnen storen. Zeker het
lowerst-common-ancestoralgoritme is hier erg kwetsbaar voor (een
enkele toevalstreffer in een verder goede read kan resulteren in een
ongeïdentificeerde read). Zulke toevalstreffers komen bijna altijd apart
voor: de omliggende peptiden zullen niet teruggevonden worden in de
index, of zullen wel op de correcte identificatie mappen. Om die reden
werd de `umgap seedextend` tool toegevoegd. Deze tool zal alleenliggende
hits uit de lijst van hits schrappen.

Het gaat te werk door eerst enkele seeds te zoeken in de lijst van hits.
Dit zijn *s*, de minimum seed size, opeenvolgende hits op eenzelfde
taxon. Vervolgens wordt elk van deze seeds uitgebreid naar links en
rechts tot een extended seed. Zo'n uitbereiding kan er komen als er
op afstand *g*, de maximum gap size, of minder nog een hit ligt,
onafhankelijk of deze op hetzelfde taxon valt of niet. Merk op dat een
extended seed dus ook meerdere nabijgelegen seeds kan bevatten. Finaal
zal `seedextend` enkel de hits uitschrijven die binnen één van de
extended seeds vallen.

Zo'n seed-extendalgoritme kan geïmplementeerd worden als een eenmalige
overloping van de lijst van hits, tijdens dewelke een verzameling
van kandidaat extended seeds wordt bijgehouden. Het algoritme wordt
hieronder in pseudocode omschreven.

TODO pseudocode

#### Usage

The input is given in a FASTA format on standard input. It should
consist of taxon IDs separated by newlines, and the order of these taxa
should reflect their location on a peptide, such as output by the `umgap
prot2kmer2lca -o` command. As such, 3 consecutive equal IDs representing
9-mers, for instance, indicate a 11-mer match. This so-called seed could
still be extended with other taxa, forming an extended seed. The command
writes all taxa in any of these extended seeds to standard output.

```sh
$ cat dna.fa
>header1
CGCAGAGACGGGTAGAACCTCAGTAATCCGAAAAGCCGGGATCGACCGCCCCTTGCTTGCAGCCGGGCACTACAGGACCC
$ umgap translate -n -a < dna.fa | umgap prot2kmer2lca 9mer.index > input.fa
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
$ umgap seedextend < input.fa
>header1|1
9606 9606 2759 9606 9606 9606 9606 9606 9606 9606 8287
>header1|2
>header1|3
>header1|1R
>header1|2R
>header1|3R
```

Taxon IDs are separated by newlines in the actual output, but are
separated by spaces in this example.

The number of consecutive equal IDs to start a seed is 2 by default, and
can be changed using the `-s` option. The maximum length of gaps between
seeds to join in an extension can be set with `-g`, no gaps are allowed by
default.

The command can be altered to print only the extended seed with the
highest score among all extended seeds. Pass a taxonomy using the `-r
taxon.tsv` option to activate this. In this scored mode, extended seeds
with gaps are given a penalty of 5, which can be made more or less
severe (higher or lower) with the `-p` option.

#### Options & flags

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-g / --max-gap-size g`
  ~ The maximum length of a gap between seeds in an extension [default: 0]

`-s / --min-seed-size s`
  ~ The minimum length of equal taxa to count as seed [default: 2]

`-p / --penalty p`
  ~ The score penalty for gaps in extended seeds [default: 5]

`-r / --ranked r`
  ~ Use taxon ranks in given NCBI taxonomy tsv-file to pick extended seed with highest score