---
template: admin.html
title: Cheeto Introduction
---

Cheeto is the swissarmytoolknife of account, storage, QoS, group, etc, creation and manipulation. All manipulation is
done by `hippo-user` on the system `accounts`. **BE VERY CAREFUL** There are no prompts, and there is no undo.

Most changes require a sync process to run on a different system. This happens automatically via cron on the appropriate
systems, so changes are **not** instantaneous on the clusters.

## Manipulating the database that drives most of the systems

#### Show a user

`cheeto db user show --site=##cluster## --user=##LoginID##`

#### Dump all user Login IDs in a cluster

`cheeto db user show --site=##cluster## --list`

#### Dump all user data in a cluster

`cheeto db user show --site=##cluster##`

#### Find a user

`cheeto db user show --find jeff`

#### Create a new Partition

```console
export PARTITION="##PartitionName##"
export CLUSTER="##ClusterName##"

cheeto database slurm new partition --name=${PARTITION} --site=${CLUSTER}

# Give the HPC staff access to this new partition, but use our high partition QoS so we have no limits.
cheeto database slurm new assoc --group=hpccfgrp --partition=${PARTITION} --qos=hpccfgrp-high-qos --site=${CLUSTER}
```

#### Add a new QoS:

Two step process, first create the Qos, then allow the group to access it.

???+ warning "Slurm Bug in 25.05.0"

    Slurm 25.05.0 [has a bug](https://support.schedmd.com/show_bug.cgi?id=23127) that prevents Cheeto's newly added QoSs from working.
    The work-around is to restart the slurmdbd service after new QoSs are added.

```console
export GROUP="##GroupName##"
export PARTITION="##PartitionName##"
export CLUSTER="##ClusterName##"

cheeto database slurm new qos --group-limits mem=####G,cpus=##,gpus=## --qosname=${GROUP}-${PARTITION}-qos --site=${CLUSTER}

cheeto database slurm new assoc --group=${GROUP} --partition=${PARTITION} --qos=${GROUP}-${PARTITION}-qos --site=${CLUSTER}
```

??? note "Example: **DO NOT BLINDLY COPY/PASTE**"

    ```console
    export GROUP="rudolphgrp"
    export PARTITION="high"
    export CLUSTER="hive"

    ###cheeto database slurm new qos --group-limits mem=3000G,cpus=384,gpus=0 --qosname=${GROUP}-${PARTITION}-qos --site=${CLUSTER}
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    group_limits:
        cpus: 384
        mem: 3072000M
    job_limits:
        cpus: -1
        gpus: -1
    qosname: rudolphgrp-high-qos
    sitename: hive
    user_limits:
        cpus: -1
        gpus: -1

    ###cheeto database slurm new assoc --group=${GROUP} --partition=${PARTITION} --qos=${GROUP}-${PARTITION}-qos --site=${CLUSTER}
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    group: rudolphgrp
    partitionname: high
    qos:
    sitename: hive
    qosname: rudolphgrp-high-qos
    group_limits:
        cpus: 384
        mem: 3072000M
    user_limits:
        cpus: -1
        gpus: -1
    job_limits:
        cpus: -1
        gpus: -1
    sitename: hive
    ```

#### Edit a QoS

`cheeto db slurm edit qos --site=##cluster## --qosname=##group-name##-##partition-name##-qos --group-limits mem=####G,cpus=###,gpus=#`

#### Show an association

```console
export GROUP="##GroupName##"
export PARTITION="##PartitionName##"

cheeto db slurm show assoc --site=##cluster## --partition=${PARTITION} --group=${GROUP} --qos=${GROUP}-high-qos
```

#### Find the name of a storage:

`cheeto db storage show --site=##cluster## --host=##hostname##`

#### Adjust a quota

Use the correct `name:` value from [Find the name of a storage](#find-the-name-of-a-storage)

`cheeto db storage edit source --name=##storage-name## --site=##cluster## --quota=##T`

#### Add an approver (sponsor) to a PI group

Note, all approvers must already have an account on the cluster in question.

`cheeto database group add sponsor --site=##cluster## --user=##LoginID## --group=##group-name##`

Note, there is no error shown if the user does not already have an account, so double check the
[sponsors list](#show-members-and-sponsors-of-a-pi-group) after.

#### Create a lab group

Sometimes, PIs need an additional group that are named after the lab they run. These can be created with:

`cheeto database group new lab --site=##cluster## --groups=##lab-name##-grp --sponsors=##sponsor##`

#### Show members, and sponsors, of a PI group

`cheeto db group show --site=##cluster## --group=##group-name##`

## Fixes for common errors

#### User not in `login-ssh-users`

Occasionally, cheeto gets cheated by a MongoDB issue, causing a new user to be unable to login to a cluster. From the
users side, the connection just closes. You can diagnose on the login node by running `showuser.sh ##Login-ID##` and
looking for `User is NOT in login-ssh-users, and thus not allowed to login. This is usually a bug.`. You can also run
`id ##Login-ID##` and see there is no `login-ssh-users` listed for that user.

To fix, you can run the following command on accounts:

`cheeto database site to-ldap --site=##cluster## --force`

This takes approximately 15 seconds on Franklin, and 2 minutes on Farm. During that time, users may run into issues
logging in.

Then, on the login node, you can run `sudo sss_cache -E`. Then re-verify with `showuser.sh` or `id`. You can also
directly check LDAP:

```console
┌─omen@franklin².hpc: ~
└─0 $ source /opt/hpccf/etc/cluster_name.conf

┌─omen@franklin².hpc: ~
└─0 $ ldapsearch -o ldif-wrap=no -LLL -x -b ou=groups,ou=${CLUSTER_NAME},dc=hpc,dc=ucdavis,dc=edu  cn=login-ssh-users | grep ##Login-ID##
memberUid: ##Login-ID##
```
