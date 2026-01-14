---
title: December 2025 Maintenance Window
---

The fall 2025 maintenance window coincides with the campus data center generator test and is scheduled for the week of
December 15th. HPC@UCD will be bringing servers down on Monday, December 15th, and they will be made available for use
after planned maintenance tasks are completed. During this time, Farm, Franklin, and Hive will be unavailable for use,
and all jobs will be stopped.

Jobs that have a runtime longer than the current time until the start of the maintenance window will not start. This
exact amount of time is printed every time you log in to each of the clusters. If your job is held because of the
maintenance reservation, you will see this in your `squeue` output:

`(ReqNodeNotAvail, Reserved for maintenance)`

## All Clusters

During the maintenance window, the following software items will be updated:

- CVMFS (Software Distribution)
- Linux cgroups
- NVidia GPU drivers
- Open OnDemand
- Quobyte
- Slurm
- ZFS

## Farm Specific

Farm sells hardware and storage with a five-year guarantee. Many Farm hardware components have exceeded their lifecycle
and will be retired during the December 2025 maintenance window. At the request of CA&ES IT, all hardware more than five
years old will be retired, and those Slurm partitions will be removed. Additionally, the partition names for the newer
hardware will be renamed.

### Farm Slurm Partition Status as of December 15, 2025

| Old partition name | New Name/Status                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------ |
| `bigmemh`          | Deleted                                                                                    |
| `bigmeml`          | Deleted                                                                                    |
| `bigmemm`          | Deleted                                                                                    |
| `bigmemht`         | Deleted                                                                                    |
| `bit150h`          | Deleted                                                                                    |
| `bmh` / `bml`      | No change                                                                                  |
| `bmm`              | Deleted                                                                                    |
| `ecl243h`          | Deleted                                                                                    |
| `gpul`             | Functionality folded into `low`. Access with: <br/>`--partition=low --gres=gpu:TYPE:COUNT` |
| `gpuh` / `gpum`    | No change                                                                                  |
| `high`             | Deleted                                                                                    |
| `high2`            | `high`                                                                                     |
| `low`              | Deleted                                                                                    |
| `low2`             | `low`                                                                                      |
| `med`              | Deleted                                                                                    |
| `med2`             | Deleted                                                                                    |

If you need to start an order for new hardware, see
[https://hippo.ucdavis.edu/Farm/product/index](https://hippo.ucdavis.edu/Farm/product/index). Note that there are
significant delays in the delivery of computing hardware.

### ALL Farm queued jobs killed

Because of the above partition work, all queued jobs had to be killed.

### New Public Access Group Name

The long-term group name used for free-tier Farm access will be changing. The new group name will be `publicgrp`, but
the description in Hippo will remain the same (`CA&ES Free Tier sponsored by Adam Getchell`). All users in the previous
group will be automatically transitioned.

### Changed Public Access to Resources

As part of the CA&ES-requested changes to Farm during the December maintenance window, sponsored access to all high
partitions was removed. The only sponsored compute resources available on Farm are accessed through the low partition.

The low partition has access to all unused resources on Farm. For instance, you can request GPU resources with
--partition=low --gres=gpu:1, or you can request access to an abundance of RAM with --mem=300G.

Please note that the high2 partition has been renamed to high, and users who were formerly in the adamgrp are now
members of publicgrp.

To view all partitions you have access to on Farm, please run: /opt/hpccf/bin/slurm-show-resources.py --full

### New Login Node

Farm's login node will be upgraded to a new system. Changes:

- CPUs: 32 -> 256
- RAM: 64 GB -> 512 GB

## Franklin Specific

None at this time.

## Hive Specific

### New Login Nodes

The two current virtual login nodes will be replaced with physical hardware. Changes:

- CPUs: 32 -> 64
- RAM: 64 GB -> 256 GB

Additionally, the physical machines have InfiniBand, which should reduce overhead when accessing storage.

### H100 GPUs removed

The PI who owned the single Hive node with H100s has withdrawn it. This means Hive no longer has any H100 available to
be used in `low`.
