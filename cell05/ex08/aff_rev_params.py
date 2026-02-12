#!/usr/bin/env python
import sys
if(len(sys.argv)>=3):
    for i in range (len(sys.argv)-1):
        text=sys.argv[-(i+1)];
        print(f"{text}");
else:
    print("none");