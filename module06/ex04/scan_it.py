#!/usr/bin/env python3

import re
import sys

parameters= len(sys.argv)-1

if parameters == 2:
    result= len(re.findall(sys.argv[1],sys.argv[2], re.IGNORECASE))
    print(result)
else:
    print("none")