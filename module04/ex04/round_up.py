#!/usr/bin/env python3

user_input = input("Enter a number")
number= float(user_input)

if number % 1 == 0:
	print(number)
else :
	r_number=int(number)+1
	print(r_number)
