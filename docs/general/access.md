
## X11 Forwarding

Some software has a Graphical User Interface (GUI), and so requires X11 to be enabled.
X11 forwarding allows an application on a remote server (in this case, Franklin) to render its GUI on a local system (your computer).
How this is enabled depends on the operating system the computer you are using to access Franklin is running.

### Linux

If you are SSHing from a Linux distribution, you likely already have an X11 server running locally, and can support forwarding natively.
If you are on campus, you can use the `-Y` flag to enable it, like:

```bash
$ ssh -Y [USER]@franklin.hpc.ucdavis.edu
```

If you are off campus on a slower internet connection, you may get better performance by enabling compression with:

```bash
$ ssh -Y [USER]@franklin.hpc.ucdavis.edu
```

### MacOS

MacOS does not come with an X11 implementation out of the box.
You will first need to install the free, open-source [XQuartz](https://www.xquartz.org/) package, after which you can use the same `ssh` flags as described in the [Linux instructions](access.md#linux).

### Windows

If you are using our recommend windows SSH client, [MobaXterm](https://mobaxterm.mobatek.net/), X11 forwarding should be enabled by default.
You can confirm this by checking that the `X11-Forwarding` box is ticked under your Franklin session settings.
For off-campus access, you may want to tick the `Compression` box as well.