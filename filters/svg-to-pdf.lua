function Image(elem)
	if elem.src:find(".svg$") ~= nil then
		local basename = elem.src:sub(0, -5)
		local pdfdate = io.popen("stat -c %Y " .. basename .. ".pdf"):read()
		local svgdate = io.popen("stat -c %Y " .. basename .. ".svg"):read()
		if pdfdate == nil or pdfdate <= svgdate then
			local output = pandoc.pipe(
				"inkscape",
				{ "--export-area-page", "--export-type=pdf", "-o", basename .. ".pdf", basename .. ".svg" },
				"")
		end
		return pandoc.Image(elem.caption, basename .. ".pdf", elem.title, elem.attr)
	else
		return elem
	end
end
