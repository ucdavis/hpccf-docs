---
title: Free Access to HPC Resources
---

Farm and Hive both provide free/sponsored access to a limited amount of resources.

## Farm

See [here](..//general/account-requests.md#hippo) for instructions to request access to the free/sponsored resources for
Farm.

#### Slurm account name `adamgrp`

-   Partition `high2`: the entire group has combined access to 352 CPUs and 768 GB of RAM.
-   Partition `high`: the entire group has combined access to 192 CPUs and 500 GB of RAM.

#### Slurm account name `gpul-users`

-   Partition: `gpul`: provides access to currently idle GPUs.

    -   Each job is limited to a maximum of:

        -   1 day (`1-00`) of runtime
        -   1 node

    -   You can access these resources by adding `--account=gpul-users --partition=gpul --gpus=1` to your srun or sbatch
        command.

    -   If you require a specific type of GPU, you can request with `--gpus=TYPE:1`. The available types are: `a100`,
        `a5500`, `titan`, and `v100`.

## Hive

#### Slurm account name `publicgrp`

-8<- "docs/include/hive-free-access.md"

On Hive, every user is automatically a member of `publicgrp` and has access. You may need to add `--account=publicgrp`
to Slurm jobs to access these resources.
