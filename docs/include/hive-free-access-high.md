In the `high` partition, every member of `publicgrp` has combined access to 128 CPUs, 2000 GB of RAM, and 4 GPUs (NVIDIA A6000s).

- Each job is limited to a maximum of:
    - 8 CPUs
    - 128 GB of RAM
    - 1 GPU

- You can access these resources by adding `--account=publicgrp --partition=high` to your `srun` or `sbatch` command.
