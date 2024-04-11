#Requesting Access to HPC resources

In order, to qualify for an account on any of HPC clusters, you must have a UC Davis affiliation and must be sponsored by a lab owner/PI or an equipment owner. You can find out about your cluster association when you 
know: Which lab you and your sponsored PI (Principle Investigator) are associated with. Which resource you need access to or which resources your PI has sponsored in a particular cluster. Account Request forms can be 
found on HPC website - <https://hpc.ucdavis.edu/account-request-forms> For Farm, Peloton and Franklin clusters' account request forms, use Hippo via this link:- <https://hippo.ucdavis.edu/clusters>

##Temporary Affiliation Form

TAF is used for sponsoring and requesting access for external users. It is a process created to grant external constituents (visiting faculty, concurrent students, vendors, and others) access to UC Davis computer 
resources. By registering for temporary access, affiliates have access to the UC Davis network, a ucdavis.edu email address, and a unique user name and password which is used to verify identity and enable subsequent 
access privileges to various parts of the network. The sponsoring PI can go to this link to register the new user
 <https://taf-admin.ucdavis.edu/taf-admin/>

##Authentication

SSH keys are an authentication method used to gain access to an encrypted connection between systems and then ultimately use that connection to access and manage the remote system. An SSH key pair is always required 
to log into HPC clusters. SSH keys are generated as a matched pair of a private key and a public key. Keep your private key safe and use a strong, memorable passphrase. We support one key per user. If you need to 
access the cluster from multiple computers, such as a desktop and a laptop, copy your private key. Note that if you forget your passphrase or lose your private key, we cannot reset it, you'll need to generate a new 
key pair, following the same directions as when you first created it. Besides, to avoid typing the passphrase for every login, an SSH-agent or keychain can be used. The next section gives information about command 
line applications to use and generate SSH keypair.

##Command Line Application

We recommend using terminal on Macbook and Mobaxterm on Windows machines in order to create SSH keypair and connect to the HPC clusters: Using the link, download the Home edition- Installer edition of Mobaxterm:- 
<https://mobaxterm.mobatek.net/download-home-edition.html> After opening a terminal window or Mobaxterm tab, enter the following command to create a new SSH keypair: `$ ssh-keygen` The `ssh-keygen` command will 
generate two files: the private key (usually named id_rsa), and the public key (usually named id_rsa.pub) in the .ssh/ directory under your home directory. The file with the .pub extension is your public key and 
should be sent for HPC access. The file without an extension is your private key and should be kept secret. To make sure your keys are inside .ssh folder and is readable via command line, enter the command: `$ ls -al 
.ssh` This command will list down the key pair. There should be two files; the privat key- id_rsa and the public key - id_rsa.pub

##Connecting to the Clusters

Users can use the ssh command to connect to the clusters. `ssh [userid]@[cluster-name].hpc.ucdavis.edu` Remember that ssh used private and public keys to authenticate users. If a user has different keys in the local 
machine, the option -i can be used to identify the private key for connection. `ssh -i /path/to/the/private/key [user-id]@[cluster-id].hpc.ucdavis.edu` For the login issues with ssh key pair check the next section.

##X11 Forwarding

Some software has a Graphical User Interface (GUI), and so requires X11 to be enabled. X11 forwarding allows an application on a remote server to render its GUI on a local system (your computer). How this is enabled 
depends on the operating system the computer you are using to access HPC clusters is running.

### Linux

If you are SSHing from a Linux distribution, you likely already have an X11 server running locally, and can support forwarding natively. If you are on campus, you can use the `-Y` flag to enable it, like: ```bash $ 
ssh -Y [USER]@[cluster-name].hpc.ucdavis.edu ``` If you are off campus on a slower internet connection, you may get better performance by enabling compression with: ```bash $ ssh -Y 
[USER]@[cluster-name].hpc.ucdavis.edu ```

### MacOS

MacOS does not come with an X11 implementation out of the box. You will first need to install the free, open-source [XQuartz](https://www.xquartz.org/) package, after which you can use the same `ssh` flags as 
described in the [Linux instructions](access.md#linux).

### Windows

If you are using our recommend windows SSH client, [MobaXterm](https://mobaxterm.mobatek.net/), X11 forwarding should be enabled by default. You can confirm this by checking that the `X11-Forwarding` box is ticked 
under your cluster session settings. For off-campus access, you may want to tick the `Compression` box as well.
