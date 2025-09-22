---
title: Hive
---

![Hive Logo](../assets/hive-icon.png){ width="256" align="right" }

# Hive

Hive is a centrally managed cluster with standardized hardware and connectivity and a defined life cycle of support.
Hive was built to provide greater access to HPC for a larger number of users on campus while maintaining support for
college-level needs. HPC@UCD offers [two tiers of support](https://hpc.ucdavis.edu/model-hpc-hardware-support) moving
forward and incentives to merge existing hardware when possible.

## Hive Hardware

The core of Hive consists of 20 nodes, each with 128 CPU cores and 2 TB of RAM, and 5x NVIDIA A6000s for general use. In
the `low` partition, there are 4x NVIDIA H100 GPUs, 8x NVIDIA A100 GPUs, and 4x NVIDIA A6000s that can be used when not
in-use by the PI groups that paid for them. Nodes that are new enough are being migrated from other campus clusters to
simplify administration and maintenance.

As of September 22nd, 2025, there are a total of 6,720 CPU cores and 61 TiB of RAM.

Hive uses a parallel file system, [Quobyte](https://www.quobyte.com) for storage. This is a very exciting change and a
first for any cluster at UC Davis. A parallel file system allows performance and capacity to grow over time, keeping up
with research demands, all while keeping a single directory for PIs.

## Access to Hive

UC Davis staff, faculty, and graduate students are entitled to free access to:

-8<- "docs/include/hive-free-access.md"

In addition to this, each new user is allocated a 20 GB home directory.

To request free access, follow the [request a new account](../general/account-requests.md) documentation and request
access to the `UCD HPC Sponsored Public Access (publicgrp)` from the list of sponsors through
[Hippo](https://hippo.ucdavis.edu/Hive/myaccount).

Additional resources on Hive may be purchased two ways. Sponsors (PIs and group leads) may purchase individual compute
cores and TB of storage at our current [rates](https://hpc.ucdavis.edu/rates#hive). In consultation with HPC@UCD,
sponsors may also purchase approved nodes to contribute to Hive. HPC@UCD will work with sponsors to understand budgets
and specifications and request quotes.

Contributors receive priority access to the amount of resources that they have purchased through the `high` partition.
No guarantees are made, but generally, jobs will start within a couple of minutes. There are some
[edge cases](scheduling.md#high-partition-edge-cases).

Finally, Hive has a node available for use in graduate teaching. Contact [support](../support.md) to request information
or access to these resources.

## Hive Administration

Hive hardware and software are administered by the [HPC@UCD team](https://hpc.ucdavis.edu/people).

### Current Rates

Rates for Hive can be found [here](https://hpc.ucdavis.edu/rates#hive).

For purchases and inquiries, please contact [support](../support.md).
