---
title: Module System
summary: An overview of the software module system and how to use it.
---

# Module System

## Intro

High performance compute clusters usually have a variety of software with sometimes conflicting dependencies. Software
packages may need to make modifications to the [user environment](../general/environment.md), or the same software may
be compiled multiple times to run efficiently on differing hardware within the cluster. To support these use cases,
software is managed with a module system that prepares the user environment to access specific software on load and
returns the environment to its former state when unloaded. A _module_ is the bit of code that enacts and tracks these
changes to the user environment, and the module _system_ is software that runs these modules and the collection of
modules it is aware of. Most often, a module is associated with a specific software package at a specific version, but
they can also be used to make more general changes to a user environment; for example, a module could load a set of
configurations for the [BASH](https://www.gnu.org/software/bash/) shell that set color themes.

The two most commonly deployed module systems are [environment modules](https://modules.readthedocs.io/en/latest/) (or
`envmod`) and [lmod](https://lmod.readthedocs.io/en/latest/index.html). All HPC@UCD clusters currently use `envmod`.

## Usage

The `module` command is the entry point for users to manage modules in their environment. All module operations will be
of the form `module [SUBCOMMAND]`. Usage information is available on the cluster by running `module --help`.

The basic commands are: `module load [MODULENAME]` to load a module into your environment; `module unload [MODULENAME]`
to remove that module; `module avail` to see modules available for loading; and `module list` to see which modules are
currently loaded. We will go over these commands, and some additional commands, in the following sections.

### Listing

#### `module avail`

Lists the modules **currently available** to load on the system. The following is some example output from the Franklin
cluster:

```console
$ module avail
--------------------- /share/apps/22.04/modulefiles/spack/core ----------------------
aocc/4.1.0                 intel-oneapi-compilers/2023.2.1  pmix/4.2.6+amd
cuda/8.0.61                libevent/2.1.12                  pmix/4.2.6+intel
cuda/11.2.2                libevent/2.1.12+amd              pmix/default
cuda/11.7.1                libevent/2.1.12+intel            slurm/23-02-6-1
cuda/default               libevent/default                 slurm/23-02-7-1
environment-modules/5.2.0  openmpi/4.1.5                    ucx/1.14.1
gcc/7.5.0                  openmpi/4.1.5+amd                ucx/1.14.1+amd
gcc/11.4.0                 openmpi/4.1.5+intel              ucx/1.14.1+intel
gcc/13.2.0                 openmpi/default                  ucx/default
hwloc/2.9.1                pmix/4.2.6

------------------- /share/apps/22.04/modulefiles/spack/software --------------------
abyss/2.3.5           igv/2.12.3                        pplacer/1.1.alpha19
alphafold/2.3.2       infernal/1.1.4                    prodigal/2.6.3
amdfftw/4.1+amd       intel-oneapi-mkl/2023.2.0+intel   prokka/1.14.6
amdfftw/default       intel-oneapi-mkl/default          py-checkm-genome/1.2.1
angsd/0.935           intel-oneapi-tbb/2021.10.0+amd    py-cutadapt/4.4
aragorn/1.2.41        intel-oneapi-tbb/2021.10.0+intel  py-deeptools/3.5.2
aria2/1.36.0          intel-oneapi-tbb/default          py-htseq/2.0.3
...
```

Each entry corresponds to software available for [load](modules.md#loading-and-unloading). Modules that are currently
loaded will be highlighted.

#### `module list`

Lists the modules **currently loaded** in the user environment. By default, the output should be similar to:

```console
$ module list
Currently Loaded Modulefiles:
 1) slurm/23-02-7-1   2) ucx/1.14.1   3) openmpi/default

```

Additional modules will be added or removed as you load and unload them.

### Loading and Unloading

#### `module load`

This **loads** the requested module into the active environment. Loading a module can edit environment variables, such
as prepending directories to `$PATH` so that the executables within can be run, set and unset new or existing
environment variables, define shell functions, and generally, modify your user environment arbitrarily. The
modifications it makes are tracked, so that when the module is eventually unloaded, any changes can be returned to their
former state.

Let's load a module.

```console
$ module load bwa/0.7.17
bwa/0.7.17: loaded.
```

Now, you have access to the `bwa` executable. If you try to run `bwa mem`, you'll get its help output. This also sets
the appropriate variables so that you can now run `man bwa` to view its manpage.

Note that some modules have multiple versions. Running `module load [MODULENAME]` without specifying a version will load
the latest version, unless a default has been specified.

Some modules are nested under a deeper hierarchy. For example, `relion` on Franklin has many variants, under both
`relion/cpu` and `relion/gpu`. To load these, you must specify the second layer of the hierarchy: `module load relion`
will fail, but `module load relion/cpu` will load the default module under `relion/cpu`, which has the full name
`relion/cpu/4.0.0+amd`. More information on this system can be found under [Organization](modules.md#organization).

The modules are all configured to set a `$NAME_ROOT` variable that points to the installation prefix. This will
correspond to the name of the module, minus the version. For example:

```console
$ echo $BWA_ROOT
/share/apps/22.04/spack/opt/software/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/bwa-0.7.17-y22jt6d7qm63i2tohmu7gqeedxytadky
```

Usually, this will be a very long pathname, as most software on the cluster is managed via the
[spack](https://spack.readthedocs.io/en/latest/) build system. This would be most useful if you're
[developing software](developing.md) on the cluster.

#### `module unload`

As one might expect, `module unload` removes a loaded module from your environment. Any changes made by the module are
undone and your environment is restored to its state prior to loading the module.

### Searching and Metadata

#### `module whatis`

This command prints a description of the module, if such a description is available. For example:

```console
$ module whatis gsl
-------------------------------------------- /share/apps/22.04/modulefiles/spack/software --------------------------------------------
           gsl/2.7.1: The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers. It is free software under the GNU General Public License. The library provides a wide range of mathematical routines such as random number generators, special functions and least-squares fitting. There are over 1000 functions in total with an extensive test suite.
```

#### `module show`

`module show` will list all the changes a module would make to the environment.

```console
$ module show gcc/11.4.0
-------------------------------------------------------------------
/share/apps/22.04/modulefiles/spack/core/gcc/11.4.0:

module-whatis	{The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, and Go, as well as libraries for these languages.}
conflict	gcc
prepend-path	--delim : LD_LIBRARY_PATH /share/apps/22.04/spack/opt/core/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/gcc-11.4.0-evrz2iaatpna4lvzwh5sjujgfrlqprx5/lib64
...
setenv		CC /share/apps/22.04/spack/opt/core/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/gcc-11.4.0-evrz2iaatpna4lvzwh5sjujgfrlqprx5/bin/gcc
setenv		CXX /share/apps/22.04/spack/opt/core/linux-ubuntu22.04-x86_64_v3/gcc-11.4.0/gcc-11.4.0-evrz2iaatpna4lvzwh5sjujgfrlqprx5/bin/g++
...
```

This is particularly useful for developing with libraries where you might be interested in variables relevant to your
build system.

#### `module search`

The `module search` command allows you to search the names and whatis information for every module. The result will be a
list of matching modules and the highlighted matching search terms.
