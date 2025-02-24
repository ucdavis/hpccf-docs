---
template: admin.html
title: Home Directory and PI group directory Backups
---

## Home directories

???+ failure

    This is internal, for development purposes. **CURRENTLY THERE ARE NO BACKUPS**.

### Hive

All of Hive's home directories have a quota of 20 GB and all backed up automatically every night. If you ever need to
restore a file, you can:

```console
$ cd ~
$ /quobyte/pbs/bin/restore.sh
```

If everything is working correctly, you should see a list of snapshots. Pick the one you want to restore the file from
(up/down arrows), then press enter. The snapshot you selected will be automatically mounted to a random directory, which
is printed. You can open another connection to Hive, then cd into that directory, find the file you need to restore, and
cp it into your
