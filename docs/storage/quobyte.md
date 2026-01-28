---
title: Quobyte Storage
---

[Quobyte](https://www.quobyte.com/) is a fault-tolerant, high-performance parallel file system. There is an extensive
[whitepaper](https://www.quobyte.com/product/whitepaper/) for those interested in the details.

Quobyte is currently available from both Farm and Hive. Farm storage can be purchase through
[Hippo](https://hippo.ucdavis.edu/Farm/product/index). Hive storage can be purchased by contacting
[support](../support.md) with an amount to purchase and a campus chart string. Share names are normally the PI's Login
ID followed by `grp`, e.g. `jrigrp`. For campus organizations, we can also create the share based on your lab.

## Quobyte concurrent file writes from multiple nodes

Due to a known pathology in the Quobyte parallel file system, multiple clients writing to the same file cause lock
contention and eventually full blockage, preventing data from being written to that file. This prevents `slurmd` from
being able to finalize those tasks, which causes the nodes to get kicked out of the cluster, which requires admin
intervention to resolve.

!!! warning

    Because this causes cluster-wide impact, jobs found doing this are subject to being killed and the user's account temporarily locked.

We have an open feature request to allow an error to be returned to the client in these cases. In the meanwhile, please
ensure you do not write to the same file from multiple nodes.
