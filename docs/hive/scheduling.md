---
title: Hive Job Scheduling
---

## Free Access

See the [Free Access](../scheduler/free-access.md#hive) docs.

## Paid Access

Hive resources are generally purchased by the CPU. The current rates can be seen [here](https://hpc.ucdavis.edu/rates).
Specialized needs (entire nodes or GPU nodes) can be purchased by contacting [HPC@UCD support](../general/support.md).
HPC will work with you to find a configuration suitable to use in Hive.

### College/Group Resources

Some colleges have purchased group resources, which you may be able to request access to through
[Hippo](../general/account-requests.md#how-to-request-access-to-another-group-on-a-cluster).

Once you have access to group resources, you can request to use them with
`--account={account-name}grp --partition=high`. For a PI group, `{account-name}` will typically be the PI's UCD Login
ID, followed by `grp`. A summary of the Slurm accounts you have access to, as well as the amount of resources in those
accounts, is printed every time you log in to Hive.

### Slurm Resource Mediation

Access to resources is mediated by Slurm. Nodes are not assigned to a user/group/PI. Instead, Slurm grants access to the
requested resources on the next available node. This allows a group to continue to access resources, even when any
particular node is down.

### WARNING: `--exclusive` sbatch/srun flag

Note for users coming from other clusters. The use of the `--exclusive` flag will cause your job to take a very long
time to schedule. If you are using this flag and your job will not start on Hive, please remove it and resubmit. Slurm
erroneously flags these jobs with `(QOSGrpCpuLimit)`.

### MPI jobs

Not all nodes that have been brought into Hive have InfiniBand hardware, so jobs that do MPI and require InfiniBand
connectivity need to use the `--constraint=mpi` flag.

Additionally, we have configured Slurm to understand the InfiniBand switch topology, so for maximum internode
throughput, you can use the `--switches=1` flag. Like any Slurm constraint, it will take longer for your job to schedule
with this flag enabled.

MPI jobs generally need to request one task per MPI worker. If you need 128 MPI workers, you can request `--ntasks=1`.
If you instead request CPUs with `--cpus-per-task=128` then you will end up with a single MPI worker that has access to
128 CPUs, which is generally not what you want.
