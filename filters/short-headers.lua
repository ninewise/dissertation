-- after https://groups.google.com/g/pandoc-discuss/c/S_tfobmK3vQ

-- Print a formatted warning to stderr
function warnf (...)
  io.stderr:write(string.format(...))
end

function Header (el)
  -- Replace heading with raw LaTeX if pageheading is used to specify a
  -- shorter form of the title to use in page headers.
  if el.attributes.pageheading then
    local commands = {'chapter', 'section', 'subsection'}
    local modifier = ""
    if el.classes:includes("unnumbered") then
      modifier = "*"
    end
    if el.level > #commands then
      warnf('pageheading attribute not supported for level %d headings', el.level)
      return el
    end
    -- Produce LaTeX like pandoc does, but with two additional arguments
    -- to specify a short for of the page heading to memoir.
    local title = pandoc.utils.stringify(el)
    local latexStr = string.format('\\%s[%s]{%s}', commands[el.level] .. modifier, el.attributes.pageheading, title)
    local label = string.format('\\label{%s}', el.identifier)
    -- wrap in hypertarget
    latexStr = string.format('\\hypertarget{%s}{%%\n%s%s}', el.identifier, latexStr, label)
    return pandoc.RawBlock('latex', latexStr)
  end
end