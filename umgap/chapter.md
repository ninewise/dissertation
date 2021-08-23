# The Unipept Metagenomics Analysis Pipeline

_Dit hoofdstuk omschrijft eerst de structuur en samenstelling van
de *pipeline*. De verschillende commando's en hun interface worden
overlopen. Daarna volgt een bespreking van het resultaat, zoals
gepubliceerd._

## Opzet en structuur

De analyse van *Shotgun Metagenomics data* kan op twee wijzen
opgesplitst worden. Enerzijds is de data traditioneel opgeslagen in
FASTA- of FASTQ-bestanden. Beide vormen lange sequenties van *reads*.
Elk van deze reads kan individueel verwerkt worden. Slechts na de
verwerking van de individuele reads komen ze met elkaar in aanraking,
tijdens de aggregatie van de hele dataset, bijvoorbeeld om een
frequentietabel op te stellen. Dit suggereert een opsplitsing per
*read*. Anderzijds gebeurt ook de verwerking in een aantal logische
stappen, dewelke elke *read* zal doormaken.

De eerste manier van opsplitsing heeft als groot voordeel de
mogelijkheid tot parallellisatie. Op triviale wijze kan elke *read* in
een aparte *thread* verwerkt worden. Op die manier kan de volledige
kracht van de uitvoerende machine gebruikt worden.

De tweede manier van opsplitsing kan echter de verschillende stappen
apart beter optimaliseren. Elke stap kan specialiseren in zijn taak
en krijgt de mogelijkheid om een gemeenschappelijke initialisatie te
delen over alle *reads* die hij zal verwerken. Daarbij kunnen alle
stappen gelijktijdig in eigen process uitgevoerd worden, waarbij *reads*
doorgegeven worden aan het volgende process in de verwerking zodra dit
process zijn taak volbracht heeft. Tenslotte biedt zo'n opsplitsing de
mogelijkheid om de verschillende stappen in te wisselen om delen van de
verwerking te wijzigen.

De UMGAP koos voor de tweede manier van opsplitsen. Elke logische stap
werd geprogrammeerd als een apart subcommando van de `umgap` executable,
op basis van een gedeelde broncode. De processen worden samengebracht
in één ketting van commando's met behulp van UNIX pipes, die met elkaar
communiceren via standaard invoer en standaar uitvoer in FASTA-achtige
formaten.

## Componenten

_Overlopen van de componenten en hun interface. Samenhang moet ik hier
niet meer overlopen, die komt in de paper erna._

### [fastq2fasta](components/fastq2fasta.md){.include}

### [translate](components/translate.md){.include}

### [digestion](components/digestion.md){.include}

### [filter](components/filter.md){.include}

## [paper](paper.md){.include}
