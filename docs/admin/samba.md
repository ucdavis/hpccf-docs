---
template: admin.html
title: Samba Access to HPC@UCD Storage
---

## How to grant Samba access on supported clusters

Currently, Samba is supported on Hive and Franklin.

### Hive

Hive's Samba access is currently controlled through Puppet. At the top of `data/nodes/samba.hive.hpc.ucdavis.edu.yaml`,
there is a `hpccf::samba::users:` section with a list of Hive users that will have Samba passwords created for them by
Puppet.

1.  Verify the user is on Hive and is in a group that has a Samba share.

    -   As of this documentation publication, the only group is:

        -   `metabolomicsgrp`

            -   Access IP: `128.120.208.42`

    -   You can verify on `samba.hive` with `grep 'grp]' /etc/samba/smb.conf`

1.  Edit that file to add the new user's Login ID and ticket # number to the list under the appropriate group comment.

    ???+ Note "hpccf::samba::users:"

        ```yaml
        hpccf::samba::users:
        # hpccfgrp
        - mclewis
        - omen
        # metabolomicsgrp
        ...
        - newuserhere # INCNNNNNNN
        ```

1.  Commit the changes to git.

1.  Push the changes to GitHub.

1.  Run puppet on `puppet.hive`.

1.  verify `~{newuserhere}/samba-password` exists, update the ticket with wording like:

    ???+ Note "INC wording"

    ```
    You have been added to Hive's Samba. Your password for this service can be found in "[code]<code>~/samba-password</code>[/code]" on Hive. The share is "[code]<code>metabolomicsgrp</code>[/code]" and the host IP is 128.120.208.42.

    Let me know if you have additional questions or run into any issues.
    ```

    **Note:** the IP may depend on the group.

#### TODO: automate through Cheeto

This entire process should be moved into Cheeto with Puppet applying the changes. This requires Cheeto to support
Quobyte, and probably additional development.

### Franklin

TODO
