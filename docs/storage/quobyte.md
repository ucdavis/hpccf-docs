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

-8<- "docs/include/quobyte-concurrent-writes.md"

Unique filenames can be generated using a combination of the host name, and variables that Slurm sets.

For a normal job: `OUTPUT_FILE="$(hostname)-${SLURM_JOB_ID}.results"`

For an array job: `OUTPUT_FILE="$(hostname)-${SLURM_JOB_ID}_${SLURM_ARRAY_TASK_ID}.results"`

If you are writing software, then you need to use [file locks](https://en.wikipedia.org/wiki/File_locking).

We have an open feature request to allow an error to be returned in these cases. In the meanwhile, please ensure you do
not write to the same file from multiple nodes.
