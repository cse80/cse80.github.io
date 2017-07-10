#!/bin/bash

fatal() {
    echo $@ >&2
    exit 1
}

fn=$1
shift
[[ "$fn" == *.md ]] || fatal "Requires a markdown file"

pandoc \
    -s --highlight-style kate --css pandoc.css $fn \
    -o ${fn%md}html --toc --toc-depth=3 $@
