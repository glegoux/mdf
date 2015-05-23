#!/usr/bin/env python3

##
#  ex7-s-sequences-generator/ :
#  Read input from STDIN.
#  Use 'print' to output your result, use the '\n' constant at the end of each result line.
#  Use 'local_print(variable, ... )' to display simple variables in a dedicated area.
#

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

seq=list(lines[0])
s_seq=""
lifo=[]
label=""
bo_markup=False
bc_markup=False
e_markup=False
pos=0

for k, c in enumerate(seq):

    if c == "<" and seq[k+1] != "/":
        bo_markup=True
        pos=k
    elif seq[k-1] == "<" and c == "/":
        bc_markup=True
        pos=k-1
        continue
    elif c.isalpha():
        label += c
    elif c == ">":
        if not(bc_markup):
            s_seq += "(" + label 
        e_markup=True
        
    if bo_markup and e_markup and not(bc_markup):
        lifo.append(label)
        label=""
        e_markup=False
        
    if bc_markup and e_markup:
        if not(bo_markup):
            print("E {} <{}> </{}>".format(pos, label, lifo[-1]))
            break
        if label != lifo[-1]:
            print("E {} {} {}".format(pos, label, lifo[-1]))
            break
        else:
            s_seq += ")"
            del lifo[-1]
        label=""
        if len(lifo) == 0:
            bo_markup=False
        bc_markup=False
        e_markup=False

else:
    print(s_seq)
