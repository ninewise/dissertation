function Image(elem)
	if elem.src:find(".svg$") ~= nil then
		local basename = elem.src:sub(0, -5)
		local output = pandoc.pipe(
			"inkscape",
			{ "--export-area-page", "--export-type=pdf", "-o", basename .. ".pdf", basename .. ".svg" },
			"")
		return pandoc.Image(elem.caption, basename .. ".pdf", elem.title, elem.attr)
	else
		return elem
	end
end
