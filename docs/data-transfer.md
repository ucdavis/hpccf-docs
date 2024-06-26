# Data Transfer
HPC users can transfer data between their local machine and the clusters.
They can use software or commands to do the data transfer.

## Available Software
There are multiple transfer software available to copy data between the HPC clusters and the user's computer.

- [Filezilla](https://filezilla-project.org/) is a multi-platform client commonly used to transfer data to and from the cluster.

- [Cyberduck](https://cyberduck.io/) is another popular file transfer client for Mac or Windows computers.

- [WinSCP](https://winscp.net/eng/index.php) is Windows-only file transfer software.

- [Globus](https://www.globus.org/) is another common solution, especially for larger transfers.

## Data Transfer using Commmand Line

The commands `rsync` and `scp` are command-line tools to transfer data to and from the cluster, and they should be run on your computer, not on the cluster:

To transfer something to HPC clusters from your local computer:


`scp -r local-directory [USER]@[CLUSTER].hpc.ucdavis.edu:~/destination/`

To transfer something from a cluster to your local computer:


`scp -r [USER]@[CLUSTER].hpc.ucdavis.edu:~/[CLUSTER-DATA] local-directory`

To use `rsync` to transfer a file or directory from cluster to your local computer:


`rsync -aP -e ssh [USER]@[CLUSTER].hpc.ucdavis.edu:~/[CLUSTER-DATA] .`

`rsync` has the advantage that if the connection is interrupted for any reason you can just up-arrow and run the exact same command again and it will resume where it stopped.

See `man scp` and `man rsync` for more information.

If you are trying to copy over data from a web server file to your local machine or other server use the following command:

*Note that you don't have to log into the cluster to run this command and the files shouldn't be password protected:-*

`scp -r [WEB-URL]:/home/[USER]/public_html/files path/to/the/directory/you/want/to/copy`


`scp -r [CLUSTER].hpc.ucdavis.edu:/home//[USER]public_html/public_web_files /path/to/the/directory/you/want/to/copy/destination`