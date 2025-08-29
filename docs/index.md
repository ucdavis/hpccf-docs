---
title: Documentation Overview
---

![HPC unit signature](assets/HPC-unit-signature.png){width="400" align="right"}

Welcome to the High-Performance Computing (HPC@UCD) Documentation Site. These pages are intended to be a how-to for
commonly asked questions about resources supported by High-Performance Computing at UC Davis.

HPC@UCD is a [core faciilty](https://research.ucdavis.edu/research-support/research-core-facilities/) reporting through
the Office of Research and supported by individual university colleges, the Office of the Provost, and the Vice
Chancellor for Research.

Before contacting HPC support, first try searching this documentation. This site provides information on accessing and
interacting with HPC supported clusters, an overview of available software ecosystems, and tutorials for commonly used
software and access patterns. It is split into a Users section for end-users and an Admin section with information
relevant to system administrators and advanced users.

Questions about the documentation or resources supported by the HPC can be directed to [hpc-help@ucdavis.edu](mailto:hpc-help@ucdavis.edu).

## Getting Started with HPC

Please read the [Supported Services](https://hpc.ucdavis.edu/supported-services) page.

The high-performance computing model at UC Davis starts with a principal investigator (PI) purchasing resources
(compute, GPU, storage) and making them available to their lab. HPC@UCD will assist in onboarding and providing support.

As a new principal investigator who is interested in purchasing resources, please read the **Our Clusters** section
below to determine which clusters are appropriate for onboarding. HPC@UCD can assist with hardware and storage
investments for condo clusters and sell fair-share priority, primary and archive storage for fair-share clusters. Please
email [hpc-help@ucdavis.edu](mailto:hpc-help@ucdavis.edu) with your affiliation to start the onboarding process. Resources external to UC Davis can
also purchase resources by inquiring at the hpc-help email address.

For getting started with HPC access under an existing PI, please see
[requesting an account](general/account-requests.md).

### Our Clusters

#### Condo Clusters

An HPC condo-style cluster is a shared computing infrastructure where different users or groups contribute resources
(such as compute nodes, storage, or networking) to a common pool, similar to how individual condo owners share common
amenities.

[**Farm**](farm/index.md): Sponsored by the College of Agriculture and Environmental Sciences. Farm resources can be purchased
by principal investigators regardless of affiliation.

[**Franklin**](franklin/index.md): Sponsored by units within the College of Biological Sciences, Franklin is open to PI's
within the Center for Neuroscience, Microbiology and and Molecular Genetics, Molecular and Cellular Biology, and other
approved collaborators.

[**Hive**](hive/index.md): A centrally managed cluster, with standardized hardware and connectivity, and a defined life cycle
of support, facilitates greater access to HPC for a more significant number of users on campus while maintaining support
for college-level needs. HPC@UCD offers two tiers of support moving forward and incentives to merge existing hardware
with the new cluster when possible.

**HPC2**: Sponsored by the College of Engineering and Computer Science and is open to principal investigators associated
with COE.

**Peloton**: Peloton is open to principal investigators associated with the College of Letters and Science. Peloton has
a shared tier open to users associated with CLAS.

#### Fair-Share Clusters

A fair-share HPC algorithm is a resource allocation strategy used to ensure equitable access to computing resources
among multiple users or groups over a long time horizon. The goal is to balance the workload and prevent any single user
or group from monopolizing the resources.

**LSSC0 (Barbera)** an HPC shared resource which is coordinated and run by HPC@UCD. LSSC0 is run with a fair-share
algorithm.

## How to request help

Emails sent to HPC@UCD are documented in Service Now via [hpc-help@ucdavis.edu](mailto:hpc-help@ucdavis.edu). HPC@UCD staff are available to respond to
requests on scheduled university work days from 8:00 am until 5:00 pm, and will respond to your inquiry as soon as
possible.

To ensure the best possible help, please send us all of the following information:

1. Your username, the cluster name you are running on, and your sponsor name.

2. The exact sequence of command(s) you ran and the directory you ran them in.

3. Errors you are getting (please copy-paste the output from the terminal window), or attach as a `.txt` file.

4. Slurm JobID if running via Slurm.

## Contributing to the documentation

This site is written in markdown using [MkDocs](https://daringfireball.net/projects/markdown/) with the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. If you would like to contribute, you may
[fork our repo :material-source-fork:](https://github.com/ucdavis/hpccf-docs/fork) and submit a pull request.

## Additional Information

-   [HPC@UCD home page](https://hpc.ucdavis.edu)
-   [Research Computing at UC Davis](https://researchcomputing.ucdavis.edu)
-   [UC Davis DataLab](https://datalab.ucdavis.edu)
