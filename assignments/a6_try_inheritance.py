'''
Assignment 6: Try inheritance

Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called. Change your Square and Rectangle classes from the previous challenges to inherit from Shape, create Square and Rectangle objects, and call the new method on both of them.

'''

class Shape:

   

    def what_am_i(self):

        print('I am a shape')

   

class Rectangle(Shape):

   

    def __init__(self,length,width):

        self.width=width

        self.length=length

   

    def calculate_perimeter(self):

        return 2 * (self.length + self.width)


class Square(Shape):

    def __init__(self,s1):

        self.s1 = s1

       

    def calculate_perimeter(self):

        return 4 * (self.s1)

       

    def change_size(self,change_size_by):

        self.s1 = self.s1 + change_size_by

       

       

rect = Rectangle(2,3)

sq = Square(2)


rect.what_am_i()

sq.what_am_i()