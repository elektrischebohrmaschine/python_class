#!/usr/bin/env python3

import sys

parameter= len(sys.argv) -1

if parameter != 1:
        print("none")
else:
    user_input = input("What was the parameter? ")
    if sys.argv[1] == user_input:
        print("Good Job!")
    else:
        print("Nope, sorry...")
        
