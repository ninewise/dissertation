#!/bin/sh
if pdflatex -version > /dev/null; then
	pdfengine="pdflatex"
else
	pdfengine="tectonic"
fi

pandoc --pdf-engine="$pdfengine" \
       -o dissertation.pdf \
       --metadata-file=frontmatter.yml \
       --lua-filter=filters/include.lua \
       --from markdown+citations+footnotes+smart \
       --citeproc \
       README.md
