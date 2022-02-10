#!/bin/sh
set -e

if tectonic --version > /dev/null; then
	pdfengine="tectonic"
else
	pdfengine="pdflatex"
fi

pandoc -s -o "dissertation.tex" \
       --syntax-definition=syntax/shell-example.xml \
       --metadata-file=frontmatter.yml \
       --lua-filter=filters/include.lua \
       --lua-filter=filters/smaller-codeblocks.lua \
       --lua-filter=filters/smaller-captions.lua \
       --lua-filter=filters/svg-to-pdf.lua \
       --lua-filter=filters/floating-tables.lua \
       --lua-filter=filters/landscaper.lua \
       --lua-filter=filters/short-headers.lua \
       --from markdown+citations+footnotes+smart \
       --citeproc \
       README.md

"$pdfengine" dissertation.tex
