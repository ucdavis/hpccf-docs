---
template: admin.html
---

# Open OnDemand

This is meant to be a general configuration guide to Open OnDemand (OOD) for admins. But, I'd also like this to serve as an admin troubleshooting tutorial for OOD. So, the bulk of relevant OOD configs are located in `/etc/ood/config/` but the contents within are controlled by puppet. Usually, OOD is served by, or behind, apache and those configs are located in `/etc/apache2/` and the default served dir is located at `/var/www/ood` but these are also heavily controlled by puppet. For the rest of this config documentation I'll be categorizing by the file names, but I'll also try to refer to the puppet-openondemand class for that file as well.

## OOD Interactive Apps
Apps in OnDemand are located in `/var/www/ood/apps/sys/<app name>`. The OOD dashboard itself is considered an app and is located here. The "dev" made apps are cloned here by puppet (`openondemand::install_apps:`) from hpccf's github (i.e. <https://github.com/ucdavis/hpccf-ood-jupyter>). OOD apps are, put simply, sbatch scripts that are generated from ERB templates. Inside the app's directory, what is of most interest to admins is the: `form.yml`, `submit.yml`, and the `template/` directory. I would guess that the majority of troubleshooting is happening here. Note that any of the files within this dir can end in `.erb` if the you want its contents dynamically generated. To learn more about apps you can find the docs here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive.html>

### form.yml
This file represents the form users fill out and the fields for selecting clusters, partitions, cpu, mem, etc. If you wanted to add another field you can do it here. Or, **if you suspect there's a bug with the web form I recommend starting here**. More about form.yml can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/form.html#>

### submit.yml
This file contains the contents of the sbatch job as well as job submission parameters that are submitted to slurm (or whatever scheduler you are using). Also, here you can configure the shell environment in which the app is run.  **If you suspect a bug might be a slurm, slurm submission, or a user environment issue I'd start here**. More about submit.yml can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/submit.html>

### template/
This directory is the template for the sbatch job that the interactive app is run in. Any code, assets, etc. necessary with the app itself should be included here. When a user launches an OOD app this directory is processed by ERB templating system then copied to `~/ondemand/data/sys/dashboard/batch_connect/sys/...`. In this directory you may see three files of interest to admins: `before.sh`, `script.sh`, `after.sh`. As their names suggest there's a script that runs before the job, one after, and the job itself. OOD starts by running the main script influenced by `submit.yml` and forks thrice to run the `before.sh`, `script.sh`, and `after.sh`. More about `template/` can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/template.html>

### view.yml
This is just the html view of the app form. I doubt you need to be editing this.

### manifest.yml
This is where you set the app's name that shows on the dashboard and the app's category. More about `manifest.yml` can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/manifest.html>

### OOD App Developers
If you want to edit, add, or create OOD apps you must be enabled as a dev app developer. In puppet this is done by placing your username under `openondemand::dev_app_users:` and puppet will then do the following:

```
mkdir -p /var/www/ood/apps/dev/<username>
sudo ln -s ~/ondemand/dev /var/www/ood/apps/dev/<username>/gateway
```
After that, you can `git clone` apps to your OOD app developer environment located in `~/ondemand/dev/`. Your dev apps will show in a separate sidebar from the production ood apps and won't be visible by anyone else unless shared.

## clusters.d
`/etc/ood/config/clusters.d/` is the config dir where OOD is coupled with a cluster and global scheduler options are specified. For OOD apps to work and be submitted to a cluster this yaml needs to be present and must be named after the cluster's hostname i.e. `/etc/ood/config/clusters.d/farm.yml`. This area is controlled by puppet under `openondemand::clusters:`. The most relevant section of this file for people not named Teddy is `batch_connect:`, and more specifically the `script_wrapper:`, is where you can put shell commands that will always run when an OOD app is ran.

### Batch Connect
```
batch_connect:
    basic:
      script_wrapper: |
        source /etc/profile
        module purge
        %s
      set_host: host=$(facter fqdn)
    vnc:
      script_wrapper: |
        source /etc/profile
        module purge
        module load conda/websockify turbovnc
        export WEBSOCKIFY_CMD="websockify"
        turbovnc-ood
        %s
      set_host: host=$(facter fqdn)
```

### Script Wrapper
Under `batch_connect:` is the script wrappers listed by the parent app category. Apps like JupyterLab and RStudio are in the `basic` category, and VNC has its own category. Anything set in the `script_wrapper:` under the app category is always run when an app of that category is run. So if you add a `module load openmpi` to the script wrapper under `basic:` then that will be ran, and openmpi will be loaded, whenever RStudio or JupyterLab is started. The `%s` is a placeholder for all the scripts from the aforementioned `template/` dir . You can use the placeholder to differentiate whether you want your commands to be run before or after your OOD app is started.

The `facter fqdn` within `set_host:` key should resolve to the fqdn of the compute/gpu node the job is running on.

More about `clusters.d/` can be found here: <https://osc.github.io/ood-documentation/latest/installation/add-cluster-config.html>

## ood_portal.yml
`/etc/ood/config/ood_portal.yml` is the top most config for OOD. **Here be dragons, don't edit this file unless you know what you are doing!** Here you can set the server name and port number that OOD will listen on. As well as, OOD related apache configs, certs, proxies, CAS confs, root uri, node uri, logout uri, etc.

## nginx_stage.yml and the Per User NginX (PUN) session. 
Once a user authenticates with OOD, apache then starts the PUN as the user. `/etc/ood/config/nginx_stage.yml` determines all the properties of the PUN including global settings for every user's shell env. If you suspect a bug is a user shell env problem, first check the local app env configs set in: `submit.yml` in the app's directory first. More about nginx_stage.yml can be found here: <https://osc.github.io/ood-documentation/latest/reference/files/nginx-stage-yml.html>

## Announcements: announcements.d
You can make an announcement to be displayed within a banner on OOD by creating a yml or md file in `/etc/ood/config/announcements.d/`. When any user navigates to OOD's dashboard, OOD will check here for the existence of any files.

Here's an example announcement yaml:

```
type: warning
msg: |
On Monday, September 24 from 8:00am to 12:00pm there will be a **Maintenece downtime**, which will prevent SSH login to compute nodes and running OnDemand 
```

You can also create an `test-announcement.yml.erb` to take advantage of ERB ruby templating. More about OOD announcements can be found here: <https://osc.github.io/ood-documentation/latest/customizations.html#announcements>

## Message of the Day (MOTD)
You can have the OOD dashboard display the system MOTD by setting these environment variables:

```
MOTD_PATH="/etc/motd" # this supports both file and RSS feed URIs
MOTD_FORMAT="txt" # markdown, txt, rss, markdown_erb, txt_erb
```

In `/etc/ood/config/apps/dashboard/env`

## ondemand.d 
`/etc/ood/config/ondemand.d/` is home to nearly all other OOD configs not mentioned here (i.e. ticket submission, nav customizations, branding, etc.). The contents are controlled by puppet, under `openondemand::confs:`, and the puppet formatting to properly place yamls here is as follows:

```
openondemand::conf:
<name of yaml (i.e. tickets; If you want to create a tickets.yml)>
  data: (denotes the content to put in yaml)
    <yaml key>: <yaml value>
```

```
support_ticket:
  data:
    support_ticket:
      email:
        from: "noreply@%{trusted.domain}"
        to: hpc-help@ucdavis.edu
```

More about `ondemand.d`, `openondemand::confs`, and their function and format can be found
here: <https://osc.github.io/ood-documentation/latest/reference/files/ondemand-d-ymls.html>
and here: <https://forge.puppet.com/modules/osc/openondemand/>


## Admin Troublshooting

```mermaid
sequenceDiagram
  user->>apache: `/var/log/apache2/error.log`
  apache->>CAS: `/var/cache/apache2/mod_auth_cas/`
  CAS->>apache: return
  apache->>pun: `/var/log/apache2/$fqdn_error.log`
  pun->>dashboard: `/var/log/ondemand-nginx/$user/error.log`
  dashboard->>oodapp: `$home/ondemand/data/sys/dashboard/batch_connect/sys/$app/output/$session_id/output.log`
  oodapp->>user: render
```

1. Apache
  
  To start, all users who navigate to the ondemand website first encounter the apache server. Any errors encountered at this step will be in the log(s) at `/var/log/apache2/error.log`. This also the part where apache redirects any users who arrive at http://ondemand...:80 to https://ondemand...:443; You can narrow down if this is indeed the problem by just checking if the https url works. If the http site works but the https site doesn't, then it's an ssl proxy error check the apache configs.

2. CAS
  
  Apache then redirects the users to CAS for authentication. You can `grep -r $USER /var/cache/apache2/mod_auth_cas/` to check if users have been authed to CAS and a cookie has been set.

3. Apache part deux
  
  CAS brings us back to apache and here apache runs all sorts of OOD Lua hooks. Any errors encountered at this step will be in the l
og(s) at `/var/log/apache2/$fqdn_error.log`

4. The PUN (Per User Nginx) session
  
  Apache then starts an NginX server as the user and most things like the main dashboard, submitting jobs, running apps, etc happen here in the PUN. Any errors encountered at this step will be in the logs at `/var/log/ondemand-nginx/$user/error.log`. You can also see what might be happening here by running commands like `ps aux | grep $USER` to see the users PUN, or `ps aux | grep -i nginx` to see all the PUNs. From the ondemand web UI theres an option to "Restart Web Server" which essentially kills and restarts the users PUN.

5. Dashboard (/pun/sys/dashboard)
  
  The dashboard is mostly covered in section 4 as part of the PUN, but just wanted to denote that apache then redirects us here after the PUN has been started where users can do everything else. At this step OOD will warn you about things like "Home Directory Not Found" and such. If you get this far I'd recommend you troubleshoot issues with users' home dir, NASii, and free space: `df | grep $HOME`, `du -sh $HOME`, `journalctl -u  autofs`, `mount | grep $HOME`, `automount -m`, and all the nfs homedir stuff. You should also check zfs, connection speed, and logs on the NAS where users' homedir is located with some things like `zpool status` as root.

6. OOD Apps
  
  When users start an app like JuyterLab or a VNC desktop the job is submitted by the users' PUN and here OOD copies and renders (with ERB) the global app template from `/var/www/ood/apps/sys/<app_name>/template/*` to `$HOME/ondemand/data/sys/dashboard/batch_connect/sys/<app_name>/(output)/<session_id>`. Any errors encountered at this step will be in `$HOME/ondemand/data/sys/dashboard/batch_connect/sys/<app_name>/(output)/<session_id>/*.log`. i.e. output.log or vnc.log

7. Misc
  
  Maybe the ondemand server is just in some invalid state and needs to be reset. I'd recommend you check the puppet conf at `/etc/puppetlabs/puppet/puppet.conf`, run `puppet agent -t` , and maybe restart the machine. Running puppet will force restart the apache server and regenerate OOD from the ood config yamls. Then you can restart the server by either ssh-ing to the server and running `reboot`, or by ssh-ing to proxmox and running `qm reset <vmid>` as root. TIP: you can find the vmid by finding the server in `qm list`. 


## OOD FQDNs

### Farm
#### Production: `ondemand.farm.hpc.ucdavis.edu`
#### Dev: `dood.vm.farm.hpc.ucdavis.edu`

### Franklin
#### Production: `ondemand.franklin.hpc.ucdavis.edu`

### Hive
#### Production: `ondemand.hive.hpc.ucdavis.edu`
