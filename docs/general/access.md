To access an HPC cluster, you connect to it over the internet using a protocol called SSH (Secure Shell). SSH lets
you control a remote computer from your local terminal. Most HPC clusters require an SSH key pair for authentication
instead of a password — the exception is Hive, which also accepts your UC Davis campus passphrase.

## How do I connect to a cluster?

Once your account is active, open a terminal and run:

```bash
ssh your-username@cluster.hpc.ucdavis.edu
```

Replace `cluster` with `farm`, `franklin`, or `hive` depending on which cluster you have access to. Your username
is your UC Davis Login ID (e.g., `cheeto`).

The first time you connect, SSH will display a fingerprint and ask you to confirm. Compare it against the
[known fingerprints below](#ssh-key-fingerprints-for-major-clusters) before typing `yes`.

## How do I open a terminal?

=== "macOS"

    Open **Terminal** by pressing `Command + Space` to open Spotlight, typing `Terminal`, and pressing Enter. You
    can also find it under **Applications → Utilities → Terminal**.

=== "Linux"

    Open your distribution's terminal emulator. This is usually found in your applications menu, or you can press
    `Ctrl + Alt + T` on many desktop environments.

=== "Windows"

    We recommend [MobaXterm](https://mobaxterm.mobatek.net/) as the most straightforward SSH client on Windows.
    Download the free **Home Edition (Installer Edition)** — avoid the Portable Edition, as it deletes the contents
    of your home directory by default when it exits. Once installed, open its built-in terminal.

    Alternatively, if you are comfortable with Linux, you can use
    [Windows Subsystem for Linux 2 (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install). Once installed,
    open your WSL2 distribution's terminal and follow the macOS/Linux instructions throughout this page.

## How do I generate an SSH key pair?

An SSH key pair consists of two files: a **private key** (kept securely on your computer) and a **public key**
(shared with HPC@UCD to grant you access). Think of the public key as a lock you give to the cluster, and the
private key as the only key that opens it.

To generate a key pair, open a terminal and run:

```
ssh-keygen -t rsa -b 4096
```

The `-t rsa` flag specifies the RSA key type, and `-b 4096` sets the key length to 4096 bits.

You will be prompted with a few questions:

1. **"Enter file in which to save the key"** — Press Enter to accept the default location (`~/.ssh/id_rsa`).
   This is fine for most users.

2. **"Enter passphrase"** — This is an optional password that protects your private key. We recommend setting one.
   You will be asked to enter it when you use your key.

Once complete, you will have two files in your `~/.ssh/` directory:

- `id_rsa` — your **private key**. Never share this file with anyone.
- `id_rsa.pub` — your **public key**. This is what you submit to HPC@UCD.

To view your public key, run:

```
cat ~/.ssh/id_rsa.pub
```

The output will be a long string starting with `ssh-rsa`. Copy the entire line — this is what you paste into
[HiPPO](https://hippo.ucdavis.edu) when requesting an account.

Once you have your public key, return to the [account request](account-requests.md) page to submit it.

## SSH agent

If you set a passphrase on your SSH key (which we recommend), you will be prompted for it each time you connect.
An SSH agent caches your passphrase for the duration of your local session so you only need to enter it once:

```bash
ssh-add ~/.ssh/id_rsa
```

On macOS, the SSH agent runs automatically and your passphrase can be saved to the system Keychain. On Linux,
you may need to start the agent manually:

```bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa
```

## SSH config file

Typing the full connection command every time quickly becomes tedious. You can create an SSH config file at
`~/.ssh/config` to set up shortcuts. For example:

```
Host farm
    HostName farm.hpc.ucdavis.edu
    User your-username
    ServerAliveInterval 60

Host franklin
    HostName franklin.hpc.ucdavis.edu
    User your-username
    ServerAliveInterval 60

Host hive
    HostName hive.hpc.ucdavis.edu
    User your-username
    ServerAliveInterval 60
```

With this in place, you can connect by simply typing `ssh farm`, `ssh franklin`, or `ssh hive` instead of the
full command.

The `ServerAliveInterval 60` line sends a 'keepalive' signal every 60 seconds, which prevents idle SSH sessions
from timing out and disconnecting.

If the file does not exist yet, create it with:

```bash
touch ~/.ssh/config
chmod 600 ~/.ssh/config
```

## Keeping sessions alive with tmux

If your SSH connection drops while you are running an interactive job, the process will be killed. A terminal
multiplexer like `tmux` runs your session on the server independently of your SSH connection — if you disconnect,
your work continues and you can reattach later.

Basic `tmux` usage:

| Command | Action |
|---------|--------|
| `tmux` | Start a new session |
| `tmux attach` | Reattach to your last session |
| `Ctrl+B`, then `D` | Detach from the session (leaves it running) |
| `Ctrl+B`, then `%` | Split pane vertically |
| `Ctrl+B`, then `"` | Split pane horizontally |

`tmux` is installed on all HPC clusters. We strongly recommend using it for any interactive work.

## Mosh

[Mosh](https://mosh.org/) (Mobile Shell) is an alternative to SSH designed for unreliable or mobile connections.
Unlike SSH, Mosh uses UDP and automatically reconnects if your connection drops — closing your laptop, switching
networks, or losing signal will not interrupt your session.

Mosh is particularly useful if you are:

- Working off-campus on a slow or unstable connection
- On a laptop that frequently sleeps or switches between WiFi and a hotspot
- Running long interactive sessions where a dropped SSH connection would be disruptive

To connect with Mosh:

```bash
mosh your-username@cluster.hpc.ucdavis.edu
```

Mosh must be installed on both your local machine and the cluster. Check whether it is available on the cluster
with `which mosh` after logging in via SSH first.

## X11 Forwarding

Some software has a Graphical User Interface (GUI), and so requires X11 to be enabled. X11 forwarding allows an
application on a remote server to render its GUI on your local computer. This is only needed for specific
graphical applications — most users will not need it.

=== "Linux"

    You likely already have an X11 server running and can enable forwarding with the `-Y` flag:

    ```bash
    ssh -Y your-username@cluster.hpc.ucdavis.edu
    ```

    For slower connections, add `-C` to enable compression:

    ```bash
    ssh -Y -C your-username@cluster.hpc.ucdavis.edu
    ```

=== "macOS"

    macOS does not include X11 by default. Install the free [XQuartz](https://www.xquartz.org/) package first,
    then use the same `-Y` flag as described in the Linux instructions above.

=== "Windows"

    If you are using MobaXterm, X11 forwarding is enabled by default. You can confirm this
    by checking that the **X11-Forwarding** box is ticked under your session settings. For off-campus access,
    tick the **Compression** box as well.

    If you are using WSL2, X11 support depends on your Windows version:

    - **Windows 11**: WSL2 includes built-in X11 support via WSLg. Use the same `-Y` flag as Linux:

        ```bash
        ssh -Y your-username@cluster.hpc.ucdavis.edu
        ```

    - **Windows 10**: You will need a third-party X server such as
      [VcXsrv](https://sourceforge.net/projects/vcxsrv/). Launch it before connecting, then set the display
      variable and use the `-Y` flag:

        ```bash
        export DISPLAY=:0
        ssh -Y your-username@cluster.hpc.ucdavis.edu
        ```

If you have multiple SSH key pairs and want to specify which one to use, pass the `-i` flag:

```bash
ssh -i ~/.ssh/id_hpc your-username@cluster.hpc.ucdavis.edu
```

## SSH key fingerprint issues

### Are you sure you want to continue connecting (yes/no/[fingerprint])?

This prompt appears the first time you connect to a server. Compare the displayed fingerprint against the
[fingerprints listed below](#ssh-key-fingerprints-for-major-clusters). If they match, type `yes`. If you cannot
find a match, [open a support ticket](../support.md) before proceeding.

??? "Example prompt"

    ```console
    The authenticity of host 'farm.hpc.ucdavis.edu (128.120.146.1)' can't be established.
    ED25519 key fingerprint is SHA256:qiPI72KfRjrAeEdww3RVkrM1Bi7GE6sEoS4JRnKzC1I.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

### WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED

This error usually means the server was reinstalled and its host key changed. Compare the `SHA256:...` string
against the fingerprints below. If they match, it is safe to update your known hosts file by running the command
shown in the error output (`ssh-keygen -f ...`). If they do not match, [open a support ticket](../support.md).

??? "Example warning"

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
    Add correct host key in /home/YourLocalLoginID/.ssh/known_hosts to get rid of this message.
    Offending ECDSA key in /home/YourLocalLoginID/.ssh/known_hosts:32
    remove with:
    ssh-keygen -f "/home/YourLocalLoginID/.ssh/known_hosts" -R "Server.You.SSH'd.To"
    ECDSA host key for Server.You.SSH'd.To has changed and you have requested strict checking.
    ```

### SSH key fingerprints for major clusters

#### Farm (`farm.hpc.ucdavis.edu`)

-   `RSA: SHA256:aPUfAVTLNju9Omu8yIr5NYXAmZVKjsCLvewfAt8BLo8`
-   `ECDSA: SHA256:XsfxXdolugXtm5/nWuEX0UB3mkllshTHTx+yHXQTrE0`
-   `ED25519: SHA256:qiPI72KfRjrAeEdww3RVkrM1Bi7GE6sEoS4JRnKzC1I`

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
