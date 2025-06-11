---
template: admin.html
title: DNS
---

TODO: allow the Globus flag to be set by Cheeto per-share and put the work back into Puppet.

TO SOLVE: how to auto-login when Puppet runs the commands?

Hosts to run the commands on:

-   `hive`: `transfer.hive`

-   `farm`: login node

-   `franklin`: login node

```bash
> sudo su - globus-user

# Password in 1pass
> globus-connect-server session update ucdhpc@globusid.org

> export PI_SHARE="ShareName11" # WITHOUT any path components
> export PI="PI-Login-ID"
> export PI_GRP="PI-Group-Name"

> ./bin/globus-storage-gateway-user-directories.sh $PI_SHARE $PI $PI_GRP

> ./bin/globus-storage-gateway.sh $PI_SHARE $PI $PI_GRP
Collection ID: UUID
```

If you do not get a `Collection ID:` printed, re-run the `globus-storage-gateway.sh` command.

```bash
# Verify it all worked
> globus-connect-server collection show UUID-from-above
Display Name:                farm.hpc.ucdavis.edu: jbondgrp2
Owner:                       ucdhpc@globusid.org
ID:                          UUID
Storage Gateway ID:          DIFFERENT UUID

```

Login to [https://app.globus.org/](https://app.globus.org/), and search for the `Display Name:` shown in the show
command.

Send the `Display Name:` to the PI/ticket for what to search for.
