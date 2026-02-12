#!/usr/bin/env python
import sys
if len(sys.argv) == 2:
    match=input("What was the parameter? ")
    target_string = sys.argv[1]
    if(match==target_string):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")