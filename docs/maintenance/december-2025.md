---
title: December 2025 Maintenance Window
---

The Fall 2025 maintenance window coincides with the campus data center generator test and is scheduled for the week of
December 15th. HPC@UCD will be bringing servers down on Monday, December 15th, and they will be made available for use
after planned maintenance tasks are completed. During this time, Farm, Franklin, and Hive will be unavailable for use,
and all jobs will be stopped.

## All Clusters

During the maintenance window, the following software items will be updated:

- CVMFS (Software Module Distribution)
- Linux Cgroups
- NVidia GPU drivers
- Open OnDemand
- Slurm
- ZFS

## Farm Specific

Farm sells hardware and storage with a five-year guarantee. Many Farm hardware components have exceeded their lifecycle
and will be retired during the December 2025 maintenance window. At the request of CAES IT, all hardware more than five
years old will be retired, and those Slurm partitions will be removed. Additionally, the partition names for the newer
hardware will be renamed.

### Farm Slurm Partition Status as of December 15, 2025

| Old partition name    | New Name/Status                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------ |
| `high2`               | `high`                                                                                     |
| `med2`                | Deleted                                                                                    |
| `low2`                | `low`                                                                                      |
| `high`                | Deleted                                                                                    |
| `med`                 | Deleted                                                                                    |
| `low`                 | Deleted                                                                                    |
| `bigmemh`             | Deleted                                                                                    |
| `bigmemm`             | Deleted                                                                                    |
| `bigmeml`             | Deleted                                                                                    |
| `bit150h`             | Deleted                                                                                    |
| `ecl243`              | Deleted                                                                                    |
| `bmh` / `bmm` / `bml` | Untouched                                                                                  |
| `gpul`                | Functionality folded into `low`. Access with: <br/>`--partition=low --gres=gpu:TYPE:COUNT` |

If you need to start an order for new hardware, see
[https://hippo.ucdavis.edu/Farm/product/index](https://hippo.ucdavis.edu/Farm/product/index). Note that there are
significant delays in the delivery of computing hardware.

## Franklin Specific

## Hive Specific
