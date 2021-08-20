---
papersize: A4
geometry:
- margin=1in
links-as-notes: true
classoption:
 - oneside
documentclass: report
pagestyle: empty
colorlinks: true
...
# Misclassifications

## Kraken HiSeq dataset

* `umgap -1 HiSeq_input.fa -t high-precision -o HiSeq_input.high-precision.output`

Momenteel zitten we aan `grep -c '^>' HiSeq_input.high-precision.output` 8501 reads, dus we verliezen 15% aan noncoding reads.

### Misklassificaties op Genus

* Samenrapen van de read ID's, annotaties, classificaties en beide op genus rang in een CSV:
  ```sh
  sed -n 's/^>.*\.\([^_]*\).*/\1/p' < HiSeq_input.high-precision.output > reads
  sed -n 's/^>\([0-9]*\).*/\1/p' < HiSeq_input.high-precision.output > annotations.taxa
  sed '/^>/d' < HiSeq_input.high-precision.output > classifications.taxa
  umgap snaptaxon -r genus taxons.tsv < annotations.taxa > annotations.genus
  umgap snaptaxon -r genus taxons.tsv < classifications.taxa > classifications.genus
  paste -d, reads annotations.taxa classifications.taxa annotations.genus classifications.genus > genus.csv
  ```

Het aantal correct voorspellingen op genus-niveau is `awk -F, '$4 == $5' genus.csv | wc -l` 6365.

Het aantal coding reads waar we niets voor vinden is `grep -c ',1$' genus.csv` 2082.

* De fouten afzonderen:
  `awk -F, '$4 != $5 && $5 != 1' genus.csv > wrong-genus.csv`

Dit zijn er 54, waarvan 37 unieke `sort wrong-genus.csv | uniq -c`:

  # read ID   annot.  classi.   genus    genus  namen / gemeenschappelijke voorouder
 -- ------- -------- -------- ------- --------  -------------------------------------------------------------
  1  725173  1001740     1773  670516     1763  Mycobacteroides vs Mycobacterium, family Mycobacteriaceae
  1  339018  1001740    36814  670516  1866885  Mycobacteroides vs Mycolicibacterium, family Mycobacteriaceae
  1   46852  1001740   512350  670516     1865  Mycobacteroides vs Actinoplanes, class Actinobacteria
  1  505763  1053231   123214    1386   182899  Bacillus vs Persephonella, superkingdom Bacteria
  1  293580  1053231  2136116    1386  2136116  Bacillus vs Candidatus Sulfotelmatobacter, superkingdom Bacteria
  1  887137  1053231   427683    1386      407  Bacillus vs Methylobacterium, superkingdom Bacteria
  5  287456  1073377    13687     642    13687  Aeromonas vs Sphingomonas, phylum Proteobacteria
                                                + 679086 783280 954516 991691
  1  468205  1073377   165695     642   165695  Aeromonas vs Sphingobium, phylum Proteobacteria
  1   62540  1073377      192     642      191  Aeromonas vs Azospirillum, phylum Proteobacteria
  1  637274  1073377      662     642      662  Aeromonas vs Vibrio, order Vibrionales
  3  452657  1073387     1350     816     1350  Bacteroides vs Enterococcus, superkingdom Bacteria
                                                + 461516 980528
  1  932869  1073387     1351     816     1350  Bacteroides vs Enterococcus, superkingdom Bacteria
  1  356705  1073387   165179     816      838  Bacteroides vs Prevotella, order Bacteroidales
  1  475700  1073387      642     816      642  Bacteroides vs Aeromonas, superkingdom Bacteria
  1  896090  1149860  1123286  365348     2375  Pelosinus vs Sporomusa, family Sporomusaceae
  5  275127  1149860  1286362  365348  2719231  Pelosinus vs Lacrimispora, phylum Firmicutes
                                                + 295228 51029 682654 73256
  1  616937  1149860     1301  365348     1301  Pelosinus vs Streptococcus, phylum Firmicutes
  1  982899  1149860     1386  365348     1386  Pelosinus vs Bacillus, phylum Firmicutes
  1  148493  1149860   151549  365348   151548  Pelosinus vs Eumeta, root (Insecta)
  4  265785  1149860  2719231  365348  2719231  Pelosinus vs Lacrimispora, phylum Firmicutes
                                                + 840159 927784 995158
  1  697341  1149860    44249  365348    44249  Pelosinus vs Paenibacillus, phylum Firmicutes
  1  531056  1185664     1350     338     1350  Xanthomonas vs Enterococcus, superkingdom Bacteria
  1  139849  1185664  2607817     338  1155738  Xanthomonas vs Moorea, superkingdom Bacteria
  1  831306  1185664    59201     338      590  Xanthomonas vs Salmonella, class Gammaproteobacteria
  5  462591  1213734     1386    1279     1386  Staphylococcus vs Bacillus, order Bacillales
                                                + 479573 484155 494276 950443
  1  295412  1213734     3870    1279     3869  Staphylococcus vs Lupinus, root (Fabaceae)
  1  817489   170187     1350    1301     1350  Streptococcus vs Enterococcus, order Lactobacillales
  1  142547   170187     1605    1301  2767887  Streptococcus vs Ligilactobacillus, order Lactobacillales
  1  702075   272943  1150469    1060  1612157  Rhodobacter vs Pararhodospirillum, family Rhodospirillaceae
  1  476780   272943     3870    1060     3869  Rhodobacter vs Lupinus, root (Fabaceae)
  1   40507   272943      469    1060      469  Rhodobacter vs Acinetobacter, phylum Proteobacteria
  1  561178   991923   347534     662   347533  Vibrio vs Zobellella, class Gammaproteobacteria
  1  345112   991923   471874     662      586  Vibrio vs Providencia, class Gammaproteobacteria (Enterobacterales)
  1  256020   991923    55209     662    53335  Vibrio vs Pantoea, class Gammaproteobacteria (Enterobacterales)
  1  718167   991923      573     662      570  Vibrio vs Klebsiella, class Gammaproteobacteria (Enterobacterales)
  1  597689   991923      626     662      626  Vibrio vs Xenorhabdus, class Gammaproteobacteria (Enterobacterales)
  1  709214   991923    65700     662      551  Vibrio vs Erwinia, class Gammaproteobacteria (Enterobacterales)

### Misklassificaties op Species

* Samenrapen van de annotaties, classificaties en beide op species rang in een CSV:
  ```sh
  umgap snaptaxon -r species taxons.tsv < annotations.taxa > annotations.species
  umgap snaptaxon -r species taxons.tsv < classifications.taxa > classifications.species
  paste -d, reads annotations.taxa classifications.taxa annotations.species classifications.species > species.csv
  ```

Het aantal correct voorspellingen op species-niveau is `awk -F, '$4 == $5' species.csv | wc -l` 2232.

Het aantal coding reads waar we niets voor vinden is `grep -c ',1$' species.csv` 6096.

* De fouten afzonderen:
  `awk -F, '$4 != $5 && $5 != 1' species.csv > wrong-species.csv`

Dit zijn er 173, waarvan 52 unieke `sort wrong-species.csv | uniq -c`:

   # read ID   annot.   class.  species  species  gemeenschappelijke voorouder
 --- -------  -------  -------  -------  -------  ---------------------------------------------------------------
   1  725173  1001740     1773    36809     1773  family Mycobacteriaceae
   1  339018  1001740    36814    36809    36814  family Mycobacteriaceae
   1   46852  1001740   512350    36809   512350  class Actinobacteria
   1  505763  1053231   123214     1396   309805  superkingdom Bacteria
   1   14352  1053231     1392     1396     1392  species group Bacillus cereus group
   5  640970  1053231     1405     1396     1405  species group Bacillus cereus group
                                                  + 682511 823673 876520 906637
   1  994674  1053231  1808955     1396  1808955  genus Bacillus
   1  982689  1053231  1890302     1396  1890302  species group Bacillus cereus group
   2  306270  1053231   315749     1396   580165  species group Bacillus cereus group
                                                  + 919309
   1  673158  1053231   412694     1396     1428  species group Bacillus cereus group
   1  887137  1053231   427683     1396   427683  superkingdom Bacteria
   1  797170  1053231   527000     1396    64104  species group Bacillus cereus group
   1   59596  1073377  1268236      644   271417  genus Aeromonas
   1   62540  1073377      192      644      192  phylum Proteobacteria
 103  108407  1073377   196024      644   196024  genus Aeromonas (Aeromonas hydrophila vs Aeromonas dhakensis)
                                                  + 116919 123355 125657 135903 141577 147861 148182 170858
                                                  + 181134 187016 216992 242823 24308 253267 253872 259793
                                                  + 261348 277263 279798 28275 285665 307225 310116 323536 
                                                  + 327515 336548 347052 365134 370275 371419 374641 377940
                                                  + 399127 403609 407358 417661 436104 437103 445060 458481
                                                  + 459748 480230 482244 489574 489785 495423 575010 583127
                                                  + 584339 597711 597863 600279 616747 622604 623597 628093
                                                  + 630564 652454 664490 682367 720510 725609 730941 730983
                                                  + 741577 744939 749456 751174 753900 759910 767813 768278
                                                  + 769643 775239 781193 782959 787536 808760 817549 819907
                                                  + 823846 827700 837913 83977 839934 840731 846293 847024
                                                  + 87300 885316 888186 890381 907681 916255 928512 934118
                                                  + 94090 945521 959549 964820 977771 996860
   3  292863  1073377      645      644      645  genus Aeromonas
                                                  + 453666 463927
   1  435936  1073377      648      644      648  genus Aeromonas
   1    7294  1073377   931529      644   931529  genus Aeromonas
   1  932869  1073387     1351      817     1351  superkingdom Bacteria
   1  356705  1073387   165179      817   165179  order Bacteroidales
   1  356695  1073387  2026724      817  2026724  superkingdom Bacteria
   1  844588  1073387   411901      817    47678  genus Bacteroides
   1  468533  1073387      820      817      820  genus Bacteroides
   1  896090  1149860  1123286   365349   112900  family Sporomusaceae
   2  261029  1149860  1123291   365349   380084  genus Pelosinus
                                                  + 449843
   5  275127  1149860  1286362   365349    29354  phylum Firmicutes
                                                  + 295228 51029 682654 73256
   1  148493  1149860   151549   365349   151549  root (Insecta)
   1  125075  1185664  1418095  1985254    56448  genus Xanthomonas
   1  767115  1185664   190486  1985254      346  genus Xanthomonas
   1  139849  1185664  2607817  1985254  2607817  superkingdom Bacteria
   2  629346  1185664   291331  1985254      347  genus Xanthomonas
                                                  + 875312
   1   98530  1185664      346  1985254      346  genus Xanthomonas
   2  388050  1185664   427082  1985254      346  genus Xanthomonas
                                                  + 72974
   1  506423  1185664   509169  1985254      339  genus Xanthomonas
   4  268289  1185664    56448  1985254    56448  genus Xanthomonas
                                                  + 563982 745683 804652
   1  831306  1185664    59201  1985254    28901  class Gammaproteobacteria
   1   83607  1213734    29378     1280    29378  genus Staphylococcus
   1  295412  1213734     3870     1280     3870  root (Fabaceae)
   1  202399   170187     1303     1313     1303  genus Streptococcus
   1  142547   170187     1605     1313     1605  superkingdom Bacteria
   3  142289   170187    28037     1313    28037  genus Streptococcus + 183565 248707
   1   57909   170187    40041     1313     1336  genus Streptococcus
   1  880144   170187   585203     1313    28037  genus Streptococcus
   1  418525   170187   871237     1313    68892  genus Streptococcus
   1  702075   272943  1150469     1063     1084  order Rhodospirillales
   1  476780   272943     3870     1063     3870  root (Fabaceae)
   1  721774   272943   445629     1063   445629  genus Rhodobacter
   1  561178   991923   347534      666   347534  class Gammaproteobacteria
   1  345112   991923   471874      666      588  class Gammaproteobacteria
   1  256020   991923    55209      666    55209  class Gammaproteobacteria
   1  718167   991923      573      666      573  class Gammaproteobacteria
   1  709214   991923    65700      666    65700  class Gammaproteobacteria

Peter vond dit artikel over Aeromonas dhakensis:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4882333/
> The virulent A. hydrophila SSU strain recently reclassified as A.
> dhakensis SSU was originally isolated from a patient with diarrhea in
> Philippines (Grim et al., 2014).

* Telling per strain:
  - 1000 - FGS-verlies: `sort annotations.taxa | uniq -c`
  - aantal root-voorspellingen: `grep ',1$' species.csv | cut -d, -f2 | sort | uniq -c`
  - aantal correcte: `awk -F, '$4 == $5 { print $2 }' species.csv | sort | uniq -c`
  - aantal foute: `awk -F, '$4 != $5 && $5 != 1 { print $2 }' species.csv | sort | uniq -c`

* Oplijsting misklassificaties met aantallen:
  `awk -F, '$4 != $5 && $5 != 1 { print $2, $5 }' species.csv | sort | uniq -c`

* Oplijsting namen misklassificaties:
  ```sh
  awk -F, '$4 != $5 && $5 != 1 { print $2, $5 }' species.csv | sort | uniq \
    | cut -d' ' -f2 | umgap taxonomy taxons.tsv \
    | awk -F'\t' '{ printf "%s (%s)\n", $2, $1 }'
  ```

+---------+-----------------+------+---------+-----------------------------------------------------------+
|      ID | strain name     | none | correct | misclassifications                                        |
+========:+:================+=====:+========:+:==========================================================+
| 1001740 | Mycobacteroides |  701 |  296    | - Mycobacterium tuberculosis (1773) (x1)                  |
|         | abscessus       |      |         | - Mycolicibacterium rhodesiae (36814) (x1)                |
|         | 6G-0125-R       |      |         | - Actinoplanes xinjiangensis (512350) (x1)                |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1053231 | Bacillus cereus |  939 |   47    | - Bacillus mycoides (1405) (x5)                           |
|         | VD118           |      |         | - Bacillus cytotoxicus (580165) (x2)                      |
|         |                 |      |         | - Bacillus anthracis (1392) (x1)                          |
|         |                 |      |         | - Bacillus thuringiensis (1428) (x1)                      |
|         |                 |      |         | - Bacillus mesophilus (1808955) (x1)                      |
|         |                 |      |         | - Bacillus wiedmannii (1890302) (x1)                      |
|         |                 |      |         | - Persephonella marina (309805) (x1)                      |
|         |                 |      |         | - Methylobacterium platani (427683) (x1)                  |
|         |                 |      |         | - Bacillus pseudomycoides (64104) (x1)                    |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1073377 | Aeromonas       |  890 |    0    | - **Aeromonas dhakensis (196024) (x103)**                 |
|         | hydrophila      |      |         | - Aeromonas salmonicida (645) (x3)                        |
|         | SSU             |      |         | - Azospirillum brasilense (192) (x1)                      |
|         |                 |      |         | - Aeromonas molluscorum (271417) (x1)                     |
|         |                 |      |         | - Aeromonas caviae (648) (x1)                             |
|         |                 |      |         | - Aeromonas lusitana (931529) (x1)                        |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1073387 | Bacteroides     |  590 |  405    | - Enterococcus faecalis (1351) (x1)                       |
|         | fragilis        |      |         | - Prevotella copri (165179) (x1)                          |
|         | HMW 615         |      |         | - Chloroflexi bacterium (2026724) (x1)                    |
|         |                 |      |         | - Bacteroides caccae (47678) (x1)                         |
|         |                 |      |         | - Bacteroides uniformis (820) (x1)                        |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1149860 | Pelosinus       |  549 |  442    | - Lacrimispora celerecrescens (29354) (x5)                |
|         | fermentans      |      |         | - Pelosinus propionicus (380084) (x2)                     |
|         | A11             |      |         | - Sporomusa acidovorans (112900) (x1)                     |
|         |                 |      |         | - Eumeta japonica (151549) (x1)                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1185664 | Xanthomonas     |  918 |   68    | - Xanthomonas arboricola (56448) (x5)                     |
|         | axonopodis      |      |         | - Xanthomonas citri (346) (x4)                            |
|         | pv. manihotis   |      |         | - Xanthomonas oryzae (347) (x2)                           |
|         | str. UA323      |      |         | - Moorea sp. SIOASIH (2607817) (x1)                       |
|         |                 |      |         | - Salmonella enterica (28901) (x1)                        |
|         |                 |      |         | - Xanthomonas campestris (339) (x1)                       |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
| 1213734 | Staphylococcus  |  495 |  503    | - Staphylococcus arlettae (29378) (x1)                    |
|         | aureus M0927    |      |         | - Lupinus albus (3870) (x1)                               |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|  170187 | Streptococcus   |  776 |  216    | - Streptococcus mitis (28037) (x4)                        |
|         | pneumoniae      |      |         | - Streptococcus oralis (1303) (x1)                        |
|         | TIGR4           |      |         | - Streptococcus equi (1336) (x1)                          |
|         |                 |      |         | - Ligilactobacillus animalis (1605) (x1)                  |
|         |                 |      |         | - Streptococcus infantis (68892) (x1)                     |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|  272943 | Rhodobacter     |  913 |   84    | - Pararhodospirillum photometricum (1084) (x1)            |
|         | sphaeroides     |      |         | - Lupinus albus (3870) (x1)                               |
|         | 2.4.1           |      |         | - Rhodobacter johrii (445629) (x1)                        |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|         |                 |      |         |                                                           |
+---------+-----------------+------+---------+-----------------------------------------------------------+
|  991923 | Vibrio          |  824 |  171    | - Zobellella denitrificans (347534) (x1)                  |
|         | cholerae        |      |         | - Pantoea cypripedii (55209) (x1)                         |
|         | CP1032(5)       |      |         | - Klebsiella pneumoniae (573) (x1)                        |
|         |                 |      |         | - Providencia stuartii (588) (x1)                         |
|         |                 |      |         | - Erwinia tracheiphila (65700) (x1)                       |
+---------+-----------------+------+---------+-----------------------------------------------------------+

## Metabenchmark setA1

In setA1 zitten `grep -c '^@.*/1$' setA1_1.fq` 28912778 reads.

* `umgap-analyse.sh -1 setA1_1.fq -2 setA1_2.fq -t high-precision -o setA1.high-precision.output`

Via FGS verliezen we er 1330582, er blijven `grep -c '^>' setA1.high-precision.output` 27582196 reads over.

```sh
sed -n 's/^>\(.*\)_[0-9]*$/\1/p' setA1.high-precision.output > names
```

```python
with open('name_taxid.csv', 'r') as f:
	next(f) # header
	name_taxid = { name: int(taxid) for (name, taxid) in (l.strip().split('\t') for l in f) }

with open('setA1.high-precision.output', 'r') as r, open('annotations.taxa', 'w') as w:
	for line in r:
		if line[0] == '>':
			print(name_taxid['_'.join(line[1:].split('_')[:-1])], file=w)
```

```sh
sed '/^>/d' < setA1.high-precision.output > classifications.taxa
umgap snaptaxon -r species ../taxons.tsv < annotations.taxa > annotations.species
umgap snaptaxon -r species ../taxons.tsv < classifications.taxa > classifications.species
paste -d, names annotations.taxa classifications.taxa annotations.species classifications.species > species.csv
```

* Het aantal correcte voorspellingen op species-rang is `awk -F, '$4 == $5' species.csv | wc -l` 10905443.
* Het aantal voorspelde reads waar we niets voor vinden is `grep -c ',1$' species.csv` 18189764.
* Het aantal foute voorspellingen is `awk -F, '$4 != $5 && $5 != 1' species.csv | wc -l` 299140.

```sh
awk -F, '$4 != $5 && $5 != 1' species.csv > wrong-species.csv
```

* Het aantal unieke foute voorspellingen is `sort wrong-species.csv | uniq -c | wc -l` 103505.

## Metabenchmark grote tabel

```sh
ranks="strain species genus family order class phylum superkingdom"
for r in $ranks; do umgap snaptaxon -r $r ../taxons.tsv < annotations.taxa > annotations.$r; done
for r in $ranks; do umgap snaptaxon -r $r ../taxons.tsv < classifications.taxa > classifications.$r; done
```

Notes:
- Tabellen per type reads

- "Acidobacteria bacterium": Acidobacteria is een phylum
- analoog bij andere "XXX bacterium" in eerste record
- "wrong species" > waar zijn de verkeerde op andere niveau's

