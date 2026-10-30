#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    print("parameters:", len(parameters))
    for parameter in parameters:
        print(parameter, len(parameter))

