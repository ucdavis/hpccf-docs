---
template: admin.html
title: Internal HPCCF Scripts
---

Like every sysadmin group in the world, we have a number of internal-use scripts to accomplish various tasks. Some of
the standout scripts are documented here.

## /opt/hpccf/bin/

-   `cleanup.sh` `directory`: cleanup the emacs and jed editor detritus.

-   `sacctmgr-show-qos.sh`: show the Slurm QoS settings.

-   `showuser.sh` `LoginID`: Show information about a user from LDAP and Slurm.

-   `slurm-job-history.sh` `[today|yesterday|week|(2,3-)months|year] [user|node|job|account] query-subject`: a wrapper
    for `sacct`.

-   `ucd` `Name | email`: check our LDAP tree to try to figure out who a user is.

-   `zfs-list.sh`: show zfs file-systems with compression and quota.
    -   Optional arguments passed directly to `zfs list`.

## /opt/hpccf/sbin/

These commands normally require sudo.

-   `cobbler-add-*.sh`: obsolete scripts to add new nodes. The replacement [pulls from NetBox](/admin/cobbler/).

-   `cvmfs-transaction` `open | close | status`: a wrapper for starting/stopping a CVMFS transaction.

-   `hpccf-mkswap.sh`: generate the swap file in the `/scratch/` directory. Called by a systemd unit file on boot.

-   `ib-topology-generate.py`: a wrapper around `ibnetdiscover` to pretty-print the InfiniBand links. - Optional
    arguments:

    -   `-s | --switches-only`: only show switch-to-switch links.

    -   `-g | --graphviz`: generate GraphViz output in `ib-topology.dot`. Visualize with `xdot` or
        [Graphviz Visual Editor](https://magjac.com/graphviz-visual-editor/).

-   `ipmi.sh` `NodeName` `ipmi command to run`: wrap ipmitool to automatically use our IPMI username and password.

-   `iptables-disable.sh`: purge the host's iptables firewall. Use for testing only. Puppet will re-create the rules on
    next run.

-   `ldap-authorized-keys.sh`: pull the user's keys from LDAP. Used when users log in.

-   `mlx-node-desc.sh`: updated the InfiniBand node description with the hostname so it show up in `ibnetdiscover`.

-   `puppetserver-production-git-pull.sh`: called from cron to pull the newest git Puppet data.

-   `purge-local-users.sh`: post-migration to LDAP cleanup script to purge all local users.

-   `reset-gpu-power.sh`: reset NVidia GPUs to default power limits.

-   `set-gpu-power.sh` `PowerLimitInWatts`: set the NVidia GPU power limits.

-   `slurmd-launch` | `slurmctld-launch` | `slurmdbd-launch`: a wrapper around Slurm services that exit non-zero if the
    Slurm storage is not yet available.

-   `upgrade-reboot-ALL-down-nodes.sh`: without arguments, looks for down nodes, and run the `upgrade-reboot-node.sh`
    script on them, one node per screen window.

    -   Optional arguments, one of:
        -   `node1 node2 node3 ...`
        -   `partition-name`

-   `upgrade-reboot-node.sh` `NodeName`: run the sequence of steps that bring most nodes back into compliance and tries
    to re-add the node to Slurm.

-   `victoria-download.sh` `logs | metrics` `version`: download the specified version of the Victoria product and stow
    it.

-   `whoami-ssh`: process the authlog for SSH ssh keys to figure out who the actual logged-in user is.
