'''
ce1 : Your first program
print "Hello, World!"
'''

print('Hello, World!')


'''
ce2: Printing a Different String
Print the string "I am a self-taught programmer!" 
'''

print('I am a self-taught programmer!')

'''
ce3: Calculate
Print 8 multiplied by 9
'''

print(8*9)

'''
ce4: Arithmetic Operators Exercise 1
Create a program that creates two variables: x and y. Set x to 15 and y to 4. Then print the remainder when you divide x by y. 
'''

x=15
y=4
print(x%y)

'''
ce5: Arithmetic Operators Exercise 2
Create a program that prints the quotient when you divide 30 by 4. 
'''

print(30//4)

'''
ce6: Arithmetic Operators Exercise 3
Raise two to the third power and print the result 
'''

print(30//4)

'''
ce7: Comparison Operators Exercise
Print code that returns True if 10 and 10 are equal.
'''

print(10==10)

'''
ce8: Logical Operators Exercise 1
Change the following code so it evaluates to False: 1==1 and 3==3. Then, print your code. 
'''

print(not 1==1 and 3==3)

'''
ce9: Logical Operators Exercise 2
Print an expression using the keyword or that evaluates to True. 
'''

print(2==2 or 5>6)

'''
ce10: Statements Exercise
Write a program that has a variable called age and prints "You are old!" if age is over 18 and "You are young!" if it is less than 18. Then, assign the variable age to 21. 
'''

age = 21
if age>18:
    print('You are old!')
else:
    print('You are young!')
    

'''
ce11: Functional Excercise 1
Write a function named square that takes a number, n, as a parameter and returns that number squared. 
'''

def square(n):
    return n*n
    

'''
ce12: Functional Excercise 2
Create a function called print_string that accepts a string as a parameter and prints it.
'''

def print_string(str):
    print(str)
    


'''
ce13: Functional Excercise 3
Write a function called opt that takes three required parameters and two optional parameters.
'''

def opt(x,y,z,p=2,q='hola'):
    pass


'''
ce14: Built-in Functions Excercise 
Write a function called convert that takes a string as a parameter, converts it to a float and returns the result. Write a docstring that lets the user of the function know the string needs to be a number like this "100".
'''

def convert(s):
    '''
    Returns float value for the passed string
    :param s: string
    :return :float
    input string should be like'100'
    '''
    return float(s)


'''
ce15 : List excercise 1
create a list of your favourite musicians
'''

artists = ['Sonu Nigam','Arijit','Shreya Ghoshal','Sona Mohapatra','Gajendra Verma']

'''
ce16 : List excercises 2
create a list of your favourite musicians. save 'John Lennon' at index 4
'''

artists = ['Sonu Nigam','Arijit','Shreya Ghoshal','Sona Mohapatra','Gajendra Verma']
artists[4]='John Lennon'


'''
ce17 : List excercises 3
create a list of your favourite musicians. Append one artist to the list
'''

artists = ['Sonu Nigam','Arijit','Shreya Ghoshal','Sona Mohapatra','Gajendra Verma']
artists.append('Atif Aslam')
print(artists)


'''
ce18 : Tuple excercise
create a tuple of your favourite authors. 
'''
authors = ('P.L.Deshpande','V.P.Kale','Shivaji Savant','Vasant Kanetkar','Sane Guruji',)
print(authors)

'''
ce19 : Dictinary excercise
create a dictionary containing different attributes about you: height, favourite author, favourite color etc 
'''

me={'height':6.0,'favourite color':'green','favourite author':'Shivaji Savant',}

'''
ce20 : Containers excercise
Create a list called my_list. It should contain two tuples. Each tuple should have the longitude and latitude of somewhere you've lived or visited. The longitude and latitude should be floating-point numbers.
'''

my_list=[(40.7128,74.0060),(35.5585,75.4665)]


'''
ce21 : Strings excercise 1
Print every character in the string "Camus".
'''

for ch in "Camus":
    print(ch)

'''
ce22 : Strings excercise 2
Use a method to make the string "aldous was born in 1894." grammatically correct by capitalizing the first letter in the sentence. Then, print your new string. 
'''

print('aldous was born in 1894.'.capitalize())


'''
ce23 : Strings excercise 3
Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: ["Where now", "Who now", "When now"]. Print the list. 
'''

s = 'Where now? Who now? When now?'
splited_s = s.split('?')
print(splited_s)


'''
ce24 : Strings excercise 4
Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into the string "The fox jumped over the fence ." (Don't forget, you learned a method that turns a list of strings into a single string.) Note, there should be a blank space between the final "e" and the period at the end. Make sure to print your new string. 
'''

input_list=["The","fox","jumped","over","the","fence","."]
sentence = " ".join(input_list)
print(sentence)

'''
ce25 : Strings excercise 5
Create the string "threethreethree" using concatenation and print it. And then print it again using multiplication.
'''

concatenated_string = "three"+'three'+'three'
print(concatenated_string)
string_using_multiplication = 'three'*3
print(string_using_multiplication)


'''
ce26 : Strings II excercise 1
Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the characters before the comma and print it. 
'''

input_string = "It was a bright cold day in April, and the clocks were striking thirteen."
index_of_comma = input_string.index(',')
print(input_string[:index_of_comma])

'''
ce27 : Strings II excercise 2
Find dialogue in your favorite book (containing quotes) and turn it into a string and print it. Make sure your string contains double-quotes. 
'''

print("She said \"It's Awesome!!\"")

'''
ce28 : Strings II excercise 3
Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign and print the result. 
'''

input_string = "A screaming comes across the sky."
print(input_string.replace('s','$'))


'''
ce29 : Strings II excercise 4
Use a method to find the first index of the character "m" in the string "Hemingway" and print it. 
'''

print("Hemingway".index('m'))



'''
ce30 : For loops excercise 1
Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].
'''

input_list= ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for item in input_list:
    print(item)

'''
ce31 : For loops excercise 2
Print all the numbers from 20 to 30.
'''

for num in range(20,31):
    print(num)

'''
ce32 : For loops excercise 3
Print each item in the list ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"] and its index. Make sure to print its index first. Then, print the movie name.
'''

input_list =  ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for i in range(len(input_list)):
    print("{}\n{}".format(i,input_list[i]))
	


'''
ce33 : while loops excercise 
Write a while-loop and inside of your while-loop count down backward from 10 to 0. 
'''

i=10
while i>=0:
    print(i)
    i = i-1


'''
ce34 : Modules Exercise
Import the built-in statistics module. Use the mean function from it to calculate and print the mean of the following list: [1,2, 2, 3]. 
'''

import statistics

print(statistics.mean([1,2,2,3]))





'''
ce35 : Four Pillars Exercise 1
Create Rectangle and Square classes. Rectangle should have two instance variables: self.width and self.length. Square should have one instance variable self.s1. Define a method for both classes called calculate_perimeter that calculates the perimeter of the shapes they represent ad returns it. Then, create Rectangle and Square objects and call the method on both of them.
'''

class Rectangle:
    
    def __init__(self,length,width):
        self.width=width
        self.length=length
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square:
    def __init__(self,s1):
        self.s1 = s1
        
    def calculate_perimeter(self):
        return 4 * (self.s1)
        
rect = Rectangle(2,3)
sq = Square(2)

rect.calculate_perimeter()
sq.calculate_perimeter()

'''
ce36 : Four Pillars Exercise 2
Define a method in your Square class called change_size that allows you to pass in a number that increases or decreases (if the number is negative) each side of a Square object by that number. Make sure your Square class's instance variable is self.s1. 
'''

class Rectangle:
    
    def __init__(self,length,width):
        self.width=width
        self.length=length
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square:
    def __init__(self,s1):
        self.s1 = s1
        
    def calculate_perimeter(self):
        return 4 * (self.s1)
        
    def change_size(self,change_size_by):
        self.s1 = self.s1 + change_size_by
        
        
rect = Rectangle(2,3)
sq = Square(2)

rect.calculate_perimeter()
sq.calculate_perimeter()


'''
ce37 : More OOP Exercise 1
Add a square_list class variable to a class called Square and set your class up so that every time you create a new Square object, the new object gets added to the square_list.
'''
class Square:
    square_list=[]
    def __init__(self,s1=None):
        self.s1 = s1
        self.square_list.append(self)
        
    def calculate_perimeter(self):
        return 4 * (self.s1)
        
    def change_size(self,change_size_by):
        self.s1 = self.s1 + change_size_by
        

sq = Square(2)
sq2 = Square(3)
print(sq.square_list)

'''
ce38 : More OOP Exercise 2
Create a Square class that has one method that calculates its perimeter. When you print a Square object, a message should print telling you the length of each of the four sides of the shape. For example, the code print(Square(29))  should print "29 by 29 by 29 by 29".
'''

class Square:
    
    def __init__(self,s1):
        self.s1 = s1
        
        
        
    def calculate_perimeter(self):
        return 4 * (self.s1)
        
    def __repr__(self):
         return ('{} by {} by {} by {}'.format(self.s1,self.s1,self.s1,self.s1))
        

square = Square(5)
print(square)


'''
ce39 : More OOP Exercise 3
Write a function that takes two objects as parameters and returns True if they are the same object, and False if not.
'''

class Square:
    def __init__(self):
        self.name = 'Square'

def same(a, b):
        return a is b
		

'''
ce40 : Match Two
Create a regular expression that matches any word that starts with any character and is followed by two o's. Then use Python's re module to match boo and loo in the sentence "The ghost that says boo haunts the loo". Save the result in a variable and print it. 
'''

class Square:
import re

input_string = "The ghost that says boo haunts the loo"
input_string_list = input_string.split(' ')

re_pattern = ".oo"

result = re.findall(re_pattern,input_string)
print(result)

'''
ce41 : Match Two
Use a list comprehension to turn [1, 7, 5, 3, 2] into a new list. The new list should contain all of the integers in the original list multiplied by 7. Then, print your new list.   
'''

input_list=[1,7,5,3,2]
new_list = [num*7 for num in input_list]
print(new_list)


'''
ce42 : Data Structures Exercise 1
Reverse the string "yesterday" using a stack and print it. You should use a class called Stack. You need to define a push and pop method in your class. 
'''

class Stack:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    


def reverse_string(input_string):
    stack = Stack()

    for c in input_string:
        stack.push(c)
    
    reversed_string_list=[]

    for i in range(stack.size()):
        reversed_string_list.append(stack.pop())
        
    return ''.join(reversed_string_list)
        
print(reverse_string('yesterday'))

'''
ce43 : Data Structures Exercise 2
Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5].   
'''

class Stack:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
def reverse_list(input_list):
    stack = Stack()
    
    for element in input_list:
        stack.push(element)
    
    reversed_list =[]
    
    for i in range(stack.size()):
        reversed_list.append(stack.pop())
        
    return reversed_list

print(reverse_list([1,2,3,4,5]))












