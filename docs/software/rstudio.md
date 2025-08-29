# :simple-r: :simple-rstudio: R and RStudio

## Using RStudio
You can run RStudio on our clusters using OpenOnDemand by navigating to [https://ondemand.<clustername>.hpc.ucdavis.edu](https://ondemand.<clustername>.hpc.ucdavis.edu). OpenOnDemand (OOD) allows access to cluster resources and software via a web browser. Learn more about OpenOnDemand [here](ondemand.md#open-ondemand)

## RStudio Troubleshooting

### Clearing Your R Cache

Generally, many of the RStudio issues users come across can be resolved by clearing out your old rsession caches. First, ssh to the cluster on which you are using rstudio. Then, remove these files:

#### rsession

Your rsession cache stores any of your previous sessions with your previously installed libraries you chose to save and this rsession data can be located in these locations:

`~/.RData`
`~/.local/share/rstudio*`

We also recommend ensuring that the "Restore .RData into workspace at startup" setting, under Options>General>Workspace, be disabled to prevent recurring issues.

#### configs

In most cases it might not be necessary to clear these files, but in case it is you can find the rest of your cached rstudio configs here:

`~/.cache/rstudio*`
`~/.config/rstudio*`

If you solely use RStudio via OpenOnDemand and you do not have SSH access to the host cluster, you'll have to create a support ticket asking us to clear your rsession cache for you. Be sure to include your username, cluster name, and make the subject something along the lines of: "Clear rsession cache on Farm"
