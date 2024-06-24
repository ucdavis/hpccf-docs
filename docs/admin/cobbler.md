# Cobbler

HPCCF uses [cobbler](https://cobbler.github.io/) for provisioning and managing
internal [DNS](dns).

There is a cobbler server per cluster as well as one for the public HPC VLAN.

- `cobbler.hpc` - public HPC VLAN.
- `cobbler.hive` - hive private and management VLANs
- `cobbler.farm` - farm 
- `cobbler.peloton` - peloton
- `cobbler.franklin` - franklin

`hpc1`, `hpc2`, and `lssc0` do not have associated cobbler servers. 

## Add a new host

```
cobbler system add --name=<hostname> --profile=infrastructure --netboot=false --interface=default --mac=xx:xx:xx:xx:xx:xx --dns-name=hostname.cluster.hpc.ucdavis.edu --hostname=<hostname> --ip-address=10.11.12.13
```
