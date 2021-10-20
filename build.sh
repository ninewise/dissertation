#!/bin/sh
if tectonic --version > /dev/null; then
	pdfengine="tectonic"
else
	pdfengine="pdflatex"
fi

output="${1:-dissertation.pdf}"

pandoc --pdf-engine="$pdfengine" \
       -o "$output" \
       --syntax-definition=syntax/shell-example.xml \
       --metadata-file=frontmatter.yml \
       --lua-filter=filters/include.lua \
       --lua-filter=filters/svg-to-pdf.lua \
       --lua-filter=filters/floating-tables.lua \
       --lua-filter=filters/landscaper.lua \
       --lua-filter=filters/short-headers.lua \
       --from markdown+citations+footnotes+smart \
       --citeproc \
       README.md

