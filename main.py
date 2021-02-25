import random


# Generate a word from word list
def hangman():
    data = (open('words.txt').read().split())
    word = random.choice(data)
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ""


    #check if word is not empty
    while len(word) > 0:
        main = ""
        missed = 0

        #check if letter is valid
        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main = main + "-" + ""

        if main == word:
            print(word)
            print("You win!")
            break

        print("Guess the word: " + main)
        guess = input()

        #check if letter are valid
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Letter is not valid!" '\n' "Enter an alphabet letter")
            guess = input("Enter a letter: ")

        #check if guess is in word
        if guess not in word:
            print("Wrong guesses: " + guessmade)
            turns -= 1
            if turns == 9:
                print("Number of tries: 9")
                print("-----")
            if turns == 8:
                print("Number of tries: 8")
                print("-----")
                print("  0   ")
            if turns == 7:
                print("Number of tries: 7")
                print("-----")
                print("  0  ")
                print("  |  ")
            if turns == 6:
                print("Number of tries: 6")
                print("-----")
                print("  0  ")
                print("  |  ")
                print(" /   ")
            if turns == 5:
                print("Number of tries: 5")
                print("-----")
                print("  0  ")
                print("  |  ")
                print(" / \ ")
            if turns == 4:
                print("Number of tries: 4")
                print("-----")
                print("  0  ")
                print("  |\ ")
                print(" / \ ")
            if turns == 3:
                print("Number of tries: 3")
                print("-----")
                print("  0  ")
                print(" /|\ ")
                print(" / \ ")
            if turns == 2:
                print("Number of tries: 2")
                print("-----")
                print("  0  ")
                print(" /|\ ")
                print(" / \ ")
            if turns == 1:
                print("Number of tries: 1")
                print("-----")
                print("  0_ ")
                print(" /|\ ")
                print(" / \ ")
            if turns == 0:
                print("-----")
                print("  0_|")
                print(" /|\ ")
                print(" / \ ")
                print("You lose!")
                print("The correct word was: " + word)
                break














# Develop the user interface

name = input("Enter your name: ")
print("Hello " + name + ".", "Time to play hangman!")
print("------------------------------------")
hangman()
print("Guess the word in less than 10 tries")
