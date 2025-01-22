# :simple-python: Open OnDemand

Some HPCCF clusters have a [Open OnDemand](https://openondemand.org/) (OOD). OOD allows browser access to specific resources running within a cluster. All OOD apps are launched through individual Slurm jobs, so you have access to the same resources you can access through the CLI over SSH.

## Clusters with Open OnDemand:

* [Farm](https://ondemand.farm.hpc.ucdavis.edu)
* [Franklin](https://ondemand.franklin.hpc.ucdavis.edu)
* [Hive](https://ondemand.hive.hpc.ucdavis.edu)

## Applications offered with Open OnDemand

* JupyterLab
* Desktop
* VSCode Server
* RStudio Server

## User OnDemand debugging

If your OOD jobs launches, but fails very quickly, please click the long, random `Session ID:`. From there, open the `output.log` file and carefully look over the output. 

### Incorrect Conda environment specified

Some OOD Apps allow you to specify a specific conda environment that will load. If you see a line like this in `output.log`, you have specified an invalid conda environment: 
```
EnvironmentNameNotFound: Could not find conda environment: r-4.3.3-typo
You can list all discoverable environments with `conda info --envs`.
```

### Out of Memory (OOM) events

If your Jupyter or RStudio jobs keep failing with errors `abnormally terminated due to an unexpected crash`, and, when your job finishes, you see a line like this in `output.log`, then you have not requested enough RAM:
```
slurmstepd: error: Detected 3 oom_kill events in StepId=20294700.batch. Some of the step tasks have been OOM Killed.
```

### Self installed conda or miniconda break RStudio Server

If you self-install conda, or miniconda, it will conflict with our centrally installed conda. If you see lines like this, then you need to remove that to use RStudio Server:
```
ERROR: CONDA_EXE is currently defined: /home/omen/conda/bin/conda.
This module will almost certainly interfere with your conda installation.
Remove existing conda installation and its shell hooks from your PATH before proceeding.
```
See [Migrating from User-installed Conda](../ondemand/#applications-offered-with-open-ondemand)