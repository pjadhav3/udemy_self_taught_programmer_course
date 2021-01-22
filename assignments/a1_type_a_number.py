'''
Assignment 1 : Type a number
Questions for this assignment
Write a program that asks the user to type a number. Convert the number to an integer and print it. If you can't convert their input to an integer, print a message that says "Please type an integer."
'''

num = input('type a number')

try:
    print(int(num))
	
except ValueError:
    print('Please type an integer.')