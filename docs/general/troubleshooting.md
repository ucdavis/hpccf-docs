## Common SSH Issues

Here are some of the most common issues users face when using SSH. 


### Keys

The following clusters use SSH keys: Atomate, Farm, Franklin, HPC1, HPC2, Impact, Peloton. 

If you connect to one of these and are asked for a password (as distinct from a passphrase for your key), 
your key is not being recognized. This is usually because of permissions or an unexpected filename. 
SSH expects your key to be one of a specific set of names. Unless you have specified something other than
the default, this is probably going to be **.ssh/id_rsa**.

If you specified a different name when generating your key, you can specify it like this:

```bash
ssh -i .ssh/newkey [USER]@[cluster].hpc.ucdavis.edu
```

If you kept the default value, your permissions should be set so that only you can read and write the key (-rw------- or 600). 

If you are trying to use a key to access LSSC0, this will not work. 
