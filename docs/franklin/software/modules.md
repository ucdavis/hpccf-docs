Franklin currently uses `lmod`, which is cross-compatible with `envmod`. See our [`lmod` docuementation](../../software/modules.md) for more information on using the module system.


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


## Spack-managed Modules

These modules are built and managed by our Spack deployment.
Most were compiled for generic architecture, meaning they can run on any node,
but some are Intel or AMD specific, and some require GPU support.

{{ spack_modules_list() }}