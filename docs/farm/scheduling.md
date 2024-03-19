
 Slurm is the job scheduler used for batch queue management in the clusters.
 Slurm is an open-source resource manager (batch queue)  and job scheduler designed for Linux clusters of all sizes.
The general idea with a batch queue is that you don't have to babysit your jobs. You submit it, and it'll run until it dies, or there is a problem. You can configure it to notify you via email when that happens. This allows very efficient use of the cluster. You can still babysit/debug your jobs if you wish using an interactive session (ie qlogin).

Our main concern is that all jobs go through the batch queuing system. Do not bypass the batch queue. We don't lock anything down but that doesn't mean we can't or won't. If you need to retrieve files from a compute node feel free to ssh directly to it and get them, but don't impact other jobs that have gone through the queue.

Here are some useful Slurm commands with their purpose:
sinfo reports the state of partitions and nodes managed by SLURM. It has a wide variety of filtering, sorting, and formatting options.
smap reports state information for jobs, partitions, and nodes managed by SLURM, but graphically displays the information to reflect network topology.
sbatch is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks.
squeue reports the state of jobs or job steps. It has a wide variety of filtering, sorting, and formatting options. By default, it reports the running jobs in priority order and then the pending jobs in priority order.
srun is used to submit a job for execution or initiate job steps in real time. srun has a wide variety of options to specify resource requirements, including: minimum and maximum node count, processor count, specific nodes to use or not use, and specific node characteristics (so much memory, disk space, certain required features, etc.).
A job can contain multiple job steps executing sequentially or in parallel on independent or shared nodes within the job's node allocation.
smap reports state information for jobs, partitions, and nodes managed by SLURM, but graphically displays the information to reflect network topology.
scancel is used to stop a job early. Example, when you queue the wrong script or you know it's going to fail because you forgot something.
See more in "Monitoring Jobs" in the Slurm Example Scripts article in the Help Documents.
More in depth information at http://slurm.schedmd.com/documentation.html