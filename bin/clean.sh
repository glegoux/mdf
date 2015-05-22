#!/bin/sh

# execute this script from another folder than the current one
cd $(dirname "$0")

# import color
. "../bin/color.sh"
. "../bin/helper.sh"

message $YELLOW "--- BEGIN: Clean MDF $(basename "$(pwd)") ($(pwd)) ---"

exos=$(ls -d */)
for exo in $exos; do
    message $BLUE "** $exo"
    echo -n "Do you want really reset answer.py ? (y/n): "
    read answer
    if test "$answer" != "y"; then
        continue
    fi
    cd "$exo"
    if ! test -w ./answer.py; then
        error "missing or unwritable answer.py"
        exit 1
    fi
    cat <<EOF > ./answer.py
#!/usr/bin/env python3

#  $exo :
#  Read input from STDIN.
#  Use print to output your result, use the '\n' constant at the end of each result line.
#  Use local_print (variable, ... ) to display simple variables in a dedicated area.
#

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

print("TODO")
EOF
    success "clean answer.py"
    cd ..
done

message $YELLOW "--- END ---"
exit 0
