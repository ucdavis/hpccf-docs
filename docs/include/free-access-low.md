The `low` partition allows access to all the unused resources in the cluster. The downside is that when a job is submitted to `high` that needs these resources, your job will be killed and requeued. Unless your job can do automatic check-pointing and restarting, all progress is lost when the job is killed.

- Each job is limited to a maximum of 7 days (`7-00`) of runtime.

- You can access these resources by adding `--account=publicgrp --partition=low` to your `srun` or `sbatch` command.

Every user is automatically a member of `publicgrp` and has access to the `low` partition.
