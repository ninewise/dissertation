pandoc.utils = require 'pandoc.utils'
pandoc.path = require 'pandoc.path'
pandoc.system = require 'pandoc.system'

function fix_links(directory)
	return function(elem)
		if elem.target:find("^http") == nil then
			elem.target = pandoc.path.join({ directory, elem.target })
		end
		return elem
	end
end

function fix_images(directory)
	return function(elem)
		if elem.src:find("^http") == nil then
			elem.src = pandoc.path.join({ directory, elem.src })
		end
		return elem
	end
end

function Header(elem)
	if #elem.content == 1
	and elem.content[1].tag == "Link"
	and elem.content[1].classes:includes "include" then
		local file = io.open(elem.content[1].target)
		local document = pandoc.read(file:read("*a"))
		local dir = pandoc.path.directory(elem.content[1].target)
		return pandoc.walk_block(
			pandoc.Div(document.blocks),
			{ Header = Header, Link = fix_links(dir), Image = fix_images(dir) }
		).content
	end
	return elem
end
