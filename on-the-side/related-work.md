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

* SMAP
