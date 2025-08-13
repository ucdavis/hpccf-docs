---
title: Data Transfer
---

There are four general methods for getting data to/from a cluster.

## Globus

Farm, Franklin, and Hive have Globus v5 installed, use the [Globus File Manager](https://app.globus.org/) to access
exported collections.

### Home directories

Home directories for all three clusters are already exported. On Globus, you can find the home directory collection by
searching for `UC Davis CLUSTER-NAME home`.

### PI directories

Because of the way Globus v5 works, each PI directory must be exported manually by HPC@UCD staff. If you need a PI
directory exported, please contact HPC support and CC your PI for approval.

Once the PI group directory is exported, you can find it by searching for a collection named
`UC Davis CLUSTER-NAME PI-share-name`. In the Globus File Manager for that collection, you will be able to read any file
you normally have access to, but for security reasons, you will only be able to write files to
`/globus-write/Your-Login-ID/`. On the cluster, your newly written files will be under your PI's storage.

**Farm:**

: `/group/Your-PI-Group-grp/globus-write/Your-Login-ID/`

**Hive:**

: `/quobyte/Your-PI-Group-grp/globus-write/Your-Login-ID/`

???+ Warning "Globus Free File Transfer limitations"

    HPC@UCD does not have a paid subscription for Globus, and uses the `Free File Transfer…for users at non-profit research institutions` tier. This means you either need to have a login on both ends of the transfer, or the remote end must have the paid version.

## Command-line tools

### scp — OpenSSH secure file copy

If you only need to move a single file, or a small directory, scp will work well. From your desktop/laptop you can push,
or pull, file(s) and/or directories.

To push a file, you specify the source from your local system, and the destination on a cluster:

: `scp -rp local-file local-directory/ UCD-Login-ID@CLUSTERNAME.hpc.ucdavis.edu:`

To pull a file from a cluster to your local machine:

: `scp -rp UCD-Login-ID@CLUSTERNAME.hpc.ucdavis.edu:location/on/cluster .`

The final `.` will put the files/directories into the current directory.

`scp` arguments:

-   `-r` Recursively copy entire directories. Note that scp follows symbolic links encountered in the tree traversal.

-   `-p` Preserves modification times, access times, and file mode bits from the source file.

See `man scp` for the full manual.

### rsync - a fast, versatile, remote (and local) file-copying tool

From the `rsync` manual:

: Rsync is a fast and extraordinarily versatile file copying tool. It can copy locally, to/from another host over any
remote shell, or to/from a remote rsync daemon. It offers a large number of options that control every aspect of its
behavior and permit very flexible specification of the set of files to be copied. It is famous for its delta-transfer
algorithm, which reduces the amount of data sent over the network by sending only the differences between the source
files and the existing files in the destination. Rsync is widely used for backups and mirroring and as an improved copy
command for everyday use.

Like scp, rsync can operate in a push, or a pull, mode, depending on which arguments you put first. To use rsync to copy
files from your local system, to a cluster, preserving permissions, ownership, and file times, you can use the following
command.

`rsync --archive --one-file-system --info=progress2 local-directory/ UCD-LOGIN-ID@CLUSTERNAME.hpc.ucdavis.edu:~/destination/`

To pull a directory from a cluster to your local machine:

`rsync --archive --one-file-system --info=progress2 UCD-LOGIN-ID@CLUSTERNAME.hpc.ucdavis.edu:~/remote-directory/ local-directory/`

#### Explanation of options:

-   `--archive` preserves symbolic links, permissions, ownership, file timestamps, and recursively copies directories.
-   `--one-file-system` don't cross filesystem boundaries.
-   `--info=progress2` show reasonable progress as rsync processes files.

-8<- "docs/include/rsync-warnings.md"

As always, see `man rsync` for the manual.

## Open OnDemand

For clusters that have [Open OnDemand](/software/ondemand/), you can copy files to/from your home directory. Log in to
the OnDemand dashboard for the cluster, and select `Files` -> `Home Directory`. Files larger than a couple hundred
megabytes will fail to transfer through OnDemand, so you will need to use a different method.

## GUI tools

GUI tools do exist to help with file transfer. However, HPC@UCD cannot provide support for them, so you will need to
contact your local IT support, or make an appointment with [DataLab](/#additional-information) for help.

-   Filezilla is a multi-platform client commonly used to transfer data to and from the cluster.

-   Cyberduck is another popular file transfer client for Mac or Windows computers.

-   WinSCP is Windows-only file transfer software.
