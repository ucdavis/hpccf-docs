---
title: Free Access to HPC Resources
---

Hive provides free/sponsored access to a limited amount of resources and well as access to otherwise unused compute and GPU resources. Farm only allows access to otherwise unused compute and GPU resources.

See [here](../general/account-requests.md#hippo) for instructions to request access to the free resources on Farm and Hive.

## Hive

### Partition high

-8<- "docs/include/hive-free-access-high.md"

## Farm and Hive

### Low partition

-8<- "docs/include/free-access-low.md"

### GPUs

All GPUs in both clusters are available for use when not otherwise used by the PIs who paid for them. The partition `low` provides access to currently idle GPUs.

- Each job is limited to a maximum of 7 days (`7-00`) of runtime.

- You can access these resources by adding `--partition=low --gpus=1` to your `srun` or `sbatch` command.

- If you require a specific type of GPU, you can request it with `--gpus=TYPE:1`. You can run this command to see the types and counts of GPUs on each cluster: `sinfo -p low -o "%G|%D" | column -s'|' -t`
