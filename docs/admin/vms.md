# Virtual Machines

HPCCF uses [Proxmox](https://www.proxmox.com/en/) for virtualization.  Current
servers are `proxmox1`, `proxmox2`, and `proxmox3`.  

To log in, point your browser to `port 8006` on any of the proxmox servers, and choose
`UCD-CAS` as the realm.

## Create a new VM

Use [Netbox](netbox) to locate a free IP address, or allocate one in the appropriate
[cobbler](cobbler) server.  Choose an empty VM ID number.  

To add a new ISO, copy it to `/mnt/pve/DDN-ISOs/template/iso/` on one of the
proxmox hosts.

Click on "create VM".  Defaults are fine for most options.  Do make sure to select
`VirtIO (paravirtualized)` for the network type.  See Netbox for a 
[list of vlans](https://netbox.hpc.ucdavis.edu/ipam/vlans/).

Do not forget to add to [DNS](dns).

## Migrate a VM

Click on the VM you wish to migrate and choose "migrate" from the top bar.
