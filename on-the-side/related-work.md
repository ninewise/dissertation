## Related Work {#section:relatedwork}

TODO vermelden wat we kunnen bijdragen hebben

"vanuit het vak is een samenwerking ontstaan..."

### SPeDE: Spectral Dereplication

SPeDE [@dumolin] is a program that is used to dereplicate large sets of
MALDI-TOF MS spectra. The analysis consist of screening the dataset for
spectra with unique spectral features and outputs the reduced set of
selected reference spectra. Spectra not assigned as a reference are
matched according to their matching reference spectra.

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

When introduced, the implementation of the described algorithm was
insufficiently fast for common use. As part of the Computational
Biology 2018 course, I guided the students through optimizing this
implementation.

The foremost optimization applied was the parallelization of the
calculation of the uniqueness matrix. Each value on position $(i, j)$ in
the uniqueness matrix is calculated independent of all other values except
the value on position $(j, i)$, allowing for massive parallelization.

Additionally, optimizations were done on the calculation of the unique
peaks (mostly by reducing the data stored), some indexing algorithms
(replacing linear with binary search in sorted arrays) and removing code
with unused results.

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

<!-- TODO 2019: focus on haplotype calling -->

<!-- TODO 2021: focus on haplotype window -->
