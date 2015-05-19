#!/usr/bin/env python3

import sys
import traceback
import os
from io import StringIO

pwd = sys.argv[1]
scriptname = pwd + "/" + sys.argv[2]
output_file = pwd + "/" + sys.argv[3]

def local_print(*args, **kwargs):
    global output_file
    f = open(output_file, "a")
    first_arg = True
    for arg in args:
        if first_arg:
            first_arg = False
        else:
            f.write(" ")
        f.write(str(arg))
    if kwargs.get("end", True) != "":
        f.write("\n")
    f.close()

def include(scriptname):
    if os.path.exists(scriptname):
        stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(open(scriptname).read())
        sys.stdout = stdout
        print(redirected_output.getvalue(), end="")
    else:
        exit(1)

os.system('rm -f "' + output_file + '" &> /dev/null')
include(scriptname)
exit(0)
