# Requesting Resources


## Partitions

Each **node** -- physically distinct machines within the cluster -- will be a member of one or more
**partitions**. A partition consists of a collection of nodes, a policy for job scheduling on that
partition, a policy for conflicts when nodes are a member of more than one partition (ie.
preemption), and a policy for managing and restricting resources per user or per group referred to
as Quality of Service.
The Slurm documentation has detailed information on how [preemption](https://slurm.schedmd.com/preempt.html) and [QOS
definitions](https://slurm.schedmd.com/qos.html) are handled; our per-cluster _Resources_ sections
describe how partitions are organized and preemption handled on our clusters.

## Accounts

Users are granted access to resources via Slurm **associations**. An association links together a
**user** with an **account** and a QOS definition. **Accounts** most commonly correspond to your
lab, but sometimes exist for graduate groups, departments, or institutes.

To see your associations, and thus which accounts and partitions you have access to, you can use the
`sacctmgr` command:

``` console
$ sacctmgr show assoc user=$USER
   Cluster    Account       User  Partition     Share ...   MaxTRESMins                  QOS   Def QOS GrpTRESRunMin 
---------- ---------- ---------- ---------- --------- ... ------------- -------------------- --------- ------------- 
  franklin   hpccfgrp       camw mmgdept-g+         1 ...               hpccfgrp-mmgdept-gp+                         
  franklin   hpccfgrp       camw mmaldogrp+         1 ...               hpccfgrp-mmaldogrp-+                         
  franklin   hpccfgrp       camw cashjngrp+         1 ...               hpccfgrp-cashjngrp-+                         
  franklin   hpccfgrp       camw jalettsgr+         1 ...               hpccfgrp-jalettsgrp+                         
  franklin   hpccfgrp       camw jawdatgrp+         1 ...               hpccfgrp-jawdatgrp-+                         
  franklin   hpccfgrp       camw        low         1 ...                   hpccfgrp-low-qos                         
  franklin   hpccfgrp       camw       high         1 ...                  hpccfgrp-high-qos                         
  franklin  jawdatgrp       camw        low         1 ...                    mcbdept-low-qos                         
  franklin  jawdatgrp       camw jawdatgrp+         1 ...               jawdatgrp-jawdatgrp+                         
  franklin jalettsgrp       camw jalettsgr+         1 ...               jalettsgrp-jalettsg+                         
  franklin jalettsgrp       camw        low         1 ...                    mcbdept-low-qos                         
```

The output is very wide, so you may want to pipe it through `less` to make it more readable:

``` console
sacctmgr show assoc user=$USER | less -S
```

Or, perhaps preferably, output it in a more compact format:

``` console
$ sacctmgr show assoc user=$USER format="account%20,partition%20,qos%40"
             Account            Partition                                      QOS 
-------------------- -------------------- ---------------------------------------- 
            hpccfgrp          mmgdept-gpu                 hpccfgrp-mmgdept-gpu-qos 
            hpccfgrp        mmaldogrp-gpu               hpccfgrp-mmaldogrp-gpu-qos 
            hpccfgrp        cashjngrp-gpu               hpccfgrp-cashjngrp-gpu-qos 
            hpccfgrp       jalettsgrp-gpu              hpccfgrp-jalettsgrp-gpu-qos 
            hpccfgrp        jawdatgrp-gpu               hpccfgrp-jawdatgrp-gpu-qos 
            hpccfgrp                  low                         hpccfgrp-low-qos 
            hpccfgrp                 high                        hpccfgrp-high-qos 
           jawdatgrp                  low                          mcbdept-low-qos 
           jawdatgrp        jawdatgrp-gpu              jawdatgrp-jawdatgrp-gpu-qos 
          jalettsgrp       jalettsgrp-gpu            jalettsgrp-jalettsgrp-gpu-qos 
          jalettsgrp                  low                          mcbdept-low-qos 
```

In the above example, we can see that user `camw` has access to the `high` partition via an
association with `hpccfgrp` and the `jalettsgrp-gpu` partition via the `jalettsgrp` account.

## Resource Types

### CPUs / cores

CPUs are the central compute power behind your jobs.
Most scientific software supports multiprocessing (multiple instances of an executable with discrete memory resources,
possibly but not necessarily communicating with each other), multithreading (multiple paths, or threads, of execution
within a process on a node, sharing the same memory resources, but able to execute on different cores), or both.
This allows computation to scale with increased numbers of CPUs, allowing bigger datasets to be analysed.

Slurm's CPU management methods are complex and can quickly become confusing.
For the purposes of this documentation, we will provide a simplified explanation; those with advanced needs
should consult [the Slurm documentation](https://slurm.schedmd.com/cpu_management.html).

Slurm follows a distinction between its physical resources -- cluster nodes and CPUs or cores on a node -- and virtual
resources, or **tasks**, which specify how requested physical resources will be grouped and distributed.
By default, Slurm will minimize the number of nodes allocated to a job, and attempt to keep the job's CPU requests
localized within a node.
**Tasks** group together CPUs (or other resources): CPUs within a task will be kept together on the same node.
Different tasks may end up on different nodes, but Slurm will exhaust the CPUs on a given node before splitting tasks between
nodes unless specifically requested.

!!! note "A Complication: SMT / Hyperthreading"

    Slurm understands the distinction between physical and logical cores.
    Most modern CPUs support [Simultaneous Multithreading (SMT)](https://en.wikipedia.org/wiki/Simultaneous_multithreading),
    which allows multiple independent processes to run on a single
    physical core.
    Although each of these is not a *full fledged* core, they have independent hardware for certain operations, and can
    greatly improve scalability for some tasks.
    However, using an individual thread within a single core makes little sense, as it shares hardware with the other SMT threads
    on its core; so, Slurm will always keep these threads together.
    In practice, this means if you ask for an odd number of CPUs, your request will be rounded up so as not to split an SMT
    thread between different job allocations.

The primary parameters controlling these are:

- `--cpus-per-task/-c`: How many CPUs to request per task. The number of CPUs requested here will always be on the same node. By default, 1.
- `--ntasks/-n`: The number of tasks to request. By default, 1.
- `--nodes/-N`: The *minimum* number of nodes to request, by default, 1.

Let's explore some examples. The simple request would be to ask for 2 CPUs.
We will use `srun` to request resources and then immediately run the `nproc` command within the allocation
to report how many CPUs are available:

```slurm
$ srun -c 2 nproc 
srun: job 682 queued and waiting for resources
srun: job 682 has been allocated resources
2
```

We asked for 2 CPUs per task, and Slurm gave us 2 CPUs and 1 task.
What happens if we ask for 2 tasks instead of 2 CPUs?

```slurm
$ srun -n 2 nproc
srun: job 683 queued and waiting for resources
srun: job 683 has been allocated resources
1
1
```

This time, we were given 2 separate tasks, each of which got 1 CPU.
Each task ran its own instance of the `nproc` command, and so each reported `1`.
If we ask for more CPUs per task:

```slurm
$ srun -n 2 -c 2 nproc
srun: job 684 queued and waiting for resources
srun: job 684 has been allocated resources
2
2
```

We still asked for 2 tasks, but this time we requested 2 CPUs in each.
So, we got 2 instances of `nproc`, each reported `2` CPUs in their task.

!!! abstract "Summary"

    If you want to run multithreaded jobs, use `--cpus-per-task N_THREADS` and `-ntasks 1`.
    If you want a multiprocess job (or an MPI job), increase `-ntasks`.

??? info "The SMT Edge Case"

    If we use `-c 1` without specifying the number of tasks, we might be taken by surprise:

    ```slurm
    $ srun -c 1 nproc     
    srun: job 685 queued and waiting for resources
    srun: job 685 has been allocated resources
    1
    1
    ```

    We only asked for 1 CPU per task, but we got 2 tasks! This is due to SMT, described in the note above.
    Because Slurm will not split SMT threads, and there are 2 SMT threads per physical core, the request
    was rounded up to 2 CPUs total.
    In order to keep with the 1 CPU-per-task constraint, it spawned 2 tasks. Similarly, if we specify
    that we only want 1 task, CPUs per task will instead be bumped:

    ```slurm
    $ srun -c 1 -n 1 nproc
    srun: job 686 queued and waiting for resources
    srun: job 686 has been allocated resources
    2
    ```

### Nodes

Let's explore multiple nodes a bit further.
We have seen previously that the `-n/ntasks` parameter will allocate discrete groups of cores.
In our prior examples, however, we used small resource requests.
What happens when we want to distribute jobs across nodes?

Slurm uses the [block distribution](https://slurm.schedmd.com/sbatch.html#OPT_block) method by default to distribute
tasks between nodes.
It will exhaust all the CPUs on a node with task groups before moving to a new node.
For these examples, we're going to create a script that reports both the hostname (ie, the node) and the number
of CPUs:

``` { .bash .copy title="<code>host-nprocs.sh</code>" }
#!/bin/bash

echo `hostname`: `nproc`
```

And make it executable with `#!bash chmod +x host-nprocs.sh`. 

Now let's make a multiple-task request:

```console
$ srun -c 2 -n 2 ./host-nprocs.sh
srun: job 691 queued and waiting for resources
srun: job 691 has been allocated resources
c-8-42: 2
c-8-42: 2
```

As before, we asked for 2 tasks and 2 CPUs per task.
Both tasks were assigned to `c-8-42`, because it had enough CPUs to fulfill the request.
What if it did not?

```console
$ srun -c 120 -n 3 ./host-nprocs.sh
srun: job 692 queued and waiting for resources
srun: job 692 has been allocated resources
c-8-42: 120
c-8-42: 120
c-8-50: 120
```

This time, we asked for 3 tasks each with 120 CPUs.
The first two tasks were able to be fulfilled by the node `c-8-42`, but that node did not have enough
CPUs to allocate another 120 on top of that.
So, the third task was distributed to `c-8-50`.
Thus, this task spanned multiple nodes.

Sometimes, we want to make sure each task has its own node.
We can achieve this with the `--nodes/-N` parameter.
This specifies the *minimum number of nodes* the tasks should be allocated across.
If we rerun the above example:

```console
$ srun -c 120 -n 3 -N 3 ./host-nprocs.sh
srun: job 693 queued and waiting for resources
srun: job 693 has been allocated resources
c-8-42: 120
c-8-50: 120
c-8-58: 120
```

We still asked for 3 tasks and 3 CPUs per task, but this time we specified we wanted a minimum of 3 nodes.
As a result, we were allocated portions of `c-8-42`, `c-8-50`, and `c-8-58`.

### RAM / Memory

Random Access Memory (RAM) is the fast, volatile storage that your programs use to store data during execution.
This can be contrasted with disk storage, which is non-volatile and many orders of magnitude slower to access,
and is used for long term data -- say, your sequencing runs or cryo-EM images.
RAM is a limited resource on each node, so Slurm enforces memory limits for jobs using [cgroups](https://en.wikipedia.org/wiki/Cgroups).
If a job step consumes more RAM than requested, the step will be killed.

Some (mutually exclusive) parameters for requesting RAM are:

- `--mem`: The memory required *per-node*. Usually, you want to use `--mem-per-cpu`.
- `--mem-per-cpu`: The memory required *per CPU or core*. If you requested $N$ tasks, $C$ CPUs per task, and $M$ memory per CPU, your total memory usage will be $N * C * M$. Note that, if $N \gt 1$, you will have $N$ discrete $C * M$-sized chunks of RAM requested, possibly across different nodes.
- `--mem-per-gpu`: Memory required *per GPU*, which will scale with GPUs in the same way as `--mem-per-cpu` will with CPUs.

For all memory requests, units can be specified explicitly with the suffixes `[K|M|G|T]` for `[kilobytes|megabytes|gigabytes|terabytes]`,
with the default units being `M`/`megabytes`.
So, `--mem-per-cpu=500` will requested 500 megabytes of RAM per CPU, and `--mem-per-cpu=32G` will request 32 gigabytes
of RAM per CPU.

Here is an example of a task overrunning its memory allocation.
We will use the `stress-ng` program to allocate 8 gigabytes of RAM in a job that only requested 200 megabytes.

```console
$ srun -n 1 --cpus-per-task 2 --mem-per-cpu 200M stress-ng -m 1 --vm-bytes 8G --oomable         1 ↵
srun: job 706 queued and waiting for resources
srun: job 706 has been allocated resources
stress-ng: info:  [3037475] defaulting to a 86400 second (1 day, 0.00 secs) run per stressor
stress-ng: info:  [3037475] dispatching hogs: 1 vm
stress-ng: info:  [3037475] successful run completed in 2.23s
slurmstepd: error: Detected 1 oom-kill event(s) in StepId=706.0. Some of your processes may have been killed by the cgroup out-of-memory handler.
srun: error: c-8-42: task 0: Out Of Memory
srun: launch/slurm: _step_signal: Terminating StepId=706.0
```


### GPUs / GRES
#### Requesting GPU Resources (GRES / GPUs)

To use GPU-equipped nodes, you must request the GPU resource via Slurm’s Generic RESources (GRES) system. Below are guidelines and examples:

**Basic syntax**

Add the following option to your `sbatch` or `srun` command:

`--gres=gpu:<count>`

- `gpu` is the generic resource name.

- `<count>` is the number of GPUs you need (e.g. 1, 2, etc.).

Example:
`#SBATCH --gres=gpu:1
`
This requests 1 GPU on whichever node your job is scheduled.

You may also combine it with other resource flags, for example:

```console
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
```


#### Partition / QOS constraints

Some GPU nodes may only be available in certain partitions (e.g. `gpu-a100` on Hive, `gpul` on Farm cluster and `cnsdept-gpu` on Franklin cluster). Be sure to request the GPU-compatible partition, e.g.:

`#SBATCH --partition=gpul`


Your account or QOS may also impose limits on how many GPUs you are allowed to use concurrently. The cluster scheduler enforces those limits.

You can check your associations via:


 `/opt/hpccf/bin/slurm-show-resources.py --full`


You can view the information about a GPU partition using the command:-

`scontrol show partition <partition-name>`


