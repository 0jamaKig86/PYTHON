
import random
# library that we use in order to choose
# on random words from a list of words
my_file = open("test.txt", "r")
dictionary = my_file.read()

print("HELLO =))")


words = dictionary.split("\n")

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 13


while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char, end="\n")

        else:
            print("_")

    # for every failure 1 will be
    # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("\nYou Win")

    # this print the correct word
        print("The word is:", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("Guess a character:")[0]
    turns -= 1

    # every input character will be stored in guesses
    
    print(guesses)
    # check input with the character in word
    if guess not in word:

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

    # this will print the number of
    # turns left for the user
    print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You Loose")

my_file.close()
