# FragGeneScan

One of the important steps in the UMGAP is the translation of DNA
reads to amino acid sequences via gene prediction. When starting out,
the domain standard, FragGeneScan, and its faster reimplementation
FragGeneScan+ were used. However, both have their own set of problems.
As a masters thesis, @degraef forked FragGeneScan+ to FragGeneScan++
to solve a number of bugs found in FragGeneScan+. Due to the complex
thread model and codebase, not all bugs were fixable. Finally, we
decided to create a brand new implementation of FragGeneScan, called
FragGeneScanRs. The application note publishing this implementation can
be found in this chapter.

#### [frag-gene-scan](main.md){.include}
