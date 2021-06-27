---
title: Assembly of long, error-pront reads using repeat graphs
author: Mikhail Kolmogorov, Jeffrey Yuan, Yu Lin, and Pavel A. Pevzner
date: 05.07.2021
titlepage-color: "3C9F53"
header-includes:
  - \usepackage{fontspec}
mainfont: "Noto Sans"
---

# Genome assembly in general

>- reconstruct target sequence from the reads

>- different graph structures (De-Bruijn, Overlap-layout, String)

>- repeats $\rightarrow$ assembly fragmentation

>- error rate long read <-> short read

>- Flye should resolve these repeats correctly

# Disjointigs

>- most assemblers spent much time on correct contig assembly

>- Flye uses a different approach:
	+ we don't care (at least at the initial stage)
	+ correct assembly graph 
>- generate paths from overlapping reads without checking for correct assembly -> disjointigs

![](presentation/images/orly-owl.jpg){ width=30% }

<!--
![](presentation/images/repeat_graph_1.png){ width=60% }
-->


# Disjointigs

- current assemblers use much time on correct contig assembly

- Flye uses a different approach:

- generate paths from overlapping reads without checking for correct assembly -> disjointigs

![](presentation/images/repeat_graph_2.png){ width=60% }

# Disjointigs

- current assemblers use much time on correct contig assembly

- Flye uses a different approach:

- generate paths from overlapping reads without checking for correct assembly -> disjointigs

![](presentation/images/repeat_graph_3.png){ width=100% }


# Repeat graph creation

![](presentation/images/genome.png){ width=100% }

# Repeat graph creation

![](presentation/images/genome_and_reads.png){ width=100% }

# Repeat graph creation

![](presentation/images/disjointigs.png){ width=100% }

# Repeat graph creation

![](presentation/images/dot_plot.png){ width=60% }

# Repeat graph creation

![](presentation/images/plot_to_repeat_graph.png){ width=100% }

# Results

![](presentation/images/results_HUMAN.png){ width=100% }

# References

# Appendix

# Dot plot creation

![](presentation/images/dot_plot_creation.png)

# Repeat graphs

>- generalization of de bruijn graphs

>- structure

>- creation
    >- from disjointigs = random walk of reads on the repeat graph 
    >- means the repeat graph hasn't to be known

# Difference repeat graph de Bruijn graph

>- A-Bruijn graph (alignments) generalizes the de Bruijn graph

>- We thus argue that the time has come to explain that the breakpoint graphs and the de Bruijn graphs are two identical data structures (if one ignores a cosmetic difference between them) as they both represent specific instances of a general notion of the A-Bruijn graph introduced in [13]. The A-Bruijn graphs are based on representing genomes as sets of labeled paths and further gluing identically labeled edges (breakpoint graphs) or vertices (de Bruijn graphs) in the resulting paths.

>- de Bruijn graphs need correct bases

>- otherwise tangled graph

# Segmental duplications

![](presentation/images/SDs.png)

>- Segmental duplications are duplicated blocks of genomic DNA typically ranging in size from 1-200 kb (IHGSC 2001)
>- They often contain sequence features such as high-copy repeats and gene sequences with intron-exon structure. 


# Contigity improvement

![](presentation/images/contigity_improvement.png)

- colors are contigs

- color changes -> fragmented

<!--
From: 
https://www.youtube.com/watch?v=z6elrX-ZzW8&t=636s
(Youtube nanopore talk)
-->

# Repeat graph creation

![](presentation/images/dot_plot_to_repeat1.png)

# Repeat graph creation

![](presentation/images/dot_plot_to_repeat2.png)

# Repeat graph creation

![](presentation/images/dot_plot_to_repeat3.png)

# Repeat graph creation

![](presentation/images/dot_plot_to_repeat4.png)

# Repeat resolution

