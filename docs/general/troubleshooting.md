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

If you are trying to use a key to access LSSC0 or any of the Genome Center login nodes, SSH keys will not work. It is possible
to use `kinit` locally and `GSSAPI` to avoid entering a password on every login. 
