## Common SSH Issues

Here are some of the most common issues users face when using SSH. 


### Keys

The following clusters use SSH keys: Atomate, Farm, Franklin, HPC1, HPC2, Impact, Peloton. 

If you connect to one of these and are asked for a password (as distinct from a passphrase for your key), 
your key is not being recognized. This is usually because of permissions or an unexpected filename. 
SSH expects your key to be one of a specific set of names. Unless you have specified something other than
the default, this is probably going to be `$HOME/.ssh/id_rsa`.

If you specified a different name when generating your key, you can specify it like this:

```bash
ssh -i $HOME/.ssh/newkey [USER]@[cluster].hpc.ucdavis.edu
```

If you kept the default value, your permissions should be set so that only you can read and write the key `(-rw------- or 600)`. 
To ensure this is the case, you can do the following:

```bash
chown 600 $HOME/.ssh/id_rsa
```

On HPC2, your public key is kept in `$HOME/.ssh/authorized_keys`. Please make sure to not remove your key from this file.
Doing so will cause you will lose access.

If you are trying to use a key to access LSSC0 or any of the Genome Center login nodes, SSH keys will not work, but there is 
another method. 

To enable logins without a password, you will need to enable GSSAPI, which
some systems enable by default.  If not enabled, add the following to your 
`$HOME/.ssh/config` file (create it if it doesn't exist):

	GSSAPIAuthentication yes
	GSSAPIDelegateCredentials yes

The `-K` command line switch to ssh does the same thing on a one-time
basis.

Once you have `GSSAPI` enabled, you can get a Kerberos ticket using

```bash
kinit [USER]@GENOMECENTER.UCDAVIS.EDU
```

SSH will use that ticket while it's valid.
