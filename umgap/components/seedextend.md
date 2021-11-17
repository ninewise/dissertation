### Location-based Taxon Filtering

When mapping peptides on taxa, mutations and read-errors can cause
accidental identifications of completely unrelated taxa. These wrong
identifications could disrupt the aggregation of the taxa further
on in the pipeline. Especially the lowest common ancestor algorithm
is vulnerable to such mistakes (a single arbitrary hit can cause an
otherwise correctly identified read to be reported as unidentifiable).

Fortunately, such accidental hits are usually surrounded by
unidentified peptides, especially when using the overlapping *k*-mer
fragmentation. The `umgap seedextend` tool can be used to filter
isolated identifications from the list of taxa for each read.

It starts by identifying seeds in the list of taxonomic identifications.
These seeds are ranges of *s*, the minimum seed size, or more identical
taxa. Next, each of these seeds is extended to the left and the right,
forming an extended seed. An identified taxon is included in an extended
seed if it lies withing *g* taxa of an extended seed, with *g* the
maximum gap size. Note that an extended seed may contain multiple
seeds. Finally, the `seedextend` command will write out only those taxa
contained in any of the extended seeds.

Such a seed extend algorithm can be implemented as a linear aggregation
of a set of extended seeds and a single candidate extended seed
over a list of taxonomic identifications, as shown in Algorithm
\ref{alg:seedextend}.

<!-- TODO decrease vertical size -->

\begin{algorithm}[h]
  \DontPrintSemicolon
  \KwData{The minimum seed size $s$, the maximum gap size $g$, and a list of taxa $r$.}
  \KwResult{A list of ranges marking the selected taxa $l$.}
  \SetKwData{LastTid}{last tid}
  \SetKwData{SameTid}{same tid}
  \SetKwData{SameMax}{same max}
  \SetKwData{Start}{start}
  \SetKw{And}{and}
  \BlankLine
  $l \longleftarrow \emptyset$\;
  $b \longleftarrow 0$ \tcp{begin of current extended seed}
  $e \longleftarrow 1$ \tcp{end of current extended seed}
  (\LastTid, \SameTid, \SameMax) $\longleftarrow (r[b], 1, 1)$\;
  \While{$e < \mathtt{length}(t)$}{
    \uIf{\LastTid $= r[e]$}{
      \tcp{same taxon ID as last, add to seed}
      \SameTid $\longleftarrow$ \SameTid + 1\;
    }
    \uElseIf{\LastTid $= 0$ \And \SameTid $> g$}{
      \tcp{gap larger than maximum gap size}
      \If{\SameMax $\ge s$}{
        \tcp{extended seed contains seed}
        append $[b, e - \text{\SameTid}[$ to $l$\;
      }
      $b \longleftarrow e$\;
      (\LastTid, \SameTid, \SameMax) $\longleftarrow (r[b], 1, 1)$\;
    }
    \uElseIf{\LastTid $= 0$ \And $e - b =$ \SameTid}{
      \tcp{unidentified taxon at start, do not include it}
      $b \longleftarrow e + 1$\;
    }
    \Else{
      \If{\LastTid $\not= 0$}{
        \tcp{change of taxon at current extended end}
        \SameMax $\longleftarrow \mathtt{max}(\text\SameMax, \text\SameTid)$\;
      }
      \LastTid $\longleftarrow r[e]$\;
      \SameTid $\longleftarrow 1$\;
    }
    $e \longleftarrow e + 1$\;
  }
  \If{\SameMax $\ge s$}{
    \tcp{final extended seed contains seed}
    \If{\LastTid $= 0$}{
      $e \longleftarrow e - \text\SameTid$\;
    }
    append $[b, e[$ to $l$\;
  }
\caption{The seed-extend algorithm to find regions of consecutive identifications.}
\label{alg:seedextend}
\end{algorithm}

#### Usage {#use-seedextend}

The input is given in a FASTA format on standard input. It should
consist of taxon IDs separated by newlines, and the order of these taxa
should reflect their location on a peptide, such as output by the `umgap
prot2kmer2lca -o` command. As such, 3 consecutive equal IDs representing
9-mers, for instance, indicate a 11-mer match. This so-called seed could
still be extended with other taxa, forming an extended seed. The command
writes all taxa in any of these extended seeds to standard output.

```shell
$ cat dna.fa
>header1
CGCAGAGACGGGTAGAACCTCAGTAATCCGAAAAGCCGGG
ATCGACCGCCCCTTGCTTGCAGCCGGGCACTACAGGACCC
$ umgap translate -n -a < dna.fa | \
  umgap prot2kmer2lca 9mer.index > input.fa
>header1|1
9606 9606 2759 9606 9606 9606 9606 9606 9606 9606 8287
>header1|2
2026807 888268 186802 1598 1883
>header1|3
1883
>header1|1R
27342 2759 155619 1133106 38033 2
>header1|2R
>header1|3R
2951
$ umgap seedextend < input.fa
>header1|1
9606 9606 2759 9606 9606 9606 9606 9606 9606 9606 8287
>header1|2
>header1|3
>header1|1R
>header1|2R
>header1|3R
```

Taxon IDs are separated by newlines in the actual output, but are
separated by spaces in this example.

The number of consecutive equal IDs to start a seed is 2 by default, and
can be changed using the `-s` option. The maximum length of gaps between
seeds to join in an extension can be set with `-g`, no gaps are allowed
by default.

The command can be altered to print only the extended seed with the
highest score among all extended seeds. Pass a taxonomy using the `-r
taxon.tsv` option to activate this. In this scored mode, extended seeds
with gaps are given a penalty of 5, which can be made more or less
severe (higher or lower) with the `-p` option.

#### Options & Flags {#opts-seedextend}

`-h / --help`
  ~ Prints help information

`-V / --version`
  ~ Prints version information

`-g / --max-gap-size g`
  ~ The maximum length of a gap between seeds in an extension [default: 0]

`-s / --min-seed-size s`
  ~ The minimum length of equal taxa to count as seed [default: 2]

`-p / --penalty p`
  ~ The score penalty for gaps in extended seeds [default: 5]

`-r / --ranked r`
  ~ Use taxon ranks in given NCBI taxonomy TSV-file to pick extended seed with highest score
