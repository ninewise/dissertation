pandoc.utils = require 'pandoc.utils'

function Header(elem)
	if elem.level == 4
	and elem.content[1].tag == "Link"
	and pandoc.utils.stringify(elem.content[1].content)
	      == "include " .. elem.content[1].target then
		file = io.open(elem.content[1].target)
		document = pandoc.read(file:read("*a"))
		return document.blocks
	end
	return elem
end
