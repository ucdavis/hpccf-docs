Note: the trailing `/` is critical on both the source and the destination, otherwise the files will not end up in the
location you are expecting.

If you want to make the destination directory **exactly** the same as the source directory, i.e., delete files in the
destination directory that do not exist on the source, you can add the `--delete-after` argument to rsync.

-   `--delete-during`: Deletes files on the destination that are not present on the source.

???+ danger "PERMANENT DATA LOSS"

    If you add the `--delete-after` argument to rsync, but use the wrong source or destination directory in the rsync command, **YOU MAY CAUSE PERMANENT DATA LOSS** on the destination side. Please be extra cautious when having rsync delete files.
