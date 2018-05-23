#!/usr/bin/env python3

import sys

def copy_f(a_f,b_f):
    with open(a_f,'r') as afile:
        with open(b_f,'w') as bfile:
            bfile.write(afile.read())

if __name__=='__main__':
    if len(sys.argv)==3:
        copy_f(sys.argv[1],sys.argv[2])
    else:
        print("parameter error")
        print(sys.argv[0],"enter a_f and b_f")
        sys.exit(-1)
    sys.exit()



