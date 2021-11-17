## Related Work {#section:relatedwork}

During my PhD, one of the courses of which I was the teaching assistant
is the Computational Biology course. This is a course given to the
3rd year computer science students. In this course, they are taught
practical optimization algorithms and methods, in a mild biological
context. Since it's a practical course, part of the work is an
optimization project.

To offer the students experience in working on an existing code base,
and to keep the course interesting for both us and them, we elected to
work together with external partners on a project. We look for a third
party with a (partial) developed code base stuck on the execution time.

I start by analyzing the code myself, to ensure there is room for
optimizations our students could handle. If there is, we slightly
package the problems into a cleaner assignment for the students. We
guide the students through the optimization, serving as first line
contact for questions (forwarding more complex biological questions to
the partner). At the end of the semester, while grading, I take notes on
the results of students (often things I hadn't thought of myself during
the prior inspection). I present these results to the partner, and
possibly provide aid in implementing them in the actual product.

Below I describe two of the projects we've worked on. The first
partner, in 2018, was the Department of Molecular Biology at the Ghent
University. Charles Dumolin, Aurélien Carlier and Peter Vandamme
introduced us to the SPeDE project. In 2019, we visited the Flanders
Research Institute for agriculture, fisheries and food (ILVO) with
the students on invitation of Tom Ruttink and Dries Schaumont. They
introduced our students to the SMAP project. In 2020, we partnered
with ourselves as the Unipept team, and had the students work on
the FragGeneScan project, the results of which leaded to Chapter
\ref{chapter:fgsrs}. In 2021, we once more joined up with Tom and Dries
on the SMAP project.

### SPeDE: Spectral Dereplication

SPeDE is a program that is used to dereplicate large sets of MALDI-TOF
MS spectra. The analysis consist of screening the dataset for spectra
with unique spectral features and outputs the reduced set of selected
reference spectra. Spectra not assigned as a reference are matched
according to their matching reference spectra.

The dereplication starts out by creating, for a list of $n$ spectra,
a $n \times n$ uniqueness matrix of integers. The value at $(i, j)$ in
the matrix corresponds to the number of peaks in spectrum $j$ which
do not occur in spectrum $i$. The list of spectra is reordered to
sort the columns according to descending column sum. Going to the
matrix in reading order, encountering a zero value at position $(i, j)$
means spectrum $j$ has no peaks which do not occur in spectrum $i$.
Both spectra are put in the same cluster (possibly along with earlier
clustered spectra). Furthermore, if they are clustered together, the
Pearson correlation coefficient between the two spectra is calculated.
Should it be above a specified threshold, spectrum $i$ is marked as a
reference spectrum for $j$.

When SPeDE was introduced to us, it offered an interesting new
technology, but the implementation was insufficient. For a small sample
data set of 500 spectra, the original code took about 15 minutes. More
realistic data sets would take several weeks to compute. This makes the
program unusable in practice.

The foremost optimization applied was the parallelization of the
calculation of the uniqueness matrix. Each value on position $(i,
j)$ in the uniqueness matrix is calculated independent of all other
values except the value on position $(j, i)$, allowing for massive
parallelization.

Additionally, optimizations were done on the calculation of the unique
peaks (mostly by reducing the data stored), some indexing algorithms
(replacing linear with binary search in sorted arrays) and removing code
with unused results.

Applying these optimizations, some students managed to process the same
sample data set in less than a minute and the realistic data sets (5000
spectra) just under 2 hours.

These results were passed to the Department of Molecular Microbiology,
and they hired a short-term programmer to combine them and further
polish the program. A graphical user interface was added, and the final
result was published [@dumolin].

### SMAP

SMAP is a software package that analyzes read mapping distributions and
performs haplotype calling to create multi-allelic molecular markers.
SMAP delineate processes a series of aligned reads. It groups all
reads from a single locus (region of reads) with the same start and
end positions in a stack, with the number of reads in the stack called
the stack depth. Each of the start and end positions is called a Stack
Mapping Anchor Point (SMAP). These stacks are gathered per sample into a
stack cluster (with the number of reads called the stack cluster depth).
Finally, the collection of all SMAP positions across a sample set is
called a merged cluster.

#### SMAP Haplotype

SMAP haplotype is the haplotype calling component of the software
package. Given the SMAP and Single Nucleotide Polymorphism (SNP)
positions, it calculates the haplotype for each read in all samples.
It compares the nucleotide on each SMAP or SNP position with that same
position in the reference genome. This position is either the same
(0), different (1) or missing (.) in the read. The resulting string
of zeroes, ones and points is the haplotype. Finally, it reports the
frequency of each haplotype on every locus in each sample.

<!-- TODO 2019: focus on haplotype calling
- pagina 38 & 76 (Marzougui & Renders) 
                           Dataset (GB)  Originele   Na optimalisatie Versnelling
4n ind HiPlex PE DOMtetra  0.0572         1m10.329s   0m7.420s         9.4783
4n ind HiPlex PE DOStetra  0.1159         1m09.047s   0m7.222s         9.5606
2n pools HiPlex PE         0.1438         3m13.870s   0m9.312s        20.8194
2n ind HiPlex PE           0.2336        11m18.590s  0m24.987s        27.1577
4n ind GBS PE DOMtetra     1.9           62m44.140s  3m14.171s        19.3857
2n ind GBS PE              3.1           49m15.363s  2m55.788s        16.8121
4n ind GBS PE DOStetra     3.9           61m48.741s  3m17.864s        18.7439
4n pools GBS PE            18.3          68m53.461s  2m59.557s        23.0203
2n pools GBS PE            19.3          83m42.120s  3m28.785s        24.0540
-->

The software package was introduced to us and the students as a nearly
complete product, with the execution speed as a blocking factor for
publication.
For HiPlex dataset of about 230MB, the initial implementation took 10
minutes to process. For a GBS dataset of 19.3G, this was 83 minutes. The
first problem in the initial implementation was the iteration of the
loci. Per reference genome, all reads were considered for haplotyping;
not just the ones in the current locus. By filtering on locus, most
reads can be skipped in each iteration.

Secondly, many of the reads are equal, so they will have the same
haplotype as well. Instead of calculating the haplotype for a read we've
encountered before, we memoize (some) past reads in a cache with a least
recently used replacement policy.

The final large optimization is the iteration of the aligned reads
when constructing the haplotype string. Originally, the whole reads
were iterated over, considering for each base pair if it lies on a SNP
or SMAP position. Instead, iterating over the SNP and SMAP positions
is much faster, as the vast majority of the base pairs is irrelevant
for the haplotype string. Utilizing the CIGAR string, which describes
the insertions and deletions in the alignment, the nucleotides on the
SNP and SMAP positions can be retrieved in linear time in the number of
indels instead of in the number of base pairs.

The combination of these major optimizations with some smaller changes
introduced a speedup of factor 25, bringing the execution time for the
previous data sets to 24 seconds for the smaller and 3.5 minutes for the
larger. The final product was presented at the International Plant &
Animal Genome conference [@ruttink].

#### SMAP Haplotype-window

SMAP haplotype-window is an alternative method for haplotyping reads.
It is primarily meant for use with targeted resequencing: a number of
mutations are chosen and applied to a great number of clones, inducing
to each clone a random subset of the mutations. Such a multiplex
combinatorial screen allows testing multiple mutations at the same
time, and their interactions. SMAP haplotype-window comes in play after
sequencing the resulting genomes. By deriving a haplotype from the
sequence in the windows in which the mutations were induced, it groups
together the combinations of mutations.

In short, the algorithm links reads to windows, and trims the forward
and reverse primers from the read. The DNA sequence in the resulting
window is the haplotype of the read. The haplotypes are aggregated in a
frequency table.

As with SMAP haplotype, the software presented to us was in a nearly
finalized state, with extensive documentation and usage manuals. The
implementation seemed more advanced to me than the SMAP haplotype code
(before our interference), but still lacking in some areas.

Before starting optimizations, a bug was found in the original
implementation. When encountering reversed reads (not in the same
reading direction as the reference sequence), the read was swapped for
its reverse complement for the remainder of the algorithm. However, when
multiple reverse reads where encountered in consecutively, the read was
reversed each time, resulting in alternating incorrect reads.

Major optimizations could be made in the implementation by reducing the
number of dependencies. First, a library called Cutadapt [@cutadapt] was
used to trim the reads to windows. The Cutadapt library, however, is
meant for intelligent trimming, allowing errors in the primers. Because
SMAP haplotype window only needs exact matches, dropping the library and
matching ourselves proved to be a significant optimization. Second, the
pybedtools library [@pybedtools] was used to find intersections between
windows. Unfortunately, to communicate with the fast BedTools executable
[@bedtools], the reads need to be written to disk. This proves to be a
bottleneck sufficiently large to outweigh the use of a fast library. A
fairly simple intersection algorithm was added to the SMAP haplotype
window code instead.

Further minor optimizations included replacing a list with a dictionary
for faster lookup of the windows and the combination of several
filtering loops into a single one.

Over all, the students managed a speedup of 6.8 (reducing the execution
time from 245 to 36 seconds for an example data set).
