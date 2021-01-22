'''
Assignment 2: Guess a number

Write a program with an infinite loop and a list of numbers.Each time through the loop the program should ask the user to guess a number(or type q to quit). If they type q, the program should end. Otherwise, it should tell them whether or not they successfully guessed a number in the list or not.
'''

nums = [3,6,9]


while True:

    guess = input('Guess the number! or type \'q\' to quit\n')

    if guess=='q':

        break

    try:

        if int(guess) in nums:

            print('Guesses Successfully!')

        else:

            print("Try again!")

    except ValueError:

        print('Enter a number')