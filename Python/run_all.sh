#!/bin/sh

low=1
high=999
if [ ! -z $1 ]; then low=$1; fi
if [ ! -z $2 ]; then high=$2; fi

i=1
for f in problems/p*.py; do
    if [ $i -ge $low ]; then
        echo -n "$i;"
        python3 $f | tail -n1 | cut -c 7-
    fi

    i=$((i+1))
    if [ $i -gt $high ]; then exit; fi
done