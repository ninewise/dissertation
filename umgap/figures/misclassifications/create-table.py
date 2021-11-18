#!/usr/bin/env python
from collections import defaultdict, Counter
import sys
import itertools

ranks = ["species", "genus", "family", "order", "class", "phylum", "superkingdom"]
above_species = ["superkingdom", "kingdom", "subkingdom", "superphylum", "phylum", "subphylum", "superclass", "class", "subclass", "infraclass", "superorder", "order", "suborder", "infraorder", "parvorder", "superfamily", "family", "subfamily", "tribe", "subtribe", "genus", "subgenus", "species_group", "species_subgroup", "species"]

class Organism:
	__slots__ = ["name", "annotation", "reads"]
	def __init__(self, name, annotation):
		self.name = name
		self.annotation = annotation
		self.reads = []

class TaxonRanks:
	__slots__ = ["free", "ranked"]
	def __init__(self, free, ranked):
		self.free = free
		self.ranked = ranked

class Table:
	__slots__ = ["header", "cols", "justify", "rows"]

	def __init__(self, *headers):
		self.header = list(headers)
		self.cols = len(headers)
		self.justify = [str.ljust] * self.cols
		self.rows = []

	def add_row(self, *cells):
		self.rows.append([str(c) for c in cells])

	def rjust(self, column):
		self.justify[column] = str.rjust

	def print(self):
		columnwidth = [ max(len(line) for row in itertools.chain([self.header], self.rows)
		                              for line in row[col].split('\n'))
		                for col in range(len(self.header)) ]

		def print_separator(c):
			print('+' + '+'.join((w + 2) * c for w in columnwidth) + '+')

		def print_row(row):
			print('| ' + ' | '.join(self.justify[i](row[i] or '', columnwidth[i])
			                        for i in range(self.cols)) + ' |')

		print_separator('-')
		print_row(self.header)
		print_separator('=')
		for r, row in enumerate(self.rows):
			if r > 1:
				print_row([''] * self.cols)
				print_separator('-')
			for line in itertools.zip_longest(*[column.split('\n') for column in row]):
				print_row(line)
			print_separator('-')

stripped = lambda lines: (l.strip() for l in lines)
splitted = lambda iterable: (i.split('\t') for i in iterable)

def paired(iterable):
	i = iter(iterable)
	try:
		while True:
			yield next(i), next(i)
	except StopIteration:
		return

with open("readinfo.tsv") as r:
	next(r)
	readinfo = { name: (int(tid), int(count)) for name, tid, count in splitted(stripped(r)) }

with open("../taxons.tsv") as t:
	taxons = { int(tid): (name, rank, int(parent), valid != '\0') for tid, name, rank, parent, valid in splitted(stripped(t)) }

organisms = {}
files = ["names"] + [ f"{t}.{r}" for r in (["taxa"] + ranks) for t in ("annotations", "classifications") ]
files = [open(f) for f in files]
for name, annotation, classification, *ranked in zip(*files):
	name = name.strip()
	if not (o := organisms.get(name)):
		o = organisms[name] = Organism(name, TaxonRanks(int(annotation), [int(r_annotation) for r_annotation in ranked[0::2]]))
	o.reads.append(TaxonRanks(int(classification), [int(r_classification) for r_classification in ranked[1::2]]))
for f in files:
	f.close()

normal_table = Table("Operational Taxonomic Unit (OTU)", "Correct identifications                         ", "Wrong or overspecific identifications at species rank")
random_table = Table("Operational Taxonomic Unit (OTU)", "Correct identifications                         ", "Wrong or overspecific identifications at species rank")
simul_table = Table("Operational Taxonomic Unit (OTU)", "Correct identifications                         ", "Wrong or overspecific identifications at species rank")

for organism in sorted(organisms.values(), key=lambda o: taxons.get(o.annotation.free, ["ZZZZZZZ"])[0]):
	table = normal_table
	if '_Random' in organism.name:
		table = random_table
	elif '_Simulated' in organism.name:
		table = simul_table

	corrects = [0] * len(ranks)
	wrongs = [Counter() for _ in range(len(ranks))]
	unspecifieds = [0] * len(ranks)
	# corrects['unspecified'] = len(organism.reads) # FIXME actually include reads FGS dropped
	for read in organism.reads:
		for r, rank in enumerate(ranks):
			if read.ranked[r] == organism.annotation.ranked[r]:
				corrects[r] += 1
			elif read.ranked[r] == 1:
				unspecifieds[r] += 1
			else:
				wrongs[r][f'{taxons[read.ranked[0]][0]} [taxid {read.ranked[0]}]'] += 1

	s = lambda r, n: f'{r}: {n} ({n * 100000 // readinfo[organism.name][1] / 1000}%)'
	b = lambda s, c: f'**{s}**' if c else s

	target = organism.annotation.free
	while target != 1 and (not taxons.get(target, {3:False})[3] or taxons.get(target, {1:None})[1] not in above_species):
		target = taxons.get(target, {2:1})[2]
	name = ( f'Benchmark OTU ID: `{organism.name}`\n\n'
	       + f'OTU taxon: {taxons.get(organism.annotation.free, [organism.name])[0]} [taxid {organism.annotation.free}]\n\n'
	       + f'Expected: {taxons[target][0] if target != 1 else "unknown"} [taxid {target}] ({taxons[target][1]})\n\n'
	       + f'Number of reads: {readinfo[organism.name][1]}\n\n'
	       + s('Number of identified reads', len(organism.reads))
	       )

	previouscorrect = 0
	usedranks = []
	rankscolumn = []
	for r, rank in enumerate(ranks):
		if organism.annotation.ranked[r] != 1:
			usedranks.append(rank)
			rankscolumn.append(corrects[r] - previouscorrect)
			previouscorrect = corrects[r]
	usedranks.append('root')
	rankscolumn.append(unspecifieds[-1])
	rankscolumn = [ b(s(rank, count), count == max(rankscolumn)) for rank, count in zip(usedranks, rankscolumn) ]

	wrongshere = wrongs[0].most_common()
	wrongscolumn = [b(s(n, c), 50 * c >= len(organism.reads)) for n, c in wrongshere[:len(usedranks)]]
	if len(wrongshere) > len(usedranks) + 1:
		wrongscolumn.append(s('other', sum(c for _, c in wrongshere[len(usedranks):])))

	table.add_row(name,
	              '\n'.join(f'- {l}' for l in rankscolumn),
	              '\n'.join(f'- {l}' for l in wrongscolumn))

print('number of rows in normal:', len(normal_table.rows), file=sys.stderr)
if len(normal_table.rows) > 0:
	print('', '## Sampled reads', '', sep='\n')
	normal_table.print()
	print('\\newpage')
print('number of rows in random:', len(random_table.rows), file=sys.stderr)
if len(random_table.rows) > 0:
	print('', '## Random reads', '', sep='\n')
	random_table.print()
	print('\\newpage')
print('number of rows in simul:', len(simul_table.rows), file=sys.stderr)
if len(simul_table.rows) > 0:
	print('', '## Simulated reads', '', sep='\n')
	simul_table.print()
	print('\\newpage')
