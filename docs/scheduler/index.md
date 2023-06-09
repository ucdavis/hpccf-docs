# Slurm

HPC clusters run [job schedulers](https://en.wikipedia.org/wiki/Job_scheduler) to distribute and manage
computational resources.
Generally, schedulers:

- Manage and enforce resource constraints, such as execution time, number of CPU cores, and amount of RAM a job may use;
- Provide tools for efficient communication between nodes during parallel workflows;
- Fairly coordinate the order and priority of job execution between users;
- Monitor the status and utilization of nodes.


![Slurm](../img/Slurm_logo.png){ align="right" }

Franklin uses [Slurm](https://slurm.schedmd.com/documentation.html) as its job scheduler.
A central controller runs on one of the file servers, which users submit jobs to from the access node using the
[`srun` and `sbatch` commands](jobs.md).
The controller then determines a priority for the job based on the resources requested and schedules it on the queue.
Priority calculation can be complex, but the overall goal of the scheduler is to optimize a tradeoff between throughput on the cluster as a whole and turnaround time on jobs.

The [**Jobs**](jobs.md) section describes how to submit and manage jobs with Slurm.
The [**Queueing**](queues.md) section describes Franklin's queuing policy and structure.
The [**Status**](status.md) section details how to use Slurm to monitor the status of the cluster as whole.