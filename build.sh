#!/bin/sh
if tectonic --version > /dev/null; then
	pdfengine="tectonic"
else
	pdfengine="pdflatex"
fi

pandoc --pdf-engine="$pdfengine" \
       -o dissertation.pdf \
       --metadata-file=frontmatter.yml \
       --lua-filter=filters/include.lua \
       --lua-filter=filters/svg-to-pdf.lua \
       --from markdown+citations+footnotes+smart \
       --citeproc \
       README.md
