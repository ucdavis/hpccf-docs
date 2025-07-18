---
template: admin.html
title: Cobbler
---

HPC@UCD uses [cobbler](https://cobbler.github.io/) for provisioning and managing internal [DNS](../dns).

There is a cobbler server per cluster as well as one for the public HPC VLAN.

-   `cobbler.hpc` - public HPC VLAN.
-   `cobbler.hive` - hive private and management VLANs
-   `cobbler.farm` - farm
-   `cobbler.peloton` - peloton
-   `cobbler.franklin` - franklin

`hpc1`, `hpc2`, and `lssc0` do not have associated cobbler servers.

## Add a new host

### Hive

`**something**` or bold text must be replaced with correct, per-host values.

???+ "Initial setup"

    ```console
    ssh root@cobbler.hive
    cd /var/www/cobbler-html
    export HOSTNAME=**cluster-location-row-rack-U*2**
    ```

    **Pay attention to the output from the scripts.** Some of it is large amounts of spew from cobbler, but the rest could have critical information.

    Configure the BMC first.

    `./cobbler-add-from-netbox.sh "$HOSTNAME" bmc`

    Then the main Ethernet iface.

    If this is a host with a 25G Mellanox Ethernet card that we have not
    been able to PXE boot from, you need to add: **-I InstallationEthDeviceFromNetbox**

    `./cobbler-add-from-netbox.sh -I eth**M** "$HOSTNAME" eth**N**`

    IFF this is not a _standard_ hive node disk configuration (pair of smaller, one larger NVMe),
    you will need to add: `-d name_of_disk_layout_template`

    Available options in: `hpccf-cobbler-templates/partitions/`

    Pay attention to the information at the end, it will have the installation hostname, IP, BMC hostname, BMC IP, etc.

[UPDATE BIOS TO PXE INSTALL](/admin/PXE/)

Reset the system, watch in BMC, OR, watch in SSH: `ssh installer@**HOSTNAME**(-install)?`

Wait for installation to finish

???+ "Find production Ethernet MAC"

    `ssh root@**HOSTNAME**(-install)?`

    Look at `ethtool '*'` and `ifconfig eth*N*` to figure out which one is the >1G Ethernet connection that will be used in production.

???+ "Puppet work"

    `ssh puppet.hpc`

    * Create: `data/nodes/**HOSTNAME**.hive.hpc.ucdavis.edu.yaml`

    * Contents: `infiniband::network::netplan::ethmac: **10G::mac::addr:here**`

    ```console
    git add data/nodes/**HOSTNAME**.hive.hpc.ucdavis.edu.yaml
    git commit
    ```

    Contact Omen or Camille for review and push. Note, this change will go live on Hive without a push.

???+ "Final host work"

    ```console
    ssh **HOSTNAME**(-install)?**
    puppet agent -t
    reboot
    ```

???+ "Verify host rebooted correctly"

    ```console
    ssh $USER@**HOSTNAME**`
    sudo puppet agent -t
    ```

    Verify this Puppet run did not make any changes.

    Verify everything looks okay

???+ "Check Monitoring"

    Verify no alerts:

    `https://monitoring.hpc.ucdavis.edu/icingaweb2/monitoring/host/services?host=**fqdn**`

???+ "Update Slurm's topology"

    Farm and Hive are using Slurm's topology plugin. The InfiniBand switch connection data requires re-generation every time a node with InfiniBand is added, or removed.

    ```console
    ssh -A $USER@hive-dc-7-10-18
    ib-topology-generate.py --topology --cluster=**cluster** # <-- Can be either Hive or Farm
    ```
    Follow printed instructions to scp the newly generated file to puppet, then:
    ```console
    ssh $USER@puppet.hpc
    cd /etc/puppetlabs/code/environments/production
    git commit modules/hpccf/slurm/templates/**cluster**.hpc.ucdavis.edu/slurm/topology.conf.epp
    ```
    Contact Omen or Camille for review and push. Note, this change will go live on Hive without a push.

???+ "Validate node"

    Add to Slurm's `burnin` partition.

    Checklist TBD, but including test in Slurm.

    Move to Slurm's production partition(s).

Rejoice.
