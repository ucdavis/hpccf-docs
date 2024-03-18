# Python and Conda

Farm and Peloton clusters have Python software available in Conda. Users can load it and use it by entering the following commands:

`module load conda`

`Python`


Many of the most up-to-date Python-based software packages may be found under the conda module. Load the module and see a complete and up-to-date list:

`module load conda`

`conda list`

You can install your required conda package using the following commands

`conda create -n [name of the environment] -c [name of the channels] [list of packages to install]`

`conda activate [name of environment]`

Note that you can leave off the -c bioconda, because the system-wide conda configuration already has the bioconda channel configured as well as conda-forge

You can also replace conda with mamba in the create phase, it will solve the environment much more quickly. When the environment is active, you can run the following command to see that it lives in your home directory:

`echo $CONDA_PREFIX`

If you can't find a piece of software on the cluster, you can request an installation for cluster-wide use. Contact the hpc-help@ucdavis.edu with the name of the cluster, your username, the name of the software, and a link 
to the software's website, documentation, or installation directions, if applicable.
