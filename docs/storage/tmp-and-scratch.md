---
title: Temporary Storage
---

## Overview

Each node in every cluster has some amount of shared temporary space that can be used while jobs are running.

Franklin:

- Local temporary storage on each node: `/tmp`: self-clean. Please clean up after yourself at the end of each job.

Farm:

- Local storage on each node: `/tmp` and `/scratch`: auto-clean. Both point to the same storage and are automatically cleaned as your job exits.

Hive

- Local storage on each node: `/tmp` and `/scratch`: auto-clean. Both point to the same storage and are automatically cleaned as your job exits.

- Shared scratch: `/nfs/hive/scratch`: [auto-cleaned](#shared-scratch-auto-clean-policy) on a schedule.

- Shared MPI-IO scratch: `/nfs/hive/scratch-mpi-io`: mounted with options to work with MPI-IO. [auto-cleaned](#shared-scratch-auto-clean-policy) on a schedule.


## Shared scratch auto-clean policy

{% set threshold = "75%" %}
{% set days_ago = "35" %}


Hive shared scratch (and MPI-IO scratch) is auto-cleaned daily if the storage is more than {{ threshold }} full. The algorithm is to sort the files by access time and start deleting until the usage falls below {{ threshold }}. If the cleanup process gets to files that were last accessed less than {{ days_ago }} days ago, it will sort the files by creation time and delete the oldest until usage falls below {{ threshold }}.

NOTE: Both of these options can delete files that are still in use, so it is to everyone's benefit if every user cleans their temporary files so this auto-clean never needs to run.


