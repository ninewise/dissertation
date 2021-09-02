### Requesting taxonomy information

While watching results or intermediate output from the pipeline, taxon
IDs aren't easy to interpret and remember. The `umgap taxonomy` command
takes one or more NCBI taxon IDs as input, searches for them in the
taxonomy and outputs more information about them in a TSV format.

#### Usage

The input is given on standard input and may be any sequence of FASTA
headers and/or lines containing a single NCBI taxon ID. A TSV header is
printed to standard output. The FASTA headers (any line starting with
a `>`) are just copied over. Each of the taxon IDs on the other lines
is looked up in a taxonomy, and the ID, name and rank of the taxon are
written out separated by tabs.

A taxonomy file must be passed as argument.

```shell
$ cat input.fa
2026807
888268
186802
1598
1883
$ umgap taxonomy taxons.tsv < input.fa
taxon_id	taxon_name	taxon_rank
2026807	Zetaproteobacteria bacterium	species
888268	Dichanthelium oligosanthes	species
186802	Clostridiales	order
1598	Lactobacillus reuteri	species
1883	Streptomyces	genus
```

The `-H` flag can be used to suppress the TSV header, for instance when
dealing with FASTA input.

```shell
$ cat input2.fa
>header1
2026807
888268
186802
1598
1883
$ umgap taxonomy -H taxons.tsv < input2.fa
>header1
2026807	Zetaproteobacteria bacterium	species
888268	Dichanthelium oligosanthes	species
186802	Clostridiales	order
1598	Lactobacillus reuteri	species
1883	Streptomyces	genus
```

The `-a` flag can be used to request a complete ranked lineage.

```shell
$ cat input3.fa
888268
$ umgap taxonomy -a taxons.tsv < input3.fa
taxon_id	taxon_name	taxon_rank	superkingdom_id	superkingdom_name	kingdom_id	kingdom_name	subkingdom_id	subkingdom_name	superphylum_id	superphylum_name	phylum_id	phylum_name	subphylum_id	subphylum_name	superclass_id	superclass_name	class_id	class_name	subclass_id	subclass_name	infraclass_id	infraclass_name	superorder_id	superorder_name	order_id	order_name	suborder_id	suborder_name	infraorder_id	infraorder_name	parvorder_id	parvorder_name	superfamily_id	superfamily_name	family_id	family_name	subfamily_id	subfamily_name	tribe_id	tribe_name	subtribe_id	subtribe_name	genus_id	genus_name	subgenus_id	subgenus_name	species_group_id	species_group_name	species_subgroup_id	species_subgroup_name	species_id	species_name	subspecies_id	subspecies_name	varietas_id	varietas_name	forma_id	forma_name
888268	Dichanthelium oligosanthes	species	2759	Eukaryota	33090	Viridiplantae					35493	Streptophyta	131221	Streptophytina			3398	Magnoliopsida	1437197	Petrosaviidae					38820	Poales									4479	Poaceae	147369	Panicoideae	147428	Paniceae	1648011	Dichantheliinae	161620	Dichanthelium							888268	Dichanthelium oligosanthes						
```

#### Options & flags

`-a / --all`
  ~ Show the full lineage of a taxon

`-h / --help`
  ~ Prints help information

`-H / --no-header`
  ~ Do not output the TSV header

`-V / --version`
  ~ Prints version information
