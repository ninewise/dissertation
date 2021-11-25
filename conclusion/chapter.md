# Conclusion

In it's current state, UMGAP is unfortunately unable to better all
similar metagenomics diversity analysis tools. The roundtrip through
metaproteomics UMGAP makes carries a hit on performance with it, and it
enforces an upper limit on sensitivity because only coding regions can
be matched to a protein database. Still, UMGAP's accuracy rivals that of
the best tools around and it has a hard-to-measure advantage on unknown
genomes because it is based on database with a wide spectrum.

## Future Work

### Adaptive k-mer Length

One method to improve accuracy further would be to adapt the size of
the k-mers according to their lowest common ancestors. Currently, the
whole index consists of 9-mer peptides. Nearly 10% of those 9-mers,
however, have an LCA of rank phylum or less specific, which is near
useless in most diversity analyses. It would be interesting to see if
the 10-mers these 9-mers are subsequences of, would be more specific. If
so, the k-mer-to-LCA mapping command could, thanks to the structure of
the index, relatively easily be patched to work with k-mers of differing
length. The challenge would be in generating such an index in reasonable
time and space.

### Targeted Index Files

Another way to improve specificity would be to use targeted index files.
At the moment, two general purpose index files are provided for use
with the UMGAP: the tryptic peptide index and the 9-mer index. Both
are based on the complete UniProtKB database. While this is advantages
when analysing unknown samples, in most studies there is preliminary
knowledge about the sample or an interest in only some aspects of the
sample. Constructing an index from only the relevant data would not only
result in a more specific index, but the index would also be smaller and
as such the analysis would be faster. Of course, one should remain wary
of the bias implicit in such an index: some peptides which would match
only against a specific organism in such a database might occur in many
other organisms not included.

Such targeted index files would especially be useful for studies on
samples taken to analyse viral or fungal diversity. Both are strongly
underrepresented in the UniProtKB. Viral genomes in particular are often
included in assemblies of their host genomes, resulting in at best a
'root' identification for the whole genome (if the viral genome is also
included in UniProtKB separately) or a completely wrong identification
(if it isn't). Similarly, targeted index files could also provide a
solution for overrepresentation in the UniProtKB. Organisms with a lot
of recorded genomes tend to occur randomly in completely unrelated
samples.

### Functional Annotations

Because UMGAP predicts genes and links those genes to taxonomic
annotations, it could, in principle, be extended to also link to
functional annotations, similar to how functional annotations were
added to Unipept [@gurdeep]. Indeed, each tryptic peptide or 9-mer
in the UniProtKB can easily be associated with a list of functional
annotations.

The problem is the aggregation of this list. Taxonomic annotations are
structured in a tree with sufficient depth, which makes aggregation
strategies such as the lineage-based and modified LCA possible.
Functional annotations are are structured in a tree of insufficient
depth (e.g. EC-numbers have 4 ranks), which is too few for relevant
aggregation, in a directed acyclic graph (e.g. GO-terms), which is a too
complex structure for meaningful aggregations, or are not structured at
all.

In Unipept, which is for the tryptic peptide index, this was solved by
simply not aggregating them. Tryptic peptides are mapped to a list of
annotations. When visualizing samples, the frequency of each annotation
in all lists is reported, as shown in Figure \ref{fig:go-terms}. While
this is a viable and valuable solution for tryptic peptides, this method
is simply impossible with the current 9-mer index. The associated lists
would increase the size of the index beyond usability.

![GO terms related to biological processes found in the marine example data set in Unipept. On the left, a list is shown with the related terms ordered by the numbered of peptides annotated with them. On the right, the relation between the 5 most occuring terms can be zoomed in on. This graph is provided by QuickGO [@quickgo].\label{fig:go-terms}](./go-terms.png)

Should a practical and meaninful aggregation strategy be found,
functional annotation would be a great addition to UMGAP, as they would
allow exploring the functional potential of a metagenomics sample.

### Metatranscriptomics via Metaproteomics

As shown in section \ref{section:transcript}, by removing the gene
prediction step from UMGAP, it can be applied to metatranscriptomics
data sets. Experimentation shows this modified UMGAP (UMPAP?) is a
potential metaproteomics analysis tool, but further finetuning and
benchmarking studies are in order. Combining such an extension with
functional annotations as detailed above would result in a very useful
metaproteomics tools, allowing both taxonomic diversity and functional
activity analyses.

### Integration in Desktop Application

UMGAP was originally developed separately from the Unipept web
application because the data set size in metagenomics would make
network traversal an issue. Even though most other metagenomics tools
are command line clients as well, a graphical client would most
likely be appreciated by many users. Now Unipept has a desktop client
[@verschaffelt2021], UMGAP could be integrated in this client without
the rest of network issues.

There are several possible approaches to integrate UMGAP in the desktop
client. One would be to call the command line client from the desktop
client as a child process. This is possibly the most loose coupling of
the two programs, and the least work. However, the users would need to
install both tools themselves, which makes this approach less attractive
(the main reason for integration being usability).

Secondly, UMGAP could be linked into the desktop client as a native
library. Some work would be required to make the commands offered by
UMGAP more generic. For instance, most command currently assume input
via *standard input* or files, and a library would also need to accept
input via streams or other data structures. Finding a proper method of
integrating native libraries in the self-contained and sandboxed desktop
client might also be a challenge.

Thirdly, because UMGAP was written in Rust, it could be compiled into
web assembly instead of native code. The resulting library would be more
easily callable from the desktop client's typescript code, but there
would likely be a performance impact on UMGAP.

Nevertheless, integration in the desktop client would be an interesting
avenue. Apart from ease of use, it would also allow more complex
visualizations on the results of the analysis. For instance, comparative
studies are supported by the current version of UMGAP, but the results
can only be viewed as CSV frequency tables. While these can be
visualized in other software, proper visualizations provided by UMGAP
(or the desktop client) would be of better quality.

Moreover, should UMGAP be integrated in the metaproteomics desktop
client, and metatranscriptomics support be extended, the Unipept desktop
client could become a powerful tool for generalized meta-omics studies,
in which the three types of study could work together to draw all
possible information from a single sample.
