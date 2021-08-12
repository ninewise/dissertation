#!/bin/sh
pandoc --citeproc -o dissertation.pdf --metadata-file=frontmatter.yml --from markdown+citations+footnotes+smart README.md
