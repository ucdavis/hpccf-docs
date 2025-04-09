---
template: admin.html
title: Home Directory and PI group directory Backups
---

???+ failure

    This is internal, for development purposes. **CURRENTLY THERE ARE NO BACKUPS FOR ANY HPC CLUSTERS**.

## What software is used?

HPC@UCD has written a custom backup system based around the
[Proxmox Backup Server (PBS)](https://www.proxmox.com/en/products/proxmox-backup-server/overview).

## Home Directories

### Hive

All of Hive's home directories have a quota of 20 GB and all backed up automatically every night. As of March 2025, the
snapshot keep schedule is listed below, but this is subject to revision as the backup space fills. Individual files
and/or directories can be restored by each user.

| Snapshot type | Keep count |
| ------------- | ---------- |
| daily         | 7          |
| weekly        | 5          |
| monthly       | 12         |
| yearly        | 2          |

## Group directories

### Rates

Group directory backups are available by request on Hive. The current rates are posted on
[https://hpc.ucdavis.edu/rates](https://hpc.ucdavis.edu/rates) under `Rates for Hive` ->
`Cost of Backup/Archival (snapshot copy) Storage`.

### How do I purchase backups for my group directory?

All Hive purchases are through [Hippo](https://hippo.ucdavis.edu/). Select the cluster you are purchasing for, click
`Orders` -> `Products`. Then order `Backup Storage`. To expedite the process, in the `Notes` section, please include the
following information:

1. The list of contacts (email addresses) that are responsible for monitoring the backup status.

1. The [number and type of snapshots](#what-types-of-snapshots-are-available) you would like.

Please see the [How much backup space do I need?](#how-much-backup-space-do-i-need) section if you have questions about
how much backup space to purchase.

### What is backed up?

The **only** data that is backed up is the data that resides within the `BACKED-UP/` directory at the top level of the
PI share. **NO OTHER DATA IS BACKED UP**. If you have questions about what is being backed up, you should try a test
restore.

### Who monitors the backups?

You, the PI, or a designated list of email addresses. HPC@UCD does NOT, and we cannot emphasize this enough, **does
NOT** monitor the individual backups. It is up to you to monitor those and open a ticket if you see any issues.

### How much backup space do I need?

This is a surprisingly complex question and depends on how much data you are backing up, how much that data changes
(churn), and the total number of snapshots you keep. PBS only stores a single copy of each unique data chunk, so
unchanging data is only stored a single time. The short version is you need approximately
`(initial quantity * snapshots) + (churn * snapshots)`.

| Quantity of Data | Data Churn      | Snapshots                    | Total Required Space |
| ---------------- | --------------- | ---------------------------- | -------------------- |
| 1 TB             | 0 Bytes per day | Any                          | 1 TB                 |
| 1 TB             | 1 TB per day    | last=1                       | 1 TB                 |
| 1 TB             | 1 TB per day    | daily=7                      | 7 TB                 |
| 1 TB             | 1 TB per day    | daily=7, weekly=4, monthly=6 | 17 TB                |
| 1 TB             | 100 GB per day  | daily=7, weekly=4, monthly=6 | 2.7 TB               |

### What happens when my backups exceed my purchased space?

An error will be sent the email address(es) you designated to monitor your backups.

???+ Warning "Purchased quota exceeded example message"

    ```console
    !!!!!!!!!! ERROR !!!!!!!!!!

    Backup quota exceeded, backed up data is greater than purchased quota.

    Please see https://docs.hpc.ucdavis.edu/backups for information about
    purchasing more space, or contact HPC@UCD to adjust your retention policy,
    which is currently: --keep-daily=14 --keep-weekly=5 --keep-monthly=2 **EXAMPLE ONLY**

    BACKUP CANCELLED!
    ```

At this point you have 4 options:

1. Purchase more space by visiting [Hippo](https://hippo.ucdavis.edu/) and ordering additional backup space.

1. Backup less data by reducing the amount of data in your `BACKED-UP/` directory. This will require old data to age out
   before new data can be backed up.

1. Ignore it. Eventually old data will age out and new data will be able to backed up again.

1. Reduce the number of snapshots you keep by emailing `hpc-help@`ucdavis.edu`. For example, if you keep 6 monthly, you
   could reduce that to 3. This will age-out (delete) the data greater than 3 months, freeing up space for new data.

### How often are backups taken?

The backup system starts at midnight every night and works its way through a randomly shuffled list of PI areas it needs
to backup. The actual start time of _your_ backup depends on how much data needs to be backed up before you, and your
order in the shuffle.

### What types of snapshots are available?

PBS offers the following types of snapshots:

-   `last`: Keep the last N snapshots.
-   `daily`: Keep the last N daily snapshots.
-   `weekly`: Keep the last N weekly snapshots.
-   `monthly`: Keep the last N monthly snapshots.
-   `yearly`: Keep the last N annual snapshots.

There is a [simulator](https://pbs.proxmox.com/docs/prune-simulator/) to test various settings.

Note, `last=1` means a single copy (the latest) will be retained of each file. This is effectively a "snapshot" copy for
disaster recovery purposes only.

### How many snapshots do I need?

Unfortunately, we cannot help with this. It depends on your contractual obligations, and/or how far back in time you
need to be able to retrieve old versions, or deleted, files.

### Are my backups encrypted?

Yes, all backups are encrypted with a key that is unique to every PI group. This key is protected with normal Linux
file-system permissions, and only users in the PI group will be able to even read it to restore data.

### Who can restore files?

Anyone in the PI group can initiate a restore, however, you will only be able to restore files you had read access to at
the time the file was backed up. This means that files/directories with permissions that prevent PI access on disk also
prevent PI restore. If you, as a PI, run into this situation, please contact HPC@UCD support by emailing
`hpc-help@ucdavis.edu` with the following information, and we can restore the files for you.

-   The cluster.
-   The full path to the files/directories you need restored.
-   The full path to the place you would like them restored to.

### How do I make changes to my snapshots or monitoring designee list?

Changes can be made by emailing `hpc-help@ucdavis.edu`.

## How to restore files or directories

### Restore a file from your home directory

```console
$ cd ~
$ /quobyte/pbs/bin/restore.sh
```

You will see a list of snapshots. Pick the one you want to restore the file from (up/down arrows), then press enter. The
snapshot you selected will be automatically mounted to a random directory, which is printed (for example
`/home/omen/restore-fCnNXIUr`).

??? Note "Please chose a snapshot to restore from."

    ```
    ┌─────────────────┤ Please chose a snapshot to restore from. ├─────────────────┐
    │ Snapshots, newest to oldest:                                                 │
    │                                                                              │
    │                      1  host/omen/2025-03-18T07:13:02Z                       │
    │                      2  host/omen/2025-03-17T22:51:54Z                       │
    │                      3  host/omen/2025-03-16T07:16:32Z                       │
    │                      4  host/omen/2025-03-15T07:15:07Z                       │
    │                      5  host/omen/2025-03-14T07:00:04Z                       │
    │                      6  host/omen/2025-03-13T07:05:46Z                       │
    │                      7  host/omen/2025-03-12T07:17:56Z                       │
    │                      8  host/omen/2025-03-09T08:10:37Z                       │
    │                      9  host/omen/2025-03-02T08:17:44Z                       │
    │                      10 host/omen/2025-02-23T08:08:58Z                       │
    │                                                                              │
    │                     <Ok>                         <Cancel>                    │
    │                                                                              │
    └──────────────────────────────────────────────────────────────────────────────┘
    ```

You can open another connection to Hive, then cd into that directory (`cd /home/omen/restore-fCnNXIUr`), find the
file(s) or directory(s) you need to restore, then `cp` to your desired location.

??? Note "Snapshot selected."

    ```
    ┌─omen@login1.hive: ~
    └─0 $ /quobyte/pbs/bin/restore.sh
    Loading snapshots, done.
    Mounting chosen snapshot: host/omen/2025-03-18T07:13:02Z to /home/omen/restore-zCgS0D1Z
    Encryption key file: '"/quobyte/pbs/home/omen.json"'
    Encryption key fingerprint: '21:96:a0:ec:62:62:ae:34'
    FUSE library version: 3.14.0

    Backups mounted on /home/omen/restore-zCgS0D1Z

    Please open another shell and copy any file(s)/directory(s) you need to restore.

    It will remain mounted for 1 hour, then automatically unmount.
    You can issue Control-c to unmount earlier.
    ```

Note, this backup mount (`/home/omen/restore-fCnNXIUr` in this example) will automatically unmount in 1 hour. Any shells
that have `cd`'d into this directory will remain functional until you close them (or `cd` out). You can force the
directory to umount earlier by pressing Control-c in window where you ran the restore program.

### Restore a file from your group directory

Restoring files from your group directory is similar to restoring files in your
[home directory](#restore-a-file-from-your-home-directory). There are only two differences. First, start in the PI group
directory:

```console
$ cd /quobyte/*PI*grp/
$ /quobyte/pbs/bin/restore.sh
```

Second, the temporary directory will be created in `/quobyte/*PI*grp/`.

## FAQ

### Where is the backup server located?

The backup server is located in the [Academic Surge](https://maps.app.goo.gl/4Xj6HUaBeVRUZyuT9) building, so it is
outside the Campus Data Center, but still on-campus. This may be important for certain grant requirements.

### What happens if the backup server is also destroyed?

At this point, the data would be permanently lost. HPC@UCD does **not** replicate the backup data to any off-site
location(s).
