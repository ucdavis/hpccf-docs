

Most packages that are installed are available as environment modules. You can find out about an installed software/module using the following command:-
 
module avail -l | grep -i <module-name>
This command will list all the installed software and modules in your cluster.

Use:
module load <module/version>        to load a module
module unload <module/version>    when done.

Generally, use as few modules as possible at a time–once you're done using a particular piece of software, unload the module before you load another one, to avoid incompatibilities.

If you cannot find a piece of software on the cluster, you can request an installation for cluster-wide use. Contact the hpc-help@ucdavis.edu with the name of the cluster, your username, the name of the software, and a link to the software's website, documentation, or installation directions, if applicable.