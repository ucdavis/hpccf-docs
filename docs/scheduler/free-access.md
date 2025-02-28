---
title: Free Access to HPC Resources
---

Farm and Hive both provide free/sponsored access to a limited amount of resources. The limits are:

-   Farm (group name `adamgrp`):

    -   Partition `high2`: the entire group has combined access to 352 CPUs and 768 GB of RAM.
    -   Partition `high`: the entire group has combined access to 192 CPUs and 500 GB of RAM.

-   Hive (group name `publicgrp`):
    -   Partition `high`: the entire group has access to 128 CPUs, 2000 GB of RAM, and 4 GPUs (NVIDIA A6000s).
        -   Each job is limited to a maximum of 8 CPUs, 128 GB of RAM, and 1 GPU.
    -   Partition `low`: This partition allows access to all the unused resources in the cluster. The downside is that
        when a job is submitted to `high` that needs these resources, your job will be killed and requeued. Unless your
        job can do automatic check-pointing and restarting, all progress is lost when the job is killed.
        -   Each job is limited to a maximum a maximum runtime of 3 days (`3-00`).

See [here](/general/account-requests/#hippo) for instructions to request access to the free/sponsored resources for
Farm.

On Hive, every user is automatically a member of `publicgrp` and has access. You may need to add `--account=publicgrp`
to Slurm jobs to access these resources.
