---
template: admin.html
title: Cheeto Introduction
---

Cheeto is the swissarmytoolknife of account, storage, QoS, group, etc, creation and manipulation. All manipulation is
done by `hippo-user` on the system `accounts`. **BE VERY CAREFUL** There are no prompts, and there is no undo.

#### Show a user

`cheeto db user show --site=**cluster** --user=**LoginID**`

#### Dump all user Login IDs in a cluster

`cheeto db user show --site=**cluster** --list`

#### Dump all user data in a cluster

`cheeto db user show --site=**cluster**`

#### Find a user

`cheeto db user show --find jeff`

#### Create a new Partition

```console
export PARTITION="**PartitionName**"
export CLUSTER="**ClusterName**"

cheeto database slurm new partition --name=${PARTITION} --site=${CLUSTER}

# Give the HPC staff access to this new partition, but use our high partition QoS so we have no limits.
cheeto database slurm new assoc --group=hpccfgrp --partition=${PARTITION} --qos=hpccfgrp-high-qos --site=${CLUSTER}
```

#### Add a new QoS:

Two step process, first create the Qos, then allow the group to access it.

```console
export GROUP="**GroupName**"
export PARTITION="**PartitionName**"
export CLUSTER="**ClusterName**"

cheeto database slurm new qos --group-limits mem=****G,cpus=**,gpus=** --qosname=${GROUP}-${PARTITION}-qos --site=${CLUSTER}

cheeto database slurm new assoc --group=${GROUP} --partition=${PARTITION} --qos=${GROUP}-${PARTITION}-qos --site=${CLUSTER}
```

#### Edit a QoS

`cheeto db slurm edit qos --site=**cluster** --qosname=**group-name**-**partition-name**-qos --group-limits mem=****G,cpus=***,gpus=*`

#### Show an association

```console
export GROUP="**GroupName**"
export PARTITION="**PartitionName**"

cheeto db slurm show assoc --site=**cluster** --partition=${PARTITION} --group=${GROUP} --qos=${GROUP}-high-qos
```

#### Find the name of a storage:

`cheeto db storage show --site=**cluster** --host=**hostname**`

#### Adjust a quota

Use the correct `name:` value from [Find the name of a storage](#find-the-name-of-a-storage)

`cheeto db storage edit source --name=**storage-name** --site=**cluster** --quota=**T`

#### Add an approver (sponsor) to a PI group

Note, all approvers must already have an account on the cluster in question.

`cheeto database group add sponsor --site=**cluster** --user=**LoginID** --group=**group-name**`

Note, there is no error shown if the user does not already have an account, so double check the
[sponsors list](#show-members-and-sponsors-of-a-pi-group) after.

#### Create a lab group

Sometimes, PIs need an additional group that are named after the lab they run. These can be created with:

`cheeto database group new lab --site=**site** --groups=**lab-name**-grp --sponsors=**sponsor**`

#### Show members, and sponsors, of a PI group

`cheeto db group show --site=**cluster** --group=**group-name**`
