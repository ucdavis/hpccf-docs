---
template: admin.html
title: LSSC0
---

## AFS

#### Become the AFS admin:

1. `kinit admin`
1. `aklog`

### Do admin things

#### List AFS group memberships

`pts membership admin:rcc`

#### Show AFS groups a user is a member of

`pts membership omen`

#### Add a user to an AFS group

`pts adduser -user omen -group admin:rcc`

## Firewalls

### Names

Genome Center firewalls are in pairs and run FreeBSD. Normally, the 1st one in the pair will be the primary/active.

TODO: add the actual VLANs (CR name, CIDR, and tag #) that each pair covers.

#### General

1. fw1.genomecenter
1. fw2-gc4.genomecenter

#### Instrument VLAN

1. inst-fw1
1. inst-fw2

#### HPC VLANs

1. fw1.hpc
1. fw2.hpc

### To access

```console
ssh GCLoginID@garbanzo.genomecenter.ucdavis.edu
ssh root@FireWall#1
```

### To make rule changes

1. `ssh root@active(usually #1)`
1. Figure out which file to edit: `ls -l /etc/pf.conf*`
1. Edit resolved symlink: `vim ResolvedSymlink`
1. Check to make sure new rules can load: `pfctl -n -f /etc/pf.confFullNameOfSymlink`
1. Apply the new rules: `pfctl -f /etc/pf.confFullNameOfSymlink`
1. Check into git:
    1. `kinit GCLoginID`
    1. `cd /opt/gc/config/pf`
    1. `git status`
    1. `git add file1 file2 file3 ...`
    1. `git commit`
    1. `git push`
1. Apply to other firewall in pair:
    1. `ssh root@#2`
    1. `kinit GCLoginID`
    1. `cd /opt/gc/config/pf`
    1. `git pull`
    1. `pfctl -n -f /etc/pf.confFullNameOfSymlink`
    1. `pfctl -f /etc/pf.confFullNameOfSymlink`

## Allied Telesis switches

https://docs.google.com/document/d/1aHBZtZ_hx0vyjEEpX8jYg32Cb9MsBPanXtjb1viHtow/edit?tab=t.0

TODO: move gdoc here.

## DNS

Dunno, but it probably looks a bit like firewall changes? Maybe.
