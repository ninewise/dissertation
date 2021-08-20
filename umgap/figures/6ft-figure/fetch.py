import requests
import sys
from contextlib import contextmanager
import subprocess
import io
from functools import wraps
import pprint
import itertools
import xml.etree.ElementTree

import drawSvg as draw # pip install drawSvg

server = 'http://rest.ensembl.org'

@contextmanager
def get(path, **headers):
	r = requests.get(path, headers=headers)
	if not r.ok:
		print('ensembl API unavailable')
		r.raise_for_status()
	yield r


@contextmanager
def run(*process, stdin=''):
	p = subprocess.run(process, input=stdin, capture_output=True, text=True)
	if p.returncode != 0:
		print(p.stderr)
		p.check_returncode()
	yield p.stdout


def fasta(taxon, species, chromosome, start, end):
	with get(f'{server}/sequence/region/{species}/{chromosome}:{start}..{end}:1?', content_type='text/x-fasta') as r:
		return r.text


def fetch_genes(taxon, species, chromosome, start, end):
	with get(f'{server}/overlap/region/{species}/{chromosome}:{start}..{end}:1?feature=gene', content_type='application/json') as r:
		return r.json()


def fetch_transcript(gene):
	with get(f'https://www.uniprot.org/uniprot?query={gene}&format=xml') as r:
		xmlContent = xml.etree.ElementTree.fromstring(r.text)
		return xmlContent.findall(".//*[@type='EnsemblBacteria']/*[@type='protein sequence ID']")[0].get('value')


def on_adler(command, fasta):
	with run('ssh', 'Adler', command, stdin=fasta) as output:
		return output


def run_fgs(fasta):
	return on_adler(('/data/felix/FragGeneScanPlusPlus/FGSpp -s stdin -o stdout -w 0 -r "/data/felix/FragGeneScanPlusPlus/train" -t "illumina_10" -p 16 -c 240 |'
	                 '~/.cargo/bin/umgap prot2kmer2lca -o /data/felix/database/2020-12-02/ninemer.fst |'
	                 "sed 's/^0$/1/' |" # no match means root
	                 '~/.cargo/bin/umgap taxonomy -a -H /data/felix/database/2020-12-02/taxons.tsv' # get full taxonomy
	                ), fasta)


def run_fgsrs(fasta):
	return on_adler(('~/.cargo/bin/FragGeneScanRs -r "/data/felix/frag_gene_scan_rs/train" -t "illumina_10" |'
	                 '~/.cargo/bin/umgap prot2kmer2lca -o /data/felix/database/2020-12-02/ninemer.fst |'
	                 "sed 's/^0$/1/' |" # no match means root
	                 '~/.cargo/bin/umgap taxonomy -a -H /data/felix/database/2020-12-02/taxons.tsv' # get full taxonomy
	                ), fasta)


def run_6ft(fasta):
	return on_adler(('~/.cargo/bin/umgap translate -a -n |'
	                 '~/.cargo/bin/umgap prot2kmer2lca -o /data/felix/database/2020-12-02/ninemer.fst |'
	                 "sed 's/^0$/1/' |" # no match means root
	                 '~/.cargo/bin/umgap taxonomy -a -H /data/felix/database/2020-12-02/taxons.tsv' # get full taxonomy
	                ), fasta)


def get_lineage(taxon):
	return on_adler('~/.cargo/bin/umgap taxonomy -H -a /data/felix/database/2020-12-02/taxons.tsv',
	                str(taxon))

class Marker:

	__slots__ = [ 'start', 'end', 'frame', 'color', 'opacity' ]

	def __init__(self, start, end, frame, color='black', opacity=1):
		self.start = start
		self.end = end
		self.frame = frame
		self.color = color
		self.opacity = opacity

	def translate(self, y):
		self.frame += y

	def draw(self, d, scale, margin, height_per_frame, frames):
		d.append(draw.Line(
			self.start * scale,
			frames * height_per_frame - self.frame * height_per_frame - height_per_frame / 2,
			self.end * scale,
			frames * height_per_frame - self.frame * height_per_frame - height_per_frame / 2,
			stroke=self.color,
			stroke_width=5,
			stroke_linecap='round',
			opacity=self.opacity))


class Strand:

	__slots__ = [ 'start', 'end', 'frame', 'text' ]

	def __init__(self, start, end, frame):
		self.start = start
		self.end = end
		self.frame = frame
		self.text = ['1', '2', '3', '-1', '-2', '-3'][frame]

	def translate(self, y):
		self.frame += y

	def draw(self, d, scale, margin, height_per_frame, frames):
		d.append(draw.Line(
			self.start * scale,
			frames * height_per_frame - self.frame * height_per_frame - height_per_frame / 2,
			self.end * scale,
			frames * height_per_frame - self.frame * height_per_frame - height_per_frame / 2,
			stroke='#000000',
			#stroke_width=1,
			stroke_linecap='round'))
		d.append(draw.Text(self.text, 10,
			-4,
			(frames - self.frame - 1/2) * height_per_frame,
			text_anchor='end',
			alignment_baseline='middle'))


class Annotation:

	__slots__ = [ 'start', 'end', 'text', 'frame', 'color' ]

	def __init__(self, start, end, text, frame, color='000000'):
		self.start = start
		self.end = end
		self.text = text
		self.frame = frame
		self.color = color

	def translate(self, y):
		# self.frame += y # annotation on gene
		pass # annotation on top

	def draw(self, d, scale, margin, height_per_frame, frames):
		d.append(draw.Text(self.text, 14, 
		    (self.start + self.end) / 2 * scale,
		    # (frames - self.frame - 1/2) * height_per_frame, # annotation on gene
		    (frames - 1) * height_per_frame, # annotation on top
		    text_anchor='middle',
		    alignment_baseline='middle'))


def strip_lineage(lineage):
	return '\t'.join(lineage.strip().rstrip('\t').split('\t')[3:])


def translate(y, markers):
	for marker in markers:
		marker.translate(y)
		yield marker


def parse_6ft(width, reflineage, sixft):
	frame = -1
	offsets = [0, 1, 3, 0, 1, 2]
	forward = [True] * 3 + [False] * 3
	for line in sixft.split('\n'):
		if line.startswith('>'):
			frame += 1
			yield Strand(0, width, frame)
			start = 0
		else:
			curlineage = strip_lineage(line)
			color = '#2e7d32' if reflineage.startswith(curlineage) else '#f44336'
			opacity = sum(c == '\t' for c in curlineage) / 60
			genestart = 3 * start + offsets[frame] if forward[frame] else width - 3 * start + offsets[frame] - 9*3 - 3
			yield Marker(genestart, genestart + 3, frame, color=color, opacity=opacity)
			start += 1


def parse_fgs(width, reflineage, fgs):
	for frame in range(6):
		yield Strand(0, width, frame)
	for line in fgs.split('\n'):
		if line.startswith('>'):
			*_, start, end, strand = line.strip().split('_')
			start, end, strand = int(start) - 1, int(end), strand == '+'
			frame = toframe(strand, start, end - 1, width)
			yield Marker(start, end, frame, color='#1565c0')
			offset = 0
		else:
			curlineage = strip_lineage(line)
			color = '#2e7d32' if reflineage.startswith(curlineage) else '#f44336'
			opacity = sum(c == '\t' for c in curlineage) / 60
			genestart = start + offset if strand else end - offset - 9*3 - 5
			yield Marker(genestart, genestart + 3, frame + 0.5, color=color, opacity=opacity)
			offset += 3


def parse_genes(start, width, genes):
	for frame in range(6):
		yield Strand(0, width, frame)
	for gene in genes:
		frame = toframe(gene['strand'] > 0, gene['start'] - start, gene['end'] - start, width)
		yield Marker(max(gene['start'] - start, 0),
		             min(gene['end'] - start, width),
		             frame,
		             color='#ff8f00')
		name = gene.get('transcript', gene['id'])
		yield Annotation(max(gene['start'] - start, 0),
		                 min(gene['end'] - start, width),
		                 name,
		                 frame,
		                 color='#ff8f00')


def toframe(f, s, e, width):
	if f:
		return s % 3
	else:
		return 3 + (width - e) % 3


def main(imgfile, taxon, species, chromosome, start, end):
	width = end - start
	read = fasta(taxon, species, chromosome, start, end)
	lineage = strip_lineage(get_lineage(taxon))
	genes = fetch_genes(taxon, species, chromosome, start, end)
	for gene in genes:
		gene['transcript'] = fetch_transcript(gene['id'])
	gene_markers = translate(2, parse_genes(start, width, genes))
	fgs_markers = translate(11, parse_fgs(width, lineage, run_fgs(read)))
	fgsrs_markers = translate(20, parse_fgs(width, lineage, run_fgsrs(read)))
	ft6_markers = translate(29, parse_6ft(width, lineage, run_6ft(read)))

	margin = 20
	height_per_frame = 10
	frames = 36
	targetwidth = 700
	d = draw.Drawing(targetwidth + 2 * margin, margin + frames * height_per_frame, origin=(-margin, -margin))
	for element in itertools.chain(gene_markers, ft6_markers, fgs_markers, fgsrs_markers):
		element.draw(d, targetwidth / width, margin, height_per_frame, frames)

	def title(s, h):
		d.append(draw.Text(s, 14, 0, (frames - h) * height_per_frame, alignment_baseline='middle'))
	title('RefSeq', 1.5)
	title('FGS++', 10.5)
	title('FGSrs', 19.5)
	title('six-frame translation', 28.5)

	d.saveSvg(imgfile)


A0A009H596 = ('image.png', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.17_1', 53253, 55397)
interesting = ('image.svg', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.8_1', 38308, 40888)
other = ('image.png', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.8_1', 23000, 26000)
chosen = ('final-raw.svg', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.8_1', 37700, 39530)
experiment_fgs = ('fgsfgs.svg', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.8_1', 37700, 39530)
experiment_rs = ('fgsrs.svg', 470, 'Acinetobacter_baumannii_118362_gca_000580515', 'ab118362.contig.8_1', 37700, 39530)
