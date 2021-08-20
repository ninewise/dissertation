umgap printindex /data/felix/database/2020-04-tryptic.index \
	| pv -l -s 1209812069 \
	| sed 's/^/>/;s/\t/\n/' \
	| umgap taxonomy /data/felix/database/2020-04-taxons.tsv \
	| sed '/>/{N;s/\n/,/};s/>//;s/,.*,/,/' \
	| python count.py \
	| tee ranklengthcounts

# $ cat count.py
# import sys
# import collections
# 
# m = collections.defaultdict(int)
# 
# for line in sys.stdin:
# 	peptide, rank = line.strip().split(',')
# 	m[(len(peptide), rank)] += 1
# 
# print(dict(m))
