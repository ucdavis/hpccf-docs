# Open OnDemand
This is meant to be a general configuration guide to Open OnDemand (OOD) for admins. But, I'd also like this to serve as an admin troubleshooting tutorial for OOD. So, the bulk of relevant OOD configs are located in `/etc/ood/config/` but the contents within are controlled by puppet. Usually, OOD is served by, or behind, apache and those configs are located in `/etc/apache2/` and the default served dir is located at `/var/www/ood` but these are also heavily controlled by puppet. For the rest of this config documentation I'll be categorizing by the file names, but I'll also try to refer to the puppet-openondemand class for that file as well.

## OOD Interactive Apps
Apps in OnDemand are located in `/var/www/ood/apps/sys/<app name>`. The OOD dashboard itself is considered an app and is located here. The "dev" made apps are cloned here by puppet (`openondemand::install_apps:`) from hpccf's github (i.e. <https://github.com/ucdavis/hpccf-ood-jupyter>). OOD apps are, put simply, sbatch scripts that are generated from ERB templates. Inside the app's directory, what is of most interest to admins is the: `form.yml`, `submit.yml`, and the `template/` directory. I would guess that the majority of troubleshooting is happening here. Note that any of the files within this dir can end in `.erb` if the you want its contents dynamically generated. To learn more about apps you can find the docs here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive.html#>

### form.yml
  This file represents the form users fill out and the fields for selecting clusters, partitions, cpu, mem, etc. If you wanted to add another field you can do it here. Or, **if you suspect there's a bug with the web form I recommend starting here**. More about form.yml can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/form.html#>

### submit.yml
  This file contains the contents of the sbatch job as well as job submission parameters that are submitted to slurm (or whatever scheduler you are using). Also, here you can configure the shell environment in which the app is run.  **If you suspect a bug might be a slurm, slurm submission, or a user environment issue I'd start here**. More about submit.yml can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/submit.html#>

### template/
  This directory is the template for the sbatch job that the interactive app is run in. Any code, assets, etc. necessary with the app itself should be included here. When a user launches an OOD app this directory is processed by ERB templating system then copied to `~/ondemand/data/sys/dashboard/batch_connect/sys/...`. In this directory you may see three files of interest to admins: `before.sh`, `script.sh`, `after.sh`. As their names suggest there's a script that runs before the job, one after, and the job itself. OOD starts by running the main script influenced by `submit.yml` and forks thrice to run the `before.sh`, `script.sh`, and `after.sh`. More about `template/` can be found here: <https://osc.github.io/ood-documentation/latest/how-tos/app-development/interactive/template.html#>

### view.yml
  This is just the html view of the app form. I doubt you need to be editing this.

### OOD App Developers
  If you want to edit, add, or create OOD apps you must be enabled as a dev app developer. In puppet this is done by  (`openondemand::dev_app_users:`). Adding your name to a list of app developers, and puppet will then do the following:

  ```
  mkdir -p /var/www/ood/apps/dev/<username>
  sudo ln -s ~/ondemand/dev /var/www/ood/apps/dev/<username>/gateway
  ```
  After that, you can `git clone` apps to your OOD app dev env located in `~/ondemand/dev/`. Your dev apps will show in a separate sidebar from the production ood apps.

## clusters.d
`openondemand::clusters` and `/etc/ood/config/clusters.d/` is the config dir where OOD is coupled with a cluster and global scheduler options are specified. For OOD apps to work and be submitted to a cluster this yaml needs to be present and must be named after the cluster's hostname i.e. `/etc/ood/config/clusters.d/farm.yml`. The most relevant section of this file for people not named Teddy is `batch_connect:`, and more specifically the `script_wrapper:`, is where you can put shell commands that will always run when an OOD app is run. Here's what it normally looks like:

### Batch Connect
  ```
  batch_connect:
      basic:
        script_wrapper: |
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
Under `batch_connect:` is the app category. JupyterLab and RStudio are in the `basic` category, and VNC has its own category. Anything set in the `script_wrapper:` under the app category is always run when an app of that category is run. So if you add a `module load openmpi` to the script wrapper under `basic:` then that will be ran, and openmpi will be loaded, whenever RStudio or JupyterLab is started. The `%s` is a placeholder for all the scripts from the aforementioned `template/` dir . You can use the placeholder to differentiate whether you want you commands to be run before or after your OOD app is started.

The `facter fqdn` within `set_host:` key should resolve to the fqdn of the compute/gpu node the job is running on.

## ood_portal.yml

  ood_portal.yml is the top most config for OOD. **Here be dragons, don't edit this file unless you know what you are doing!** Here you can set the servername and port num that OOD will listen on. As well as, OOD related apache configs, certs, proxies, CAS confs, root uri, node uri, logout uri, etc.

## nginx_stage.yml and the PUN: Per User NginX session. 

  Once a user logs into OOD, CAS gets and sets the username and apache immediately starts the PUN as the user. This config yaml determines all the properties of the PUN; Including global settings for every user's shell env. If you suspect a bug is a user shell env problem first check the `submit.yml` in the app's directory first. Then you can check here. More about this can be found here: <https://osc.github.io/ood-documentation/latest/reference/files/nginx-stage-yml.html#>

