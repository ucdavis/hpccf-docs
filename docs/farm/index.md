# Farm

![CAES unit signature](../assets/UCDavis_CAES_logo_RGB_vector.svg){ width="400" align="right" }

Farm is a Linux-based supercomputing cluster for the
[College of Agricultural and Environmental Sciences](https://caes.ucdavis.edu/) (CA&ES) at UC Davis. Designed for both
research and teaching, it is a significant campus resource primarily for CPU and RAM-based computing, with a wide
selection of centrally-managed software available for research in genetics, proteomics, and related bioinformatics
pipelines, weather and environmental modeling, fluid and particle simulations, geographic information system (GIS)
software, and more.

## Farm Hardware

Farm is an evolving cluster that changes and grows to meet the current needs of researchers, and has undergone three
phases, with Farm III as the most recent evolution.

Farm III consists of 60 parallel nodes with up to 64 CPUs and 256GB RAM each in `low`/`high`, plus 27 "bigmem" nodes
with up to 128 CPUs and 2 TB RAM each in the `bml`/`bmh` queue. All Farm III bigmem and newer parallel nodes and storage
are on EDR/100Gbit interconnects.

Hardware from Farm III is still in service; Farm I has been decommissioned as of 2014, and Farm II has been
decommissioned as of 2025-12.

Farm also has multiple file servers with over 5.3PB of storage space in total.

## Access to Farm

All researchers in CA&ES are entitled to free access to:

- 4 nodes with 352 CPUs and 768GB RAM each in Farm III's low, and high-priority batch queues.

- The `bml` (bigmem, low priority/requeue) partition, which has 27 nodes with a combined 30 TB of RAM.

In addition to this, each new user is allocated a 20 GB home directory. If you want to use the CA&ES free tier, select
"CA&ES free tier" from the list of sponsors [here](https://hippo.ucdavis.edu/Farm/myaccount).

Additional usage and access may be purchased by contributing to Farm III through the node and/or storage rates or by
purchasing equipment and contributing through the rack fee rate.

Contributors always receive priority access to the resources that they have purchased within one minute with the
“one-minute guarantee.” Users can also request additional unused resources on a “fair share” basis in the medium or low
partitions.

## Farm Administration

Farm hardware and software are administrated by the [HPC Core Facility Team](https://hpc.ucdavis.edu/people).

New purchases for Farm can be placed through [Hippo](https://hippo.ucdavis.edu/Farm/product/index).

### Bring your own equipment (BYOE):

Equipment may be purchased directly by researchers based on actual cost. Equipment quotes are available upon request. If
you BYOE, then the racking rate of $375 per year per rack unit for five years will apply. You require custom equipment
not available through Hippo, you can start a discussion with [Adam Getchell](mailto:acgetchell@ucdavis.edu) or
[HPC@UCD](../support.md).
