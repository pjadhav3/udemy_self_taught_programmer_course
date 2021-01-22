'''
Assignment 5: Modify Hangman

Modify your Hangman game, so a word is selected randomly from a list of words.

'''

def hangman(word):

    print(word)

    wrong = 0

    stages = ["",

             "________        ",

             "|               ",

             "|        |      ",

             "|        0      ",

             "|       /|\     ",

             "|       / \     ",

             "|               "

              ]

    rletters = list(word)

    board = ["__"] * len(word)

    win = False

    print("Welcome to Hangman")

    while wrong < len(stages) - 1:

        print("\n")

        msg = "Guess a letter"

        char = input(msg)

        if char in rletters:

            cind = rletters.index(char)

            board[cind] = char

            rletters[cind] = '$'

        else:

            wrong += 1

        print((" ".join(board)))

        e = wrong + 1

        print("\n".join(stages[0: e]))

        if "__" not in board:

            print("You win!")

            print(" ".join(board))

            win = True

            break

    if not win:

        print("\n"

              .join(stages[0: wrong]))

        print("You lose! It was {}.".format(word))


# modified code

words = ['mat','school','paper','game','run']


random_index = random.randint(0, len(words))

print(random_index)

random_word = words[random_index]


hangman(random_word)