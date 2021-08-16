# The Unipept Metagenomics Analysis Pipeline

_Dit hoofdstuk omschrijft eerst de structuur en samenstelling van
de *pipeline*. De verschillende commando's en hun interface worden
overlopen. Daarna volgt een bespreking van het resultaat, zoals
gepubliceerd._

## Opzet en structuur

De analyse van *Shotgun Metagenomics data* kan op twee wijzen
opgesplitst worden. Enerzijds is de data traditioneel opgeslagen in
FASTA- of FASTQ-bestanden. Beide vormen lange sequenties van *reads*.
Elk van deze reads kan individueel verwerkt worden. Slechts na de
verwerking van de individuele reads komen ze met elkaar in aanraking,
tijdens de aggregatie van de hele dataset, bijvoorbeeld om een
frequentietabel op te stellen. Dit suggereert een opsplitsing per
*read*. Anderzijds gebeurt ook de verwerking in een aantal logische
stappen, dewelke elke *read* zal doormaken.

De eerste manier van opsplitsing heeft als groot voordeel de
mogelijkheid tot parallellisatie. Op triviale wijze kan elke *read* in
een aparte *thread* verwerkt worden. Op die manier kan de volledige
kracht van de uitvoerende machine gebruikt worden.

De tweede manier van opsplitsing kan echter de verschillende stappen
apart beter optimaliseren. Elke stap kan specialiseren in zijn taak
en krijgt de mogelijkheid om een gemeenschappelijke initialisatie te
delen over alle *reads* die hij zal verwerken. Daarbij kunnen alle
stappen gelijktijdig in eigen process uitgevoerd worden, waarbij *reads*
doorgegeven worden aan het volgende process in de verwerking zodra dit
process zijn taak volbracht heeft. Tenslotte biedt zo'n opsplitsing de
mogelijkheid om de verschillende stappen in te wisselen om delen van de
verwerking te wijzigen.

De UMGAP koos voor de tweede manier van opsplitsen. Elke logische stap
werd geprogrammeerd als een apart subcommando van de `umgap` executable,
op basis van een gedeelde broncode. De processen worden samengebracht
in één ketting van commando's met behulp van UNIX pipes, die met elkaar
communiceren via standaard invoer en standaar uitvoer in FASTA-achtige
formaten.

## Componenten

_Overlopen van de componenten en hun interface. Samenhang moet ik hier
niet meer overlopen, die komt in de paper erna._

### Omzetting van FASTQ- naar FASTA-bestanden

The `umgap fastq2fasta` command takes one or more FASTQ files and
interleaves them into a single FASTA file.

Zo worden ze omgezet naar het formaat dat de *pipeline* intern gebruikt.
Als je meerdere bestanden aan het commando meegeegt, zorgt er het ook
voor dat deze *interleaved* in 1 *stream* terecht komen. Zo komen de
reads uit *paired-end reads*, waarbij de twee eindes in aparte bestanden
opgeslagen worden, naast elkaar in de stream. Dit is cruciaal voor
latere stappen in de pipeline, waar we de conclusies over beide eindes
willen samenvoegen om een conclusie over de gehele *read* te trekken.

#### Usage

The FASTQ input files are given as command line arguments. In order, a
single record is taken from each of these files, and the record header
and sequence are written to standard output in FASTA format, dropping
the quality scores, until any of the files runs out or records.

This command is generally used to combine two paired-end FASTQ files
into a single FASTA file.

```sh
$ cat input_1.fq
@record1/1
GATAGCCGTCGAGCGTCCCGACATCCATATACAGCTCGCCGCAGTGCGTCGCCCGCACGGCATCGCGCGCCGCGATGTACGCATTCAACCAGCGTCCGAG
+
AADGGGG<GI@IIKJKKKKH4EIJCHJ9:IJHKIKDIKDKGDJD@C@<>KD=;FEA:DA=I$EEED$>C@1EDE?D:CEAC;CDE:E$D$=D$EAD?AEE
@record2/1
CCCAGGTCCCCGGCATCGTCGCGGCCTCGCCCATGATCCAGCTCCACGACCAGATCCCCGTTCCCGGCGGTAAAGAGCGCGGCGTGCTCATCCTCGGAGT
+
ADDEEG@GIGIIHKCJKH@HHGKHHKHKKJJBA.GFIGK(IHKKEKECBEEEEDIKC@H<EDBJDEA36;6EE$E:G6C=E$E@CE?EE9FEE?E:F$?$
$ cat input_2.fq
@record1/2
CATTGTTCGCTACTTTGCGGAGCGCAATTATGCCGCGGAGATCTTCTACGTGGTGCAGCAGAAGCTGGCGGGCTGGTGCGATGCGTTGTATCGGCCCGAG
+
DDDEGGG?HIHIIKHK?@2KBHGDCJKI(JEJJKKHKKHBHKKFICEICECCFFEICCCC$E6ED$?CEEDDED$DEDCFFECEEEEFB$CCEC$6C=CA
@record2/2
GGACACGCTCTCAGGACGATGGCGCGATTGCAGGACTTGCTGGATCTCCTCCGTCGCCAAGGGGACGCGCTCGGAGTGGCTCATGGAGCAGACGAGTTCT
+
AADGGGEGIIIHIJKGCK<KD:KKHI?HIHHJKFJEKKJIGE$CKHE$EE$FEEEI=EAE8EAIKFBEE$EADEEDB$DEEDE=?B6C$C$6$A$$=BEE
$ umgap fastq2fasta input_1.fq input_2.fq
>record1/1
GATAGCCGTCGAGCGTCCCGACATCCATATACAGCTCGCCGCAGTGCGTCGCCCGCACGGCATCGCGCGCCGCGATGTACGCATTCAACCAGCGTCCGAG
>record1/2
CATTGTTCGCTACTTTGCGGAGCGCAATTATGCCGCGGAGATCTTCTACGTGGTGCAGCAGAAGCTGGCGGGCTGGTGCGATGCGTTGTATCGGCCCGAG
>record2/1
CCCAGGTCCCCGGCATCGTCGCGGCCTCGCCCATGATCCAGCTCCACGACCAGATCCCCGTTCCCGGCGGTAAAGAGCGCGGCGTGCTCATCCTCGGAGT
>record2/2
GGACACGCTCTCAGGACGATGGCGCGATTGCAGGACTTGCTGGATCTCCTCCGTCGCCAAGGGGACGCGCTCGGAGTGGCTCATGGAGCAGACGAGTTCT
```

### Vertaling van DNA-sequenties naar eiwitfragmenten

_Verder kopiëren en aanvullen van de documentatie op de website..._

#### [paper](paper.md){.include}
