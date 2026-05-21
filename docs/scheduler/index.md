---
title: Cluster Overview
---

## Login nodes

The login node is the point where most users directly interact with the cluster via [SSH](../general/access.md#how-do-i-connect-to-a-cluster). Once you have an open shell on the login node, you can run small processes and submit larger, longer-running work to the compute nodes using [Slurm](#slurm). Resources accessed through Slurm (either with `sbatch` or `srun`) are dedicated to the user for the length of that Slurm job. However, login nodes are a shared resource, so technical restrictions are put in place to reduce the chance of an individual user impacting every user.

### Resource restrictions

On the login nodes, each user is limited to:

- 2 CPUs (200%)
- 7.5% of the total RAM
- 500 MB of swap
- 512 total processes
- 16,384 open files.

Any long-running processes that require intense IO or computation must be run on the compute nodes using Slurm.

Users causing performance issues on the login node are subject to having all of those processes killed, even if they are within these limitations.

## Slurm

HPC clusters run [job schedulers](https://en.wikipedia.org/wiki/Job_scheduler) to distribute and manage computational
resources. Generally, schedulers:

-   Manage and enforce resource constraints, such as execution time, number of CPU cores, and amount of RAM a job may
    use;
-   Provide tools for efficient communication between nodes during parallel workflows;
-   Fairly coordinate the order and priority of job execution between users;
-   Monitor the status and utilization of nodes.

![Slurm](../img/Slurm_logo.png){ align="right" }

HPC@UCD clusters use [Slurm](https://slurm.schedmd.com/documentation.html) for job scheduling. A central controller runs
on one of the file servers, which users submit jobs to from the access node using the
[`srun` and `sbatch` commands](commands.md). The controller then determines a priority for the job based on the
resources requested and schedules it on the queue. Priority calculation can be complex, but the overall goal of the
scheduler is to optimize a tradeoff between throughput on the cluster as a whole and turnaround time on jobs.

The [**Commands**](commands.md) section describes how to manage jobs and check cluster status using standard Slurm
commands. The [**Resources**](resources.md) section describes how to request computing resources for jobs. The
[**Job Scripts**](jobscripts.md) section includes examples of job scripts to be used with `sbatch`.
