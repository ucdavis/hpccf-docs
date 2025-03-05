---
template: admin.html
title: Provisioning
---

#How to Provision a New Node
##Receive
Once a node is received, check the PO against [NetBox](https://netbox.hpc.ucdavis.edu). 
If there is a note with a location specified, update the node information to reflect
that location. Add the serial number. 
##Rack
Rack the node in the location specified in [NetBox](https://netbox.hpc.ucdavis.edu). Connect
BMC, 10G fiber and Infiniband. If the node has a Mellanox 25G fiber card, connect a secondary
install cable to the 10G copper interface. 
##Record
Record interfaces and relevant cable connections in NetBox. Make a note of the BMC IP.
The bare minimum that needs to be recorded is the BMC MAC address, primary fiber ethernet MAC
address, secondary install MAC address (if connected), and board serial number. 
##Connect
Connect to the BMC via. the IP address recorded previously. Passwords depend on the chassis manufacturer.
###Asus
The default username is `admin` and the default password is `admin`. When connecting
to the BMC for the first time, you will be prompted to set the password. Use the value
from 1Password.
###Gigabyte
The default username is `admin` and the default password is the board serial number. 
##Install
Follow the [Cobbler](/admin/cobbler) instructions for node installation.
