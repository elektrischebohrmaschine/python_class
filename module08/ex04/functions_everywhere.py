#!/usr/bin/env python3

def shrink(str):
    str= str[:8]

def enlarge(str):
    enlarged= "z"
    for x in range(8 - len(str)):
        str+= enlarged

def function(str= "0"):
    if str == "0":
        print("none")
    else:
        if len(str)==8:
            print(str)
        if len(str) < 8:
            enlarge(str)
            print(str)
        else:
            shrink(str)
            print(str)

function("vanja")
function()
function("backpack")
function("elektrischebohrmaschine")
