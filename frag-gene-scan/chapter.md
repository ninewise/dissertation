# FragGeneScanRust
\label{chapter:fgsrs}

One of the important steps in UMGAP is the translation of DNA reads to
amino acid sequences via gene prediction. When starting out, the domain
standard, FragGeneScan, and its faster reimplementation FragGeneScan+
were used. However, both have their own set of problems. As a masters
thesis, @degraef forked FragGeneScan+ to FragGeneScan++ to solve a
number of bugs found in FragGeneScan+. Due to the complex thread model
and codebase, not all bugs were fixable. Finally, we decided to create
a brand new implementation of FragGeneScan, called FragGeneScanRs. The
application note publishing this implementation can be found in this
chapter.

<!-- TODO Peter schrapt paragraaf; again why not abstract + cite on first page -->

#### [frag-gene-scan](main.md){.include}

## Performance on Complete Genomes

Originally intended for detecting fragmented genes in short metagenomics
reads, FragGeneScan had a feature added in 1.16 to allow predicting
genes from contigs. This feature consists of an additional training set
(called "complete") and a flag which triggers alternative behaviour
while calculating the probabilities in the Hidden Markov Model and
during the postprocessing of the detected genes. First, the flag
disallows all deletion states in the Markov Chain, effectively banning
deletions in detected genes. Second, the flag increases the minimum size
of detected genes to 120 base pairs instead of 60. Finally, it causes a
scan in the area surrounding the beginning and end of the detected gene
to search for start and stop codons, refining the detected gene.

As the same behaviour is implemented in FragGeneScanRs, a benchmark
comparing the prediction results from FragGeneScan, FragGeneScan+
and FragGeneScanRs on a complete and annotated genome is possible.
Also included in the benchmark is a tool specifically built for
detecting genes in complete prokaryotic genomes and assemblies, Prodigal
[@hyatt2010].

Each tool was executed on the genome of *Geobacter anodireducens*
strain SD-1 [@anodireducens]. To compare the results, each single base
pair is considered either as part of a predicted gene on the forward
strand, part of a predicted gene on the reverse strand, or not in a
predicted gene at all. Table \ref{table:fgs-classification} shows the
classification of the base pairs when compared to the annotated genes.
Table \ref{table:fgs-metrics} shows the resulting quality metrics.

 Annotation \\ Prediction  Forward strand  Reverse strand  None
 ------------------------- --------------- --------------- ---------------
 Forward strand            TP              FP              FN
 Reverse strand            FP              TP              FN
 None                      FP              FP              TN

 Table: Classification of base pairs based on their inclusion in
 annotations and predictions on the forward and reverse strands for gene
 predictors.\label{table:fgs-classification}

 Metric                           FGS      FGS+     FGSrs  Prodigal
 -------------------------- --------- --------- --------- ---------
 True Positives                68.05%    72.61%    68.05%    68.33%
 False Positives                6.31%    14.56%     6.31%     2.78%
 True Negatives                17.92%     9.86%    17.92%    20.72%
 False Negatives                7.72%     2.98%     7.72%     8.17%
 Precision                     91.51%    83.30%    91.51%    96.09%
 Sensitivity                   89.81%    96.06%    89.81%    89.32%
 Specificity                   73.96%    40.38%    73.96%    88.18%
 Negative Predictive Value     69.89%    76.79%    69.89%    71.72%
 Matthews Correlation C.       62.58%    46.79%    62.58%    72.49%
 Speed (bp/s)                    936K      9.6K     2088K      417K

 Table: Performance metrics on the gene predictions of FragGeneScan
 (FGS), FragGeneScan+ (FGS+), FragGeneScanRs (FGSrs) and Prodigal
 on the complete genome of *Geobacter anodireducens* strain
 SD-1. The processing speed is calculated as the length of the
 genome in base pairs over the average execution time of 5
 runs.\label{table:fgs-metrics}

Prodigal is by far the best included gene predictor for complete
genomes. FragGeneScan and FragGeneScanRs obviously have the same
results and score especially more false positives, which impacts its
specificity. Still, it is more than twice as fast as Prodigal (and 5
times faster for FGSrs). FragGeneScan+ is far worse in both quality of
results and speed.
