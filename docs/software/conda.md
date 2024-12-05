# :simple-python: :simple-anaconda: Conda and Python



HPCCF clusters have a centrally installed [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html).
__conda is our preferred and supported method for Python environments; we prefer not to centrally install any Python libraries__.
Our conda install can also be levered by users to install arbitrary software available in conda repos in their home directories without
needing to wait for systems administrators; many users may find this preferable, as our software install backlog
is substantial.


To help with troubleshooting and compatibility, we __do not__ provide support for conda installations in user home directories;
instead, users should load our central conda with `module load conda`, which will automatically perform the initialization
usually done by `conda init`.

```console
$ module load conda
Loading conda/base/latest
```

This will activate the `base` environment automatically.

More specifically, the central install is a [miniforge](https://github.com/conda-forge/miniforge) installation, which means that most `conda` commands can be replaced with `mamba` commands for a performance increase.

## Creating Conda Environments

You can create environments in your home directory using the central conda install in the same manner as any other conda installation:

```console
$ conda create -n datasci pandas seaborn ipython
Retrieving notices: ...working... done
Channels:
 - conda-forge
 - bioconda
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/camw/.conda/envs/datasci

  added / updated specs:
    - ipython
    - pandas
    - seaborn

...

Preparing transaction: done                                                                                                                       
Verifying transaction: done                                                                                                                       
Executing transaction: done                                                                                                                       
#                                                                                                                                                 
# To activate this environment, use                                                                                                               
#                                                                                                                                                 
#     $ conda activate datasci                                                                                                                    
#                                                                                                                                                 
# To deactivate an active environment, use                                                                                                        
#                                                                                                                                                 
#     $ conda deactivate   
```

The environment will be created in your home directory (alongside any other environments you may have created from a previous conda installation in your home directory -- you do not need to recreate your conda environments!).

!!! Note
    Due to a bug in `mamba`, you will get some strange errors or warnings when you use the `mamba` command to create environments or install packages:

    ```console
    $ mamba create -n datasci2 pandas

    Looking for: ['pandas']

    error    libmamba Could not open lockfile '/share/apps/conda/pkgs/cache/cache.lock'
    warning  libmamba Cache file "/share/apps/conda/pkgs/cache/497deca9.json" was modified by another program
    warning  libmamba Cache file "/home/camw/.conda/pkgs/cache/497deca9.json" was modified by another program
    error    libmamba Could not open lockfile '/share/apps/conda/pkgs/cache/cache.lock'
    warning  libmamba Cache file "/share/apps/conda/pkgs/cache/09cdf8bf.json" was modified by another program
    warning  libmamba Cache file "/home/camw/.conda/pkgs/cache/09cdf8bf.json" was modified by another program
    ```

    __These can be safely ignored.__


## Central Conda Environments

We provide a number of centrally managed conda environments, which can be loaded via modules prefixed with `conda/`: for example,
on farm:

```console
$ module avail conda      
------------------------------------------------------ /share/apps/22.04/modulefiles/manual ------------------------------------------------------
conda/angsd/0.940        conda/CRISPR-Local/4564b0c  conda/latest                   conda/pixy/1.2.7.beta1    conda/spyder/5.4.3       
conda/anvio/8            conda/ddocent/2.9.4         conda/megahit/1.2.9            conda/plink/1.90b6.21     conda/stereopy/0.12.1    
conda/apptainer/1.2.2    conda/dev/latest            conda/metabat/2.15             conda/prokka/1.14.6       conda/tensorqtl/1.0.8    
conda/augustus/3.5.0     conda/diploshic/1.0.4       conda/msprime/1.2.0            conda/pyani/0.2.7         conda/testing/latest     
conda/avocado/0.4.0      conda/fastenloc/2.0         conda/nanoporetech-pod5/0.2.4  conda/qiime2/2023.2       conda/vcflib/1.0.3       
conda/base/              conda/fgbio/2.1.0           conda/pacbio/1                 conda/qiime2/2023.5       conda/virsorter/2.2.4    
conda/base/latest        conda/foldseek/6.29e2557    conda/pandas/2.1.4             conda/r-stitch/1.6.8      conda/websockify/0.11.0  
conda/cactus/2019.03.01  conda/gtdbtk/2.4.0          conda/pcangsd/1.11             conda/repeatmasker/4.1.5  conda/whatshap/1.7       
conda/cas-offinder/2.4   conda/hifiasm/0.19.5        conda/phydrus/0.2.0            conda/rnabloom/2.0.1      
conda/cesm/2.1.3         conda/hpccf-utils/default   conda/phyluce/1.7.1            conda/shapeit/5.1.1       
conda/collections/bio    conda/idba/1.1.3.kMax600    conda/phyluce/1.7.3            conda/shapeit4/4.2.2      
conda/coverm/0.6.1       conda/jupyterlab/4          conda/picrust2/2.5.2           conda/singlem/0.18.0
```

Running `module load conda/qiime2/2023.5` is the same as running `module load conda` followed by `conda activate qiime2-2023.5`.
The central conda environments also show up with a `conda list`:

```console
$ conda env list
# conda environments:
#
...
base                     /share/apps/conda/conda-root
CRISPR-Local-4564b0c     /share/apps/conda/environments/CRISPR-Local-4564b0c
alphafold-2.3.2          /share/apps/conda/environments/alphafold-2.3.2
angsd-0.940              /share/apps/conda/environments/angsd-0.940
anvio-8                  /share/apps/conda/environments/anvio-8
apptainer-1.2.2          /share/apps/conda/environments/apptainer-1.2.2
augustus-3.5.0           /share/apps/conda/environments/augustus-3.5.0
avocado-0.4.0            /share/apps/conda/environments/avocado-0.4.0
cactus-2019-3-1          /share/apps/conda/environments/cactus-2019-3-1
cas-offinder-2.4         /share/apps/conda/environments/cas-offinder-2.4
cesm-2.1.3               /share/apps/conda/environments/cesm-2.1.3
cheeto                   /share/apps/conda/environments/cheeto
coverm-0.6.1             /share/apps/conda/environments/coverm-0.6.1
...
```

Unloading the `conda` module also deactivates all conda environments.

## Migrating from User-installed Conda

If you have installed conda in your home directory already, you will get an error when you try to load
the conda module. This is necessary because user-installed condas set environment variables that clash
with the central install.
In order to migrate, you will need to remove the initialization code that the conda installer adds to your shell
configuration. This code will most likely be in either `~/.bashrc` or `~/.bash_profile`, and will look something like:

```bash
__conda_setup="$('/home/camille/miniconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/camille/miniconda/etc/profile.d/conda.sh" ]; then
        . "/home/camille/miniconda/etc/profile.d/conda.sh"
    else
        export PATH="/home/camille/miniconda/bin:$PATH"
    fi
fi
unset __conda_setup
```

Delete this block, and log out and back in to the cluster, after which you should be able to `module load conda`.
If you run into problems with migrating, file a support ticket at [hpc-help@ucdavis.edu](mailto:hpc-help@ucdavis.edu?subject=Migrating%20to%20Central%20Conda), being sure to specify which cluster you are using.