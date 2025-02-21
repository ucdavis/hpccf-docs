---
template: admin.html
title: Cobbler
---

HPCCF uses [cobbler](https://cobbler.github.io/) for provisioning and managing internal [DNS](../dns).

There is a cobbler server per cluster as well as one for the public HPC VLAN.

- `cobbler.hpc` - public HPC VLAN.
- `cobbler.hive` - hive private and management VLANs
- `cobbler.farm` - farm
- `cobbler.peloton` - peloton
- `cobbler.franklin` - franklin

`hpc1`, `hpc2`, and `lssc0` do not have associated cobbler servers.

## Add a new host

### Hive

`**something**` or bold text must be replaced with correct, per-host values.

???+ "Initial setup"

    ```
    ssh root@cobbler.hive
    cd /var/www/cobbler-html
    HOSTNAME=**cluster-location-row-rack-U*2**
    ```

    **Pay attention to the output from the scripts.** Some of it is large amounts of spew from cobbler, but the rest could have critical information.

    Configure the BMC first:

    `./cobbler-add-from-netbox.sh "$HOSTNAME" bmc`

    Then main Ethernet iface:

    If this is a host with a 25G Mellanox Ethernet card that we have not
    been able to PXE boot from, you need to add: **-I InstallationEthDeviceFromNetbox**

    `./cobbler-add-from-netbox.sh -I eth**N** "$HOSTNAME" eth**N**`

    IFF this is not a _standard_ hive node disk configuration (pair of smaller, one larger NVMe),
    you will need to add: `-d name_of_disk_layout_template`

    Available options in: `hpccf-cobbler-templates/partitions/`

    Pay attention to the information at the end, it will have the installation hostname, IP, BMC hostname, BMC IP, etc.

[UPDATE BIOS TO PXE INSTALL](/admin/PXE/)

Reset the system, watch in BMC, OR, watch in SSH: `ssh installer@$HOSTNAME**(-install)?**`

Wait for installation to finish

???+ "Find production Ethernet MAC"

    `ssh root@$HOSTNAME**(-install)?**`

    Look at `ethtool '*'` and `ifconfig eth*N*` to figure out which one is the >1G Ethernet connection that will be used in production.

???+ "Puppet work"

    `ssh puppet.hpc`

    * Create: `data/nodes/**HOSTNAME**.hive.hpc.ucdavis.edu.yaml`

    * Contents: `infiniband::network::netplan::ethmac: **10G::mac::addr:here**`

    ```
    git add data/nodes/**HOSTNAME**.hive.hpc.ucdavis.edu.yaml
    git commit
    ```

    Contact Omen or Camille for review and push. Note, this change will go live on Hive without a push.

???+ "Final host work"

    ```
    ssh $HOSTNAME**(-install)?**
    puppet agent -t
    reboot
    ```

???+ Verify host

    `ssh $USER@$HOSTNAME`

    Verify everything looks okay

???+ "Check Monitoring"

    Verify no alerts:

    `https://monitoring.hpc.ucdavis.edu/icingaweb2/monitoring/host/services?host=**fqdn**`

Add to Slurm.

Rejoice.
