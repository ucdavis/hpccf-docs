---
title: Hive Job Scheduling
---

### Free Access

See the [Free Access](../scheduler/free-access.md#hive) docs.

### Paid Access

Hive resources are generally purchased by the CPU. The current rates can be seen [here](https://hpc.ucdavis.edu/rates).
Specialized needs (entire nodes, or GPU nodes) can be purchased by contacting [HPC@UCD support](../general/support.md).
HPC will work with you to find a configuration suitable to use in Hive.

Some colleges have purchased group resources, which you may be able to request access to through
[Hippo](../general/account-requests.md#how-to-request-access-to-another-group-on-a-cluster).

Once you have access to group resources, you can request to use them with
`--account={account-name}grp --partition=high`. For a PI group, the account-name will generally be the PI's UCD Login
ID, followed by `grp`. A summary of the accounts you have access to, as well as the amount of resources in those
accounts, is printed every time you login to Hive.

Access to resources is mediated by Slurm. Nodes are not assigned to a user/group/PI. Instead, Slurm grants access to the
requested resources on the next available node. This allows a group to continue to access resources, even when any
particular node is down.

Note for users coming from other clusters. The use of the `--exclusive` flag will cause your job to take a very long
time to schedule. Use of this flag on Hive is highly discouraged.
