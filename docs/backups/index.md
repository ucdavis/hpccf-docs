---
title: Home Directory and PI group directory Backups
---

## Backups? Backups! On Hive only.

Currently, HPC@UCD only offers backups on Hive. On Hive, we automatically backup home directories once a day. PI/group
directory backups [can be purchased](#group-directories).

???+ danger "NO BACKUPS ON OTHER CLUSTERS"

    HPC@UCD does not offer backups on any clusters except Hive. You are responsible for ensuring your critical data is properly backed up offsite.

## What software is used?

HPC@UCD has written a custom backup system based around [Restic](https://restic.readthedocs.io/en/stable/).

## How to restore files or directories

### Restore a file from your home directory

```console
$ cd ~
$ /quobyte/backups/bin/restore.sh

Backups will be mounted on /home/omen/backup-mount-UgySgiqt/snapshots/
and will remain mounted until you press Control-c.

Please open another shell to this host and copy any file(s)/directory(s) you need to restore.

Mounting backups, this may take several minutes...
repository 3dfc0b37 opened (version 2, compression level auto)
unable to open cache: mkdir /nfs: permission denied
[0:00] 100.00%  18 / 18 index files loaded
Now serving the repository at /home/omen/backup-mount-UgySgiqt
Use another terminal or tool to browse the contents of this folder.
When finished, quit with Ctrl-c here or umount the mountpoint.
```

This backup mount (`/home/omen/backup-mount-UgySgiqt/snapshots/` in this example) will remain mounted until you
Control-c the restore script.

### Restore a file from your group directory

Restoring files from your group directory is similar to restoring files in your
[home directory](#restore-a-file-from-your-home-directory). There are only two differences. First, start in the PI group
directory:

```console
$ cd /quobyte/*PI*grp/
$ /quobyte/backups/bin/restore.sh
```

Second, the temporary directory will be created in `/quobyte/*PI*grp/`.

## Home Directories

### Hive

All of Hive's home directories have a quota of 20 GB and all backed up automatically every night. As of March 2025, the
snapshot keep schedule is listed below, but this is subject to revision as the backup space fills. Individual files
and/or directories can be restored by each user.

[comment]: # "See: /quobyte/restic/home/.restic/config"

| Snapshot type | Keep count |
| ------------- | ---------- |
| daily         | 7          |
| weekly        | 5          |
| monthly       | 3          |
| yearly        | 0          |

## Group directories

### Rates

Group directory backups are available by request on Hive. The current rates are posted on
[https://hpc.ucdavis.edu/rates](https://hpc.ucdavis.edu/rates) under `Rates for Hive` ->
`Cost of Backup/Archival (snapshot copy) Storage`.

### How do I purchase backups for my group directory?

<!--
All Hive purchases are through [Hippo](https://hippo.ucdavis.edu/). Select the cluster you are purchasing for,
click `Orders` -> `Products`. Then order `Backup Storage`. To expedite the process, in the `Notes` section, please
include the following information:
-->

You can purchase backups for your storage by emailing HPC@UCD help and including:

1. The full path to the PI group storage you need backed up.

1. The amount of storage you would like to purchase.

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

This is a surprisingly complex question. It depends on how much data you are backing up, how much that data changes
(`added files + deleted files + changed data` = `churn`), and the total number of snapshots you keep. Restic only stores
a single copy of each unique data chunk, so unchanging data is only stored a single time. The short version is you need
approximately `(initial quantity * snapshots) + (churn * snapshots)`.

| Quantity of Data | Data added + deleted + changed | Snapshots                    | Total Required Space |
| ---------------- | ------------------------------ | ---------------------------- | -------------------- |
| 1 TB             | 0 Bytes per day                | Any                          | 1 TB                 |
| 1 TB             | 1 TB per day                   | last=1                       | 1 TB                 |
| 1 TB             | 1 TB per day                   | daily=7                      | 7 TB                 |
| 1 TB             | 1 TB per day                   | daily=7, weekly=4, monthly=6 | 17 TB                |
| 1 TB             | 100 GB per day                 | daily=7, weekly=4, monthly=6 | 2.7 TB               |

Also see backups compared to [archives](#what-is-the-difference-between-a-backup-and-an-archive).

### What happens when my backups exceed my purchased space?

An error will be sent the email addresses you designated to monitor your backups.

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

<!---
1. Purchase more space by visiting [Hippo](https://hippo.ucdavis.edu/) and ordering additional backup space.
-->

1. Contacting HPC@UCD support and purchasing additional backup storage space.

1. Backup less data by reducing the amount of data in your `BACKED-UP/` directory. This will require old data to age out
   before new data can be backed up.

1. Ignore it. Eventually old data should age out and new data should be able to be backed up again.

1. Reduce the number of snapshots you keep by contacting HPC@UCD support. For example, if you keep 6 monthly, you could
   reduce that to 3. This will age-out (delete) the data greater than 3 months, freeing up space for new data.

### What types of snapshots are available?

Restic offers the following types of snapshots:

- `last`: Keep the last N snapshots.
- `daily`: Keep the last N daily snapshots.
- `weekly`: Keep the last N weekly snapshots.
- `monthly`: Keep the last N monthly snapshots.
- `yearly`: Keep the last N annual snapshots.

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
prevent PI restore. If you, as a PI, run into this situation, please contact HPC@UCD support by HPC@UCD support with the
following information, and we can restore the files for you.

- The cluster.
- The full path to the files/directories you need restored.
- The full path to the place you would like them restored to.

### How do I make changes to my quota, snapshots or monitoring designee list?

Changes can be made by contacting HPC@UCD support.

### How often are backups run?

The backup system starts after midnight every night and works its way through a randomly shuffled list of PI areas it
needs to backup. The actual start time of _your_ backup depends on how much data needs to be backed up before you, and
your order in the shuffle.

## FAQ

### What is the difference between a backup and an archive?

An archive is an off-system copy of the data that mirrors what exists in your `BACKED-UP/` directory. There is no
history, so if a file is deleted in production, it will be removed from the archive overnight. A backup has history, so
if you delete a file today, it will exist in the backup until it expires due to your snapshot keep schedule.

### Where is the backup server located?

The backup server is located in the [Academic Surge](https://maps.app.goo.gl/4Xj6HUaBeVRUZyuT9) building. It is outside
the Campus Data Center but still on campus, so we do **not** provide an off-site backup. This may be important for
certain grant requirements.

### What happens if the backup server is also destroyed?

At that point, the data would be permanently lost. HPC@UCD does **not** replicate the backup data to any off-site
location(s).

### Can the backup system back up symlinks?

Yes, the backup system will back up the symlinks. However, it will not back up the files the symlinks point to. This
means that data you need backed up must reside within the [backed-up](#what-is-backed-up) directory. You are free to
create symlinks that reside outside the backup area and point to files within the backup area.

### How is Hive different than LSSC0's separate primary and archive storage?

On Hive, the only storage you have direct access to is your Quobyte PI share. In LSSC0 terminology, this could be
considered primary storage. Archive storage, as a separate PI share, does not exist. We provide a
[BACKED-UP](#what-is-backed-up) folder in your regular Quobyte share, and back up data in that folder up to the amount
of backup space you have paid for. We provide regular email logs so you can monitor your backup status and how close you
are to your backup space limit.
