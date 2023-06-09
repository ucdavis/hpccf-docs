# :material-dna: Franklin

Franklin is a high performance computing (HPC) cluster for the [College of Biological Sciences](https://biology.ucdavis.edu/) at UC Davis.
Its primary use is for research in genetics, genomics, and proteomics, structural biology via cryogenic electron microscopy, computational neuroscience, and generally, the computional biology workflows related to those fields.
Franklin currently consists of 6 AMD :simple-amd: CPU nodes each with 128 physical and 256 logical cores and 1TB of RAM,
5 GPU nodes with a total of 40 Nvidia :simple-nvidia: RTX A4000, RTX A5000, and RTX 2080 TI GPUs, and a collection
of ZFS :simple-openzfs: file servers providing over 2PB of storage.



![CBS unit signature](assets/CBS-unit-signature.png){ width="400" align="right" }

## Administration

Franklin is maintained by the [HPC Core Facility](https://hpc.ucdavis.edu/about).
Software installation and support requests should be directed to [hpc-help@ucdavis.edu](mailto:hpc-help@ucdavis.edu).



![HPC unit signature](assets/HPC-unit-signature.png){ width="400" align="right" }

## Using This Documentation

Before contacting HPCCF support, first try searching this documentation.
This site provides information on accessing and interacting with the cluster,
an overview of available software ecosystems, and tutorials for commonly used software and access patterns.
It is split into a **Users** section for end-users and an **Admin** section with information relevant to system
administators.
This documentation is being actively expanded as Franklin's software and userbase grows.

This site is written in [markdown](https://daringfireball.net/projects/markdown/) using [MkDocs](www.mkdocs.org) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
If you would like to contribute, you may [fork our repo :material-source-fork:](https://github.com/ucdavis/HPCCF-franklin-docs/fork) and submit a pull request :material-source-pull:.