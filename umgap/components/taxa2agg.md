### Per Read Taxon Aggregation

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
specific and does not exclude peptides found in mammals or primates.
The algorithm to find the modified lowest common ancestor of a list of
taxa is described in Algorithm \ref{alg:rmqlca}. It uses a fast and
space-efficient range minimum query scheme [@fischer] to find the node
with minimum depth in a range of an Euler tour [@tarjan] over the tree
of life. The preparation for these queries can be reused between all
reads in a data set. Note that the consensus taxon need not be in the
aggregated list.

\begin{algorithm}[h]
  \DontPrintSemicolon
  \SetKwData{Taxa}{taxa}
  \SetKwData{Euler}{euler tour}
  \SetKwData{Depths}{depth}
  \SetKwData{FirstOccurence}{first occurrence}
  \SetKwData{RMQ}{RMQ}
  \SetKwData{Consensus}{consensus}
  \SetKwData{JoinLevel}{join level}
  \KwData{A taxonomy $p$ with root $r$, mapping each taxon to its parent and a set to taxa to aggregate \Taxa.}
  \KwResult{The modified lowest common ancestor $a$ of \Taxa in $p$.}
  \BlankLine
  (\Euler, \Depths, \FirstOccurence, \RMQ) $ \longleftarrow \mathtt{prepareRMQ}(p, r)$\;
  (\Consensus, \JoinLevel) $ \longleftarrow (0, \infty)$\;
  \For{$t \in \text\Taxa$}{
    $i \longleftarrow \text\FirstOccurence(t)$\;
    $m \longleftarrow \text\RMQ(\text\Consensus, i)$\;
    $(c, l) \longleftarrow $ \Switch{$m = \text\Consensus, m = i$}{
      \lCase{$(\bot, \bot)$}{$(m, \text\Depths(m))$}
      \lCase{$(\top, \bot)$}{$(i, \text\JoinLevel)$}
      \lOther{$(\text\Consensus, \text\JoinLevel)$}
    }
    \If{$\text\Depths(c) > \text\JoinLevel$}{
      $c \longleftarrow m$\;
    }
    (\Consensus, \JoinLevel) $ \longleftarrow (c, l)$\;
  }
  $a \longleftarrow \text\Euler(\text\Consensus)$\;
\caption{Finding the modified lowest common ancestor of a set of taxa. This algorithm uses the fast and space-efficient range minimum query scheme to find the node with minimum depth in a range of an Euler tour over the tree of life. Note that this range minimum query can be prepared and reused for all reads in a sample.}
\label{alg:rmqlca}
\end{algorithm}

The least conservative strategy is the maximum root-to-leaf path (MRTL)
(Algorithm \ref{alg:mrtl}). This is the taxon in the list with the most
ancestors in the aggregated list. It is calculated by traveling by
direct ancestry to the root of the tree and summing the number of hits
for each of the taxa on the path.

\begin{algorithm}[h]
  \DontPrintSemicolon
  \SetKwData{Taxa}{taxa}
  \KwData{A taxonomy $p$ with root $r$, mapping each taxon to its parent and a set of taxa to aggregate \Taxa.}
  \KwResult{The taxon $m$ in \Taxa with the maximum root-to-leaf path in $p$.}
  \BlankLine
  $c \longleftarrow $ a mapping of each taxon in \Taxa onto 0.\;
  \ForEach{$t \in p$}{
    $a \longleftarrow t$\;
    \While{$a \not= r$}{
      \If{$a \in \text{\Taxa}$}{
        $c[t] \longleftarrow c[a] + 1$\;
      }
      $a \longleftarrow p[a]$\;
    }
  }
  $(m, v) \longleftarrow (r, 0)$\;
  \ForEach{$t \in p$}{
    \If{$c[t] > v$}{
      $(m, v) \longleftarrow (t, v)$\;
    }
  }
\caption{Finding the taxon with the maximum root-to-leaf path in a set of taxa.}
\label{alg:mrtl}
\end{algorithm}

The third strategy of the `umgap taxa2agg` tool is a hybrid of the above
two (Algorithm \ref{alg:hybrid}). Giving a factor *f*, the algorithm
descends from the root of the tree of life towards the leaves, on each
rank choosing the descendant which is the ascendant of most of the taxa
in the list. This, it continues, until the chosen descendant would
represent less then *f* of the strict descendants of the current taxon.
A hybrid strategy with a factor 1.0 would thus behave similar to the
modified lowest common ancestor algorithm, while a factor 0.0 follows
the maximum root-to-leaf path.

\begin{algorithm}[h]
  \DontPrintSemicolon
  \SetKwData{Taxa}{taxa}
  \SetKw{And}{and}
  \KwData{A taxonomy $p$ with root $r$, mapping each taxon to its parent, a factor $f$, and a set to taxa to aggregate \Taxa.}
  \KwResult{The hybrid consensus taxon $h$ of \Taxa in $p$.}
  \BlankLine
  \tcp{Induce a subtree of the nodes in \Taxa on $p$.}
  $c \longleftarrow $ a hashmap of nodes to a set of children\;
  $q \longleftarrow $ a queue, initially filled with the nodes in \Taxa\;
  \While{$i$ pops from $q$ \And $i \not= r$}{
    $p' \longleftarrow p[i]$\;
    \lIf{$p' \not\in c$}{append $p$ to $q$}
    insert $i$ into $c[p']$\;
  }
  \tcp{Map each taxon onto its number of descendants.}
  $v \longleftarrow $ a mapping of each taxon in \Taxa onto 0\;
  \ForEach{$t \in p$}{
    $a \longleftarrow t$\;
    \While{$a \not= r$}{
      \lIf{$a \in \text{\Taxa}$}{$v[t] \longleftarrow v[a] + 1$}
      $a \longleftarrow p[a]$\;
    }
  }
  \tcp{Descend the tree while the ratio of descendants suffices.}
  $(h', f') \longleftarrow (r, 1)$\;
  \While{$h' \in c$ \And $f' \le f$}{
    $h \longleftarrow h'$\;
    $(c, s) \longleftarrow (0, 0)$\;
    \ForEach{$t \in c[h']$}{
      \lIf{$v[t] > v[c]$}{$c \longleftarrow t$}
      $s \longleftarrow s + v[c]$\;
    }
    $(h', f') \longleftarrow (c, v[c] / s)$\;
  }
\caption{A hybrid algorithm of the LCA* and MRTL algorithms.}
\label{alg:hybrid}
\end{algorithm}

#### Usage {#use-taxa2agg}

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

#### Options & Flags {#opts-taxa2agg}

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
