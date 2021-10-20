function Div(el)
	if el.classes:includes("landscape") then
		local result = pandoc.List()
		result:insert(pandoc.RawBlock('latex', '\\begin{landscape}\n'))
		result:extend(el.content)
		result:insert(pandoc.RawBlock('latex', '\\end{landscape}\n'))
		return result
	end
end
