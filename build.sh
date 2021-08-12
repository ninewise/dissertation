#!/bin/sh
pandoc --citeproc -o dissertation.pdf --from markdown+citations+footnotes+smart README.md
