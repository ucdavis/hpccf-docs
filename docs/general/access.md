In order to access your HPC account, you may need to generate an SSH key pair for authorization. You generate a pair of
keys: a public key and a private key. The private key is kept securely on your computer or device. The public key is
submitted to HPC@UCD to grant you access to a cluster.

## How do I generate an SSH key pair?

### Windows Operating System

We recommend MobaXterm as the most straightforward SSH client. You can download the free Home Edition (Installer
Edition) from [MobaXterm](https://mobaxterm.mobatek.net/). Please download the Installer Edition. The Portable Edition
deletes the contents of your home directory by default when it exits, which will remove your freshly generate SSH key.
Once you install the stable version of MobaXterm, open its terminal and enter this command:

`ssh-keygen`

This command will create a private key and a public key. Do not share your private key; we recommend giving it a
passphrase for security. To view the .ssh directory and to read the public key, enter these commands:

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

Some software has a Graphical User Interface (GUI), and so requires X11 to be enabled. X11 forwarding allows an
application on a remote server (in this case, Franklin) to render its GUI on a local system (your computer). How this is
enabled depends on the operating system the computer you are using to access Franklin is running.

### Linux

If you are SSHing from a Linux distribution, you likely already have an X11 server running locally, and can support
forwarding natively. If you are on campus, you can use the `-Y` flag to enable it, like:

```bash
$ ssh -Y [USER]@[CLUSTER].hpc.ucdavis.edu
```

If you are off campus on a slower internet connection, you may get better performance by enabling compression with:

```bash
$ ssh -Y -C [USER]@[CLUSTER].hpc.ucdavis.edu
```

If you have multiple SSH key pairs, and you want to use a specific private key to connect to the clusters, use the
option `-i` to specify path to the private key with SSH:

```bash
$ ssh -i ~/.ssh/id_hpc [USER]@[CLUSTER].hpc.ucdavis.edu
```

### macOS

macOS does not come with an X11 implementation out of the box. You will first need to install the free, open-source
[XQuartz](https://www.xquartz.org/) package, after which you can use the same `ssh` flags as described in the
[Linux instructions](access.md#linux).

### Windows

If you are using our recommend windows SSH client ([MobaXterm](access.md#windows-operating-system)) X11 forwarding
should be enabled by default. You can confirm this by checking that the `X11-Forwarding` box is ticked under your
Franklin session settings. For off-campus access, you may want to tick the `Compression` box as well.

## SSH key fingerprint issues

### Are you sure you want to continue connecting (yes/no/[fingerprint])?

SSH key fingerprint prompts like below happen the first time you connect to a server from your system(s). You should
compare the fingerprint printed with the [fingerprints listed below](#ssh-key-fingerprints-for-major-clusters). If they
match, you can safely enter `yes`. If you cannot find a match, you should open a ticket.

??? "Are you sure you want to continue connecting (yes/no/[fingerprint])?"

    ```console
    All keys already loaded
    The authenticity of host 'farm.hpc.ucdavis.edu (128.120.146.1)' can't be established.
    ED25519 key fingerprint is SHA256:qiPI72KfRjrAeEdww3RVkrM1Bi7GE6sEoS4JRnKzC1I.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

### WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED

SSH key fingerprint errors like below are normally caused when a host is reinstalled and the newly generated SSH host
key differs from the last time you SSH'd to the server. You should compare the `SHA256:LongRandomStringHere` part
against the host fingerprints listed below. If they match, you can safely follow the instructions `ssh-keygen -f ...`.
If they differ, you should open a ticket.

??? "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED"

    ```console
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
    Someone could be eavesdropping on you right now (man-in-the-middle attack)!
    It is also possible that a host key has just been changed.
    The fingerprint for the ECDSA key sent by the remote host is
    SHA256:LongRandomStringHere.
    Please contact your system administrator.
    Add correct host key in /home/YourLocalLoginID/.ssh/known_hosts to get rid of this
    message.
    Offending ECDSA key in /home/YourLocalLoginID/.ssh/known_hosts:32
    remove with:
    ssh-keygen -f "/home/YourLocalLoginID/.ssh/known_hosts" -R "Server.You.SSH'd.To"
    ECDSA host key for Server.You.SSH'd.To has changed and you have requested strict checking.
    ```

### SSH key fingerprints for major clusters

#### Farm (`farm.hpc.ucdavis.edu`)

-   `RSA: SHA256:aPUfAVTLNju9Omu8yIr5NYXAmZVKjsCLvewfAt8BLo8 `
-   `ECDSA: SHA256:XsfxXdolugXtm5/nWuEX0UB3mkllshTHTx+yHXQTrE0 `
-   `ED25519: SHA256:qiPI72KfRjrAeEdww3RVkrM1Bi7GE6sEoS4JRnKzC1I `

#### Franklin (`franklin.hpc.ucdavis.edu`)

-   `RSA: SHA256:mXcTBeL5xCfcMmLEEYu4ppIFM82X7vc5AGJjvEyoJxg`
-   `ECDSA: SHA256:e2mldm10c9VYZceHB62MQpMtgL2sZ10W0H3U/tsUHws`
-   `ED25519: SHA256:RFw1dHndgpDgv0p8VyHW1QQt3JVq7CEzlQ9fKnfAAoY`

#### Hive (`hive.hpc.ucdavis.edu`)

-   `ECDSA: SHA256:AmJ+z2miIMXlSAcm7k8YwKlIWk5+VqxyT0R4q3fvpcA`
-   `ED25519: SHA256:b5nv86Ciaqg1yrUVai6bZ0Hk4IpzAFLWtIPDBdacbQM`

#### HPC2 (`hpc2.engr.ucdavis.edu`)

-   `RSA: SHA256:ZC23UiJLib0sozDEClkmD5q+TgeZf/mol6xzIQY30xE`
-   `ECDSA: SHA256:ymN3g0Ow4BM2Rd/zE3THZg7nv+mOs75ENCe5GcvWQoM`
-   `ED25519: SHA256:Svzxx62P/NxrsISeyPZ06nW+YkDYsE1xQc1wD/61tFI`

#### Peloton (`peloton.hpc.ucdavis.edu`)

-   `RSA: SHA256:eVU5TeDV+ezOkVHVA9d/L6CrcPihU1POpw8uPh4iXuQ`
-   `ECDSA: SHA256:QFH7ONkN7edAoYEu0GfTz7prqvi1YYu4bep7hxNrswU`
-   `ED25519: SHA256:ydOUR2t/MX3jbd3JIHDXMJyLjdhRV4OBLr9iJfQB8lw`
