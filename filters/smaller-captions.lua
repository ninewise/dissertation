function Image(el)
	el.caption:insert(1, pandoc.RawInline('latex', '\\small '))
	return el
end
