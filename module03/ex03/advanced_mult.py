#!/usr/bin/env python3
x=0

while x<=10:
	y=0
	print("\nThe Table of", x, ": ",end= '')
	while y<=10:
		result= x*y
		print (result," ",end='')
		y+=1
	x=x+1

