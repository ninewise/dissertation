### Conversion from FASTQ to FASTA Format

The `umgap fastq2fasta` command takes one or more FASTQ files and
interleaves them into a single FASTA file.

This puts them in the format used internally in the pipeline. When
passing multiple files to the command, it will interleave the reads
into a single stream, starting with the first read from each file (in
the same order they were passed as arguments), followed by the second,
continuing in this manner until any of the files runs out of reads (thus
truncating the others). This places the read ends from paired-end reads,
when saved in separate files, next to each other in the output stream,
allowing steps later in the pipeline to join them together to draw a
conclusion about the whole read.

#### Usage {#use-fastq2fasta}

The FASTQ input files are given as command line arguments. In order, a
single record is taken from each of these files, and the record header
and sequence are written to standard output in FASTA format, dropping
the quality scores, until any of the files runs out or records.

This command is generally used to combine two paired-end FASTQ files
into a single FASTA file.

```shell
$ cat input_1.fq
@record1/1
GATAGCCGTCGAGCGTCCCGACATCCATATACAGCTCGCCGCAGTGCGTC
GCCCGCACGGCATCGCGCGCCGCGATGTACGCATTCAACCAGCGTCCGAG
+
AADGGGG<GI@IIKJKKKKH4EIJCHJ9:IJHKIKDIKDKGDJD@C@<>K
D=;FEA:DA=I$EEED$>C@1EDE?D:CEAC;CDE:E$D$=D$EAD?AEE
@record2/1
CCCAGGTCCCCGGCATCGTCGCGGCCTCGCCCATGATCCAGCTCCACGAC
CAGATCCCCGTTCCCGGCGGTAAAGAGCGCGGCGTGCTCATCCTCGGAGT
+
ADDEEG@GIGIIHKCJKH@HHGKHHKHKKJJBA.GFIGK(IHKKEKECBE
EEEDIKC@H<EDBJDEA36;6EE$E:G6C=E$E@CE?EE9FEE?E:F$?$
$ cat input_2.fq
@record1/2
CATTGTTCGCTACTTTGCGGAGCGCAATTATGCCGCGGAGATCTTCTACG
TGGTGCAGCAGAAGCTGGCGGGCTGGTGCGATGCGTTGTATCGGCCCGAG
+
DDDEGGG?HIHIIKHK?@2KBHGDCJKI(JEJJKKHKKHBHKKFICEICE
CCFFEICCCC$E6ED$?CEEDDED$DEDCFFECEEEEFB$CCEC$6C=CA
@record2/2
GGACACGCTCTCAGGACGATGGCGCGATTGCAGGACTTGCTGGATCTCCT
CCGTCGCCAAGGGGACGCGCTCGGAGTGGCTCATGGAGCAGACGAGTTCT
+
AADGGGEGIIIHIJKGCK<KD:KKHI?HIHHJKFJEKKJIGE$CKHE$EE
$FEEEI=EAE8EAIKFBEE$EADEEDB$DEEDE=?B6C$C$6$A$$=BEE
$ umgap fastq2fasta input_1.fq input_2.fq
>record1/1
GATAGCCGTCGAGCGTCCCGACATCCATATACAGCTCGCCGCAGTGCGTC
GCCCGCACGGCATCGCGCGCCGCGATGTACGCATTCAACCAGCGTCCGAG
>record1/2
CATTGTTCGCTACTTTGCGGAGCGCAATTATGCCGCGGAGATCTTCTACG
TGGTGCAGCAGAAGCTGGCGGGCTGGTGCGATGCGTTGTATCGGCCCGAG
>record2/1
CCCAGGTCCCCGGCATCGTCGCGGCCTCGCCCATGATCCAGCTCCACGAC
CAGATCCCCGTTCCCGGCGGTAAAGAGCGCGGCGTGCTCATCCTCGGAGT
>record2/2
GGACACGCTCTCAGGACGATGGCGCGATTGCAGGACTTGCTGGATCTCCT
CCGTCGCCAAGGGGACGCGCTCGGAGTGGCTCATGGAGCAGACGAGTTCT
```
