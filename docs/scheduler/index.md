---
title: Job Scheduling
---

HPC clusters run [job schedulers](https://en.wikipedia.org/wiki/Job_scheduler) to distribute and manage
computational resources.
Generally, schedulers:

- Manage and enforce resource constraints, such as execution time, number of CPU cores, and amount of RAM a job may use;
- Provide tools for efficient communication between nodes during parallel workflows;
- Fairly coordinate the order and priority of job execution between users;
- Monitor the status and utilization of nodes.


![Slurm](../img/Slurm_logo.png){ align="right" }

HPCCF clusters use [Slurm](https://slurm.schedmd.com/documentation.html) for job scheduling.
A central controller runs on one of the file servers, which users submit jobs to from the access node using the
[`srun` and `sbatch` commands](commands.md).
The controller then determines a priority for the job based on the resources requested and schedules it on the queue.
Priority calculation can be complex, but the overall goal of the scheduler is to optimize a tradeoff between throughput on the cluster as a whole and turnaround time on jobs.

The [**Commands**](commands.md) section describes how to manage jobs and check cluster status using standard Slurm commands.
The [**Resources**](resources.md) section describes how to request computing resources for jobs.
The [**Job Scripts**](jobscripts.md) section includes examples of job scripts to be used with `sbatch`.
