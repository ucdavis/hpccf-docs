---
title: Temporary Storage
---

## Overview

Each node in every cluster has some amount of shared temporary space that can be used while jobs are running. This is intended to be temporary space for job output and not extra storage for your group or a home directory expansion. Abuse of this shared space can result in your jobs being cancelled and your account being locked.

Franklin:

- Local temporary storage on each node in `/tmp` requires users to delete the data as they finish with it. Please clean up after yourself at the end of each job.

Farm:

- Local storage on each node: `/tmp` and `/scratch`. Both point to the same storage and are automatically cleaned as your job exits.

Hive

- Local storage on each node: `/tmp` and `/scratch`. Both point to the same storage and are automatically cleaned as your job exits.

- Shared scratch: `/nfs/hive/scratch`: [auto-deleted](#shared-scratch-auto-delete-policy) on a schedule.

- Shared MPI-IO scratch: `/nfs/hive/scratch-mpi-io`: mounted with options to work with MPI-IO. [auto-deleted](#shared-scratch-auto-delete-policy) on a schedule.


## Shared scratch auto-delete policy

{% set threshold = "75%" %}
{% set days_ago = "35" %}

Data on Hive's shared scratch (and MPI-IO scratch) can be automatically deleted if the storage is more than {{ threshold }} full. The algorithm is to sort the files by access time and start deleting until the usage falls below {{ threshold }}. If the cleanup process gets to files that were last accessed less than {{ days_ago }} days ago, it will sort the files by creation time and delete the oldest until usage falls below {{ threshold }}.

NOTE: Both of these options can delete files that are still in use, so it is to everyone's benefit if every user cleans their temporary files so this auto-delete never needs to run.


