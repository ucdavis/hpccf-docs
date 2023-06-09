---
title: Module System
summary: An overview of the software module system and how to use it.
---

# Module System

## Intro

High performance compute clusters usually have a variety of software with sometimes conflicting
dependencies.
Software packages may need to make modifications to the [user environment](../general/environment.md), or the same
software may be compiled multiple times to run efficiently on differing hardware within the cluster.
To support these use cases, software is managed with a module system that prepares the user
environment to access specific software on load and returns the environment to its former state when
unloaded.
A _module_ is the bit of code that enacts and tracks these changes to the user environment, and the
module _system_ is software that runs these modules and the collection of modules it is aware of.
Most often, a module is associated with a specific software package at a specific version, but they
can also be used to make more general changes to a user environment; for example, a module could
load a set of configurations for the [BASH](https://www.gnu.org/software/bash/) shell that set color themes.

The two most commonly deployed module systems are [environment
modules](https://modules.readthedocs.io/en/latest/) (or `envmod`) and
[lmod](https://lmod.readthedocs.io/en/latest/index.html).
Franklin currently uses `lmod`, which is cross-compatible with `envmod`.

## Usage

The `module` command is the entry point for users to manage modules in their environment.
All module operations will be of the form `module [SUBCOMMAND]`. Usage information is available
on the cluster by running `module --help`.

The basic commands are: `module load [MODULENAME]` to load a module into your environment; `module unload [MODULENAME]` to remove that module; `module avail` to see modules available for loading; and `module list` to see which modules are currently loaded.
We will go over these commands, and some additional commands, in the following sections.

### Listing

#### `module avail`

Lists the modules **currently available** to load on the system. Some example output would be:

``` console
$ module avail

----------------------- /share/apps/franklin/modulefiles ------------------------
   conda/base/4.X                conda/cryolo/1.8.4-cuda-11 (D)    testmod/1.0
   conda/cryolo/1.8.4-cuda-10    conda/rockstar/0.1

---------------------- /share/apps/spack/modulefiles/Core -----------------------
...
   gatk/3.8.1                         pmix/4.1.2             (L)
   gatk/4.2.6.1              (D)      prokka/1.14.6
   gcc/4.9.4                 (L)      raxml-ng/1.0.2
   gcc/5.5.0                          ray/2.3.1
   gcc/7.5.0                 (D)      recon/1.05
   gctf/1.06                 (L)      relion-helper/0.1
   genrich/0.6                        relion-helper/0.2      (L,D)
...
```

Each entry corresponds to software available for [load](modules.md#loading-and-unloading).
Different sections will appear depending on loaded prerequisites, which you can read about under [`module spider`](modules.md#module-spider).
Where there are multiple versions or variants of a module, a `(D)` will be listed next to the name of the default version.
An `(L)` indicates that module is currently loaded.

Note that this does not necessarily list every possible module on the system.
Some software is compiled with a specific compiler and compiler version, and the relevant compiler
module must be loaded first.
To see all **possible** modules, use the [`module spider`](modules.md#module-spider) command.

#### `module spider`

Lists **all possible** modules that could be loaded. Some modules require a specific
compiler version to be loaded, and these modules will not be listed in `module avail`
unless that module is loaded. Module spider will list these modules anyway.
If you run the command with a specific module, it will list the prerequisite modules
required to make said module available. For example, if we try to run:

``` console
$ module load megahit

Lmod has detected the following error:  These module(s) or extension(s) exist but cannot be loaded as requested: "megahit"
   Try: "module spider megahit" to see how to load the module(s).
```

...the load fails. If we then use `spider`:

```console hl_lines="7 8 9"
$ module spider megahit

-----------------------------------------------------------------------------
  megahit: megahit/1.1.4
-----------------------------------------------------------------------------

    You will need to load all module(s) on any one of the lines below before
    the "megahit/1.1.4" module is available to load.

      gcc/4.9.4
 
    Help:
      MEGAHIT: An ultra-fast single-node solution for large and complex
      metagenomics assembly via succinct de Bruijn graph
```

...we see that we have to first load `gcc/4.9.4`. Let's do that:

``` console
$ module load gcc/4.9.4
gcc/4.9.4: loaded.

$ module avail

-------------------- /share/apps/spack/modulefiles/gcc/4.9.4 --------------------
   megahit/1.1.4

----------------------- /share/apps/franklin/modulefiles ------------------------
   conda/base/4.X                conda/cryolo/1.8.4-cuda-11 (D)
   conda/cryolo/1.8.4-cuda-10    conda/rockstar/0.1

---------------------- /share/apps/spack/modulefiles/Core -----------------------
   StdEnv                    (L)    libevent/2.1.12        (L)
   abyss/2.3.1                      mash/2.3
```

We are now presented with a new section for those modules that require `gcc/4.9.4`,
with the `megahit` module listed there. Now, we can load it:

```console
$ module load megahit

megahit/1.1.4: loaded.
```

Running `module spider` without any arguments will list all the modules that could be loaded,
unlike `module avail`, which will list only the modules available for load given any currently-loaded
prerequisites.

#### `module list`

Lists the modules **currently loaded** in the user environment. By default, the output should be
similar to:

```console
$ module list

Currently Loaded Modules:
  1) cuda/11.8.0   3) libevent/2.1.12   5) slurm/22-05-6-1   7) openmpi/4.1.4
  2) hwloc/2.8.0   4) pmix/4.1.2        6) ucx/1.13.1
```

Additional modules will be added or removed as you load and unload them.

#### `module overview`

This will give a **condensed overview** of available modules.
It is most useful when the list of modules is very large, and there are multiple versions of each
module available.
The output is a list of each module name followed by the number of versions of the module.

```console
$ module overview

----------------------- /share/apps/franklin/modulefiles ------------------------
conda/base (1)   conda/cryolo (2)   conda/rockstar (1)   testmod (1)

---------------------- /share/apps/spack/modulefiles/Core -----------------------
StdEnv         (1)   hmmer            (1)   ncbi-toolkit  (1)
abyss          (1)   homer            (1)   ncbi-vdb      (1)
amdfftw        (1)   hwloc            (1)   nextflow      (1)
aragorn        (1)   igv              (1)   openmpi       (1)
bedtools2      (1)   infernal         (1)   orthofinder   (1)
blast-plus     (1)   intel-oneapi-mkl (1)   orthomcl      (1)
blast2go       (1)   interproscan     (1)   parallel      (1)
blat           (1)   iq-tree          (1)   patchelf      (1)
```

### Loading and Unloading

#### `module load`

This **loads** the requested module into the active environment.
Loading a module can edit environment variables, such as prepending directories to `$PATH` so that
the executables within can be run, set and unset new or existing environment variables, define shell functions,
and generally, modify your user environment arbitrarily.
The modifications it makes are tracked, so that when the module is eventually unloaded, any changes can be returned
to their former state.

Let's load a module.

```console
$ module load bwa/0.7.17
bwa/0.7.17: loaded.
```

Now, you have access to the `bwa` executable. If you try to run `bwa mem`, you'll get its help output.
This also sets the appopriate variables so that you can now run `man bwa` to view its manpage.

Note that some modules have multiple versions. Running `module load [MODULENAME]` without specifying a version
will load the latest version, unless a default has been specified.
When there are multiple versions, a `(D)` will be printed next to the default version when using [`module avail`](modules.md#module-avail).

Some modules are nested under a deeper hierarchy. For example, `relion` has six variants, two under `relion/cpu` and four under `relion/gpu`.
To load these, you must specify the second layer of hierarchy: `module load relion` will fail, but `module load relion/cpu` will load the default module under `relion/cpu`, which has the full name `relion/cpu/4.0.0+amd`.
More information on this system can be found under [Organization](modules.md#organization).

The modules on Franklin are all configured to set a `$NAME_ROOT` variable that points to the installation prefix.
This will correspond to the name of the module, minus the version. For example:

```console
$  ls -R $BWA_ROOT
/share/apps/spack/spack-v0.19/opt/spack/linux-ubuntu22.04-x86_64_v3/gcc-9.5.0/bwa-0.7.17-3ogkbh2ixha52dxps2letankhc2dbeax:
bin  doc  man

...
```

Usually, this will be a very long pathname, as most software on the cluster is managed via the
[spack](https://spack.readthedocs.io/en/latest/) build system.
This would be most useful if you're [developing software](developing.md) on the cluster.

## Organization

Many modules correspond to different versions of the same software, and some software has multiple variants of the same version.
The default naming convention is `NAME/VERSION`: for example, `cuda/11.8.0` or `mcl/14-137`.
The version can be omitted when loading, in which case the highest-versioned module or the version marked as default (with a `(D)`) will be used.

### Variants

Some module names are structured as `NAME/VARIANT/VERSION`.
For these, the minimum name you can use for loading is `NAME/VARIANT`: for example, you can load `relion/gpu` or `relion/cpu`, but just trying to `module load relion` will fail.

### Architectures

Software is sometimes compiled with optimizations specific to certain hardware.
These are named with the format `NAME/VERSION+ARCH` or `NAME/VARIANT/VERSION+arch`.
For example, `ctffind/4.1.14+amd` was compiled with AMD Zen2-specific optimizations and uses the [`amdfftw`](https://github.com/amd/amd-fftw) implementation of the [`FFTW`](https://www.fftw.org/) library, and will fail on the Intel-based RTX2080 nodes purchased by the Al-Bassam lab (`gpu-9-[10,18,26]`).
Conversely, `ctffind/4.1.14+intel` was compiled with Intel-specific compiler optimizations as well as linking against the [Intel OneAPI MKL](https://www.intel.com/content/www/us/en/develop/documentation/oneapi-programming-guide/top/api-based-programming/intel-oneapi-math-kernel-library-onemkl.html) implementation of `FFTW`, and is only meant to be used on those nodes.
In all cases, the `+amd` variant of a module, if it exists, is the default, as the majority of the nodes use AMD CPUs.

Software without a `+ARCH` was compiled for a generic architecture and will function on all nodes.
The generic architecture on Franklin is [`x86-64-v3`](https://lists.llvm.org/pipermail/llvm-dev/2020-July/143289.html), which means they support `AVX`, `AVX2`, and all other previous `SSE` and other vectorized instructions.

### Conda Environments

The various conda modules have their own naming scheme.
These are of the form `conda/ENVIRONMENT/VERSION`.
The `conda/base/VERSION` module(s) load the base conda environment and set the appropriate variables to use the `conda activate` and `deactivate` commands, while the the modules for the other environments first load `conda/base` and then activate the environment to which they correspond.
The the [`conda`](conda.md) section for more information on `conda` and Python on Franklin.
