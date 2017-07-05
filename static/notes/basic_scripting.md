
# Scripting in Bash

Scripts in bash are just text files. They are interpreted (not compiled), so
they're easy to run and test. Because everything that is possible in a script is
also possible at the command line, I encourage you to try stuff out and test it.

## Creating a shell script

By convention, shell scripts are named with the '.sh' file extension. This isn't
required, but is nice (vim will give you syntax highlighting!).

In order to call a script, you'll either have to give the script to bash to run
directly, e.g.:

```
$ bash SCRIPT_NAME.sh
```

OR, you'll need to mark it as executable. You can mark a script as executable
with the command:
```
$ chmod +x SCRIPT_NAME.sh
```
(and can remove the executable flag with `-x`). We'll be revisiting `chmod` in a
future lecture.

Recall that once you've marked it as executable, you have to show bash that
you're providing a *path* to an executable, rather than an executable it should
go find in the typical places it looks. You can do that by either giving it an
absolute path (e.g. one that starts with `/`), or a relative path that starts
with `./`.

## Variables

Variables in bash are prefixed with a `$`, and are written to and accessed like
so:
```
my_variable="My variable content!"
echo $my_variable
```
You can also `unset` a variable (e.g. `unset my_variable`) to make it go away.

There are also a number of built-in variables, which we'll explore in a minute.

## Arguments

When writing shell scripts, it's often useful to pass in an argument to your
script so that it can change behavior accordingly.

By default, arguments passed into the shell are numbers `$1`, `$2`, and so on.
You can see a complete list of ALL of the arguments with `$@`.

If you only want a subset of your arguments, for instance if you wanted to save
away "all BUT the first argument" in its own variable, you can `shift` them.
e.g.:
```
$ echo $@
a b c d
$ shift
$ echo $@
b c d
$ shift 2
$ echo $@
d
```
The argument to `shift` is optional, defaults to 1, and indicates how many
arguments it should pop off the front.

In the future, if you're curious how many arguments you have, that's stored in
the intuitively-named `$#`.

## Exit Statii
Every command, function and builtin (that is, everything you can 'run') in the
shell will return a 'return code' (aka exit code or exit status). This is a
single integer that should indicate success or failure.

Zero (0) is the code for 'everything went fine'. Anything other than 0 is a
failure case.  By default, your shell script will exit with the 0 code, unless
you tell it to do otherwise.

In bash, you can grab the exit status of the most-recently-executed command with
the insightful `$?`.

Yes, these variable names are terrible. I remember them as:

 * `@` as in _all_ my arguments
 * the hash `#` as a number, the number of arguments, and
 * `?` as in "was that command successful?"

## Dying on errors

Until you have conditionals to work with (and often afterwards!) it's useful if
your script stops executing when any of the commands in your script fails. If
you add the following to the top of your script, it'll know to die whenever a
command executes with non-zero exit status:
```
set -e
```

## Other predefined variables

There exist a number of variables that you can use if you want that are
pre-defined for you. They largely recreate values that you also have commands
for:

 * `$USER`, which is equivalent to the command `whoami`, and shows your username
 * `$PWD`, which is equivalent to the command `pwd`, and shows the absolute path
    to your current directory
 * `$HOME` provides the absolute path to your home directory
 * `$PATH` contains the list of directories, `:`-delimited, of where your shell
    should look for programs to run.

## The `$PATH`

When you ask the shell to execute a program, the shell will go try and find an
executable file with that name in any of the directories it knows to look in
(that list is the contents of the `$PATH` variable). If you're curious where a
program is located, you can find it by running `which COMMAND`, e.g.
`which vim` should yield `/usr/bin/vim` on our systems.

## Subshells

It's often useful to grab the output of a command, and either store it into a
variable, or use it as an argument to a subsequent command. You can do that with
a subshell. The syntax looks like this:
```
this_dir_contents=$(ls)
```

This will become especially useful when we have loops, but it's also useful if,
for instance, you want to use the output from a command to create a filename.


## Other useful scripting tidbits.

 * Any line that starts with a `#` is considered a comment, and is ignored by the
shell. Document your code!
 * `dirname` will, given a path, give you just the part of the path that
    corresponds to the directory, e.g. `dirname /foo/bar.txt` gives you `/foo`.
 * `basename` is the complement of `dirname`: given a path, it'll give you just
    the file part of the path, e.g. `dirname /foo/bar.txt` gives you `bar.txt`.
 * `readlink -f` will, given a relative path, give you the absolute path.


