#!/usr/bin/env python3
user_input =int(input("pls enter a number"))


if user_input == 0:
	print("This number is both positive and negative")
elif user_input < 0:
	print("This number is negative")
elif user_input > 0:
	print("This number is positive")
