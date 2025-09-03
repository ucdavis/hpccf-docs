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

When generating SSH key pair, you are asked to set a password for your private key, we recommend to give a password for security purposes. 
But if you want to reset your private key password, enter this command (only when you know your current password):-

```bash
ssh-keygen -p -f /root/.ssh/id_rsa
```

If you have forgotten your private key password and cannot reset it, you can generate a new SSH key pair and assign a new password for it, but send your new public key to us.

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

## Common Slurm Scheduler Issues

These are the most common issues with job scheduling using Slurm.

### Using a non-default account

If you have access to more than one Slurm account and wish to use an account other than your default,
use the `-A` or `--account` flag. 

e.g. If your default account is in `foogrp` and you wish to use `bargrp`:
```bash
srun -A bargrp -t 1:00:00 --mem=20GB scriptname.sh
```

### No default account

Newer slurm accounts have no default specified, and in this case you might get error message like:

```
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

You will need to specify the account explicitly as explained [above](#no-default-account).
You can find out how to view your Slurm account information in the [resources
section](../scheduler/resources.md).

