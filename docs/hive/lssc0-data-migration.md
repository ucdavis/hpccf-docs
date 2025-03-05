---
title: Migrating data from LSSC0
---

## Data migration:

### Group/PI/Lab directories:

Group directories on Hive are mounted on `/quobyte/`. Please ensure that your group or lab has purchased resources
before you move data. Group directories are named after the PI or lab owner. For group directories, HPCCF staff are
happy to take care of the actual migration, but we will need to coordinate with each PI group to do the transfer. The
process looks like this:

1. The PI
   [requests a `sponsor` account on Hive](/general/account-requests/#if-you-are-a-pi-and-have-bought-or-are-planning-to-purchase-resources).

1. The PI logs into Hive to verify access.

1. All users that need access to the PI's resources on Hive requests access (either
   [`new account`](/general/account-requests/#how-to-request-a-new-account-on-a-cluster), or
   [`access to another group`](/general/account-requests/#how-to-request-access-to-another-group-on-a-cluster)) through
   Hippo.

    1. The PI approves each of those requests, allowing the accounts to be created on Hive.

1. The PI opens a ticket with HPCCF by emailing hpc-help@ucdavis.edu.

    1. In that ticket, the PI provides the LSSC0 Login ID and the corresponding UC Davis email address.

    1. Any user that does not have an active UC Davis account, will be required to create on through the
       [TAF process](https://taf.ucdavis.edu/). This TAF process happens between the PI and the user, HPCCF is not
       involved in any way.

1. HPCCF starts the initial pass of the data copy.

1. Once that finishes, HPCCF will coordinate with the PI (through the ticket opened above) for a 24-72 business-hour
   period where no new data will be added on the LSSC0 side and HPCCF will perform the final data copy to ensure Hive
   contains everything that LSSC0 contains. The exact amount of time will depend on the quantity of data and the number
   of files.

1. The share on LSSC0 will be set to read-only, and eventually fully disabled (internally renamed with
   `MIGRATED-TO-HIVE`).

### Home directories:

Home directories on Hive are mounted on `/home/LoginID`. For example, if your UC Davis Login ID is `cheeto`, your home
directory would be `/home/cheeto`. Home directories on Hive are expanded to 20G per person. If additional space is
required, the PI can purchase additional space for their PI group share.

#### Copy your LSSC0 home directory to Hive:

Please ensure you have an account on Hive by creating one at [HiPPO](https://hippo.ucdavis.edu), then SSH to
`transfer.hive.hpc.udavis.edu` using your Campus Login ID and passphrase (or SSH key pair if you submitted one via
HiPPO).

??? Note "Hive transfer node"

    HPCCF staff have set up a transfer node within Hive that has direct links to LSSCO networking to facilitate
    data transfer. However, because LSSC0 home directories reside on AFS, performance may be lower than you would expect.
    This transfer node is only for moving data into Hive, it is not for general use.

Once logged into the Hive transfer node, you can run:

`rsync --archive --one-file-system --info=progress2 LSSC0-LOGIN-ID@barbera.hpc.genomecenter.ucdavis.edu:~/ from-lssc0/`

This will prompt you for your LSSC0 password. Note, your LSSC0 Login ID might not match your Campus Login ID used on
Hive.

??? Note "Sample Output"

    ```console
    ┌─omen@login1.hive: ~
    └─0 $ rsync --archive --one-file-system --info=progress2 omen@barbera.genomecenter.ucdavis.edu:~/ from-lssc0/
    omen@barbera.genomecenter.ucdavis.edu's password:
    3,192,034,589 100%  100.09MB/s    0:00:30 (xfr#10, to-chk=0/13)

    ┌─omen@login1.hive: ~
    └─0 $
    ```

#### Interrupted transfer

If, for any reason, the transfer is interrupted, you can simply re-run the command and rsync will only copy files that
have changed on lssc0, or that have not yet been copied to Hive.

### Group/PI sub-directories:

Group/PI sub-directories can be also be transferred from LSSC0 with rsync. SSH to `transfer.hive.hpc.udavis.edu` using
your Campus Login ID and passphrase (or SSH key pair if you submitted one via HiPPO).

Once logged into the Hive transfer node, you can run:

`rsync --archive --one-file-system --info=progress2 LSSC0-LOGIN-ID@barbera.hpc.genomecenter.ucdavis.edu:/share/LSSCO-PI-lab/Sub-Directory-To-Copy/ /quobyte/Hive-PI-grp/Sub-Directory-To-Copy-from-lssc0/`

-8<- "docs/include/rsync-warnings.md"

#### Interrupted transfer

See [Interrupted transfer](#interrupted-transfer) above.
