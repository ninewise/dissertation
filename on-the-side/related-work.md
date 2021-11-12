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

SMAP haplotype is the haplotype calling component of the software
package. Given the SMAP and Single Nucleotide Polymorphism (SNP)
positions, it calculates the haplotype for each read in all samples.
It compares the nucleotide on each SMAP or SNP position with that same
position in the reference genome. This position is either the same
(0), different (1) or missing (.) in the read. The resulting string
of zeroes, ones and points is the haplotype. Finally, it reports the
frequency of each haplotype on every locus in each sample.

<!-- TODO: same as SPeDE -->

<!-- TODO 2019: focus on haplotype calling
- inputdata:  init rombaut:
  66M         110s
  134M        110s
  266M        800s
  4G           N/A
  19G        1200s
-->

<!-- TODO 2021: focus on haplotype window -->
