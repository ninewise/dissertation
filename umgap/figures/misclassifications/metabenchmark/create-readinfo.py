#!/usr/bin/env python3

import re
import sys

def main(live_file, dead_file, *fqs):
	"""
	Given a live and dead mapping file (nucl_gb.accession2taxid and dead_nucl.accession2taxid on
	ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/), produce a mapping from the headers
	occurring in the other arguments to the taxon ids. Headers not found at the given level
	shall have taxon id 1 (root).
	"""
	# Read in the mapping table
	with open(live_file, 'r') as f:
		next(f) # skip header
		acc2taxid = { name: taxid for name, _, taxid, _ in (l.strip().split('\t') for l in f) }

	with open(dead_file, 'r') as f:
		next(f) # skip header
		dead_acc2taxid = { name: taxid for name, _, taxid, _ in (l.strip().split('\t') for l in f) }

	extract_accession = re.compile('^(tpg\|)?([A-Za-z0-9]*)')
	def organism_to_taxonid(organism):
		# First, take on the edge cases:
		# (Use the second Excel appendix of the Metabenchmark to get an idea of the data)
		# (1) Randomly shuffled records
		if 'random' in organism.lower(): return 0
		# (2) The records that were simulated with the Rose simulator.
		#     The paper mentions these can all be traced back to the same accession number (AE016823)
		if '_divergence_' in organism: return 267671
		# (3) This is the fun part: some records contain barely any information at all, except
		#     for sometimes a (shortened and unusable for search) organism name and possibly a
		#     chromosome number. This is where you'll need the appendix...
		if 'Arabidopsis' in organism: return 3702  # Arabidopsis thaliana: a thale cress
		if 'chr22-_Eukaryotes' in organism: return 9606  # Homo Sapiens
		if 'chr28-_Eukaryotes' in organism: return 9031  # Gallus gallus: a chicken
		if 'chr2-_Eukaryotes' in organism: return 28377
		    # Small caution here: we don't have an organism name, only that it
		    # should be a lizard. Putting the relevant sequences through BLAST
		    # gives us the "Anolis carolinensis", i.e. the Carolina anole.
		if 'Pan_troglo' in organism: return 9598  # Pan troglodytes: a chimpansee
		if ('JH584390' in organism) or ('JH584391' in organism): return 8478
		# Chrysemys picta bellii: a western painted turtle
		if 'Haliaeetus_leucocephalus' in organism: return 52644 # Haliaeetus Leucocephalus: a bald eagle
		# (4) Some records have accessions that belong to ENA instead of NCBI.
		#     Since they don't all map cleany to a single taxon ID, we need manual lookups again.
		if organism.startswith('ENA|'): return ENA_mapping[organism[4:12]]
		accession = extract_accession.search(organism).group(2)
		try:
			return acc2taxid[accession]
		except (KeyError) as e:
			return dead_acc2taxid[accession]

	print('name', 'taxon', 'count', sep='\t')
	organisms = dict()
	extract_organism = re.compile('@(.*)_\d+/\d\n')
	for fq in fqs:
		with open(fq, 'r') as f:
			for i, l in enumerate(f):
				if i % 4 == 0:
					organism = extract_organism.fullmatch(l).group(1)
					if organism not in organisms:
						organisms[organism] = [organism_to_taxonid(organism), 1]
					else:
						organisms[organism][1] += 1
	for organism, (tid, count) in organisms.items():
		print(organism, tid, count, sep='\t')


# The authors of the metabenchmark used from the European Neucleotide Archive as well. Since
# mapping to a proper taxon id isn't always possible (or it needs elaborate parsing, and internet
# access) we'll just hardcode them here.
ENA_mapping = {
    'AL450380': 272631, # Mycobacterium leprae TN
    'AL645882': 1902,   # Streptomyces coelicolor
    'CM000636': 1768,   # Mycobacterium kansasii
    'CM000789': 1773,   # Mycobacterium tuberculosis
    'BX548020': 84588,  # Synechococcus sp. WH 8102
    'CM000748': 527025, # Bacillus thuringiensis serovar thuringiensis
    'CM000833': 320371, # Burkholderia pseudomallei 1710a
    'CM000855': 683083, # Campylobacter jejuni subsp. jejuni 414
    'BX119912': 243090, # Rhodopirellula baltica SH 1
    'BX470248': 520,    # Bordetella pertussis
    'BX470250': 518,    # Bordetella bronchiseptica
    'BX571963': 258594, # Rhodopseudomonas palustris CGA009
    'BX842601': 50701,  # Bdellovibrio bacteriovorus HD100
    'CR354532': 74109,  # Photobacterium profundum
    'AJ235269': 272947, # Rickettsia prowazekii str. Madrid E
    'AL732656': 211110, # Streptococcus agalactiae NEM316
    'BX548020': 84588,  # Synechococcus sp. WH 8102
    'BX571656': 273121, # Wolinella succinogenes DSM 1740
    'CM000438': 271848, # Burkholderia thailandensis E264
    'CM000488': 535026, # Bacillus subtilis subsp. subtilis str. NCIB 3610
    'CM000657': 479833, # Clostridioides difficile QCD-97b34
    'CM000715': 526980, # Bacillus cereus ATCC 10876
    'CM000724': 526975, # Bacillus cereus BDRD-ST26
    'CM000731': 526984, # Bacillus cereus Rock3-29
    'CM000750': 527027, # Bacillus thuringiensis serovar pakistani str. T13001
    'CM000754': 527032, # Bacillus thuringiensis serovar andalousiensis BGSC 4AW1
    'CT009589': 1718,   # Corynebacterium glutamicum
}

if __name__ == '__main__':
    main(*sys.argv[1:])
