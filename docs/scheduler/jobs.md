# Jobs

After [logging in to Franklin](../general/access.md), your session exists on the **head node**: a single,
less powerful computer that serves as the gatekeeper to the rest of the cluster.
To do actual work, you will need to write submission scripts that define your job and submit
them to the cluster along with resource requests.

## Batch Jobs: `sbatch`

Most of the time, you will want to submit jobs in the form of job scripts.
The batch job script specifies the resources needed for the job, such as the number of nodes, 
cores, memory, and walltime.
A simple example would be:

``` { .slurm .copy title="jobscript.sh" }
#!/bin/bash 
# (1)
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --mem=100MB
#SBATCH --partition=low

echo "Running on $(hostname)"
```

1. This will determine the shell Slurm uses to execute your script. You could, for example, use `/bin/sh` or `/bin/zsh`.

Which can be submitted to the scheduler by running:

``` console
$ sbatch jobscript.sh
Submitted batch job 629
```

The job script is a normal shell script -- note the `#!/bin/bash` -- that contains additional directives.
`#SBATCH` lines specify directives to be sent to the scheduler; in this case, our resource requests:

- `--ntasks`: Number of tasks to run. Slurm may schedule tasks on the same or different nodes.
- `--cpus-per-task`: Number of CPUs (cores) to allocate per task.
- `--time`: Maximum wallclock time for the job.
- `--mem`: Maximum amount of memory for the job.
- `--partition`: The queue partition to submit to. See the [queueing](queues.md) section for more details.

??? warning

    Jobs that exceed their memory or time constraints will be automatically killed.
    There is no limit on spawning threads, but keep in mind that using far more threads than requested cores
    will result in rapidly decreasing performance.

`#SBATCH` directives directly correspond to arguments passed to the `sbatch` command. As such, one could remove
the lines starting with `#SBATCH` from the previous job script and submit it with:

``` console
$ sbatch --ntasks=1 --cpus-per-task=1 --time=01:00:00 --mem=100MB --partition=low jobscript.sh
```

Using directives with job scripts is recommended, as it helps you document your resource requests.

Try `man sbatch` or [visit the official docs](https://slurm.schedmd.com/sbatch.html) for more options.
More information on resource requests can be found in the [**Resources**](resources.md) section,
and more examples on writing job scripts can be found in the [**Job Scripts**](jobscripts.md) section.

## Interactive jobs: `srun`

Sometimes, you want to run an interactive shell session on a node, such as running an [IPython](https://ipython.org/) session.
`srun` takes the same parameters as `sbatch`, while also allowing you to specify a shell.
For example:

``` console
$ srun --ntasks=1 --time=01:00:00 --mem=100MB --partition=low --pty /bin/bash
srun: job 630 queued and waiting for resources
srun: job 630 has been allocated resources
camw@c-8-42:~$
```

Note that addition of the `--pty /bin/bash` argument.
You can see that the job is queued and then allocated resources, but instead of exiting, you are brought
to a new prompt.
In the example above, the user `camw` has been moved onto the node `c-8-42`, which is indicated by the new terminal
prompt, `camw@c-8-42`.
The same resource and time constraints apply in this session as in `sbatch` scripts.

??? note

    This is the only way to get direct access to a node: you will not be able to simply do `ssh c-8-42`, for example.

Try `man srun` or [visit the official docs](https://slurm.schedmd.com/srun.html) for more options.


## Listing jobs: `squeue`

`squeue` can be used to monitor running and queued jobs.
Running it with no arguments will show *all* the jobs on the cluster; depending on how many users are active, this could be a lot!

``` console
$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               589 jawdatgrp Refine3D adtaheri  R 1-13:51:39      1 gpu-9-18
               631       low jobscrip     camw  R       0:19      1 c-8-42
               627       low Class2D/ mashaduz  R      37:11      1 gpu-9-58
...
```

To view only *your* jobs, you can use `squeue --me`.

``` console
$ squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               631       low jobscrip     camw  R       0:02      1 c-8-42
```

The format -- which columns and their width -- can be tuned with the [`--format`](https://slurm.schedmd.com/squeue.html#OPT_format) parameter.
For example, you might way to also include how many cores the job requested, and widen the fields:

``` {.console .copy}
$ squeue --format="%10i %.9P %.20j %.10u %.3t %.25S %.15L %.10C %.6D %.20R"
JOBID      PARTITION                 NAME       USER  ST                START_TIME       TIME_LEFT       CPUS  NODES     NODELIST(REASON)
589        jawdatgrp     Refine3D/job015/   adtaheri   R       2023-01-31T22:51:59         9:58:38          6      1             gpu-9-18
627              low      Class2D/job424/   mashaduz   R       2023-02-02T12:06:27        11:13:06         60      1             gpu-9-58
```

Try `man squeue` or [visit the official docs](https://slurm.schedmd.com/squeue.html) for more options.
 

## Canceling jobs: `scancel`

To kill a job before it has completed, use the scancel command:

```console
$ scancel JOBID # (1)!
```

1. Replace `JOBID` with the ID of your job, which can be obtained with [`squeue`](jobs.md#listing-jobs-squeue).

You can cancel many jobs at a time; for example, you could cancel all of your running jobs with:

``` {.console .copy}
$ scancel -u $USER #(1)!
```

1. `$USER` is an environment variable containing *your username*, so leave this as is to use it.

Try `man scancel` or [visit the official docs](https://slurm.schedmd.com/scancel.html) for more options.

## Job and Cluster Information:  `scontrol`

`scontrol show` can be used to display any information known to Slurm.
For users, the most useful are the detailed job and node information.

To display details for a job, run:

```console
$ scontrol show j 635
JobId=635 JobName=jobscript.sh
   UserId=camw(1134153) GroupId=camw(1134153) MCS_label=N/A
   Priority=6563 Nice=0 Account=admin QOS=adminmed
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=1 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
   RunTime=00:00:24 TimeLimit=01:00:00 TimeMin=N/A
   SubmitTime=2023-02-02T13:26:24 EligibleTime=2023-02-02T13:26:24
   AccrueTime=2023-02-02T13:26:24
   StartTime=2023-02-02T13:26:25 EndTime=2023-02-02T14:26:25 Deadline=N/A
   PreemptEligibleTime=2023-02-02T13:26:25 PreemptTime=None
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2023-02-02T13:26:25 Scheduler=Main
   Partition=low AllocNode:Sid=nas-8-0:449140
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=c-8-42
   BatchHost=c-8-42
   NumNodes=1 NumCPUs=2 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   TRES=cpu=2,mem=100M,node=1,billing=2
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=1 MinMemoryNode=100M MinTmpDiskNode=0
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=/home/camw/jobscript.sh
   WorkDir=/home/camw
   StdErr=/home/camw/slurm-635.out
   StdIn=/dev/null
   StdOut=/home/camw/slurm-635.out
   Power=
```

Where `635` should be replaced with the ID for your job.
For example, you can see that this job was allocated resources on `c-8-42` (`NodeList=c-8-42`),
that its priority score is 6563 (`Priority=6563`), and that the script it ran with is located at `/home/camw/jobscript.sh`.

We can also get details on nodes. Let's interrogate `c-8-42`:

```console
$ scontrol show n c-8-42
NodeName=c-8-42 Arch=x86_64 CoresPerSocket=64 
   CPUAlloc=4 CPUEfctv=256 CPUTot=256 CPULoad=0.12
   AvailableFeatures=amd,cpu
   ActiveFeatures=amd,cpu
   Gres=(null)
   NodeAddr=c-8-42 NodeHostName=c-8-42 Version=22.05.6
   OS=Linux 5.15.0-56-generic #62-Ubuntu SMP Tue Nov 22 19:54:14 UTC 2022 
   RealMemory=1000000 AllocMem=200 FreeMem=98124 Sockets=2 Boards=1
   State=MIXED ThreadsPerCore=2 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=low,high 
   BootTime=2022-12-11T02:25:44 SlurmdStartTime=2022-12-14T10:34:25
   LastBusyTime=2023-02-02T13:13:22
   CfgTRES=cpu=256,mem=1000000M,billing=256
   AllocTRES=cpu=4,mem=200M
   CapWatts=n/a
   CurrentWatts=0 AveWatts=0
   ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
```

`CPUAlloc=4` tells us that 4 cores are currently allocated on the node.
`AllocMem=200` indicates that 200MiB of RAM are currently allocated, with
`RealMemory=1000000` telling us that there is 1TiB of RAM total on the node.

## Node Status: `sinfo`

Another useful status command is `sinfo`, which is specialized for displaying information on nodes and partitions.
Running it without any arguments gives information on partitions:

```console
$ sinfo
PARTITION     AVAIL  TIMELIMIT  NODES  STATE NODELIST
low*             up   12:00:00      3    mix gpu-9-[10,18,58]
low*             up   12:00:00      8   idle c-8-[42,50,58,62,70,74],gpu-9-[26,66]
high             up 60-00:00:0      6   idle c-8-[42,50,58,62,70,74]
jawdatgrp-gpu    up   infinite      2    mix gpu-9-[10,18]
jawdatgrp-gpu    up   infinite      1   idle gpu-9-26
```

In this case, we can see that there are 3 partially-allocated nodes in the `low` partition (they have state `mix`),
and that the time limit for jobs on the `low` partition is 12 hours.

Passing the `-N` flag tells `sinfo` to display node-centric information:

```console
$ sinfo -N
NODELIST   NODES     PARTITION STATE 
c-8-42         1          low* idle  
c-8-42         1          high idle  
c-8-50         1          low* idle  
c-8-50         1          high idle  
c-8-58         1          low* idle  
c-8-58         1          high idle  
c-8-62         1          low* idle  
c-8-62         1          high idle  
c-8-70         1          low* idle  
c-8-70         1          high idle  
c-8-74         1          low* idle  
c-8-74         1          high idle  
gpu-9-10       1          low* mix   
gpu-9-10       1 jawdatgrp-gpu mix   
gpu-9-18       1          low* mix   
gpu-9-18       1 jawdatgrp-gpu mix   
gpu-9-26       1          low* idle  
gpu-9-26       1 jawdatgrp-gpu idle  
gpu-9-58       1          low* mix   
gpu-9-66       1          low* idle
```

There is an entry for each node in each of its partitions. `c-8-42` is in both the `low` and `high` partitions, while `gpu-9-10` is in the `low` and `jawdatgrp-gpu` partitions.

More verbose information can be obtained by also passing the `-l` or `--long` flag:

```console
$ sinfo -N -l
Thu Feb 02 14:04:48 2023
NODELIST   NODES     PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON              
c-8-42         1          low*        idle 256    2:64:2 100000        0      1  amd,cpu none                
c-8-42         1          high        idle 256    2:64:2 100000        0      1  amd,cpu none                
c-8-50         1          low*        idle 256    2:64:2 100000        0      1  amd,cpu none                
c-8-50         1          high        idle 256    2:64:2 100000        0      1  amd,cpu none                
c-8-58         1          low*        idle 256    2:64:2 100000        0      1  amd,cpu none
...
```

This view gives the nodes' socket, core, and thread configurations, their RAM, and the feature list, which you can read about in the [**Resources**](resources.md#features) section. Try `man scontrol` or `man sinfo`, or visit the official docs
for [`scontrol`](https://slurm.schedmd.com/scontrol.html) and [`sinfo`](https://slurm.schedmd.com/sinfo.html), for more options.