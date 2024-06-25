# About the Farm Cluster

*Updated on 10/20/2023*


Farm is a Linux-based supercomputing cluster for the [College of Agricultural and Environmental Sciences](https://caes.ucdavis.edu/) at UC Davis. 
Designed for both research and teaching, it is a significant campus resource primarily for CPU and RAM-based 
computing, with a wide selection of centrally-managed software available for research in genetics, proteomics, and 
related bioinformatics pipelines, weather and environmental modeling, fluid and particle simulations, geographic 
information system (GIS) software, and more. 

For buying in resources in Farm cluster, contact CEAS IT director Adam 
Getchell - <acgetchell@ucdavis.edu>

## Farm Hardware

Farm is an evolving cluster that changes and grows to meet the current needs of researchers, and has undergone three 
phases, with Farm III as the most recent evolution. 

Farm III consists of 32 parallel nodes with up to 64 CPUs and 
256GB RAM each in low2/med2/high2, plus 17 “bigmem” nodes with up to 96 CPUs and 1TB RAM each in the bml/bmm/bmh 
queue. All Farm III bigmem and newer parallel nodes and storage are on EDR/100Gbit interconnects. Older parallel nodes 
and storage are on FDR/55Gbit. 

Farm II consists of 95 parallel nodes with 24 CPUs and 64GB RAM each in low/med/high, 
plus 9 “bigmem” nodes with 64 CPUs and 512GB RAM each in the bigmeml/bigmemm/bigmemh queues, and 1 additional node 
with 96 CPUs and 1TB RAM. Farm II nodes are on QDR/32Gbit interconnects. 

Hardware from both Farm II and Farm III are 
still in service; Farm I has been decommissioned as of 2014. 

Farm also has multiple file servers with over 5.3PB of storage space in total.

## Access to Farm

All researchers in CA&ES are entitled to free access to:

  -  8 nodes with 24 CPUs and 64GB RAM each (up to a maximum of 192 CPUs and 512GB RAM) in Farm II’s low, medium, and high-priority batch queues, 
  
  -  4 nodes with 352 CPUs and 768GB RAM each 
in Farm III's low2, med2, and high2-priority batch queues. 

- The bml (bigmem, low priority/requeue) partition, which has 
24 nodes with a combined 60 TB of RAM. 

In addition to this, each new user is allocated a 20GB home directory. If you 
want to use the CA&ES free tier, select “CA&ES free tier" from the list of sponsors [here](https://hippo.ucdavis.edu/Farm/myaccount). 

Additional usage and access 
may be purchased by contributing to Farm III by through the node and/or storage rates or by purchasing equipment and 
contributing through the rack fee rate. 

Contributors always receive priority access to the resources that they have 
purchased within one minute with the “one-minute guarantee.” Users can also request additional unused resources on a 
“fair share” basis in the medium or low partitions.

## Farm Administration

Farm hardware and software are administrated by the [HPC Core Facility Team](https://hpc.ucdavis.edu/people).

### Current Rates

As of October 2023, the rates for Farm III: 

Node and Storage Rates (each buy-in guarantees access for 5 years): -

- **Parallel (CPU) node:** $13,500 (512 GB RAM, 128 cores/256 threads, 2 TB /scratch) 
- **Bigmem node:** 128 cores/256 threads, 
2TB RAM (bml, bmm, bmh partitions) - $25,000 
- **GPU:** $19,500 1/4 of a GPU node (A100 with 80GB GPU RAM, 16 CPU cores / 
32 threads, 256GB system RAM) 
- **Storage:** $100/TB with compression for 5 years (does not include backups)

### Bring your own equipment:

Equipment may be purchased directly by researchers based on actual cost. Equipment quote available upon request. 

- Equipment purchases not using above rates - $375/year per rack unit for five years For more information about buying 
into Farm, contact [Adam Getchell](acgetchell@ucdavis.edu) or the [Helpdesk](hpc-help@ucdavis.edu).
