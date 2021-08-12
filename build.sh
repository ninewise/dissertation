#!/bin/sh
pandoc --citeproc \
       -o dissertation.pdf \
       --metadata-file=frontmatter.yml \
       --from markdown+citations+footnotes+smart \
       README.md \
       opening.md \
       introduction.md \
       writing-umgap.md \
       frag-gene-scan.md \
       make-database.md \
       applications.md \
       related-work.md \
       conclusion.md \
       closing.md
