---
title: Assembly of long, error-pront reads using repeat graphs
author: Mikhail Kolmogorov, Jeffrey Yuan, Yu Lin, and Pavel A. Pevzner
date: 05.07.2021
---

# Long read assembly

>- error rate long read <-> short read

>- assembly fragmentation -> repeats

>- Flye shoult resolve these repeats correctly

# Disjointigs

>- current assemblers use much time on correct contig assembly

>- Flye uses a different approach:

>- generate paths from overlapping reads without checking for correct assembly -> disjointigs

>![](presentation/images/repeat_graph_1.png){ width=60% }

# Disjointigs

- current assemblers use much time on correct contig assembly

- Flye uses a different approach:

- generate paths from overlapping reads without checking for correct assembly -> disjointigs

![](presentation/images/repeat_graph_2.png){ width=60% }

# Disjointigs

- current assemblers use much time on correct contig assembly

- Flye uses a different approach:
    - generate paths from overlapping reads without checking for correct assembly -> disjointigs

![](presentation/images/repeat_graph_3.png){ width=60% }



# Long reads and de Bruijn graphs? 

>- de Bruijn graphs need correct bases

>- otherwise tangled graph

# Long reads and de Bruijn graphs? 

![](presentation/images/orly-owl.jpg){ width=50% }

# Repeat graphs

>- generalization of de bruijn graphs

>- structure

>- creation
    >- from disjointigs = random walk of reads on the repeat graph 
    >- means the repeat graph hasn't to be known

# Difference repeat graph de Bruijn graph

>- A-Bruijn graph (alignments) generalizes the de Bruijn graph

>- We thus argue that the time has come to explain that the breakpoint graphs and the de Bruijn graphs are two identical data structures (if one ignores a cosmetic difference between them) as they both represent specific instances of a general notion of the A-Bruijn graph introduced in [13]. The A-Bruijn graphs are based on representing genomes as sets of labeled paths and further gluing identically labeled edges (breakpoint graphs) or vertices (de Bruijn graphs) in the resulting paths.

# Repeat resolution

# Results

>- human dataset

# Segmental duplications

![](presentation/images/SDs.png)

>- Segmental duplications are duplicated blocks of genomic DNA typically ranging in size from 1-200 kb (IHGSC 2001)
>- They often contain sequence features such as high-copy repeats and gene sequences with intron-exon structure. 