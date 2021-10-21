pandoc.utils = require('pandoc.utils')

function inline(s)
	return pandoc.RawInline('latex', s)
end

function block(s)
	return pandoc.RawBlock('latex', s)
end

function caption(t)
	local result = pandoc.List()
	result:insert(inline('\\caption{\\small '))
	result:extend(pandoc.utils.blocks_to_inlines(t.long))
	result:insert(inline('}'))
	return pandoc.Plain(result)
end

aligns = {
	AlignDefault = "l",
	AlignLeft = "l",
	AlignCenter = "c",
	AlignRight = "r",
}

function alignment(colspecs)
	return table.concat(colspecs:map(function(p)
		return aligns[p[1]]
	end))
end

function headers(hs)
	local result = pandoc.List()
	for _, row in pairs(hs[2]) do
		result:extend(pandoc.utils.blocks_to_inlines(row[2][1].contents))
		for c = 2, #(row[2]) do
			result:insert(inline(' & '))
			result:extend(pandoc.utils.blocks_to_inlines(row[2][c].contents))
		end
		result:insert(inline(' \\\\\n\\midrule\n'))
	end
	return pandoc.Plain(result)
end
--     result.append(inlatex(r' \\\midrule'))

function contents(cs)
	local rows = pandoc.List()
	for _, body in pairs(cs) do
		for _, row in pairs(body.body) do
			local lrow = pandoc.List()
			lrow:extend(pandoc.utils.blocks_to_inlines(row[2][1].contents))
			for c = 2, #(row[2]) do
				lrow:insert(inline(' & '))
				lrow:extend(pandoc.utils.blocks_to_inlines(row[2][c].contents))
			end
			lrow:insert(inline(' \\\\\n'))
			rows:insert(pandoc.Plain(lrow))
		end
	end
	return rows
end

function Table(elem)
	local result = pandoc.List()
	result:insert(block('\\begin{table}[ht]\n\\centering\n'))
	result:insert(block('\\begin{tabular}{@{}' .. alignment(elem.colspecs) .. '@{}}\n\\toprule\n'))
	result:insert(headers(elem.head))
	result:extend(contents(elem.bodies))
	result:insert(block('\\bottomrule\n\\end{tabular}\n'))
	result:insert(caption(elem.caption))
	result:insert(block('\\end{table}'))
	return result
end
