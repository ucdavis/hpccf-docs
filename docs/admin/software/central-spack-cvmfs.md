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

At the highest level, our system consists of:

- A build machine, at `build.hpc.ucdavis.edu`, on which we concretize and build our Spack environments, as well as solve and install Conda environments (the latter of which is outside the scope of this document).
- A Statum 0 CVMFS server, at `software.hpc.ucdavis.edu`. This is the machine that processes CVMFS transactions and serves the root of our CVMFS deployment; we use `rsync` to pull the build artifacts from `build.hpc` to the CVMFS volume here. Some of our clusters point at this directly, while others point at its replicas.
- Replica (Stratum 1) CVMFS servers, which are hosted on per-cluster infrastructure. These servers replicate the Stratum 0 server, and help distribute load.
- CVMFS clients, which are basically every node we maintained. The CVMFS deployment on the clients (and servers) is read-only and mounted at `/cvmfs/hpc.ucdavis.edu`.

