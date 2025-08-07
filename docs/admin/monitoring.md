---
template: admin.html
title: Monitoring
---

## icinga2

We have two icinga2 deployments -- one for [farm](../farm/index.md), and one that covers [hive](../hive/index.md) and our internal infrastructure.

- farm: [https://monitoring.farm.ucdavis.edu/icingaweb2/](https://monitoring.farm.ucdavis.edu/icingaweb2/)
- hpc: [https://monitoring.hpc.ucdavis.edu/icingaweb2/](https://monitoring.hpc.ucdavis.edu/icingaweb2/)

Both are CAS-protected.

## puppetboard

Our primary puppet server exposes a puppetboard instance, which is also CAS-protected, that can be used to monitor the puppet clients:

- [https://puppet.hpc.ucdavis.edu/puppetboard/](https://puppet.hpc.ucdavis.edu/puppetboard/)

## grafana

Farm has a dedicated grafana instance for metrics collection:

- [https://monitoring.farm.ucdavis.edu/grafana/dashboards](https://monitoring.farm.ucdavis.edu/grafana/dashboards)

## Statuspage

Hive and Farm have dedicated Atlassian Statuspages for public incident tracking:

- Hive: [https://status.hpc.ucdavis.edu/](https://status.hpc.ucdavis.edu/)
- Farm: [https://status.farm.caes.ucdavis.edu/](https://status.farm.caes.ucdavis.edu/)

