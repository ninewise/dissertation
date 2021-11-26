# Appendix A {.unnumbered}

## Analysis of misclassifications per Operational Taxonomic Unit {.unnumbered}

This appendix contains an in-depth analysis in which we investigate the
accuracy of the taxonomic profilings of UMGAP. This analysis uses a
single setting of UMGAP (high-precision) and reports accuracy metrics
per operational taxonomic unit (OTU), i.e. all (paired-end) reads are
grouped per OTU from which they were extracted/generated. We still use
species as the target rank, but in a less stringent way compared to the
MetaBenchmark.

We performed the analysis on both datasets, used in the manuscript for
parameter tuning (smaller dataset; 10 OTUs) and benchmarking (larger
dataset; 1105 OTUs). The results are reported in four tables:

* Parameter Tuning dataset: results for the 10 OTUs in the small
  dataset. (page 3)

* Benchmark dataset - real reads: results for the 963 OTUs in the large
  dataset, excluding the evolutionary simulated and randomized OTUs in
  the large dataset. (page 6)

* Benchmark dataset - shuffled reads: results for the 110 randomized
  OTUs in the large dataset. (page 237)

* Benchmark dataset - simulated divergence reads: results for the 32
  evolutionary simulated OTUs in the large dataset. (page 265)

For each OTU, the tables report:

* (first column) OTU ID (a unique identifier) as specified in the
  benchmark dataset; this may include an accession number of the
  sequence record where the read was extracted from.

* (first column) name and taxon ID of the OTU as included in the
  benchmark and the name, taxon ID and rank of the expected
  identification; these taxa might differ for two reasons:

  - The OTU from the benchmark does not necessarily have a rank in the
    NCBI Taxonomy. It is typically an ID for a specific strain or clone.
    This taxon is mapped to its most specific ancestor with a rank in
    the NCBI Taxonomy.

  - After the previous step, some OTUs are mapped to a rank that is more
    specific (e.g. subspecies) than the target rank of the benchmark (in
    casu the species rank). These OTUs are mapped to the target rank of
    the benchmark.

  All taxon IDs (taxid) included in the report are identifiers assigned
  by the NCBI Taxonomy [@federhen].

* (first column) total number of (paired-end) reads in the dataset for
  the OTU.

* (first column) absolute and relative number of (paired-end) reads for
  the OTU that could be identified; UMGAP yields not identification if
  no peptides could be extracted from the read (e.g. because the read
  contains no coding regions or no coding regions could be predicted on
  the read).

* (second column) absolute and relative number of (paired-end) reads
  with a correct taxonomic identification (according to the expected
  identification) per taxonomic rank at or above the rank of the
  expected identification (in casu never below the species rank); UMGAP
  profiles a read to the root of the NCBI Taxonomy if not enough
  taxonomic profilings could be made for individual peptides extracted
  from the read based on the filtering options; the taxonomic rank with
  the highest number of correct identifications is marked in bold.

* (third column) absolute and relative number of (paired-end) reads with
  a wrong taxonomic identification (according to the expected
  identification) per taxon as identified by UMGAP; UMGAP
  identifications for ranks that are more specific than the rank of the
  expected identification are also reported as wrong identifications
  while technically they are not necessarily wrong (that status cannot
  be derived from the benchmark data), as this might indicate where
  UMGAP consistently identifies reads of the OTU to a more specific
  taxon than what is known about the OTU in the benchmark;
  identifications are sorted by decreasing number of reads and truncated
  after 7 OTUs; wrong identifications exceeding 2% of the total number
  of reads are marked in bold and indicate identifications that
  consistently differ from the expected identification.

The most striking observations from this more in-depth analysis:

* In addition to correct identifications at the species level (the
  typical rank of the expected identification derived from the benchmark
  data), UMGAP also identifies (paired-end) reads correctly but at less
  specific taxonomic ranks (genus level and above) as can be seen from
  the second column in the reports. For some OTUs, UMGAP yields highly
  specific identifications, i.e. most of the OTU reads are correctly
  identified at the species level (species entry marked in bold in the
  second column). For other OTUs, UMGAP yields less specific
  identifications, i.e. most of the OTU reads are correctly identified
  at the genus level or above (species entry not marked in bold in the
  second column). One particular reason for the latter are
  misidentifications in the reference databases, especially because
  UMGAP uses broad spectrum indexes built from the entire UniProt
  Knowledgebase. Using the LCA\* algorithm to compute the taxonomic
  profiling of a single peptide might correct for some
  misidentifications in UniProt, but definitely not all. For example,
  misidentifying UniProt proteins from one strain to another species of
  the same genus, might cause that the taxonomic profiles of most
  peptides of the two species (the correct and wrong identification)
  resolve at the genus level and no longer at the species level. For
  some species groups it is also well known that they are extremely hard
  to differentiate or that there’s even debate whether it is natural to
  keep them taxonomically separate (as the *Bacillus cereus* vs.
  *Bacillus anthracis* case, with multiple OTUs included in the
  MetaBenchmark). Again, problematic identification in these species
  groups also increases the possibility of misidentifications in
  UniProt.

* Wrong identifications exceeding 2% of the total number of (paired-end)
  reads (marked in bold in the third column) are rare and might indicate
  issues with the expected identification in the benchmark dataset. For
  example, in the smaller dataset used for parameter tuning of UMGAP,
  none of the reads for the OTU identified as *Aeromonas hydrophila*
  SSU are identified by UMGAP as the species *A. hydrophila*, whereas
  10% of the reads are identified as the species *A. dhakensis*. If
  we look into the history of the classification of these species,
  *Aeromonas hydrophila* subsp. *dhakensis* was established in 2002 as
  a new subspecies of *A. hydrophila* [@huys], whereas in 2015 it was
  reclassified as a separate species *A. dhakensis* by @beaz. @grim
  reclassified the virulent *A. hydrophila* SSU strain isolated
  from a patient with diarrhea in the Philippines as *A. dhakensis*
  SSU, showing that in this case UMGAP actually comes up with a correct
  identification and instead the identification in the benchmark should
  have been updated. Where @polin mention that A. dhakensis is often
  misidentified as *A. hydrophila*, *A. veronii*, or *A. caviae* by
  commercial phenotypic tests in the clinical laboratory, our analysis
  shows that UMGAP is indeed able to correctly identify reads in a
  metagenomics dataset to *A. dhakensis*. Apart from the power of the
  identification pipeline used by UMGAP, this case study also reminds
  us that taxonomy is not a constant and underscores the importance of
  using broad spectrum indexes that are constantly updated.

* Some OTUs are only identified to the genus rank (or above) in the
  MetaBenchmark, whereas UMGAP consistently identifies many of the
  corresponding (paired-end) reads to one particular species of the same
  genus. An example is *Methylovorus* sp. MP688 in the benchmark
  dataset, where UMGAP assigns 3087 of the 5556 reads (55%) to the
  species *Methylovorus glucosotrophus*. The correctness of this
  observation is confirmed by @doronina based on
  phylogenetic analysis using 16S rRNA gene sequences and mxaF amino
  acid sequences, five years after the complete genome sequence of the
  strain MP688 has been deposited [@xiong] as *Methylovorus*
  sp., a name that has never been updated in the public sequence
  databases. An important factor in this case, is the fact that the
  complete genome sequence *Methylovorus glucosetrophus* strain SIP3-4
  has been deposited in the public sequence database [@lapidus], whose proteome is also available in Uniprot.

* Almost all shuffled reads in the large dataset are mapped to the root
  of the NCBI Taxonomy, which corresponds to no identification at all.
  This reflects the robustness of UMGAP against spurious
  identifications.

* The large dataset contains reads simulated from genomes that were
  artificially diverged from a *Leptospira interrogans* reference
  genome (AE016823). In total, reads for 32 OTUs were generated from
  8 simulated genomes with either little, medium, mixed or high
  divergence. Since these genomes are not random but simulated using an
  evolutionary model, it is expected that the derived reads could be
  assigned to the correct clade. Of the OTUs generated from simulated
  genomes with little divergence, we consistently observe that 35% of
  the reads are correctly identified to the species level and 40% to
  the genus level. Of the OTUs generated from simulated genomes with
  medium divergence, only 1-2% of the reads are correctly identified at
  the species level and 5% at the genus level. Of the OTUs generated
  from simulated genomes with high divergence, almost no reads could
  be identified. OTUs generated from simulated genomes with mixed
  divergence either follow the pattern of genomes with little divergence
  or the genomes with medium divergence.

+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Operational Taxonomic Unit (OTU)                                           | Correct identifications                          | Wrong or overspecific identifications at species rank     |
+============================================================================+==================================================+===========================================================+
| Benchmark OTU ID: `A_hydrophila_HiSeq`                                     | - species: 0 (0.0%)                              | - **Aeromonas dhakensis [taxid 196024]: 103 (10.3%)**     |
|                                                                            | - **genus: 658 (65.8%)**                         | - Aeromonas salmonicida [taxid 645]: 3 (0.3%)             |
| OTU taxon: Aeromonas hydrophila SSU [taxid 1073377]                        | - family: 3 (0.3%)                               | - Aeromonas lusitana [taxid 931529]: 1 (0.1%)             |
|                                                                            | - order: 0 (0.0%)                                | - Azospirillum brasilense [taxid 192]: 1 (0.1%)           |
| Expected: Aeromonas hydrophila [taxid 644] (species)                       | - class: 69 (6.9%)                               | - Aeromonas molluscorum [taxid 271417]: 1 (0.1%)          |
|                                                                            | - phylum: 29 (2.9%)                              | - Aeromonas caviae [taxid 648]: 1 (0.1%)                  |
| Number of reads: 1000                                                      | - superkingdom: 4 (0.4%)                         |                                                           |
|                                                                            | - root: 113 (11.3%)                              |                                                           |
| Number of identified reads: 876 (87.6%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `B_cereus_HiSeq`                                         | - species: 47 (4.7%)                             | - Bacillus mycoides [taxid 1405]: 5 (0.5%)                |
|                                                                            | - **genus: 702 (70.2%)**                         | - Bacillus cytotoxicus [taxid 580165]: 2 (0.2%)           |
| OTU taxon: Bacillus cereus VD118 [taxid 1053231]                           | - family: 13 (1.3%)                              | - Bacillus anthracis [taxid 1392]: 1 (0.1%)               |
|                                                                            | - order: 11 (1.1%)                               | - Persephonella marina [taxid 309805]: 1 (0.1%)           |
| Expected: Bacillus cereus [taxid 1396] (species)                           | - class: 2 (0.2%)                                | - Bacillus thuringiensis [taxid 1428]: 1 (0.1%)           |
|                                                                            | - phylum: 4 (0.4%)                               | - Bacillus pseudomycoides [taxid 64104]: 1 (0.1%)         |
| Number of reads: 1000                                                      | - superkingdom: 14 (1.4%)                        | - Methylobacterium platani [taxid 427683]: 1 (0.1%)       |
|                                                                            | - root: 84 (8.4%)                                | - Bacillus wiedmannii [taxid 1890302]: 1 (0.1%)           |
| Number of identified reads: 877 (87.7%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `B_fragilis_HiSeq`                                       | - **species: 405 (40.5%)**                       | - Prevotella copri [taxid 165179]: 1 (0.1%)               |
|                                                                            | - genus: 249 (24.9%)                             | - Bacteroides caccae [taxid 47678]: 1 (0.1%)              |
| OTU taxon: Bacteroides fragilis HMW 615 [taxid 1073387]                    | - family: 0 (0.0%)                               | - Enterococcus faecalis [taxid 1351]: 1 (0.1%)            |
|                                                                            | - order: 100 (10.0%)                             | - Bacteroides uniformis [taxid 820]: 1 (0.1%)             |
| Expected: Bacteroides fragilis [taxid 817] (species)                       | - class: 1 (0.1%)                                |                                                           |
|                                                                            | - phylum: 7 (0.7%)                               |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 21 (2.1%)                        |                                                           |
|                                                                            | - root: 133 (13.3%)                              |                                                           |
| Number of identified reads: 916 (91.6%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `M_abscessus_HiSeq`                                      | - **species: 296 (29.6%)**                       | - Mycobacterium tuberculosis [taxid 1773]: 1 (0.1%)       |
|                                                                            | - genus: 286 (28.6%)                             | - Mycolicibacterium rhodesiae [taxid 36814]: 1 (0.1%)     |
| OTU taxon: Mycobacteroides abscessus 6G-0125-R [taxid 1001740]             | - family: 71 (7.1%)                              | - Actinoplanes xinjiangensis [taxid 512350]: 1 (0.1%)     |
|                                                                            | - order: 35 (3.5%)                               |                                                           |
| Expected: Mycobacteroides abscessus [taxid 36809] (species)                | - class: 31 (3.1%)                               |                                                           |
|                                                                            | - phylum: 1 (0.1%)                               |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 23 (2.3%)                        |                                                           |
|                                                                            | - root: 121 (12.1%)                              |                                                           |
| Number of identified reads: 864 (86.4%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `P_fermentans_HiSeq`                                     | - **species: 442 (44.2%)**                       | - Lacrimispora celerecrescens [taxid 29354]: 5 (0.5%)     |
|                                                                            | - genus: 141 (14.1%)                             | - Pelosinus propionicus [taxid 380084]: 2 (0.2%)          |
| OTU taxon: Pelosinus fermentans A11 [taxid 1149860]                        | - family: 14 (1.4%)                              | - Eumeta japonica [taxid 151549]: 1 (0.1%)                |
|                                                                            | - order: 2 (0.2%)                                | - Sporomusa acidovorans [taxid 112900]: 1 (0.1%)          |
| Expected: Pelosinus fermentans [taxid 365349] (species)                    | - class: 5 (0.5%)                                |                                                           |
|                                                                            | - phylum: 35 (3.5%)                              |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 28 (2.8%)                        |                                                           |
|                                                                            | - root: 145 (14.5%)                              |                                                           |
| Number of identified reads: 813 (81.3%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `R_sphaeroides_HiSeq`                                    | - species: 84 (8.4%)                             | - Lupinus albus [taxid 3870]: 1 (0.1%)                    |
|                                                                            | - **genus: 279 (27.9%)**                         | - Rhodobacter johrii [taxid 445629]: 1 (0.1%)             |
| OTU taxon: Rhodobacter sphaeroides 2.4.1 [taxid 272943]                    | - family: 98 (9.8%)                              | - Pararhodospirillum photometricum [taxid 1084]: 1 (0.1%) |
|                                                                            | - order: 1 (0.1%)                                |                                                           |
| Expected: Rhodobacter sphaeroides [taxid 1063] (species)                   | - class: 39 (3.9%)                               |                                                           |
|                                                                            | - phylum: 9 (0.9%)                               |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 17 (1.7%)                        |                                                           |
|                                                                            | - root: 109 (10.9%)                              |                                                           |
| Number of identified reads: 638 (63.8%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `S_aureus_HiSeq`                                         | - **species: 503 (50.3%)**                       | - Staphylococcus arlettae [taxid 29378]: 1 (0.1%)         |
|                                                                            | - genus: 217 (21.7%)                             | - Lupinus albus [taxid 3870]: 1 (0.1%)                    |
| OTU taxon: Staphylococcus aureus M0927 [taxid 1213734]                     | - family: 19 (1.9%)                              |                                                           |
|                                                                            | - order: 23 (2.3%)                               |                                                           |
| Expected: Staphylococcus aureus [taxid 1280] (species)                     | - class: 12 (1.2%)                               |                                                           |
|                                                                            | - phylum: 1 (0.1%)                               |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 16 (1.6%)                        |                                                           |
|                                                                            | - root: 86 (8.6%)                                |                                                           |
| Number of identified reads: 878 (87.8%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `S_pneumoniae_HiSeq`                                     | - species: 216 (21.6%)                           | - Streptococcus mitis [taxid 28037]: 4 (0.4%)             |
|                                                                            | - **genus: 524 (52.4%)**                         | - Streptococcus equi [taxid 1336]: 1 (0.1%)               |
| OTU taxon: Streptococcus pneumoniae TIGR4 [taxid 170187]                   | - family: 6 (0.6%)                               | - Ligilactobacillus animalis [taxid 1605]: 1 (0.1%)       |
|                                                                            | - order: 7 (0.7%)                                | - Streptococcus oralis [taxid 1303]: 1 (0.1%)             |
| Expected: Streptococcus pneumoniae [taxid 1313] (species)                  | - class: 5 (0.5%)                                | - Streptococcus infantis [taxid 68892]: 1 (0.1%)          |
|                                                                            | - phylum: 15 (1.5%)                              |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 15 (1.5%)                        |                                                           |
|                                                                            | - root: 79 (7.9%)                                |                                                           |
| Number of identified reads: 867 (86.7%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `V_cholerae_HiSeq`                                       | - species: 171 (17.1%)                           | - Pantoea cypripedii [taxid 55209]: 1 (0.1%)              |
|                                                                            | - **genus: 497 (49.7%)**                         | - Providencia stuartii [taxid 588]: 1 (0.1%)              |
| OTU taxon: Vibrio cholerae CP1032(5) [taxid 991923]                        | - family: 30 (3.0%)                              | - Zobellella denitrificans [taxid 347534]: 1 (0.1%)       |
|                                                                            | - order: 0 (0.0%)                                | - Erwinia tracheiphila [taxid 65700]: 1 (0.1%)            |
| Expected: Vibrio cholerae [taxid 666] (species)                            | - class: 47 (4.7%)                               | - Klebsiella pneumoniae [taxid 573]: 1 (0.1%)             |
|                                                                            | - phylum: 11 (1.1%)                              |                                                           |
| Number of reads: 1000                                                      | - superkingdom: 8 (0.8%)                         |                                                           |
|                                                                            | - root: 117 (11.7%)                              |                                                           |
| Number of identified reads: 881 (88.1%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
|                                                                            |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
| Benchmark OTU ID: `X_axonopodis_HiSeq`                                     | - species: 68 (6.8%)                             | - Xanthomonas arboricola [taxid 56448]: 5 (0.5%)          |
|                                                                            | - **genus: 580 (58.0%)**                         | - Xanthomonas citri [taxid 346]: 4 (0.4%)                 |
| OTU taxon: Xanthomonas axonopodis pv. manihotis str. UA323 [taxid 1185664] | - family: 58 (5.8%)                              | - Xanthomonas oryzae [taxid 347]: 2 (0.2%)                |
|                                                                            | - order: 4 (0.4%)                                | - Moorea sp. SIOASIH [taxid 2607817]: 1 (0.1%)            |
| Expected: Xanthomonas phaseoli [taxid 1985254] (species)                   | - class: 17 (1.7%)                               | - Xanthomonas campestris [taxid 339]: 1 (0.1%)            |
|                                                                            | - phylum: 21 (2.1%)                              | - Salmonella enterica [taxid 28901]: 1 (0.1%)             |
| Number of reads: 1000                                                      | - superkingdom: 16 (1.6%)                        |                                                           |
|                                                                            | - root: 127 (12.7%)                              |                                                           |
| Number of identified reads: 891 (89.1%)                                    |                                                  |                                                           |
+----------------------------------------------------------------------------+--------------------------------------------------+-----------------------------------------------------------+
