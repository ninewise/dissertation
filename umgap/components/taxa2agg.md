### Aggregation of taxa per read

At some point after mapping each peptide in a read on a taxon ID, and
possibly filtering or manipulating them with other tools, these taxa
need to be aggregated into a single prediction per read. The `umgap
taxa2agg` command offers several strategies to find such a consensus
taxon.

To find a consensus taxon, the position of each of the aggregated taxa
on the tree of life is considered. Comparing one taxon to another, it is
either it's ancestor (a more generic, higher ranked, grouping of which
the other taxon is a subset), it's descendant (the inverse, a subset of
the other more generic taxon) or unrelated.

The most conservative strategy is the modified lowest common ancestor
(LCA\*). This is the most specific taxon which does not contradict any
taxa in the aggregated list. A taxa would contradict the consensus
taxon only if it were unrelated. Consider a read in which some peptides
are found in mammals, some are found in primates, and some are found
in humans. A consensus of primates would not contradict any of these
peptides. After all, a peptide found in mammals could be found in
a primate and humans are a subcategory of primates. However, the
modified lowest common ancestor here would be human, since this is more
specific and does not exclude peptides found in mammals or primates. The
algorithm to find the modified lowest common ancestor of a list of taxa
is described in TODO pseudocode. Note that the consensus taxon need not
be in the aggregated list.

*TODO pseudocode*

The least conservative strategy is the maximum root-to-leaf path (MRTL).
This is the taxon in the list with the most ancestors in the aggregated
list. It is calculated by traveling by direct ancestry to the root of
the tree and summing the number of hits for each of the taxa on the
path.

*TODO pseudocode*

The third strategy of the `umgap taxa2agg` tool is a hybrid of the above
two. Giving a factor *f*, the algorithm descends from the root of the
tree of life towards the leaves, on each rank choosing the descendant
which is the ascendant of most of the taxa in the list. This, it
continues, until the chosen descendant would represent less then *f*
of the strict descendants of the current taxon. A hybrid strategy with
a factor 1.0 would thus behave similar to the modified lowest common
ancestor algorithm, while a factor 0.0 follows the maximum root-to-leaf
path.

*TODO pseudocode*

#### Usage

The input is given in a FASTA format on standard input. Each FASTA
record contains a list of taxon IDs, separated by newlines. The output
is written to standard output, also in a FASTA format, each record
containing a single taxon ID, which is the consensus taxon resulting
from aggregation of the given list.

The taxonomy to be used is passed as an argument to this command. This
is a preprocessed version of the NCBI taxonomy.

```shell
$ cat input.fa
>header1
571525
571525
6920
6920
1
6920
$ umgap taxa2agg taxons.tsv < input.fa
>header1
571525
```

By default, the aggregation used is the maximum root-to-leaf path
(MRTL). A variant of the lowest common ancestor (LCA\*) aggregation is
also available via the `-a` and `-m` options, as is a hybrid approach.

* `-m rmq -a mrtl` is the default aggregation strategy. It selects the
  taxon from the given list which has the highest frequency of ancestors
  in the list (including its own frequency). A range-minimum-query (RMQ)
  algorithm is used.

* `-m tree -a lca*` returns the taxon (possibly not from the list) of
  lowest rank without contradicting taxa in the list. Non-contradicting
  taxa of a taxon are either itself, its ancestors and its descendants.
  A tree-based algorithm is used.

* `-m tree -a hybrid` mixes the above two strategies, which results in a
  taxon which might have not have the highest frequency of ancestors in
  the list, but would have less contradicting taxa. Use the `-f` option
  to select a hybrid close to the MRTL (`-f 0.0`) or to the LCA\*
  (`-f 1.0`).

#### Options & flags

`-h / --help`
  ~ Prints help information

`-r / --ranked`
  ~ Let all taxa snap to taxa with a named rank (such as species) during
    calculations

`-s / --scored`
  ~ Each taxon is followed by a score between 0 and 1

`-V / --version`
  ~ Prints version information

`-f / --factor f`
  ~ The factor for the hybrid aggregation, from 0.0 (MRTL) to 1.0
    (LCA\*) [default: 0.25]

`-l / --lower-bound l`
  ~ The smallest input frequency for a taxon to be included in the
    aggregation [default: 0]

`-m / --method m`
  ~ The method to use for aggregation [default: tree] (possible values:
    tree, rmq)

`-a / --aggregate a`
  ~ The strategy to use for aggregation [default: hybrid] (possible
    values: lca\*, hybrid, mrtl)
