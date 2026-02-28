# Apptainer

For running containers on HPC systems we offer and use Apptainer ( formerly Singularity ). Other container runtimes like Docker require users to have escalated system priveleges, and for most that's typically not an issue, but for shared multi-user systems letting any and all users have escalated privileges can pose a security risk. Luckily, apptainer allows users to run unprivileged containers in user-space including Docker containers and any OCI compatible containers.

## Quickstart

The quick and dirty way to get started on exploring and testing your software in an apptainer ASAP:

`srun -A adamgrp -p high -n 1 -c 8 --mem 32G --time 60:00 --pty bash -c "module load apptainer; apptainer shell docker://tensorflow/tensorflow"`

Feel free to curtail the srun parameters for your own needs.

## Singularity Image Format

A ".sif" is just a container image that you've already downloaded and stored locally and the result of commands like:

`apptainer build tflo.sif docker://tensorflow/tensorflow`

Mostly for if you want the image in a specific location, not really necessary. By default all apptainer images are stored in the apptainer cache located in: `~/.apptainer/cache`.

Or with: `apptainer cache --help`

## Running Apptainer Images

There are a few ways to interact with your apptainers. 

`apptainer shell tflo.sif` 
as seen in the quickstart section, this will open an interactive shell within the container allowing you to interact with the installed software manually as though it were a typical VM. 

`apptainer exec docker://tensorflow/tensorflow /path/to/script.sh` 
is non-interactive and will execute the commands you specify within the container and return the output. There's also: 

`apptainer run` 
is also non-interactive and similar to exec or for if you have provided runscripts.

You can learn more about these *[here](https://apptainer.org/docs/user/latest/quick_start.html#running-a-container)*.

## Definition Files

We won't be delving into def files in this tutorial but something you should absolutely know and consider can be found *[here](https://apptainer.org/docs/user/main/quick_start.html#apptainer-definition-files)*

## Bind Mounts

If you need, you can mount directories from your host machine into the container. We can use the `APPTAINER_BIND` environment variable in our apptainer definition files to specify what directories to mount in the container. Use a comma-delimited string of bind path specifications in the format `src[:dest[:opts]]`, where `src` and `dest` are paths outside and inside of the container respectively. If dest is not given, it is set equal to src. Mount options (opts) may be specified as `ro` (read-only) or `rw` (read/write, which is the default). For example, if you need to mount your group or lab directory in the container you can add this line to your definition file: 

`export APPTAINER_BIND=/mnt,/group/subdir:container/dir:rw`

If not using a definition file:

`apptainer shell --path /mnt,/group/subdir:container/dir:rw`

## GPUs

If you want to make use of Nvidia GPUs within your apptainer you can use the `--nv` flag with `apptainer (shell | exec) --nv ...`.

## Slurm Batch Jobs

Here's a basic script template, suitable for submitting with `sbatch`, that executes a command inside an apptainer:
    ```
      #!/bin/bash
   
      #SBATCH --account=<accountname>
      #SBATCH --partition=<partitionname>
      #SBATCH --ntasks=1
      #SBATCH --cpus-per-task=8
      #SBATCH --mem=32G
      #SBATCH --gpus=1
      #SBATCH --job-name=tflo
      #SBATCH --time=10:00
      
      # load module(s)
      module purge
      module load apptainer
      
      # specify what path(s) to bind inside the apptainer
      export $APPTAINER_BIND=$PWD

      # check for an apptainer(singularity) image (.sif) and build/pull one if it doesn't exist
      if [ ! -f tflo.sif ]; then
        apptainer build tflo.sif docker://tensorflow/tensorflow:latest-gpu
      fi

      apptainer exec --nv tflo.sif python3 -c "import tensorflow as tf; print('TensorFlow version:', tf.__version__)"
    ```
Feel free to modify this script for your purposes and to potentially run multiple commands and scripts within an apptainer.

## Slurm Interactive Jobs

This is an `srun` script that is the same as the above `sbatch` script but instead runs an interactive shell within an apptainer:

    ```
    #!/bin/bash -l
    
    srun \
      --account=<accountname> \
      --partition=<partitionname> \
      --ntasks=1 \
      --cpus-per-task=8 \
      --mem=32G \
      --gpus=1 \
      --job-name=tflo \
      --time=10:00 \
      --pty \
      apptainer shell --nv tflo.sif
    ```

## Script Wrapper

For ease of use we recommend writing a wrapper script like such:

  ```
    #!/bin/bash

    # load module(s)
    module purge
    module load apptainer
    
    # specify what path(s) to bind inside the apptainer
    export $APPTAINER_BIND=$PWD

    # check for an apptainer(singularity) image (.sif) and build/pull one if it doesn't exist
    if [ ! -f tflo.sif ]; then
      apptainer build tflo.sif docker://tensorflow/tensorflow:latest-gpu
    fi
    
    apptainer shell --nv tflo.sif $@ # "$@" for additional parameters that can be passed when executing this wrapper script that are passed to the apptainer
  ```
This wrapper starts a shell inside whatever apptainer you specify 
