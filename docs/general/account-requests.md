# Requesting an Account

HPC accounts are provisioned on a per-cluster basis and granted with the permission of their principal investigator (PI). Accounts that are provisioned under each PI will have access to that PI's purchased resources and their own separate home directory.

Access to all HPC clusters are granted through the use of SSH keys. In addition, Hive offers password authentication using your campus passphrase. For information on creating SSH keys, please visit the [access](access.md) documentation page.

![HiPPO](../img/HiPPO.png){ align="right"}

## HiPPO

The High-Performance Personnel Onboarding (HiPPO) portal can provision resources for the Farm, Franklin, and Hive HPC clusters. Users can request an account on [HiPPO](https://hippo.ucdavis.edu) by logging in with UC Davis CAS and selecting their PI in the `Select a group` box.

Cluster specific information:

- `Farm`: Users who do not have a PI can select the `CA&ES free tier` (`publicgrp`) group.

- `Franklin`: No public/free-tier available.

- `Hive`: UC Davis staff, faculty, and graduate students who do not have a PI can select the `HPC@UCD Sponsored Public Access` (`publicgrp`) group.

### How to request a new account, access to a group, or become a PI so other users can request access your resources.

#### How to request a new account on a cluster:

???+ note "New account"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster you would like an account on.
    1. Under `Who is sponsoring your account?`
        - If you are a qualifying faculty or staff member intending to request your own group, enter: `New Sponsor Onboarding`
        - If you have a PI, search for their name.
        - If you need access to the free-tier, see above (Cluster specific information).
    1. Under `Who is your supervising PI?`
        - If you are the PI, enter: `self`
        - If you have a PI, enter the PI's name.
        - If you need access to the free-tier, enter: `free-tier`
    1. Under `Access Type`, select one or more:
        - If you only need access to [Open OnDemand](../software/ondemand.md), select `OpenOnDemand`.
        - If you need command-line access to the cluster via SSH, select `SshKey`.
        - Note: Hive allows SSH with campus passphrases or a SSH key, all other clusters **require** a SSH key.
        - For help generating a SSH key, see [How do I generate an SSH key pair?](access.md#how-do-i-generate-an-ssh-key-pair)
    1. Wait for a confirmation email that your account was created.
    1. If you are a qualifying faculty or staff member and require your own group, follow the [Request Group Creation](#if-you-are-a-pi-and-have-bought-or-are-planning-to-purchase-resources) instructions.

#### How to request access to another group on a cluster:

???+ note "Join another group"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster.
    1. Click the `Request Access to Another Group` button.
    1. In the first box (`Select a group`):
        - Search for the group you would like to join.
    1. Under `Who is your supervising PI?`
        - If you are the PI, enter: `self`
        - If you have a PI, enter the PI's name.
    1. Click: `Confirm`
    1. After you are granted access to this group's resources, you will need to specifically request it by adding `--account=NewlyGrantedPIgrp` to each `srun` or `sbatch` job.

#### If you are a PI and have bought, or are planning to purchase, resources:

???+ note "PI: Request Group Creation"

    1. Login to [HiPPO](https://hippo.ucdavis.edu)
    1. Select the cluster you have an account on.
    1. Click the `Request Group Creation` button.
    1. In `Display Name`:
        - Enter the text you would like your students to search fo
    1. Click: `Confirm`
    1. Wait for a confirmation that your group was created.
        1. Note: there is a [delay](#i-cannot-see-the-changes-pi-sponsor-or-group-membership-on-hippo) between the group being approved and showing on Hippo.

### How long does it take for my account to be created?

After accounts, or account changes, are requested, the PI (or delegated sponsor) will need to approve it. Once that approval happens, accounts and changes should be live on the cluster within one hour. You will receive an email after your account creation is started. After you receive the email, it still takes approximately 1 hour for the account to fully create.

### I cannot see the changes (PI sponsor or group membership) on HiPPO

You will not be able to see any group or sponsor changes until Hippo synchronizes the data. The synchronization happens every 15 minutes.

## HPC2

Users who are associated with PIs in the College of Engineering can request an account on HPC2 by filling out [this form](https://hpc.ucdavis.edu/form/account-request-form).

## LSSC0 (Barbera)

The LSSC0 cluster will be retired April 30th, 2026. Users who are interested in computing resources should [create an account](#how-to-request-a-new-account-on-a-cluster) on the Hive HPC cluster.

## Atomate, Cardio, Demon, Impact, Peloton

These clusters have been retired.
