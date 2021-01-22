'''
Assignment 3: Create a module
Create a module named cubed with a function that takes a number as a parameter, and returns the number cubed. Import and call the function from another module.
'''

#cubed.py module

def cube_of(num):

return num ** 3


#importing cubed module in other module

import cubed

print(cubed.cube_of(5))