function CodeBlock(el)
	return { 
		pandoc.RawBlock('latex', '{\\footnotesize\n'),
		el,
		pandoc.RawBlock('latex', '\n}\n')
	}
end
