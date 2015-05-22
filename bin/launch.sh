#!/bin/sh

# execute this script from another folder than the current one
cd $(dirname "$0")

# import color
. "../bin/color.sh"
. "../bin/helper.sh"

# script
message $YELLOW "--- BEGIN: Test MDF $(basename "$(pwd)") ($(pwd)) ---"

shebang=$(cat ../bin/main.py | head -1)
python_interpreter=$(echo "$shebang" | sed 's/^#![ ]*//')
version=$($python_interpreter --version 2>&1)
status_shebang=$(echo $?)
$(echo "$version" | grep -q "^Python 3")
status_version=$(echo $?)
if test $status_shebang -gt 0 -o $status_version -gt 0; then
    error "shebang '${shebang}' of main.py is incorrect, edit it.\n" \
    "The first line of main.py should be: #!<path_to_python_interpreter>.\n" \
    "To find this path, do the command 'which python'.\n" \
    "(Or 'which python3' if the version 2 is by default)\n" \
    "To use the version 3 of python"
    exit 1
fi

exos=$(ls -d */)
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
        answer=$(../../bin/main.py "$(pwd)" "answer.py" "track${number}.txt" \
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
