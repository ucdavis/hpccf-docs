---
title: Databases
---

Franklin's MMG and MCB stakeholders have kindly donated 10TB of storage space for centralized databases. The root databases directory is `/share/databases`.

## alphafold2

The core [alphafold2](software/alphafold.md) databases are in the `alphafold` subdirectory, including *uniref30*, *uniref90*, *uniprot*, *mgnify*, all relevant *pdb* databases, and alphafold's models. The provided alphafold wrapper script sets these locations automatically.

## CryoEM

Databases for [relion](software/cryoem.md#relion) and related tools like *deepemhancer* are available as well. These locations are automatically configured by the relion modules.

## NCBI Blast

The `blast` subdirectory has the following NCBI databases available in blast format:

- *nr*
- *16S_ribosomal_RNA*
- *18S_fungal_sequences*
- *28S_fungal_sequences*
- *mito*
- *nt_prok*
- *nt_viruses*
- *pdbaa*
- *pdbnt*
- *refseq_protein*
- *swissprot*
- *taxdb*

These are updated weekly via NCBI's `update_blastdb.pl` script.

Please [file a ticket](mailto:hpc-help@ucdavis.edu?subject=Franklin%20Database%20Request) to request additional databases. 