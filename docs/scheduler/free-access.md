---
title: Free Access to HPC Resources
---

Farm and Hive both provide free/sponsored access to a limited amount of resources.

## Farm (group name `adamgrp`):

-   Partition `high2`: the entire group has combined access to 352 CPUs and 768 GB of RAM.
-   Partition `high`: the entire group has combined access to 192 CPUs and 500 GB of RAM.

## Hive (group name `publicgrp`):

-8<- "docs/include/hive-free-access.md"

See [here](/general/account-requests/#hippo) for instructions to request access to the free/sponsored resources for
Farm.

On Hive, every user is automatically a member of `publicgrp` and has access. You may need to add `--account=publicgrp`
to Slurm jobs to access these resources.
