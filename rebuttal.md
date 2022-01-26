---
papersize: A4
geometry:
- margin=1.0in
fontsize: 12pt
mainfont: Nimbus Sans L
...

# Rebuttal

## Carolien De Tender

> First, the first chapter is a bit limited in information concerning
> other methods. I would advise the doctoral candidate to include
> information on the current methods available on metagenomics analyses
> (how they work, specifications, etc.) so that the comparison which is
> given in chapter 2 is easier to made. The same goes for the introduction
> of some terms like EC number, GO terms, Interpro. These are many times
> recurring in the thesis, but have not been explained (also what the
> difference is between these terms). I know the doctoral candidate has
> not focused yet on functional data, but as he mentions it multiple
> times, an explanation of these terms should be added.

<!-- TODO -->

> Second, you will see that there are several questions I asked myself
> while reading chapter 2, which are resolved when I got to chapter 4. I
> think it would be good if this comes later in another chapter, you
> should refer to this chapter, or move the information.

<!-- TODO -->

### Summary

>  1. In the summary, you first describe the methods metagenomics,
>     -transcriptomics, and -proteomics. In the following paragraph you
>     start with the word shotgun metagenomics. What is the difference
>     between metagenomics and shotgun metagenomics? Is it the same term
>     or why do you specify the shotgun?

<!-- TODO -->

>  2. What do you specifically mean with the following sentence: "Often
>     the reads are too short to identify a specific organism, because
>     they occur in a number of organisms?" Are the reads too short to
>     allocate them to an organism, or are the reads not specific enough
>     to assign them to an organism?

<!-- TODO -->

>  3. Explain the sentence: "The pipeline does offer interesting avenues
>     towards functional analysis (what organisms are doing in the
>     sample) and metatranscriptomics (analyzing RNA reads instead of
>     DNA reads)." In what way is metatranscriptomics not a functional
>     analysis of the sample? Do you refer to proteins here?

<!-- TODO -->

>  4. The sentence: "However, the existing implementations proved to
>     be insufficiently fast." Sounds a bit strange. Perhaps change to
>     insufficient in terms of speed.

Suggestion applied.

>  5. In general I would change the start of the summary. Now, it seems
>     that you have developed a platform to look into both metagenomics,
>     metagenomics and metaproteomics data. I think you should state
>     that you work further on an existing platform in the beginning
>     (Unipept) and adapted this for the analysis for metagenomics
>     data. Then you can elaborate further on FragGenescan+ and the
>     other methods, as these are part of the development on the
>     tool. I also don't see the point to start with the definition
>     of metagenomics/transcriptomics/proteomics, as for this thesis
>     proposal, you are only working with the first one. I think this is
>     good for an introductory section though.

<!-- TODO -->

### Primer on metagenomics

>  6. I must say, it is a rather interesting start of the thesis you
>     propose here, which I am not used of, but it reads easily. On the
>     end of page 11, you state that kingdoms are divided in classes
>     and orders and so forth. I would like that you also mention the
>     classification into families, genera up to species level, as this
>     is important later on to the depth on which your method could
>     distinguish the organisms.

All "main" named ranks were added, with minor changes to the sentence.

>  7. Small remark: I think on page 14, third paragraph, you forgot to
>     refer to Figure 1.3, illustrating the RNA transcription. The same
>     goes for Figure 1.4. I suppose the reference to this figure needs
>     to be present in paragraph 4 of the same page on translation.

Added references to the figures.

>  8. Page 14, paragraph 4. Can you add the nucleotide formation of a
>     start codon and stop codon between brackets here?

Done.

>  9. The sentence: "The constructed protein performs certain functions
>     before it degrades", I would add this in the paragraph above, so
>     you can start this paragraph with the Uniprot databased.

Done.

> 10. On page 15 you mention EC numbers, GO terms and (you wrote "en" in
>     Dutch) InterPro entries. What are these, why are they important to
>     mention? Can you elaborate a bit more on this?

I added a paragraph with an example protein and the cross-references,
which should clarify what these databases are.

> 11. On page 17 on studying the biopolymers, you describe the second
>     step in the process of studying the genomic DNA: the assembly of
>     the genome. Do you think this is always necessary when studying
>     the genome of an organism or when you want to look to taxonomy or
>     specific functions?

<!-- TODO Carolien 2 -->

> 12. You state that the study of a transcriptome provides similar
>     insights of that of a proteomics study. Why would you specifically
>     choose for a transcriptome or a proteome study then? Are there
>     computational limitations for either of the two? For example, the
>     number of metaproteomics studies is much more limited to those of
>     metatranscriptomics studies. What could be the reason behind this?

<!-- TODO Carolien 3 -->

> 13. During your first chapter, you always give examples of
>     higher-order organisms (e.g. fish). From point 1.4 onwards you
>     start talking about microorganisms and the extraction of the DNA
>     from those organisms (e.g. 16S rRNA genes). You already mentioned
>     these organisms in section 1.1. This goes quite drastically, and
>     an intermediate part on why you focus on bacteria/microorganisms
>     would be nice here.

<!-- TODO Carolien 4 because there are easier methods to study larger organisms? -->

> 14. In this first chapter, I am really missing a part where you
>     explain how metagenomics data is analyzed today/which tools are
>     used nowadays. I think this is important as you need to make
>     the comparison later on with your method and where you perform
>     better/worse + what differentiates your method from the current
>     existing ones. You mention this very briefly at the start of the
>     second chapter, but I think this should be described in more
>     detail.

<!-- TODO -->

### UMGAP

> 15. Page 26, you mention that metagenomics can be used to bypass the
>     cultivation step to enable genomic analysis. Maybe you should
>     define for which organisms this is the case, as with metagenomics
>     (as you mentioned), you will not only find microorganisms, but
>     also eukaryotes, such as plant or even human DNA. It can thus
>     also be used to track plant DNA in soils for example. With the
>     introduction of the first chapter I read, this is not completely
>     clear.

<!-- TODO Carolien 5 -->

> 16. For UMGAP, you know focused on the taxonomical identification;
>     However, as you translate your DNA into protein sequences and
>     map these to UniProtKB, wouldn't it be possible to retrieve the
>     functions of these proteins as well? Or is preprocessing/another
>     pipeline necessary to do so?

It is, but it's hard to link a peptide (kmer of peptide) to a single
functional identifier. EC numbers would be doable, because they're
also nodes in a tree, but the tree is not deep enough for meaningful
aggregation. GO terms and interpro represent more complex structures.
Mapping to those would require different aggregation techniques or other
mapping structures.

> 17. Page 31: you mention that false negatives and false positives
>     might occur during gene prediction. Do you have an idea how often
>     this occurs? For example, did you worked with a benchmarked
>     dataset or a mock community to verify this?

<!-- TODO Carolien 6 -->

> 18. Page 37: you indicate that UMGAP can skip these short peptide
>     fragments. As an example, you give a length of 6 amino acids. Is
>     this length fixed within the UMGAP pipeline? Can it be changed by
>     the user? For the last scenario, do you make any recommendations
>     what cut-off users should at least use?

<!-- Carolien 18 -->

This can be changed by the user, if not using one of the (later
introduced) preconfigured pipelines. I would advise using 5 as cut-off.

> 19. Overall question methodology: in the description of the pipeline,
>     I can't find if you (1) check the quality of the reads upfront
>     (or do the users need to do that in advance by themselves? If
>     this is the case, do you have any recommendations?); (2) filter
>     and trim the reads. Do you remove reads that are very small (e.g.
>     less than 20-50 bp). Do you trim the reads once the quality drops
>     below a certain phred score (e.g. 20). Is this something that is
>     implemented in the pipeline, or should the user do this upfront
>     as well? And if this is the case, do you recommend a program for
>     this?

The pipeline has neither of these steps explicitly. Removing or trimming
reads of low quality would be an interesting step to add (and trivial to
add). Removing small reads is not required: these would not slow down
the processing by much and likely give no output. Overall, it may be
important to keep (dummy-replacements of) these reads in the pipeline,
because removing them would skew the reported negatives at the end of
the pipeline.

> 20. General comment result section: did you also benchmark your method
>     by looking into mock communities (a predefined sample for which
>     you know which organisms are present).

No, because those would be harder to measure the results.

> 21. Page 41. You mentioned here that you used some smaller datasets
>     to measure and analyze the performance metrics. Please indicate
>     here which datasets you used and if these are freely available.
>     I suppose it are these of Wood and Salzberg you mention later. I
>     would already indicate these here.

Suggestion applied.

> 22. Page 43: You indicate the higher runtime and memory footprint of
>     the 9-mer configurations. How much larger is this?

3 times the execution time and 10 times the memory required. Inserted
into the text.

> 23. Page 46: It can be that I just read over it in the text, but for
>     the two tryptic configurations you selected, I understand each
>     decision except the choice of MRTL read profiling method. Why did
>     you specifically choose this one? Same question for page 49: why
>     did you select hybrid f and MRTL as the preferred methods for the
>     9-mer configurations?

<!-- Carolien 23 -->

For tryptic peptides, you did not read over it. Because there is
rarely more than a single tryptic peptide, the aggregation method does
not matter much. MTRL was chosen because it is marginally faster to
calculate and would further reduce the sensitivity least.

For the 9-mer selection, I picked the outmost variants based on Figures
2.16 and 2.18.

> 24. You compare the UMGAP methods with those of Kraken, CLARK and
>     Kaiju. Is their data processing very different from those of UMGAP
>     and if so, on which parts? It would be nice that you introduce
>     these as well in the first chapter to know the differences between
>     your method and the others.

<!-- TODO -->

> 25. UMGAP tryptic precision has a very high precision, but a low
>     sensitivity, even almost 0%. Does this mean that you have a very
>     high abundance of false negatives in your data? (sensitivity=
>     TP/(TP+FN))

Yes, the tryptic precision pipeline classifies most reads as root
because it cannot find any sure evidence in them.

> 26. Page 57-58: I suppose for this in depth analysis, you need to
>     refer to appendix A?

Reference added.

> 27. Page 60: when you show here that if the divergence increases,
>     it becomes harder to identify the reads on genus/species level,
>     would this imply for example that it will also be harder to
>     differentiate/identify more complex species (with more complex
>     genomes) such as plants or nematodes?

<!-- Carolien 27 -->

Not necessarily; the divergence here is divergence from the reference
genome by introducing errors in the reads. As long as the species do not
diverge too much from any species in Uniprot, detection is possible.

> 28. Page 60: you say you can also find viruses. I suppose it are only
>     the DNA viruses you will find here, as you are not looking into RNA.

Yes, clarified in the text.

> 29. The runtimes you indicate for UMGAP, are these based on running
>     the program locally on the computer?

No, there were executed on the rather powerful server that was mentioned
way back at the start of the results section.

> 30. At the end, a frequency table is created (page 77). For all steps
>     above, you speak about one sample you are looking at. However,
>     in most cases metagenomics samples are also used for comparison
>     between each other (e.g. because a treatment was added). Is there
>     a command in the UMGAP pipeline introduced as well that makes it
>     possible to merge several frequency tables and make it possible to
>     compare samples for further statistical analyses?

The command which produces the frequency table allows for multiple
samples. As such it should allow to incorporate multiple samples into
a single CSV file. However, UMGAP does not provide further statistical
analysis on these frequency tables.

### FragGeneScanRs

HERE

> 31. Page 88: change pair-end into paired end (normally used
> nomenclature)

TODO

> 32. You introduce here FraggenescanR. It is not clear for me if this
> is the same as FGS++ or not. If it is not the same, in which way do
> the two differ and which would be best to use in UMGAP (now you (have)
> used FGS++ if I am correct).

TODO

> 33. For this specific part, it would be nice to include a conclusion
> section on the use of FGSr.

TODO

### Putting it all in action

TODO

> 34. I am not sure if the title of this chapter covers the load of what
> is presented. Based on the title, I would have expected that you use
> some real datasets to test the methods you developed and described in
> the previous two chapters. Especially part 4.3 seems rather strange to
> include it in this chapter and maybe should be a chapter on its own?
> I would prefer you change the title so it covers the complete load of
> this chapter.

TODO

> 35. Based on the scheme you represent here, I think in the first
> chapter you really should add information on the different databases
> you use and describe, with especially Uniprot, but alo the explanation
> on EC, interpro, etc.

TODO

> 36. First sentence under 4.1.2: remove the "a" before "three tables"

TODO

> 37. You give information on how to run UMGAP for datasets, but what
> would you advise: to use the desktop version or the web-based version?

TODO

> 38. In the taxa2tree command, can you also add the frequency on the
> edges or nodes of the figure (e.g. figure 4.3)?

TODO

> 39. Page 114: I am not sure if I understand the following sentence:
> "However, since these are transcriptomics samples, instead of joining
> all reads after identification, the umgap bestof tool selects the
> single best frame out of the 6 translated and identified frames.

TODO

> 40. Page 115: it is a bit confusing that you first state that you will
> illustrate two examples here, and a bit further you describe three
> projects of which FGSr was one of them. I think it would be better if
> you phrase thepart on FGS in the paragraph above, where you introduce
> the usefulness of this project-driven work, as this was part of your
> PhD. And then you can elaborate more on two external projects.

TODO

> 41. For SPeDe, you said that you were able (together with the student)
> to reduce the analysing time to 2 hours for a realistic dataset.
> Before the improvements, what was the time of analysis?

TODO

> 42. 4.3.2: what is a haplotype? As you introduce this here, I think
> you should include some definitions as well (for example, also explain
> what a SNP is).

TODO

### Conclusions and future work

> 43. Page 123: you speak of a bias by peptides that occur in multiple
> organisms instead of a single organism. In what way do you think the
> use of Uniprot left a bias in the pipeline? To be more specific, is
> there a bias towards certain type of organisms? (e.g. the higher
> abundance of bacteria compared to eukaryotes in the database).

TODO

> 44. For the functional annotation, couldn't you refer for this to
> other methods (e.g. MG-Rast). You can still comment on this if it is a
> good strategy or not though.

TODO

> 45. In this part, shouldn't you include as well the transition
> from metagenomics to metatranscriptomics? You mention it
> briefly (although some mistakes are present in here as well:
> sometimes you write metaproteomics in this paragraph instead of
> metatranscriptomics). It would be nice that you elucidate a bit more
> on this and what the differences may be (computationally) for a
> metatranscriptomics/metagenomics dataset

TODO

## Wesley De Neve

>  1. [General] The dissertation still contains a number of typos.
>     A careful, final proofread may help in minimizing these
>     imperfections.

TODO

>  2. [General] In the different conclusions sections (e.g., Section
>     2.4), it may be good to better emphasize the robustness
>     (generalization) aspect of the UMGAP pipeline, and where
>     robustness is primarily treated as a qualitative feature of the
>     proposed pipeline (with the exception of the experiment with
>     shuffled genomes).

TODO

>  3. [Chapter 1] It would be good to add a figure that shows the
>     hierarchy of the different taxonomic ranks often used in the
>     dissertation.

TODO

>  4. [Chapter 1] It would be good to add a figure that visualizes the
>     relationship between UniProtKB, NCBI, EC numbers, GO terms, and
>     InterPro entries.

TODO

>  5. [Chapter 1, Fig. 1.5] It would be good to add an arrow that
>     denotes increasing rank.

TODO

>  6. [Chapter 1] It may be good to split up Section 1.6 into (1) a
>     section that lists the different contributions and (2) a section
>     that describes the overall organization of the dissertation.

TODO

>  7. [Chapter 2] Given the importance and the size of this chapter, it
>     may be of interest to better clarify the overall structure of this
>     chapter, so to better help the reader to navigate this chapter.
>     This could for instance be done in the introductory section of
>     Chapter 2 (this remark could also be applied to Chapter 3 and
>     Chapter 4).
>
>     Specifically, it would be good to explicitly mention that the
>     chapter consists of three major parts: methods, experiments, and
>     tools. Furthermore, in this context, it would also be good to
>     explicitly mention that the experiments section also consists of
>     three major parts: pipeline identification, benchmarking, and
>     in-depth analysis.

TODO

>  8. [Chapter 2] When mentioning the total number of investigated UMGAP
>     configurations for the first time (i.e., 3900), it would be good
>     to immediately point out that these configurations can be split
>     into 2700 tryptic configurations and 1200 9-mer configurations.

TODO

>  9. [Chapter 2] It would be good to add a note to explain what is
>     meant with 'shuffled genomes'.

TODO

> 10. [Chapter 2] The definition of Operational Taxonomic Unit (OTU) is
>     not clear. Providing an example may be helpful.

TODO

> 11. [Chapter 2] Part of Section 2.5.9, which discusses per read taxon
>     aggregation, could be merged with Section 2.2.5, or it would be
>     good to have Section 2.2.5 at least refer to Section 2.5.9.

TODO

> 12. [Chapter 3] It may be good to mention a number of pipelines,
>     frameworks, and/or projects that are making use of FragGeneScan.

TODO

> 13. [Chapter 3] Throughout the dissertation, it would be good to keep
>     the notation for FGS, FGS+, FGS++, and FGSrs consistent. For
>     example, in Section 3.4, a sudden switch from short-form notation
>     to long-form notation can be noticed for the different versions of
>     FragGeneScan.

TODO

> 14. [Chapter 3] When presenting averages, it would be good to present
>     standard deviations as well, either visually (through error bars)
>     or textually (by mentioning the standard deviation in the caption
>     of a plot).

TODO

> 15. [Chapter 4] Fig. 4.1 currently gives an overwhelming
>     impression. It may therefore be of interest to work with a
>     coarse-to-fine-grained approach, first presenting a high-level
>     visualization and then a more detailed visualization.

TODO

> 16. [Chapter 4] From the current discussion, the link between the
>     newly introduced tools and the use of a relational database was
>     not clear to me. I assume that the relational database sits at the
>     application layer.
>
>     In this context, I also would like to point out that the following
>     statement is not completely clear to me:
>
>     "While querying a relational database is fast enough for a
>     metaproteomics tool, it does not suffice for a metagenomics tool,
>     which is expected to handle much larger amounts of data."

TODO

> 17. [Chapter 4] Similar to Chapter 2 and Chapter 3, it may be good
>     to add a footnote to the beginning of Chapter 4 that efforts
>     described in this chapter contributed to (at least) two papers (as
>     implicitly mentioned in Section 4.3).

TODO

> 18. [Appendix A] I am not aware of a reference to this appendix from
>     within the main text of the dissertation. I believe it would be
>     good to incorporate such a reference (from within Chapter 2).

TODO

## Aurélien Carlier

> The dissertation entitled « The Unipept metagenomics analysis
> pipeline” by Felix Van der Jeugt is a well written manuscript,
> describing interesting work that undoubtedly advances the field
> of metagenomics analysis. The dissertation is focused on the
> development and applications of a suite of tools (notably UMGAP and
> FragGeneScanR) dedicated to metagenomics (and metatranscriptomics)
> analyses. In particular, UMGAP leverages taxonomic information
> contained in the Uniprot database and taxon schemes from NCBI to
> rapidly assign consensus taxonomic information to short sequencing
> reads. The algorithms are in general well described and easy to read
> even for a lay person, and the results of benchmarking and case
> studies clearly laid out.

> The data presented are certainly of sufficient quality to allow
> the candidate to defend his PhD. In addition, the candidate has
> contributed to several published articles as co-authors and has 2
> manuscripts submitted to journals as a first author.

### General comments

> My only general comment pertaining to the dissertation is that
> there is sometimes some confusion throughout between protein (i.e.
> the biological entity) & amino acid sequence; DNA and nucleotide
> sequence; organism and genome, etc… This can be quite confusing to
> read for a molecular biologist. Make sure to clearly distinguish
> biological entities from their representations. I tried to flag as
> many instances of such conflation the annotated PDF of the thesis,
> but I advise careful proofreading.

### Specific comments:

> There is a number of typos and grammatical errors. I will send an
> annotated PDF of the dissertation to the candidate after the closed
> defense.

#### Introduction:

> - Introduce some taxonomic and phylogenetic concepts (tree crown and
>   clade, etc…). Perhaps in the form of a box with some definitions.

TODO

> - A (brief) discussion about introns/exons is missing. The tools
>   described were clearly created with bacteria in mind, but they
>   should also be applicable to archaea and eukaryotes.

TODO

> - Maybe a sentence or two about post-translational modifications and
>   how they are expected to impact proteomics data analysis.

TODO

> - expand definitions of GO, InterPro, EC

TODO

> - P15: Misleading statement: “[…] some bacteria blend the
>   transcription and translation into a single step”. Although
>   transcription and translation are coupled in prokaryotes, this is
>   still a 2-step process.

TODO

> - P19: Add a little bit more explanation (one or two sentences) on
>   how contigs are profiled to be grouped into bins

TODO

> - Since much of this thesis relies on gene finding, or at least
>   matching DNA to AA sequences databases. It would be good to have
>   a brief overview of gene finding, and the various limitations
>   of applying gene finding software to metagenomics: higher error
>   profiles, difficulty in obtaining representative training datasets,
>   choice of codon table, problems with sometimes unreliable
>   annotations (especially true for automatically generated
>   annotations). Especially, I would have liked to see in Introduction
>   an overview of FragGeneScan, which is introduced in Chapter 2
>   without much explanation.

TODO

#### Chapter 2

> - Is FragGeneScan codon usage-aware? How are the gene models
>   created/updated?

TODO

> - P32, tryptic peptides: what do you mean by “it is a random
>   fragmentation strategy”? This seems counterintuitive since peptides
>   are digested in silico in a systematic manner.

TODO

> - P35. Peptide Filtering. The first sentence of this paragraph should
>   be rephrased. Protein fragmentation may yield false positives:
>   peptides that do not occur in proteins encoded in the read. First,
>   I’m assuming that this is referring to spurious AA sequences that
>   are translated from non-coding regions in a read, but the phrasing
>   is ambiguous. Second: do not confuse protein and amino-acid
>   sequence, and do not confuse read and gene (a read does not encode
>   anything).

TODO

> - P42. Were the simulated reads generated from coding regions only?

TODO

> - P42. Do you expect true negatives to occur in real metagenome
>   datasets? Would this depend on the sequencing technology used
>   (error profiles)?

TODO

> - Fig. 2.17 & 2.19: what was the read profiling method used to
>   generate these data?

TODO

> - The parameters for max precision are set according to results
>   presented on Fig 2.16, but it’s not obvious to me why hybrid
>   profiling is chosen over LCA*. Could you explain?

TODO

> - P52. What does snaptaxon do? This comes later in the chapter, but a
>   brief explanation would be useful here, or at least a reference to
>   the paragraph where it is described.

TODO

> - P60. The discussion on the degradation of the signal with increased
>   divergence of Leptospira reads is very interesting. Do you know by
>   how much the different simulated genomes diverged (%ANI)?

TODO

> - P61. Are other input formats supported (e.g. BAM, SAM) ?

TODO

> - Remark: A major selling point of UMGAP might be the taxonomic
>   breadth of the database (including eukaryotes). That may make the
>   tool ideally suited for host-associated microbiomes, where tools
>   like e.g. Kraken or to a smaller extent Kaiju become unwieldy.

TODO

> - P60. Discussion. You propose to further explore functional
>   characterization of metagenomes using UMGAP or similar methods. This
>   would be extremely interesting for biologists. What would the main
>   limitations be? Do you think UMGAP would perform better or worse
>   than tools like HUMAnN2 (with DIAMOND under the hood, if I remember
>   correctly)?

TODO

#### Chapter 3

> - This chapter describes an improved implementation of a piece
>   of software, FragGeneScan, used to predict coding sequences
>   in short, error-prone reads. The technical details in this
>   chapter are in general way over my head, and I do not have any
>   particular comments. From the data presented, FragGeneScanR
>   looks like convincing improvement over the older software. The
>   observation that the behavior of FGS++ deviates from FGS in terms
>   of sensitivity and precision is certainly of concern. Is this
>   specific to the latest version of FGS++ ?

TODO

> - How does FragGeneScan deal with the problem of identifying the
>   correct 5’ end (start codon) of a gene?

TODO

#### Chapter 4

> - P98. What are “unwanted” taxa?

TODO

> - P100. What are “equalized” peptides?

TODO

> - P102. Would there be anything to gain by filtering out low
>   complexity sequences in building the kmer to taxon table?

TODO

> - P115. “This sets the stage for the optional filtering of the taxa
>   based on their location”. I’m assuming you mean the location of
>   taxonomic matches within the read. Is this correct? Cold you
>   rephrase to make it less ambiguous?

TODO

> - P116. “This lists of taxa need to be aggregated…”. I find this
>   sentence unclear. It says all consecutive reads with the same
>   header are gathered… But these should all be putative genes from
>   a single read, or am I missing something? What do you mean by
>   “ends” in the sentence “translate must keep together the ends and
>   translations of a read”?

TODO

> - P120. Similar ambiguity in the sentence “instead of joining all the
>   reads after identification”

TODO

> - P123. Could you briefly explain what the HiPlex and GBS datasets
> - are?

TODO

#### Chapter 5

> - P121. Adaptive kmer length. You argue that 10-mers should be
>   investigated because they might offer more specific matches.
>   It’s difficult to compare this directly, but Fig 2.11 shows only
>   marginal improvement of tryptic peptides > 10 aa over 9 aa. Do you
>   expect 10-mers to behave differently? How would increasing the
>   length of the kmer from 9 to 10 affect memory usage? Are there any
>   possible strategies that could be applied to reduce the size of the
>   index?

TODO

> - P123. I would add that GO-terms are near useless in metagenome
>   analyses, but that’s just my opinion...

TODO
