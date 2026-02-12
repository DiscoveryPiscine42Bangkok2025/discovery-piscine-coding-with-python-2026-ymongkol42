#!/usr/bin/env python
import sys
import re
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    target_string = sys.argv[2]
    matches = re.findall(keyword, target_string)
    count = len(matches)
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")