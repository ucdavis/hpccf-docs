---
template: admin.html
title: Home Directory and PI group directory Backups
---

## Home directories

???+ failure

    This is internal, for development purposes. **CURRENTLY THERE ARE NO BACKUPS**.

### Hive

All of Hive's home directories have a quota of 20 GB and all backed up automatically every night.

### Farm

All of Farms's home directories are backed up automatically every night.

#### Restore a file from your home directory

```console
$ cd ~
$ /quobyte/pbs/bin/restore.sh
```

If everything is working correctly, you should see a list of snapshots. Pick the one you want to restore the file from
(up/down arrows), then press enter. The snapshot you selected will be automatically mounted to a random directory, which
is printed (for example `/home/omen/restore-fCnNXIUr`).

You can open another connection to Hive, then cd into that directory (`cd /home/omen/restore-fCnNXIUr`), find the
file(s) or directory(s) you need to restore, then `cp` to your desired location.

Note, this backup mount (`/home/omen/restore-fCnNXIUr` in this example) will automatically unmount in 1 hour. Any shells
that have `cd`'d into this directory will remain functional until you close them (or `cd` out).
