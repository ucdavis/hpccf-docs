-   Partition `high`: the entire group has combined access to 128 CPUs, 2000 GB of RAM, and 4 GPUs (NVIDIA A6000s).

    -   Each job is limited to a maximum of:

        -   8 CPUs
        -   128 GB of RAM
        -   1 GPU

    -   You can access these resources by adding `--account=publicgrp --partition=high` to your srun or sbatch command.

-   Partition `low`: This partition allows access to all the unused resources in the cluster. The downside is that when
    a job is submitted to `high` that needs these resources, your job will be killed and requeued. Unless your job can
    do automatic check-pointing and restarting, all progress is lost when the job is killed.

    -   Each job is limited to a maximum of:

        -   3 days (`3-00`) of runtime
        -   1 node

    -   You can access these resources by adding `--account=publicgrp --partition=low` to your srun or sbatch command.
