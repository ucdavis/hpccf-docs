---
title: Migration from LSSC0 to Hive Email
---

!!! Note "The following email will be sent to each PI as we work through the migration process"

    All

    We are starting the process of migrating users, hardware, and data from LSSC0 to Hive. Labs with login or GPU nodes
    under seven years of age will be migrated to Hive according to our hardware policy at
    https://hpc.ucdavis.edu/model-hpc-hardware-support.

    Please ensure that the software currently used by your team on LSSC0 is available on Hive. If you need specific
    software, please let us know by requesting it using the Software Request Form at
    https://hpc.ucdavis.edu/software-installation-policy . Existing software can be searched with:
    `module avail -l | grep -i softwarename`

    PIs are first required to make an account on Hive by going to the High-Performance Personnel Onboarding Portal at
    https://hippo.ucdavis.edu, selecting Hive as their cluster, and enter the `New PI Onboarding (sponsors)` group. HPC@UCD
    staff will approve the request, and the new PI group will be available for users to select. Documentation here:
    https://docs.hpc.ucdavis.edu/general/account-requests/#if-you-are-a-pi-and-have-bought-or-are-planning-to-purchase-resources

    Once the PI group has been created, users are required to make an account on Hive by going to the High-Performance
    Personnel Onboarding Portal at https://hippo.ucdavis.edu, selecting Hive as their cluster, and selecting their PI/lab’s
    group. The PI will receive an email with a link to approve the request. Once it is approved, the user will be added to
    the PI's group and will be able to log in to Hive. Documentation here:
    https://docs.hpc.ucdavis.edu/general/account-requests/#if-you-are-a-pi-and-have-bought-or-are-planning-to-purchase-resources

    Users are responsible for migrating their home directory to Hive. We have helpful instructions for those users who need
    assistance with rsync at https://docs.hpc.ucdavis.edu/hive/lssc0-data-migration/

    The lab share data migration takes place over several steps:

    1. HPC staff will copy group data from LSSC0 to Hive during an initial pass.

    1. PIs will be notified via Service Now email to stop jobs in preparation for a second pass of data and to arrange for
    the final transition to Hive. Service Now tracking allows HPC staff to keep PIs notified and the status tracked.

        Note: HPC staff will add a `.CSV` file to the ticket with user and group information from the Genome Center
        Computing Portal. It is the PI’s responsibility to validate that the group information is correct so that HPC staff
        can map user data from LSSC0 to Hive during the migration process.

        Users who have not made accounts on Hive will have their group data owned by the PI.

    1. Login nodes under seven years of age will be migrated to Hive, and groups will be provisioned with like resources.
    Login nodes over seven years of age will be decommissioned.

    1. Final pass of data and permissions adjustment. Data on LSSC0 will be marked read-only.

    HPC@UCD is maintaining a list of Frequently Asked Questions:
    https://docs.hpc.ucdavis.edu/hive/lssc0-data-migration/#what-happens-with-my-lssc0-backed-up-data
