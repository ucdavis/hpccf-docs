---
title: Hive Job Scheduling
---

## Free Access

See the [Free Access](../scheduler/free-access.md#hive) docs.

## Paid Access

Hive resources are generally purchased by the CPU. The current rates can be seen [here](https://hpc.ucdavis.edu/rates).
Specialized needs (entire nodes or GPU nodes) can be purchased by contacting [HPC@UCD support](../support.md). HPC will
work with you to find a configuration suitable to use in Hive.

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

### `high` Partition Edge Cases

Contributors receive priority access to the amount of resources that they have purchased through the `high` partition.
No guarantees are made, but generally, jobs will start within a couple of minutes. There are some edge cases:

1. The CPUs and/or RAM are already fully occupied by another user in the group. In this case, the users will see
   `(QOSGrpCpuLimit)` or `(QOSGrpMemLimit)` in the output of `squeue` for their job(s).

1. The job requested a large chunk of CPUs or RAM on a single node, but due to job fragmentation, that amount of
   resources is not currently available on a single node (rare).

1. There is a cluster-wide issue causing too many nodes to be unavailable for jobs (very rare).

1. A Slurm database backup is in-progress.

## Slurm Scheduling Requirements

### `--output=` and `--error=` files need to be unique on Quobyte

Due a known pathology in the Quobyte parallel file system, multiple clients writing to the same file cause lock
contention and eventually full blockage, allowing no data to be written to the file. When this happens with Slurm's
`StdOut` and `StdErr` files, it causes the `slurmd` process to block, which causes the nodes to get kicked out of the
cluster, which requires admin intervention to resolve.

This is a very bad thing. Luckily there is a simple workaround. When written Quobyte, every `StdOut` and `StdErr` file
needs to be unique per writer. This can easily be accomplished in sbatch files like this:

-   For a small job running on a single node, include the `%J` replacement pattern in the filename:

    ```bash
    #SBATCH --output=slurm-%J.out
    #SBATCH --error=slurm-%J.err
    ```

-   For an array job, include the `%A_%a` replacement patterns in the filename:

    ```bash
    #SBATCH --output=slurm-%A_%a.out
    #SBATCH --error=slurm-%A_%a.err
    ```

-   For an MPI job, or any other job that will run on multiple nodes, include the `%N` replacement pattern in addition
    to the other patterns:

: Standard job

    ```bash
    #SBATCH --output=slurm-%J_%N.out
    #SBATCH --error=slurm-%J_%N.err
    ```

: Array job

    ```bash
    #SBATCH --output=slurm-%A_%a_%N.out
    #SBATCH --error=slurm-%A_%a_%N.err
    ```

We have an open support case with the vendor. Quobyte has indicated they may add an option to make this type of IO
timeout and return an IO error to the application (Slurm in this case).

### `--exclusive` sbatch/srun flag

Note for users coming from other clusters. The use of the `--exclusive` flag will cause your job to take a very long
time to schedule. If you are using this flag and your job will not start on Hive, please remove it and resubmit. Slurm
erroneously flags these jobs with `(QOSGrpCpuLimit)`.

### MPI jobs

Not all nodes that have been brought into Hive have InfiniBand hardware, so jobs that do MPI and require InfiniBand
connectivity need to use the `--constraint=mpi` flag.

Additionally, we have configured Slurm to understand the InfiniBand switch topology, so for maximum internode
throughput, you can use the `--switches=1` flag. Like any Slurm constraint, it will take longer for your job to schedule
with this flag enabled.

MPI jobs generally need to request one task per MPI worker. If you need 128 MPI workers, you can request `--ntasks=128`.
If you instead request CPUs with `--cpus-per-task=128` then you will end up with a single MPI worker that has access to
128 CPUs, which is typically not what you want.

For more information about CPU cores and job scheduling, see [CPUs / cores](../../scheduler/resources/#cpus-cores)
