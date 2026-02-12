#!/usr/bin/env python
import sys
import re
if (len(sys.argv) == 2)and (re.search("z", sys.argv[1])):
    text = sys.argv[1]
    for i in text:
        if i =="z":
            print(i,end="")
else:
    print("none")