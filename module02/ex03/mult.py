#!/usr/bin/env python3
x= input("Enter ur first number")
y= input("Enter ur second number")
sum= 0

if x.isdigit() | y.isdigit():
	sum=int(x)*int(y)
	if sum < 0:
		print("The result is negative")
	if sum > 0:
		print("The result is positive")
	else:
		print("The result is zero")
else:
	print("no Number were added")
