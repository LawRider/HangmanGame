from random import choice

words = ['python', 'java', 'kotlin', 'javascript']
random_word = choice(words)
guess_word = list("-" * len(random_word))
tried_letters = set()
tries = 8


def print_word(word):
    print("\n" + "".join(word))


def check_word(letter):
    global tries, tried_letters
    if len(letter) != 1:
        print("You should input a single letter")
    elif not letter.islower():
        print("Please enter a lowercase English letter")
    elif letter in tried_letters:
        print("You've already guessed this letter")
    elif letter not in random_word:
        print("That letter doesn't appear in the word")
        tried_letters.add(letter)
        tries -= 1
    else:
        for i in range(len(random_word)):
            if letter == random_word[i]:
                guess_word[i] = letter
                tried_letters.add(letter)
        """ ANOTHER VARIANT
        for pos, let in enumerate(random_word):
            if let == letter:
                guess_word[pos] = let
                tried_letters.add(letter)
        """


print("H A N G M A N")

while True:
    print('Type "play" to play the game, "exit" to quit:')
    reply = input()
    if reply == 'play':
        while tries:
            print_word(guess_word)
            guess_letter = input("Input a letter: ")
            check_word(guess_letter)
            if '-' not in guess_word:
                print_word(guess_word)
                print("You guessed the word!\nYou survived!\n")
                break
        else:
            print("You lost!\n")
    elif reply == 'exit':
        quit()
    else:
        continue
