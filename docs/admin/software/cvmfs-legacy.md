---
template: admin.html
title: Software Deployment
---

!!! danger

    As of December 9th 2024, this document is out-of-date and **must not** be followed.

## Spack on cvmfs

### Prerequisites

- Access to `software.hpc.ucdavis.edu` as `software-user`.
- Basic understanding of Linux commands and Spack.

### Instructions

#### Connect to the Server

Log in to the server using SSH:

```bash
ssh software-user@software.hpc.ucdavis.edu
```

You must make your changes as `software-user`, not your own user.

#### Start a CVMFS Transaction

Initiate a transaction to enable read-write access:

```bash
cvmfs_server transaction hpc.ucdavis.edu
```

> **Note:** This command mounts `/cvmfs/hpc.ucdavis.edu` as read-write; prior to this, it will be read-only.

#### Load the Spack Module

Load the Spack module to set up the environment:

```bash
module load spack
```

This command moves you to the `/cvmfs/hpc.ucdavis.edu/sw/spack` directory, loads the Spack software, and activates the
`main` environment.

#### Modify the Spack Environment

The YAML files for the `main` environment live under `environments/main`:

```console
$ ls environments/main
cryoem.yaml  general.yaml  libs.yaml  spack.lock  spack.yaml  view
```

Do **not** edit `spack.yaml` directly. Instead:

- Add new libraries to `libs.yaml`.
- Add new software to `general.yaml`.

The format is `software @version +variant`. For example:

```yaml
- gromacs @2019.6 +cuda
```

Please include the version of the software. Available versions can be found at
[packages.spack.io](https://packages.spack.io). You can also use `spack info`:

```console
$ spack info gromacs
CMakePackage:   gromacs

Description:
    GROMACS is a molecular dynamics package primarily designed for
    simulations of proteins, lipids and nucleic acids. It was originally
    developed in the Biophysical Chemistry department of University of
    Groningen, and is now maintained by contributors in universities and
    research centers across the world. GROMACS is one of the fastest and
    most popular software packages available and can run on CPUs as well as
    GPUs. It is free, open source released under the GNU Lesser General
    Public License. Before the version 4.6, GROMACS was released under the
    GNU General Public License.

Homepage: https://www.gromacs.org

Preferred version:
    2024.1    https://ftp.gromacs.org/gromacs/gromacs-2024.1.tar.gz

Safe versions:
    main      [git] https://gitlab.com/gromacs/gromacs.git on branch main
    2024.1    https://ftp.gromacs.org/gromacs/gromacs-2024.1.tar.gz
    2024      https://ftp.gromacs.org/gromacs/gromacs-2024.tar.gz
    2023.4    https://ftp.gromacs.org/gromacs/gromacs-2023.4.tar.gz
    2023.3    https://ftp.gromacs.org/gromacs/gromacs-2023.3.tar.gz
...
Variants:
    build_system [cmake]                     cmake
        Build systems supported by the package
    build_type [Release]                     Debug, MinSizeRel, Profile, Reference, RelWithAssert, RelWithDebInfo,
                                             Release
        The build type to build
    cp2k [false]                             false, true
        CP2K QM/MM interface integration
    cuda [false]                             false, true
        Build with CUDA
    cycle_subcounters [false]                false, true
...
```

This lists the available versions _and_ variants for the package. It's important to take a look at these variants, as
there may be non-default variants that are needed depending on the user request.

#### Reconcretize the Environment

After making changes, reconcretize the environment:

```bash
spack concretize -j 60
```

This command will concretize only the new specifications you've added. If the concretization fails, you should probably
escalate.

#### Install the Software

If concretization is successful, proceed with the installation:

```bash
spack install -j 60 name-of-software
```

Specify the new software or pieces of software you have concretized in order to avoid needing to wait for other failed
builds to install. You do not need to specify their versions, as Spack will install the newly concretized versions
automatically. If the build fails, you may need to fork the package and make fixes, which is out of scope for this
guide. If it succeeds, proceed.

#### Generate Modulefiles

Ensure that the modulefiles are generated. This generally happens on its own, but on occasion needs to be kicked off
manually:

```bash
spack module tcl refresh name-of-software
```

#### Check the Software

You should do a cursory check that the software actually works. Usually the best way to do this is to just run
`name-of-software -h`. For example, for the software `fastani`:

```console
$ module load fastani/1.33
$ fastANI -h
-----------------
fastANI is a fast alignment-free implementation for computing whole-genome Average Nucleotide Identity (ANI) between genomes
-----------------
...
```

If it runs without errors, proceed to the next step. If not, it's probably time to escalate.

#### Commit Changes

Commit your changes to the spack-ucdavis repo. Move into it:

```bash
cd spack-ucdavis
```

Add your changes to the YAML file:

```bash
git add environments/hpccf/software.hpc/main/general.yaml
git add environments/hpccf/software.hpc/main/libs.yaml
```

Commit your changes with the following format:

```bash
git commit -m "[env:main] YOURNAME: added NEWPACKAGE"
```

Then commit the new concretized lockfile:

```bash
git add environments/hpccf/software.hpc/main/spack.lock
git commit -m "[lock] reconcretize main"
```

#### Prepare for Deployment

Perform necessary maintenance before deployment:

```bash
cd /cvmfs/hpc.ucdavis.edu/sw/spack/
find environments/ -name .cvmfscatalog -delete
```

Move out of the cvmfs directory and close out any open files you have there.

#### Publish the Changes

Publish your changes to cvmfs:

```bash
cvmfs_server publish hpc.ucdavis.edu
```

## Conda

## Other
