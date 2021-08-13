#!/bin/sh
if tectonic --help > /dev/null; then
	pdfengine="tectonic"
else
	pdfengine="pdflatex"
fi

pandoc --pdf-engine="$pdfengine" \
       -o dissertation.pdf \
       --metadata-file=frontmatter.yml \
       --lua-filter=filters/include.lua \
       --citeproc \
       --from markdown+citations+footnotes+smart \
       README.md
