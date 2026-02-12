#!/usr/bin/env python
import sys
num =len(sys.argv)
if num > 1:
    print(f"parameter: {num-1}")
    parameters = sys.argv[1:]
    for i in parameters:
        print(f"{i}: {len(i)}")

else:
    print("none")