---
template: admin.html
title: Cheeto Introduction
---

Cheeto is the swissarmytoolknife of account, storage, QoS, group, etc, creation and manipulation. All manipulation is
done by `hippo-user` on the system `accounts`. **BE VERY CAREFUL** There are no prompts, and there is no undo.

Most changes require a sync process to run on a different system. This happens automatically via cron on the appropriate
systems, so changes are **not** instantaneous on the clusters.

## Basic Architecture 

Cheeto itself consists of a Python library, command line application, and database.
The database is a mongodb instance hosted on accounts.hpc.ucdavis.edu, hereby referred to as **accounts.hpc**.

### Cheeto Instances

Cheeto's account provisioning instances are hosted on **accounts.hpc**.
Slurm sync instances are hosted in each cluster's slurm controller.
The various syncing and provisioning services are run by cron jobs on their host systems.
The run directory for each job contains `logs` and `run` subdirectories, containing the log files for
each execution and the run state, respectively.

#### HiPPO API Sync

- *Location*: **acounts.hpc**
- *Script*: `/opt/hpccf/sbin/cheeto-hippoapi-sync.sh`
- *Cron*: Every 5 minutes, starting at minute 0.
- *Run Directory*: `/home/hippo-user/.local/share/accounts.hpc.ucdavis.edu/hippoapi-sync`

Communicates with the HiPPO REST API to process new account requests, group membership requests, and SSH key updates.
Makes the appropriate updates to Cheeto's database and communicates the event processing back to HiPPO.

#### LDAP Sync

- *Location*: **acounts.hpc**
- *Script*: `/opt/hpccf/sbin/cheeto-ldap-sync.sh`
- *Cron*: Every 5 minutes, starting at minute 3.
- *Run Directory*: `/home/hippo-user/.local/share/accounts.hpc.ucdavis.edu/ldap-sync`

Synchronizes the state of users in the database out to the primary LDAP servers.
This includes basic user information (user ID, full name, email, shell, etc), group memberships, user access privileges
as mediated through special access groups such as `login-ssh-users`, and automount tables.  

#### New Puppet Sync

- *Location*: **acounts.hpc**
- *Script*: `/opt/hpccf/sbin/cheeto-newpuppet-sync.sh`
- *Cron*: Every 5 minutes, starting at minute 2.
- *Run Directory*: `/home/hippo-user/.local/share/accounts.hpc.ucdavis.edu/newpuppet-sync`

Syncs data to the [puppet.hpc-accounts](https://github.com/ucdavis/puppet.hpc-accounts) git repo.
These are only things that are required by Puppet in YAML format: namely, ZFS storage allocations and the SSH keys for the `root` user.

#### Old Puppet Sync

- *Location*: **acounts.hpc**
- *Script*: `/opt/hpccf/sbin/cheeto-oldpuppet-sync.sh`
- *Cron*: Every 5 minutes, starting at minute 3.
- *Run Directory*: `/home/hippo-user/.local/share/accounts.hpc.ucdavis.edu/oldpuppet-sync`

Used for synchronizing state with HiPPO. Writes the full account tree in YAML format to the [puppet.hpc-accounts](https://github.com/ucdavis/puppet.hpc-accounts) git repo.
*Will be deprecated in the future*.

#### Sympa Sync

- *Location*: **acounts.hpc**
- *Script*: `/opt/hpccf/sbin/cheeto-to-sympa-sync.sh`
- *Cron*: Once per hour.
- *Run Directory*: `/home/hippo-user/.local/share/accounts.hpc.ucdavis.edu/to-sympa-sync`

Writes the sympa subscriber list for each cluster to `/var/www/html/sympa-lists/${CLUSTER}.hpc.ucdavis.edu`.

#### Slurm Sync

- *Location*: Slurm controllers
- *Script*: `/opt/hpccf/sbin/cheeto-slurm-sync.sh `
- *Cron*: Every 5 minutes, starting at minute 2..
- *Run Directory*: `/home/hippo-user/.local/share/${SLURMCTLD_FQDN}/slurm-sync`

One-way sync of Slurm associations from the Cheeto database to the Slurm controller.
Slurm associations are based on group membership; associations _not_ present in the Cheeto database
that are present in Slurm's database are _deleted_.

## Database Terminology

**Site**

: A namespace within which user state should be shared. Usually a cluster: hive, farm, franklin, peloton. Can also be a general collection of machines, for example
"hpccf".

**Global User**:

: User information that is shared between all sites: username, unix ID, biographical information, shell, SSH keys, etc.

**Site User**

: User information specific to a _site_ (essentially only site specific _status_ and _access_ rights). The existence of the `SiteUser` database entry indicates the user exists on that site.

**Global Group**

: Like the corresponding global user, group information shared between all sites: group name, unix ID, group type.

**Site Group**

: Site-specific group information: members, slurmers (users that have access to the group's slurm resources but are not unix group members), sponsors, 
Slurm settings specific to the group's Slurm account.

## Cheeto CLI

Modifications to the database should be done via Cheeto's command-line interface whenever possible, though it is _not_ entirely feature complete.
The database modification commands are all nestled under the `database` subcommand, which as aliases as `db`, meaning it can be run as either
`cheeto database ...` or `cheeto db ...`:

```console
$ cheeto db --help
usage: cheeto database [-h] [--log [LOG]] [--log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}] [--quiet] [--config CONFIG] [--profile PROFILE]
                       {site,s,user,u,group,g,grp,slurm,storage,iam} ...

positional arguments:
  {site,s,user,u,group,g,grp,slurm,storage,iam}
    site (s)            Operations on sites
    user (u)            Operations on users
    group (g, grp)      Operations on groups
    slurm               Operations on Slurm
    storage             Operations on storage
    iam                 Data sync from UCD IAM
```

The **full** command tree and documentation can be viewed with the `help` subcommand:

```console
$ cheeto help
cheeto v1.4.0
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


 _______ __                 __         
|   _   |  |--.-----.-----.|  |_.-----.
|.  1___|     |  -__|  -__||   _|  _  |
|.  |___|__|__|_____|_____||____|_____|
|:  1   |                              
|::.. . |          v1.4.0
`-------'                              
                                       

usage: cheeto [-h] [--version] [--log [LOG]] [--log-level {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}] [--quiet] [--config CONFIG]
              [--profile PROFILE]
              {help,config,puppet,database,db,hippo,monitor,nocloud} ...

cheeto:
  help: Show the full subcomamnd tree
  config: Current configuration information
    show: Parse and show the config file
    write: Write a skeleton config file
  puppet: Operations on legacy puppet-consumed YAML
    validate: Validate a puppet.hpc-formatted YAML file
  database (db): Operations on the cheeto MongoDB
    site (s): Operations on sites
      new: Add a new site
      add-global-slurm: Add a group for which users are made slurmers
      to-puppet: Dump site in puppet.hpc YAML format
      sync-old-puppet: Fully sync site from database to puppet.hpc YAML repo

[...]
```

For _all_ commands, passing `-q/--quiet` will hide things like the database connection information.

### Show a user

View user account information. By default, for the global user entry:


```console
$ cheeto db user show -u camw -q
username: camw
email: ####################
fullname: Camille Scott
uid: ########
gid: ########
type: admin
status: active
access:
- login-ssh
- root-ssh
- sudo
- compute-ssh
colleges:
- RESEARCH
home_directory: /home/camw
iam_has_entry: true
iam_id: ############
ldap_synced: true
shell: /bin/zsh
sites:
- farm
- franklin
- franklin-cashjngrp
- franklin-jalettsgrp
- hive
- peloton
```

Passing the `-s/--site` argument adds in site-specific information.

```console
$ cheeto db user show -u camw -s hive -q
username: camw
email: ###########
fullname: Camille Scott
uid: #######
type: admin
status: active
access:
- root-ssh
- compute-ssh
- sudo
- slurm
- login-ssh
colleges:
- RESEARCH
home_directory: /home/camw
iam_has_entry: true
iam_id: ##########
ldap_synced: true
shell: /bin/zsh
groups:
- sudo-users
- sponsors
- hpccfgrp
- camw
slurm:
  low:
    publicgrp:
      sitename: hive
      group_limits:
        cpus: -1
        gpus: -1
[...]
```


### Dump all user Login IDs in a cluster

Useful for integration with scripts.

`cheeto db user show --site=##cluster## --list`

### Dump all user data in a cluster

_ALL_ user information for a cluster. Very verbose!

`cheeto db user show --site=##cluster##`

### Find a user

Free text search over the username, full name, and email fields.

```console
$ cheeto db user show -q --find jeff
🚩 More than 5 results for search "jeff", filtering...
username: jeffkwc
email: ##############
fullname: #############
uid: ########
gid: ########
type: user
status: active
access:
- login-ssh
home_directory: /home/jeffkwc
iam_has_entry: true
iam_id: #########
ldap_synced: true
shell: /usr/bin/bash
sites:
- hive
- peloton
```

Pass `--no-filter` if you want to get _all_ the search hits. This is a very simple home-rolled
n-gram based search, so don't expect miracles. If your results seem _really_ bad, you might need to
reinded the database:

```console
cheeto db user index
```

### Create a new Partition

This should not need to be done particularly often.

```console
export PARTITION="##PartitionName##"
export CLUSTER="##ClusterName##"

cheeto database slurm new partition --name=${PARTITION} --site=${CLUSTER}

# Give the HPC staff access to this new partition, but use our high partition QoS so we have no limits.
cheeto database slurm new assoc --group=hpccfgrp --partition=${PARTITION} --qos=hpccfgrp-high-qos --site=${CLUSTER}
```

### Add a new QoS:

Two step process, first create the Qos, then allow the group to access it.


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

### Edit a QoS

`cheeto db slurm edit qos --site=##cluster## --qosname=##group-name##-##partition-name##-qos --group-limits mem=####G,cpus=###,gpus=#`

### Show an association

```console
export GROUP="##GroupName##"
export PARTITION="##PartitionName##"

cheeto db slurm show assoc --site=##cluster## --partition=${PARTITION} --group=${GROUP} --qos=${GROUP}-high-qos
```

### Find the name of a storage:

`cheeto db storage show --site=##cluster## --host=##hostname##`

### Adjust a quota

Use the correct `name:` value from [Find the name of a storage](#find-the-name-of-a-storage)

`cheeto db storage edit source --name=##storage-name## --site=##cluster## --quota=##T`

### Add an approver (sponsor) to a PI group

Note, all approvers must already have an account on the cluster in question.

`cheeto database group add sponsor --site=##cluster## --user=##LoginID## --group=##group-name##`

Note, there is no error shown if the user does not already have an account, so double check the
[sponsors list](#show-members-and-sponsors-of-a-pi-group) after.

### Create a lab group

Sometimes, PIs need an additional group that are named after the lab they run. These can be created with:

`cheeto database group new lab --site=##cluster## --groups=##lab-name##-grp --sponsors=##sponsor##`

### Show members, and sponsors, of a PI group

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
