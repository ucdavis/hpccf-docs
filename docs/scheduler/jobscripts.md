#Slurm job Example

Open an editor and log these code in the file:
nano Test-Job.sh
Note - The # sign is required on the start of Slurm options:

`#!/bin/bash -l`

`#SBATCH -J Test-Job`
`#SBATCH --ntasks-per-node=1`
`#SBATCH --cpus-per-task=5`
`#SBATCH --time=02:00:00`
`#SBATCH --mem=32GB`
`#SBATCH --partition=med`
`#SBATCH --mail-user= youruserid@ucdavis.edu`
`#SBATCH --mail-type=END`
`#SBATCH --mail-type=FAIL`
`#SBATCH -o Test-Job-%j.output`
`#SBATCH -e Test-Job-%j.err`

`module load <module/version>`
`<code to process>`


After saving and closing that file, run it using srun or sbatch like this

`srun --partition=med --mem=32G --nodes=4 --time=02:00:00 Test-Job.sh`

OR like this:

`sbatch Test-Job.sh`
