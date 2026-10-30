#!/usr/bin/env python3

import sys
entry_list= []

if len(sys.argv)< 2:
    print("none")
else:
    for word in sys.argv:
        entry_list.append(word)
        print(entry_list[-1])