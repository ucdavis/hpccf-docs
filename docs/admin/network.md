---
template: admin.html
title: Network
---
#Network Overview
Our core network is split between Ethernet and Infiniband. The Ethernet backbone goes through 
Juniper EX and QFX switches and the Infiniband switches are from Nvidia (formerly Mellanox).
## Ethernet
### Configuring VLANs
#### EX
Log in to EX (Distribution) stack (details in [NetBox](https://netbox.hpc.ucdavis.edu)). The prompt will end with `%`. 
Enter the CLI. 
The prompt ending will change to `>` and a note about the current master will appear. 

> `% cli`

Enter Configuration mode. The prompt ending will change once more, this time to `#`. The word `edit` will 
appear beside the previous note. 

> `> conf`

Once in configuration mode, issue the following command, adjusting interface name and VLAN name as necessary. 

> `# set interfaces ge-0/0/44.0 family ethernet-switching vlan members HPCCF-1-NR`

When finished with your changes, commit them.

> `# commit`

#### QFX 

There are some diffrences when setting an interface on a QFX switch. We need to remove the `inet` family first. 
Log in to QFX (Core) stack (details in [NetBox](https://netbox.hpc.ucdavis.edu)). The prompt will end with `%`. 
Enter the CLI. 
The prompt ending will change to `>` and a note about the current master will appear. 

> `% cli`

Enter Configuration mode. The prompt ending will change once more, this time to `#`. The word `edit` will 
appear beside the previous note. 

> `> conf`

Once in configuration mode, issue the following commands, adjusting interface name and VLAN name as necessary. 

> `delete interfaces xe-0/0/28:0 unit 0 family inet`

> `set interfaces xe-0/0/28:0 unit 0 family ethernet-switching interface-mode access vlan members HPCCF-1-NR`

When finished with your changes, commit them.

> `# commit`

##Infiniband
### Cable Orientation
Cables will lock in place when properly inserted. Based on the position of the card, the cable may be oriented 
differently. When using a dual port card, make sure that the primary connection is next to the indicator lights. 
