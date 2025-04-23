---
template: admin.html
title: Proxmox Backup Server new PI backup configuration
---

## Proxmox Backup Server new PI backup configuration

#### Phoenix

`./pbs/new-PI-group.sh {CLUSTER} {PI-group-name}` and take note of the token value.

???+ Note

    ```console
    root@phoenix.hpc: ~ # ./pbs/new-PI-group.sh hive {PIgrp}
    Checking / creating datastore: hive-group-{PIgrp} in /phoenix/proxmox-backup-service/hive/{PIgrp} (slow)

    !!!!! SAVE the value field of this token to the location indicated by the backup script. !!!!!
    Result: {
    "tokenid": "{PIgrp}@pbs!pbs-hive-{PIgrp}",
    "value": "TOKEN-VALUE-HERE"
    }
    ```

#### Hive

```console
root@hive: ~ # /quobyte/pbs/bin/backup.sh group {PIgrp}

backup.sh: ERROR: no API password at $PBS_PASSWORD_FILE: /quobyte/pbs/group/{PIgrp}/backup.token
Generate an API token and put the 'value' part in that file.
```

Paste the token into the indicated file:

```console
root@hive: ~ # vim /quobyte/pbs/group/{PIgrp}/backup.token
```

Generate the default config file and other required files.

```console
root@hive: ~ # /quobyte/pbs/bin/backup.sh group {PIgrp}
/quobyte/{PIgrp}/.pbs/config does not exist, creating default.
Now you need to edit /quobyte/{PIgrp}/.pbs/config to set the QUOTA_IN_TB.
```

Edit the config file to set the quota, adjust the snapshots to keep, and set the email addresses of users who will
receive the backup status.

```console
root@hive: ~ # vim /quobyte/{PIgrp}/.pbs/config
```

??? Note "Default config file"

    ```console
    # This is the amount of backup or archive space you have purchased.
    # See https://docs.hpc.ucdavis.edu/backups for details.
    QUOTA_IN_TB="0" # <--- EDIT

    # How many snapshots to keep. Available types are:
    # --keep-last
    # --keep-daily
    # --keep-weekly
    # --keep-monthly
    # --keep-yearly
    # Simulator: https://pbs.proxmox.com/docs/prune-simulator/
    ### NOTE: leave empty to indicate no snapshots of that type.
    KEEP_LAST=
    KEEP_DAILY=14  # <--- EDIT
    KEEP_WEEKLY=5  # <--- EDIT
    KEEP_MONTHLY=3 # <--- EDIT
    KEEP_YEARLY=

    # A list of space separated email addresses to send PBS output to.
    MAIL_TO="" # <--- EDIT
    ```

Finally, start the backup. Depending on the amount of data already in `{PIgrp}/BACKED-UP`, this may take multiple days,
so run the initial backup in screen and monitor closely.

```console
root@fs6: ~ # screen
root@fs6: ~ # /quobyte/pbs/bin/backup.sh group {PIgrp}
```

### Puppet

Once the initial backup finishes, edit `data/backups.yaml` and add `{PIgrp}` to the list so it is backed up
automatically.

## TODO: explain the layout
