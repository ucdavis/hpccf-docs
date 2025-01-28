---
template: admin.html
title: Central Spack and CVMFS
---

We maintain a centrally deployed software stack which is managed via [Spack](https://spack.readthedocs.io/en/latest/) and served to our clusters using [CernVM-FS (CVMFS)](https://cvmfs.readthedocs.io/en/stable/).
Our Spack environments declare a set of compilers, libraries, and software, for which Spack generates a directed acyclic graph (DAG) of dependency specifications (specs) and manages building them from source.
It then generates [environment modules](https://modules.readthedocs.io/en/latest/) for all explicitly declared (root) specs, which end-users use via the environment modules frontend to access software.

Deploying new software in this system requires a working knowledge of, at minimum:

- Spack package specifications, environments, and package definitions
- Environment modules and how Spack exposes software through them
- CVMFS transaction basics

Unfortunately, contrary to the opening line of the documentation, Spack is not simple.
The [Spack tutorial](https://spack-tutorial.readthedocs.io/en/latest/) offers an excellent introduction, and following it while referencing the [main documentation](https://spack.readthedocs.io/en/latest/) will serve you well.
Attempting to deploy software on this system without understanding these foundations will lead to [fear, anger, hate, and suffering](https://www.youtube.com/watch?v=kFnFr-DOPf8), and these are the path to the Dark Side of *unreproducible software environments*: once you begin manually downloading tarballs and `make install`ing them by hand, forever will they control your destiny!

The rest of this page will be dedicated to describing the design of our Spack deployment.
It will assume you have read over the documentation and have a basic understanding of Spack and its terminology.
If you have not, proceed at your own peril, padawan.

## High Level Achitecture

At the highest level, our system consists of a build machine, a root CVMFS server, replica CVMFS servers, and CVMFS clients.

### Build Machine

The build machine lives at `build.hpc.ucdavis.edu`, and we just refer to it as `build.hpc` or `build`.
This is a VM on which we concretize and build our Spack environments, as well as solve and install Conda environments (the latter of which is outside the scope of this document).
The Spack instances here live at the same location as on the CVMFS servers, `/cvmfs/hpc.ucdavis.edu`, but this machie is *not* a CVMFS server *or* client: rather, here `/cvmfs` is just a regular RW mount point.
This allows us to separate concerns -- *building* the software versus *deploying* it -- while also offering performance benefits, as IO on the `/cvmfs` volume on the server itself is constrained by the CVMFS [FUSE module](https://www.kernel.org/doc/html/next/filesystems/fuse.html).

### Root (Stratum 0) CVMFS Server

The Stratum 0 CVMFS server lives at `software.hpc.ucdavis.edu`, and we just call it `software.hpc`.
This is the machine that processes CVMFS transactions and serves the root of our CVMFS deployment; we use `rsync` to pull the build artifacts from `build.hpc` to the CVMFS volume here.
Some of our clusters point at this directly, while others point at its replicas.
We _do not_ build or install any software here!
The `/cvmfs` volume on this machine is the live FUSE filesystem which is only writeable when a CVMFS transaction has been started.

### Replica (Stratum 1) CVMFS Servers

These are hosted on per-cluster infrastructure.
These servers replicate the Stratum 0 server, and help distribute the load induced by the many clients.
As of January 2025, there are replica servers for Hive and Farm, while Peloton and Franklin are served directly from the Stratum 0.

### CVMFS Clients

Basically every node we maintain other than `build.hpc`.
The CVMFS deployment on the clients (and servers) is read-only and mounted at `/cvmfs/hpc.ucdavis.edu`.
The view of the clients is only that of the last transaction published.

## Spack Design

Now that we've briefly gone over the high level overview, we'll move into a detailed breakdown of our Spack deployment.
We note once again that this is non-trivial, and it is expected that you have read the documentation.

At a high level, our Spack deployment actually consists of two distinct Spack instances.
The first, which we name `core`, defines compilers, interpreters, and SDKs, as well the primary Slurm and messaging stack.
These packages are meant to remain stable outside of major maintenace windows.
The root specs built here are projected into an [environment view](https://spack.readthedocs.io/en/latest/environments.html#environment-views), but this environment does *NOT* build any user-loadable modules.
The second instance, which we call `main`, contains all the user-loadable software, _as well as_ the roots of the `core` environment, and generates the modulefiles for both environments.
All the roots built by `core` are defined as non-buildable [externals](https://spack.readthedocs.io/en/latest/packages_yaml.html#external-packages) in `main`, with their install prefixes set to the aforementioned environment view.

This two-layer system ensures that the `core` packages like compilers and Slurm will only exist _once_ in `main`, and further ensures that reconcretizing `main` will never cause those root specs from `core` to be reconcretized.
The only other way to enforce these constraints would be to use extremely specific `require` clauses with a **unified** concretization, which would often lead to environments that cannot be concretized at all.
Instead, we concretize our environments with the `unify` flag set `false`, which allows multiple architectures and variants of the same package to coexist within the same environment.

### Directory Organization

The Spack deployment root is at `/cvmfs/hpc.ucdavis.edu/sw/spack`.
A (slightly abridged) overview of this root directory is:

```console
$ tree -d -L 2 .
.
├── config -> spack-ucdavis/config/hpccf/software.hpc/
├── core
│   ├── bin
│   ├── linux-ubuntu22.04-x86_64_v3
│   ├── linux-ubuntu22.04-zen2
│   └── linux-ubuntu22.04-zen3
├── environments -> spack-ucdavis/environments/hpccf/software.hpc
├── main
│   ├── bin
│   ├── linux-ubuntu22.04-x86_64_v3
│   ├── linux-ubuntu22.04-zen2
│   └── linux-ubuntu22.04-zen3
├── manual-mirror
│   ├── cplex
│   ├── gaussian
│   ├── gctf
│   ├── genemark-et
│   ├── maker
│   ├── motioncor2
│   └── usearch
├── modulefiles
│   ├── main -> /cvmfs/hpc.ucdavis.edu/sw/spack/spack-ucdavis/modulefiles/hpccf/software.hpc/main
│   └── system -> /cvmfs/hpc.ucdavis.edu/sw/spack/spack-ucdavis/modulefiles/hpccf/software.hpc/system
├── repos
│   ├── builtin -> ../src/main/var/spack/repos/builtin/packages
│   ├── forked -> ../spack-ucdavis/repos/forked/packages
│   └── hpccf -> ../spack-ucdavis/repos/hpccf/packages/
├── spack-ucdavis
│   ├── bin
│   ├── config
│   ├── environments
│   ├── extensions
│   ├── modulefiles
│   ├── repos
│   └── templates
└── src
    ├── core
    └── main
```

The core configuration directory is `spack-ucdavis`, a git repository which can be found on our [GitHub](https://github.com/ucdavis/spack-ucdavis/tree/software.hpc).
The top-level `config`, `environments`, `modulefiles`, and `repos` point to subdirectories of this repo.
