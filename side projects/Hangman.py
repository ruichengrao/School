import random
GUESS = 6 
wordlist = []
gameover = False 
letterList = []

with open("side projects\words.txt") as file:

    for each in file.readlines():
        splitWord = each.split()
        wordlist.append(splitWord)

global word
word = random.choice(wordlist)[0]
print(word)

def guessingLetters():
    for letter in word:
        if letter not in letterList:
            return False
    return True

printedWord = []

    
for letter in word:
    printedWord.append("")

def printWord():
    global printedWord
    global guessLetter
    global word
    letter_num = 0
    for letter in word:
        if letter in letterList:
            printedWord[letter_num] = letter
        else:
            printedWord[letter_num] = "_"
        letter_num += 1
    print(",".join(printedWord))



def main():
    global guessingLetters
    global word
    global printedWord
    global gameover
    global letterGuess

    guessCount = 0

    while gameover == False: 
        printWord()
        print("You have {} guess left".format(GUESS - guessCount))
        letterGuess = input("Guess the letters:")
        while letterGuess in letterList:
            print("You have already guessed that letter!")
            letterGuess = input("Guess the letters:")
        letterList.append(letterGuess)
        if letterGuess in word:
            print("The letter '{}' is in the word!".format(letterGuess))
            print("_____________________________________________________________")
            if guessingLetters():
                print(word)
                print("You won!")
                gameover = True
        else:
            print("The letter '{}' is not in the word!".format(letterGuess))
            print("_____________________________________________________________")

            guessCount+=1
            if guessCount == GUESS:
                print("You Lost! :( ")
                print(word)
                gameover = True

    
main()