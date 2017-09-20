#!/bin/sh

# import
cd $(git rev-parse --show-toplevel)
. "./bin/color.sh"
. "./bin/helper.sh"
cd - 2>&1 > /dev/null

# execute this script from another folder than the current one
cd $(dirname "$0")

# config
DEFAULT_EDITOR="pycharm"
ALLOWED_EDITOR_TERM="vim:nano:emacs -nw:more:less:cat"
ALLOWED_EDITOR="eclipse:gedit:atom:pycharm"

exos=$(ls -d */ 2> /dev/null)

if [ -z "$exos" ]; then
  >&2 echo "ERROR: No one exercise!"
  exit 1
fi

editor="${1:-$DEFAULT_EDITOR}"
which "$(echo $editor | cut -d " " -f1)" > /dev/null
if test $? -ne 0; then
    error "'$editor' uninstalled"
    exit 1
fi

message $YELLOW "--- BEGIN: Edit MDF $(basename "$(pwd)") ($(pwd)) ---"

term=false
known=false
IFS_OLD="${IFS}"
IFS=:
for allowed_editor in $ALLOWED_EDITOR_TERM; do
    if test "$allowed_editor" = "$editor"; then
        known=true
        term=true
    fi
done

for allowed_editor in $ALLOWED_EDITOR; do
    if test "$allowed_editor" = "$editor"; then
        known=true
    fi
done
IFS=${IFS_OLD}

if ! $known; then
    error "'$editor' unknown (allowed editors: see constants ALLOWED_EDITOR_TERM and ALLOWED_EDITOR)"
    exit 1
fi

for exo in $exos; do
    cd $exo
    message $BLUE "** $exo"
    if ! test -r ./answer.py; then
        error "missing or unreadable answer.py"
        exit
    fi
    if ! test -w ./answer.py; then
        error "missing or unwritable answer.py"
        exit
    fi
    success "Edition of answer.py"
    cd ..
done

files="$(find . -maxdepth 2 -type f -name answer.py | sort )"
if $term; then
    if test "$editor" != 'cat' -a "$editor" != more -a "$editor" != less; then
        $editor $files > /dev/null 2>&1
    else
        $editor $files
    fi
else
    $editor $files > /dev/null 2>&1 &
fi

message $YELLOW "--- END ---"
exit 0
