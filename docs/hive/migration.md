---
title: Migrating from LSSC0
---
## Data migration:
#### Home directories:

Home directories on Hive are mounted on /home/<username>. For example, if your username is Cheeto, your home directory would be `/home/cheeto`. Home directories on Hive are expanded to 20G per person.

#### Group directories:
Group directories on Hive are mounted on /quobyte. Please ensure that your group or lab
has purchased resources before you move data. Group directories are named after the PI or lab owner. 

### Moving data to Hive using rsync:

Please ensure you have an account on Hive by creating one at [HiPPO](https://hippo.ucdavis.edu).

To use rsync to copy files from one server to another while preserving permissions, ownership, and file times, you can use the following command:

`rsync -avz source/ user@destination:/path/to/target/`

##### Explanation of options:
	•	-a (archive mode): Preserves symbolic links, permissions, ownership, file timestamps, and recursively copies directories.
	•	-v (verbose): Displays the progress and details of the transfer.
	•	-z (compress): Compresses file data during transfer to save bandwidth.
	•	source/: The directory or file you want to copy. The trailing slash / ensures only the contents of the directory are copied, not the directory itself.
	•	user@destination: The username and IP/hostname of the destination server.
	•	/path/to/target/: The target directory on the destination server.

##### Example:

If you're copying files from /home/cheeto on LSSC0 to /home/cheeto on Hive, run rsync on LSSC0:

`rsync -avz /home/cheeto/ user@hive.hpc.ucdavis.edu:/home/cheeto/`

Note that this will copy your home directory as-is. Consider putting your LSSC0 files into an `oldhome/` directory on Hive to ensure that you're not copying over incompatible dot files.

`rsync -avz /home/cheeto/ user@hive.hpc.ucdavis.edu:/home/cheeto/oldhome/`

##### Additional options:
	•	--progress: Shows progress during the file transfer.
	•	--delete: Deletes files on the destination that are not present on the source.
	•	-e ssh: Explicitly specifies SSH as the transfer protocol (default when connecting to remote servers).

Please note that you will be asked for your user password when transferring data to Hive. Your username and passphrase is your campus computing account and campus Kerberos passphrase. 
