
# Basic tar usage

`tar` (Tape ARchive) is a powerful tool that bundles files into a
single archive file. By passing various additonal options, `tar` can
also use compression.

We discussed the following flags in `tar`
 * `x` -- eXtract files from a tar archive
 * `c` -- Create a tar archive
 * `v` -- verbose mode, print out files as it uses them
 * `f` -- use files as input rather than stdin and stdout
 * `C` -- perform an operation as if you changed directory to the given directory

We discussed the following compression flags for `tar`
 * `z` -- use gzip compression or decompression
 * `j` -- use bzip2 compression or decompression
 * `J` -- use xz compression or decompression

### Tar examples

`tar -czvf an_archive.tgz directory_with_files/`
 * (-f) operates on files rather than stdin/stdout
 * (-c) Creates a new archive called `an_archive.tgz`
 * (-z) Compresses that archive using `gzip`
 * (-v) print out all the files you are putting in
 * Adds everything inside of `directory_with_files/` including subdirectories
 * We referred to this type of tarfile as a 'rooted' tarfile since it
   has one directory as input.

`tar -xzvf an_archive.tgz `
 * (-f) operates on files rather than stdin/stdout
 * (-x) Extract all files from archive called `an_archive.tgz`
 * (-z) Decompresses that archive using `gzip`
 * (-v) print out all the files you are pulling out
 * Put all files starting here in the current directory

`tar -czvf an_archive.tgz file1 file2 file3`
 * (-f) operates on files rather than stdin/stdout
 * (-c) Creates a new archive called `an_archive.tgz`
 * (-z) Compresses that archive using `gzip`
 * (-v) print out all the files you are putting in
 * Adds each of file1, file2, file3 to the archive
 * We referred to this type of tarfile as a 'non-rooted' tarfile since it
 has multiple independent files as inputs

`tar -czvf an_archive.tgz -C outer_dir/ directory_with_files/`
 * (-f) operates on files rather than stdin/stdout
 * (-c) Creates a new archive called `an_archive.tgz`
 * (-z) Compresses that archive using `gzip`
 * (-v) print out all the files you are putting in
 * (-C) operate from `outer_dir` instead of the current directory
 * Adds everything inside of `outer_dir/directory_with_files/`
   including subdirectories
 * The inclusion of this -C flag allows us to make a tarfile with
   files inside of `outer_dir` without including `outer_dir` itself in
   the archive.

# Making symbolic links

`ln` (LiNk) allows you to make symbolic and hard links to files. Hard
links are not covered in detail in this class. Links are are simple
shortcuts, they do not understand how to track files or where they
are, they only are a shortcut for a path.

Both `readlink` and `ls -l` will indicate where a symbolic link points.

`ln [flags] file_to_link_to link_path`

`ln` flags
 * s -- Symbolic, always use this flag


### ln examples

`ln -s datafile_1 data_link`
 * Creates a symbolic link in the current directory called `data_link`
 * The link points to `datafile_1`
 * Either the link or the file moves, the link becomes broken

`ln -s /var/data/datafile_1 data_link`
 * Creates a symbolic link in the current directory called `data_link`
 * The link points to `/var/data/datafile_1`
 * This link only breaks if the datafile moves, since the path is absolute

`ln -s data/datafile_1 ~/data1_link`
 * Creates a symbolic link in your home directory called `data1_link`
 * With a relative path of `data/datafile_1`
 * This link is probably not valid, unless `~/data/datafile_1` exists


# Permissions

View permissions on files with `ls -l`.

Permissions are organized into 4 parts:
 * File type (1 character)
 * owner permissions (3 characters)
 * group permissions (3 characters)
 * other permissions (3 characters)

File types are one of:
 * `-` -- A regular file
 * `d` -- A directory
 * `l` -- A symbolic link

File permissions are:
 * `r` or `-` for read or no read permissions
 * `w` or `-` for write or no write permissions
 * `x`, `s` or `-` for execute, setuid execute, or no execute
   permissions. We do not discuss setuid in detail.

Example:
`-rwxr-xr-- 1 dkohlbre grad 238 Oct 21  2016 README`
 * The first `-` indicates this is a regular file, not a directory or link
 * `rw-` the first triplet indicates the user (dkohlbre) has [r]ead,
   [w]rite and e[x]ecute permissions.
 * `r-x` the second triplet indicates the group (grad) has read and
   execute but not write permissions.
 * `r--` the final triplet indicates that everyone else has read
   permissions only


### Changing permissions

`chmod` (CHange MODe) changes the permissions on a file.

Generally, you should use the `chmod` command with the `+` or `-`
options to change flags. We also discussed the numerical system that
`chmod` accepts briefly in class.

Run as `chmod CHANGE FILE[s]`

A `chmod` change has 3 parts, who to change for, add or remove, and
permission.

Valid who to change for options:
 * `u` the owner of the file
 * `g` the group for the file
 * `o` others
 * `a` all of the above (the default if not specified)

Valid permissions:
 * `r` read
 * `w` write
 * `x` execute

Example:
`chmod g+x ascript.sh`
 * (+) adds a permission
 * (g) for the group
 * (x) allowing execution
 * of the file ascript.sh
