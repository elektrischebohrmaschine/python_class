#!/usr/bin/env python3
user_input= input("Enter a number less than 25")
input= int(user_input)

if input >= 25:
	print("Error")
	exit(0)
else:
	while (input<25):
		input=input+1
		print("We r inside of the Loop. Now at",input)
		
