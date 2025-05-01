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

#### Add a new QoS:

Two step process, first create the Qos, then allow the group to access it.

```console
export GROUP="**GroupName**"

cheeto database slurm new qos --group-limits mem=****G,cpus=**,gpus=** --qosname=${GROUP}-high-qos --site=**cluster**

cheeto database slurm new assoc --group=${GROUP} --partition=high --qos=${GROUP}-high-qos --site=**cluster**
```

#### Edit a QoS

`cheeto db slurm edit qos --site=**cluster** --qosname=**group-name**-high-qos --group-limits mem=****G,cpus=***,gpus=*`

#### Show an association

```console
export GROUP="**GroupName**"

cheeto db slurm show assoc --site=**cluster** --partition=high --group=${GROUP} --qos=${GROUP}-high-qos
```

#### Find the name of a storage:

`cheeto db storage show --site=**cluster** --host=**hostname**`

#### Adjust a quota

Use the correct `name:` value from [Find the name of a storage](#find-the-name-of-a-storage)

`cheeto db storage edit source --name=**storage-name** --site=**cluster** --quota=**T`
