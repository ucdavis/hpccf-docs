---
title: Waltz temporary access on Hive
---

Peloton's Waltz server has been mounted on some Hive compute nodes. Waltz is currently only connected to Hive over
InfiniBand, so you need a node with InfiniBand to be able to access it. You can request a node with InfiniBand by adding
the `--constraint=mpi` flag to your sbatch/srun job. See the [MPI documentation](scheduling.md#mpi-jobs) for more
information.

The path to access Waltz is `/nfs/peloton/waltz/`. If you have permission issues, please open a ticket with
[HPC@UCD support](../support.md).

!!! warning "InfiniBand Limitations"

    Only some of the Hive nodes have InfiniBand, so use the `--constraint=mpi` flag to ensure your job can access Waltz.

    Neither of the Hive login nodes (`login1.hive`, and `login2.hive`), nor `transfer.hive` have InfiniBand, so you cannot access Waltz from Hive's login or transfer nodes.
