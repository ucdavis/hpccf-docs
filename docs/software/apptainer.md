# Apptainer

Apptainer and other container runtimes have many uses; Mainly, but not limited to, isolated, portable, and reproducible software execution and development. For running containers on HPC systems we offer and use Apptainer ( formerly Singularity ). Other container runtimes like Docker require users to have escalated system priveleges, and for most thats typically not an issue, for shared multi-user systems letting any and all users have escalated privileges can pose a security risk. Luckily, apptainer allows users to run unprivileged containers in user-space inluding Docker containers and any OCI compatible containers.

## Module System

On HPC systems, we provide apptainer, as an environment module. Everytime you want to use apptainer you must first run: `module load apptainer`.

## Quickstart

For the absolute fastest way to get started on testing your software in an apptainer you can use something like this: `srun -A adamgrp -p high -n 1 -c 8 --mem 32G --time 30:00 --pty bash -c "module load apptainer; apptainer shell docker://tensorflow/tensorflow"`. But, you may need to curtail some srun parameters for your own needs.

## Pulling Apptainer Images

Container images are like filesystems containing an Operating System (OS) with the relevant preinstalled software that is then booted like a Virtual Machine (VM). We recommend downloading your container image(s) locally once before your slurm job by running: `apptainer build tflo.sif docker://tensorflow/tensorflow`. After, you should find the `tflo.sif` apptainer image in your current directory. You can run this image in any number of future containers, which is why you only need to do it once and shouldn't run it in every slurm job.

## Running Apptainer Images

There are a few ways to interact with your apptainer image. Using `apptainer shell tflo.sif` will open an interactive shell within the container allowing you to interact with the installed software directly as though it were a typical VM.Using `apptainer exec tflo.sif <command(s)>...` is non-interactive and will execute the commands you specify within the container and return the output. There's also `apptainer run` if you or your apptainer have provided runscripts which you can learn more about *[here](https://apptainer.org/docs/user/latest/quick_start.html#running-a-container)*.

These commands that run, or otherwise execute containers (shell, exec) can take an --nv option, which will setup the container’s environment to use an NVIDIA GPU and the basic CUDA libraries to run a CUDA enabled application.

## Bind Mounts

If you need, you can mount directories from your host machine into the container. We use the `APPTAINER_BIND` evironment variable to specify what directories to mount in the container. Use a comma-delimited string of bind path specifications in the format `src[:dest[:opts]]`, where `src` and `dest` are paths outside and inside of the container respectively. If dest is not given, it is set equal to src. Mount options (opts) may be specified as `ro` (read-only) or `rw` (read/write, which is the default). For example, if you need to mount your group or lab directory in the container you can: `export APPTAINER_BIND=/mnt,/group/subdir:container/dir:rw`.

## GPUs

If you want to make use of GPUs within your apptainer you can use the `--nv` flag with `apptainer (shell | exec) --nv ...`.

## Script Wrapper

For ease of use we recommend writing a wrapper script like such:

  ```
    #!/bin/bash

    module purge
    module load apptainer

    if [ ! -f tflo.sif ]; then
      apptainer build tflo.sif docker://tensorflow/tensorflow:latest-gpu
    fi
    
    export $APPTAINER_BIND 
    apptainer shell --nv tflo.sif $@
  ```

## SRUN

Feel free to use this srun script as a starting template for a slurm job:

    ```
    #!/bin/bash -l
    
    srun \
      --account hpccfgrp \
      --partition=gpuh \
      --ntasks=1 \
      --cpus-per-task=8 \
      --mem=32G \
      --gpus=1 \
      --job-name=tflo \
      --time=10:00 \
      --pty \
      tflo.sh $@
    ```

## SBATCH 

Or the same thing as previous but in a form suitable for submitting with sbatch:
    ```
    #!/bin/bash
    
    #SBATCH --partition=gpuh
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=8
    #SBATCH --mem=32G
    #SBATCH --gpus=1
    #SBATCH --job-name=tflo
    #SBATCH --time=10:00
    
    module purge
    module load apptainer
    
    apptainer exec tflo.sif python3 -c "import tensorflow as tf; print("TensorFlow version:", tf.__version__)"
    ```
