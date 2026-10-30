#!/usr/bin/env python3

def shrink(str):
    str= str[:8]
    print(str)

def enlarge(str):
    enlarged= "z"
    for x in range(8 - len(str)):
        str+= enlarged
    print(str)

def function(str= "0"):
    if str == "0":
        print("none")
    
    elif len(str)==8:
        print(str)
    elif len(str) < 8:
        enlarge(str)
    else:
        shrink(str)

function("vanja")
function()
function("backpack")
function("elektrischebohrmaschine")
