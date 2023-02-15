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
    
    while gameover == False:
        letterGuess = input("Guess the letters:")
        if letterGuess in letterList:
            print("You have already guessed that letter!")
        else:
            guessingLetters()
            printWord()
            guesses = GUESS - 1
        
  


main()