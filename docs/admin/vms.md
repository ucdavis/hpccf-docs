---
template: admin.html
title: Virtual Machines
---

HPCCF uses [Proxmox](https://www.proxmox.com/en/) for virtualization.  Current
servers are `proxmox1`, `proxmox2`, and `proxmox3`.  

To log in, point your browser to `port 8006` on any of the proxmox servers, and choose
`UCD-CAS` as the realm.  You'll need to be on the HPC VLAN to access the interface.

## Create a new VM

Use [Netbox](../netbox) to locate a free IP address, or allocate one in the appropriate
[cobbler](../cobbler) server.   See [provisioning](../provisioning) for more information 
on selecting an IP/hostname and setting up PXE.

### General

Choose an unused VM ID.  Storage areas are pre-created on the DDN, on directory per
VM ID.  If more need to be created, see the [DDN documentation](../ddn).  Populate
the "Name" field with your chosen VM name.

### OS

If you're installing a machine via PXE from a cobbler server, choose "Do not use
any media."

To add a new ISO, copy it to `/mnt/pve/DDN-ISOs/template/iso/` on one of the
proxmox hosts.

### System

Check the `Qemu Agent` box.

### Disk

Defaults are fine.  Adjust disk size as needed.

### CPU

Use type `x86-64-v3`.  Adjust cores to taste.

### Memory

Recent Ubuntu installer will fail unless you use at least 4096.

### Network

See Netbox for a [list of vlans](https://netbox.hpc.ucdavis.edu/ipam/vlans/).

Make sure to select  `VirtIO (paravirtualized)` for the network type.  

### Finish

Do not forget to add to [DNS](../dns).

If this is a production VM, add the "production" tag.
