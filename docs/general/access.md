In order to access your HPC account, you may need to generate an SSH key pair for authorization. You generate a pair of keys: a public key and a private key. The private key is kept securely on your computer or device. The public key is submitted to HPCCF to grant you access to a cluster.

## How do I generate an SSH key pair?

### Windows Operating System

We recommend MobaXterm as the most straightforward SSH client. You can download the free Home Edition (Installer Edition) from [MobaXterm](https://mobaxterm.mobatek.net/). Please download the Installer Edition. The Portable Edition deletes the contents of your home directory by default when it exits, which will remove your freshly generate SSH key. Once you install the stable version of MobaXterm, open its terminal and enter this command:


`ssh-keygen`

This command will create a private key and a public key. Do not share your private key; we recommend giving it a passphrase for security. To view the .ssh directory and to read the public key, enter these commands:

```
ls -al ~/.ssh
cat ~/.ssh/*.pub
```

### macOS and Linux:

Use a terminal to create an SSH key pair using the command:

`ssh-keygen`

To view the .ssh directory and to read the public key, enter these commands:

```
ls -al ~/.ssh
cat ~/.ssh/*.pub
``` 

## X11 Forwarding

Some software has a Graphical User Interface (GUI), and so requires X11 to be enabled.
X11 forwarding allows an application on a remote server (in this case, Franklin) to render its GUI on a local system (your computer). How this is enabled depends on the operating system the computer you are using to access Franklin is running.

### Linux

If you are SSHing from a Linux distribution, you likely already have an X11 server running locally, and can support forwarding natively.
If you are on campus, you can use the `-Y` flag to enable it, like:

```bash
$ ssh -Y [USER]@[CLUSTER].hpc.ucdavis.edu
```

If you are off campus on a slower internet connection, you may get better performance by enabling compression with:

```bash
$ ssh -Y -C [USER]@[CLUSTER].hpc.ucdavis.edu
```
If you have multiple SSH key pairs, and you want to use a specific private key to connect to the clusters, use the otpion `-i` to specify path to the private key with SSH:

```bash
$ ssh -i ~/.ssh/id_hpc [USER]@[CLUSTER].hpc.ucdavis.edu
```
### macOS

macOS does not come with an X11 implementation out of the box. You will first need to install the free, open-source [XQuartz](https://www.xquartz.org/) package, after which you can use the same `ssh` flags as described in the [Linux instructions](access.md#linux).

### Windows

If you are using our recommend windows SSH client ([MobaXterm](access.md#windows-operating-system)) X11 forwarding should be enabled by default. You can confirm this by checking that the `X11-Forwarding` box is ticked under your Franklin session settings. For off-campus access, you may want to tick the `Compression` box as well.
