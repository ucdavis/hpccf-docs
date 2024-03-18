# What is R and how to load it on HPC clusters?

R is a programming language and software environment for statistical computing and graphics.  
R offers a wide variety of statistics-related libraries and provides a favorable environment for statistical computing and design. In addition, the R programming language gets used by many quantitative analysts as a 
programming tool since it's useful for data importing and cleaning.

In order to see different versions of R installed on any of HPc the cluster, run the command:

`module avail R`

You can obtain R in your environment by loading the R module i.e.:

`module load R`

The command `R --version` returns the version of R you have loaded:

`R --version`

In order to run the loaded R module you can enter this command to work with it and get the prompt:

`R`

To check available libraries and packages inside R, use the following command:

`library(library-name)`
OR
`installed.packages()`

For adding a new package that is missing you can install it using the command:

`install.packages("package-name")`

In case of any issue or error popping up, send email to <hpc-help@ucdavis.edu> - we will help you with any question and issue.

# What is Rstudio Server and how to load it on Farm cluster?

RStudio Server enables you to provide a browser-based interface to a version of R running on a remote Linux server, bringing the power and productivity of the RStudio IDE to server-based deployments of R.
There are different version of Rstudio-server installed on the Farm cluster and are available to run on the nodes, you can view different versions by running the following commands:

`module avail rstudio-server`

The command output will list down all the installed versions of the module. Following example shows how to use "rstudio-server/2022.07.1"
If you are on the login or head node, run the following command to get on a regular node:

`srun -p med2 --time=9:00:00 --cpus-per-task=4 --mem=5G --pty /bin/bash -l`

Then run:-

`module load rstudio-server/2022.07.1`

and then run:-

`rserver-farm`

Then open a new terminal and run this line:-

`ssh -L60342:c6-73:60342 userid@farm.cse.ucdavis.edu`

Then open a new tab on your browser, open this link on the browser:

`http://localhost:60342`

It should load the rstudio-server software asking for username and password.
