# Requesting an Account

HPC accounts are provisioned on a per-cluster basis and granted with the permission of their principal investigator
(PI). Accounts that are provisioned under each PI will have access to that PI's purchased resources and their own
separate home directory.

Access to all HPC clusters except Hive are granted via the use of SSH keys. An SSH public key is required to generate an
account. For information on creating SSH keys, please visit the [access](https://docs.hpc.ucdavis.edu/general/access/)
documentation page.

![HiPPO](../img/HiPPO.png){ align="right"}

## HiPPO

The High-Performance Personnel Onboarding (HiPPO) portal can provision resources for the Farm, Franklin, Hive, and
Peloton HPC clusters. Users can request an account on [HiPPO](https://hippo.ucdavis.edu) by logging in with UC Davis CAS
and selecting their PI in the `Select a group` box.

Cluster specific information:

- Farm: Users who do not have a PI and who are affiliated with the College of Agricultural and Environmental Sciences
  (CA&ES) can select the `CA&ES Free Tier sponsored by Adam Getchell` group.

- Franklin: No public/free-tier available.

- Hive: Staff, faculty, and graduate students who do not have a PI can select the `UCD HPC Sponsored Public Access`
  group.

- Peloton: Users who do not have a PI and who are affiliated with the College of Letters and Science (L&S) can select
  the Jeremy Phillips (IT director for L&S) `jeremygrp` group.

### How to request a new account or access to a group

#### How to request a new account on a cluster

??? note "Click to expand"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster you would like an account on.
    1. Under `Who is sponsoring your account?`
        - If you are a PI, enter `New Sponsor Onboarding`.
        - If you have a PI, search for their name.
        - If you need access to the free-tier, see above (Cluster specific information).
    1. Under `Who is your supervising PI?`
        - If you are the PI, enter `self`.
        - If you have a PI, enter the PI's name.
        - If you need access to the free-tier, enter `free-tier`.
    1. Under `Access Type`, select one or more:
        - If you only need access to [Open OnDemand](/software/ondemand/), select `OpenOnDemand`.
        - If you need to SSH to the cluster, select `SshKey`.
        - Note: Hive allows SSH with campus passphrases or a SSH key, all other clusters **require** a SSH key.
        - For help generating a SSH key, see [How do I generate an SSH key pair?](/general/access/#how-do-i-generate-an-ssh-key-pair)

#### How to request access to another group on a cluster

??? note "Click to expand"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster.
    1. Click the `Request Access to Another Group` button.
    1. In the first box (`Select a group`):
        - If you are a PI, enter `New Sponsor Onboarding`.
        - If you have a PI, search for their name.
        - If you need access to the free-tier, see above (Cluster specific information).
    1. Under `Who is your supervising PI?`
        - If you are the PI, enter `self`.
        - If you have a PI, enter the PI's name.
        - If you need access to the free-tier, enter `free-tier`.
    1. Click `Confirm.

#### How do I, as a PI, become a sponsor?

??? note "Click to expand"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster you would like an account on.
    1. Click the `Request Access to Another Group` button.
    1. In the first box (`Select a group`):
        - Enter `New Sponsor Onboarding`.
    1. Under `Who is your supervising PI?`
        - Enter `self`.
    1. Click `Confirm.

### How long does it take my account to be created

After accounts, or account changes, are requested, the group owner will need to approve it. Once that approval happens,
accounts should be live on the cluster within one hour.

## HPC1 and HPC2

Users who are associated with PI's in the College of Engineering can request accounts on
[HPC1](https://wiki.cse.ucdavis.edu/cgi-bin/engr.pl) and [HPC2](https://hpc.ucdavis.edu/form/account-request-form) by
going to the appropriate web form.

## LSSC0 (Barbera)

Users who want access to resources on LSSC0 can request an account within the Genome Center Computing
[Portal](https://computing.genomecenter.ucdavis.edu/) and selecting 'Request an Account' with their PI.

## Atomate

Atomate accounts can be requested [here](https://wiki.cse.ucdavis.edu/cgi-bin/atomate.pl).

## Cardio, Demon, Impact

Accounts on these systems can be requested [here](https://wiki.cse.ucdavis.edu/cgi-bin/index2.pl).
