---
template: admin.html
title: Quobyte / New PI Share
---

## GUI

All PIs get their own Quobyte Tenent, within which we create a volume.

1. Login to our [Quobyte web console](https://quobyte.hpc.ucdavis.edu:7443/)

1. Click `Volumes` on the left.

1. Verify the PI does not already have a tenant/volume.

1. `Tenant` -> `Create tenant...`

    1. `Tenant name`: `{PI-Login-ID}grp`

1. Find the new Tenant with the `Filter` box.

1. Click the three vertical dots next to the PI's tenant name

    1. `Edit tenant quota...`

        1. Ensure `Unit: Binary (Default decimal)` is set.

        1. Enter their quota into `Any type`

    1. `Create tenant volume...`

        1. `Volume name`: `{PI-Login-ID}grp`

        1. `Owner user name`: `{PI-Login-ID}`

        1. `Owner group name`: `{PI-Login-ID}grp`

        1. `POSIX permission mask`: `2770`

1. Verify the new volume exists:

    1. `ls -l /quobyte/{PI-Login-ID}grp`

1. Research!

## CLI

PREREQUISITE: update `qmgmt.sh` to use a r/w user.

1. SSH to `quobyte.hpc`.

1. `export PI={PI-Login=ID}`

1. Verify the PI tenant does not already exist.

    1. `sudo /opt/hpccf/sbin/qmgmt.sh tenant resolve ${PI}grp`

        1. Look for: `FATAL: Operation failed due to invalid input: 'No such tenant: `

1. Create the tenant: `sudo /opt/hpccf/sbin/qmgmt.sh tenant create ${PI}grp`

1. Create the volume: `sudo /opt/hpccf/sbin/qmgmt.sh volume create "${PI}grp/${PI}grp" ${PI} ${PI}grp 2770`

1. Set the quota:
   `sudo /opt/hpccf/sbin/qmgmt.sh quota create TENANT ${PI}grp LOGICAL_DISK_SPACE $(( {TiBHERE} * 1024**4))`
