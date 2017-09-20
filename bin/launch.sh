#!/bin/sh

# import
cd $(git rev-parse --show-toplevel)
ROOT_DIR="${PWD}"
. "./bin/color.sh"
. "./bin/helper.sh"
cd - 2>&1 > /dev/null

# execute this script from another folder than the current one
cd $(dirname "$0")

exos=$(ls -d */ 2> /dev/null)

if [ -z "$exos" ]; then
  >&2 echo "ERROR: No one exercise!"
  exit 1
fi

# script
message $YELLOW "--- BEGIN: Test MDF $(basename "$(pwd)") ($(pwd)) ---"

for exo in $exos; do
    message $BLUE "** $exo"
    cd "$exo"
    inputs=$(ls -1 | grep -E ^input)
    for input in $inputs; do
        echo "$input:"
        number=$(echo $input | sed 's/^input//' | sed 's/\.txt$//')
        output=output${number}.txt
        if ! test -r $ouput; then
            error "$ouput is missing or unreadable"
            exit 1
        fi
        # suppose that there is no print before a fault in the code,
        # because it will be illogical
        answer=$(${ROOT_DIR}/bin/main.py "$(pwd)" "answer.py" "track${number}.txt" \
            < "$(pwd)/$input" 2>&1)
        status_code=$(echo $?)
        if test $status_code -gt 0; then
            error "answer.py didn't execute correctly"
            # clean traceback from main.py, to keep only traceback from answer.py
            answer=$(echo "$answer" | sed '2,5d' | sed '2s/"<string>"/"answer.py"/')
            message $RED "$answer"
        fi
        if test "$answer" = "$(cat $output)"; then
            success "it's correct"
            if test -r track${number}.txt; then
                info "your track:"
                cat track${number}.txt
            fi
            continue
        else
            error "your result is incorrect"
        fi
        info "input:"
        cat $input
        echo
        info "result:"
        cat $output
        echo
        if test $status_code -eq 0; then
            info "your answer:"
            echo "$answer"
        fi
        if test -r track${number}.txt; then
            info "your track:"
            cat track${number}.txt
         fi
        exit 1
    done
    cd ..
done

message $YELLOW "--- END ---"
exit 0
