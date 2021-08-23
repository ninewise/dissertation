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
