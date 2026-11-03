---
title: December 2026 Maintenance Window
---

The fall 2026 maintenance window coincides with the campus data center generator test and will be scheduled for the week of
December 7th, pending approval from IET. HPC@UCD plans to bring servers down on Monday, December 7th, and they will be made available for use
after planned maintenance tasks are completed. During this time, Farm, Franklin, and Hive will be unavailable for use,
and all jobs will be stopped.

Jobs that have a runtime longer than the current time until the start of the maintenance window will not start. This
exact amount of time is printed every time you log in to each of the clusters. If your job is held because of the
maintenance reservation, you will see this in your `squeue` output:

`(ReqNodeNotAvail, Reserved for maintenance)`

Stay tuned for updated information as the date approaches. 
