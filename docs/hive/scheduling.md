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

### Exclusive node access

Note for users coming from other clusters: the use of the `--exclusive` flag will cause your job to take a very long
time to schedule. If you are using this flag and your job will not start on Hive, please remove it and resubmit. Slurm
erroneously flags these jobs with `(QOSGrpCpuLimit)`.

## Quobyte concurrent write pathology

The `--output=` and `--error=` files must be unique on Quobyte. This is a specialized case of the more general
[Quobyte issue](../storage/quobyte.md#quobyte-concurrent-file-writes-from-multiple-nodes) with concurrent file writes.

-8<- "docs/include/quobyte-concurrent-writes.md"

When this happens with Slurm's `StdOut` and `StdErr` files, it causes the `slurmd` process to block, which causes the
nodes to get kicked out of the cluster, which requires admin intervention to resolve.

This is a very bad thing. Luckily there is a simple workaround. When writing to Quobyte, every `StdOut` and `StdErr`
file needs to be unique per writer. This can easily be accomplished in `sbatch` files like this:

- For a small job running on a single node, include the `%j` replacement pattern in the filename:

  ```bash
  #SBATCH --output=slurm-%j.out
  #SBATCH --error=slurm-%j.err
  ```

- For an array job, include the `%A_%a` replacement patterns in the filename:

  ```bash
  #SBATCH --output=slurm-%A_%a.out
  #SBATCH --error=slurm-%A_%a.err
  ```

- For an MPI job, or any other job that will run on multiple nodes, include the `%N` replacement pattern in addition to
  the other patterns:

      MPI standard job

      ```bash
      #SBATCH --output=slurm-%j_%N.out
      #SBATCH --error=slurm-%j_%N.err
      ```

      MPI array job

      ```bash
      #SBATCH --output=slurm-%A_%a_%N.out
      #SBATCH --error=slurm-%A_%a_%N.err
      ```

## MPI jobs

Hive currently has 4 generations of AMD EYPC processors as well as several Intel Icelake. If you would like to constrain
your job to specific generations of CPU, you use the following CPU types: `zen`, `zen2`, `zen3`, `zen4`, or `icelake`.
For example: `--constraint='(zen2|zen3|zen4)'`. As with all constraints, the more you add, the longer your job will take
to schedule, as Slurm needs to wait for those node types to be available. See the official Slurm
[constraint](https://slurm.schedmd.com/sbatch.html#OPT_constraint) documentation for all the options.

MPI jobs generally need to request one task per MPI worker. If you need 128 MPI workers, you can request `--ntasks=128`.
If you instead request CPUs with `--cpus-per-task=128` you will end up with a single MPI worker that has access to 128
CPUs, which is typically not what you want.

Additionally, we have configured Slurm to understand the InfiniBand switch topology, so for maximum internode
throughput, you can use the `--switches=1@1-00` flag. This constraint means all nodes the job runs on will be no more
than 1 InfiniBand switch apart, but Slurm will not delay the job by more than 1 day if it cannot meet this requirement.

Another useful Slurm flag is `--nodes=1-4` which can be used to constrain your job to a limited number of nodes so it
does not scatter across too many nodes.

Slurm can be told to pack the jobs tighter on the nodes with `--distribution=block,pack`.

Like any Slurm constraint, it will take longer for your job to schedule with these flags enabled, but your job should
run better once it schedules.

Putting it all together, the MPI parts of a sbatch script could look like this:

```bash
#SBATCH --ntasks=256
#SBATCH --mem-per-cpu=1G

# Limit Slurm to running this on 1 to 4 nodes.
#SBATCH --nodes=1-4

#SBATCH --constraint='(zen2|zen3|zen4)'
#SBATCH --distribution=block,pack
#SBATCH --switches=1@1-00
```

For more information about CPU cores and job scheduling, see [CPUs / cores](../scheduler/resources.md#cpus-cores)

### MPI-IO

Hive has a dedicated storage area designed for MPI-IO and has special NFS mount options to support this. These options
make it unsuitable for normal use. Because this storage is specific to MPI-IO, we have created a `mpi-io-grp` that you
need to request access to. Instructions for requesting access to a group are here:
https://docs.hpc.ucdavis.edu/general/account-requests/how-to-request-access-to-another-group-on-a-cluster

Once you have been approved for the `mpi-io-grp`, you can access the storage through `/nfs/hive/scratch-mpi-io/`.

Because this is a shared area, unused files and directories are subject to automatic removal. To avoid the automatic
cleanup process, you need to create a new sub-directory in this space that is the same as your running job ID. Once your
job finishes, this data will become eligible to be purged, so be sure to copy out any results before your Slurm job
exits.
