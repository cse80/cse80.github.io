---
title:  'Shell Powertools'
...

Pipelines and looping are what make shell powerful, because they allow us to
glue together small pieces to do bigger, more interesting things.

Everything we've learned up until now (except maybe editors) is really mostly
included to facilitate this material.


## A Warning
**Before we get any further:** this file contains Bash-isms. Most of them are
marked when they occur, but if you add them to a script, ensure that the script
is being run by Bash. This means you *must* have the `#!/bin/bash` hashbang at
the top of your file, or you must always be running your script with `bash
YOUR_SCRIPT.sh`.

## Pipelines

### Text as a universal interface

In the words of Douglas McIlroy, the original creator of the pipelining
interface in Unix/Linux:

> This is the Unix philosophy: Write programs that do one thing and do it well.
> Write programs to work together. Write programs to handle text streams,
> because that is a universal interface.

So what does he mean by universal interface?

He means that humans understand readable text, and as a result, we're good at
coding around it. Programs that rely on text-based input and output, rather than
relying on some crazy binary format (type `less $(which less)` to see an
example of a human-unfriendly binary format) have the ability to interconnect
naturally and natively. If you choose a binary format, every program has to be
specifically written to support that format, and if you don't, it's hard to
interconnect them!

### `stdout`, `stderr`, `stdin`.

Throughout this class, we've seen a variety of programs that print text to the
console in front of you. We've also seen, briefly, the `>` and `>>` operators
that take that output, and redirects it to a file instead.

The shell is able to do that because the program is writing its output to a
place that the shell expects. The shell has to make the decision to show
output to you, write it to a file, or do something else entirely.

We will learn how and why we tell the shell to connect this (and other) output
channels in ways that are advantageous to us. As a result, it's important to
know what we're working with.

##### `stdout`

This standard output channel is called `stdout`. Whether you realize it or not,
the first thing you learn in any programming language is how to write to
standard out. In general, 'printing' from a program means writing data to
`stdout`. The `out` in `System.out.println` from Java is referencing `stdout`.
When you use `printf` in C, it defaults to `stdout` (you can use `fprintf` to
make it print to an arbitrary place). 

##### `stderr`
`stderr` (aka `System.err` in Java) is very similar to `stdout` (e.g. your
program can write to it), but it's designed for errors. The redirection
operators do NOT (by default) redirect `stderr`. That way, you can see an error
message even when your command redirects to a file, and programs can produce
error messages without damaging their output.

##### `stdin`
The other half of this equation is `stdin`, which is a standard way to provide
data to a program. We haven't used very much of `stdin` yet, but most of the
programs we've covered that take a filename as an argument are also happy to
read their input from `stdin` instead.

### Interconnecting programs

In addition to the output redirection operators, the shell lets you leverage the
fact that most programs accept input from `stdin` and write output to `stdout`
to let you chain programs together.

The `|` (pipe) operator allows you to do just that&mdash;provide the output of one
program as the input to the next. This allows you to build up pretty
sophisticated capabilities pretty quickly.

Before we get any further, here are some command building blocks that we can
use to demonstrate this:

 - `wc` will count bytes, words, and lines contained in any files whose names
   you give it. The `-l` flag tells it to only count lines.
 - `sort` will sort the lines you provide to it. The `-n` flag tells it to do a
   numerical-based sort (instead of alphabetical).
 - `head` will provide you with only the first few lines of output. By default
   this number is 10, but you can customize it with, for instance, `-n 4` to
   only show the top two lines.
 - `tail` works just like head, except it only does the last few lines of
   output. It can similarly be customized with the `-n` flag.

Combining these tools allows us to start answering interesting questions fairly
quickly. Assume we're inside the `~/corpus/english_words/adjectives` directory,
which contains:

```
$ ls
1syllable_adjectives.txt
2syllable_adjectives.txt
3syllable_adjectives.txt
4syllable_adjectives.txt
all_adjectives.txt
```

If we're curious how many of each type of adjectives there are, we could do: `wc
-l *`, which will yield:

```
$ wc -l *
  689 1syllable_adjectives.txt
 5187 2syllable_adjectives.txt
 6924 3syllable_adjectives.txt
 5301 4syllable_adjectives.txt
28479 all_adjectives.txt
46580 total
```

Already, we can see that there are more 3-syllable adjectives than any other.
Imagine for a moment, though, that we had a directory with hundreds of files. It
wouldn't necessarily be obvious which file had the most without having to look
through every line. We can combine `wc` with `sort`, though, to make it easier:

```
$ wc -l * | sort -n
   689 1syllable_adjectives.txt
  5187 2syllable_adjectives.txt
  5301 4syllable_adjectives.txt
  6924 3syllable_adjectives.txt
 28479 all_adjectives.txt
 46580 total
```

This is great, but if we were only interested in knowing the file with the
largest number of lines, we could add `tail` to the mix:

```
$ wc -l * | sort -n | tail -n 2
 28479 all_adjectives.txt
 46580 total
```

If we only want the single output line, we can throw `head` into the mix.

```
$ wc -l * | sort -n | tail -n 2 | head -n 1
 28479 all_adjectives.txt
```

In this way, we can combine arbitrary programs' outputs with arbitrary program's
inputs, so long as everyone is reading from `stdin` and writing to `stdout`.

### Another example

Just for fun, can you figure out what this code is doing?

~~~ {.sh}
winner=$(who \
    | cut -f 1 -d' ' \
    | sort \
    | uniq -c \
    | sort -n \
    | tail -n 1 \
    | sed 's/^ *//' \
    | cut -f2 -d' ')

echo "The winner is $winner!"
~~~




## Loops and Conditionals

Loops and conditionals, combined with pipelining, dramatically increase what the
shell can do.

### The For loop

The `for` loop looks like this:

~~~ {.sh}
for i in 1 2 3
do
    echo $i
done
# Outputs:
#  1
#  2
#  3
~~~

The loop iterates once for every value placed after the `in` keyword. Each
time through the loop, the variable (between `for` and `in`) will be equal to
one of the values placed after `in`.

This is powerful because you can place anything in that spot that the shell knows
how to manipulate:

~~~ {.sh}
# Show the first line of every text file in the current directory.
for i in *.txt
do
    head -n 1 $i
done
~~~

or even

~~~ {.sh}
# Make a directory inside ~/assignments for every
# currently-available assignment.
for assignment in $(cse80task available)
do
    mkdir ~/assignments/$assignment
done
~~~

This means that `for` in bash is really more of a `foreach`. If you want to do
the typical `for` thing (and give the variable an integer), you have to
list the integers for bash. Luckily, there are a few ways to do that:

 - The `seq [first [incr]] last` command generates a relevant sequence of
     numbers. For instance, `seq 3` will generate three lines: `1`, `2`, `3`.
 - Bash can generate its own sequences, with the somewhat-odd syntax `{N..M}`
     for a sequence from integer `N` to integer `M`, inclusive.

~~~ {.sh}
# Print all the numbers from 1 to 100, twice.
for i in $(seq 1 100)
do
    echo $i
done
for i in {1..100}
do
    echo $i
done
~~~

### Conditionals

Conditionals in shell are a bit funny, in that they tie into some of the same
mechanisms we've seen so far. The general syntax for an `if` statement is:

~~~ {.sh}
if CONDITION
then
    # any shell code here
elif CONDITION
    # any shell code here
else
    # any shell code here
fi
~~~

If you want, you can omit the `elif` and `else` portions of the block, so long
as the conditional ends with the `fi` (which is 'if' backwards).

The `CONDITION` above can be any executable that bash knows about. If it exits
with an exit status of zero (i.e. without an error), the condition is considered
'true'. Any non-zero return status is false.

That means we can do the following:

~~~ {.sh}
if mkdir $DIR_TO_CREATE
then
    echo "Directory created."
else
    echo "Directory creation failed. :-("
fi
~~~

### Testing your own conditions

Bash (and most shells) introduce some special-sauce to make a bunch of common
operations easier, since we often don't have a program that tests exactly what
we want already.

**In Bash (not other shells)**, the common syntax for this is `[[ EXPR ]]`,
where `EXPR` is an expression specific to the test you're running. This can be
thought of as having a program called `[[`, which requires some special
arguments.

**Two notes about syntax:**

1. If you find yourself reading other people's code, you may also see
   something like `[ EXPR ]` (note the single brackets). This is the official
   POSIX-compliant syntax, but it has fewer operations. If you're
   using Bash, you should be using the `[[` syntax.
1. You *must* have spaces between the brackets and the expression.
   `[[EXPR]]` will fail. This is because the system treats `[[` like a program,
   and `[[EXPR` would be a different program! Similarly, `EXPR]]` would be
   parsed as a single argument, and the `[[` command expects its final
   argument to be just `]]`.

The expression inside the brackets can either be unary (e.g. "is this file
executable?") or binary ("is this variable equal to that variable?").

##### Conditional expressions
One common operator is `-e`, a unary operator indicating whether a file exists.
If you were writing a blog generator, for instance, you might want to include a
special header on your page, but only if that header file exists:

~~~ {.sh}
if [[ -e $HEADER_FILE ]]
then
    cat $HEADER_FILE
fi
...
~~~

##### NOT
You can precede commands with the unary `!` operator, which negates whatever
follows it. You could, for instance, do the following:

~~~ {.sh}
# If there isn't an author file, write my username to it.
if [[ ! -e author ]]
then
    whoami > author
fi
...
~~~

##### Other operators
There are a bunch of file testing operators because, as it turns out,
files make up a big part of what you do with shell. There are, however, other
operators too:

 - Basic string comparisons can be done with the `==` operator (e.g.
   `[[ "apple" == "$fruit" ]]`). You can even use wildcards, if you're clever:
   `[[ "$fruit" == *berry ]]`.
 - Numerical comparisons use operators like `-gt` for **g**reater **t**han, e.g.
   `[[ "$n" -gt 3 ]]`. The other operators are named similarly, but are always
   two characters long.

The full list of conditional flags is available in the Bash `man`-page. Search
for `^CONDITIONAL EXPRESSIONS` (we'll explain that `^` at a later point).

##### Combining operators
You can combine operators with the operators `&&` (for 'and') and `||` (for
'or'). Thus, it's totally valid to do:

~~~ {.sh}
if [[ $n_users -ge 1 && $n_files_open -lt 20 ]]; then ...
~~~

This condition executes only if the number of users is greater than or equal to
(`-ge`) one AND the number of files open is less than 20.

### Conditional execution outside of `[[ ]]`s...

So far in this class, we've covered the output redirection operators (`>`,
`>>`), the pipe operator (`|`), and the semicolon (`;`). These operators work
not within the context of `[[ ]]`, but just between commands.

It turns out that `&&` and `||` can work between commands too. This leads to a
method of easily only running subsequent commands if the preceding command
exited with a zero exit status (for `and`) or only if it exited with a non-zero
exit status (for `or`).

~~~ {.sh}
# If the required file doesn't exist, print an error
# exit w/ exit code 1
[[ -e $RQD_FILE ]] || echo "ERROR: Missing file" && exit 1
~~~

To avoid making lines crazy-long, unless you only have a command or two to run,
we recommend using the full `if`-style conditional to maintain clarity and
readability.

### While loops

Now that we have conditionals, we can revisit loops. `while` loops execute so
long as a condition remains true. The syntax is:

~~~ {.sh}
while CONDITION
do
    ...
done
~~~

You can use any program's exit status, or any conditional expression discussed
in the section above in a `while` loop's `CONDITION`.

## Piping into Loops

Perhaps one of the most compelling use cases for `while` is when you need to do
line-by-line processing of some input. In this case, you can pipe data into your
loop, and read it in one line at a time with the `read` command:

~~~ {.sh}
# Input lines of the form 'TYPE CONTACT'
#
# Where TYPE is either 'web' or 'mail'
#  and 'CONTACT' is a URL (for web) or email address (for mail)
#
# For each contact, send them the info in the appropriate way.
cat $NOTIFICATION_RECIPIENTS | while read line
do
    if [[ "$line" == web* ]]; then
        # Send the info to the website
    elif [[ "$line" == mail* ]]; then
        # Email them the info
    fi
done
~~~
    

### A real-life example

An early version of the autograder used in this class split each assignment into
its own directory (titled `999_example`), and a single executable program within
that directory (e.g. `ASSIGNMENT_DIRECTORY/999_example/run_checker.sh`). We
'activated' an assignment by marking it as executable (`chmod +x
ASSIGNMENT_FILE`), and de-activated it by marking it not executable.

The `cse80task` program would locate these files, and do whatever it needed to
do. When you ran `cse80task available`, it did something very much like this:

~~~ {.sh}
# for each file/dir contained in directories in ASSIGNMENTS_DIR
for file in $ASSIGNMENTS_DIR/*/*; do
    # if it's a file and an executable
    if [[ -f "$file" && -x "$file" ]]; then
        # print out just the name of the directory it's in:
        # dirname removes the file's name from the path, then
        # basename removes all except for the final file/dir name
        echo $(basename $(dirname $file))
    fi
done
~~~

## Additional topics covered in class

In class, in addition to the topics above, we also covered basic use of:

 - `grep`
 - `sed`
 - `cut`

Please see the command reference page on the website for a discussion of these
tools.

