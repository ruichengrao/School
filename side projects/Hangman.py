import random
GUESS = 6 
wordlist = []


with open("words.txt") as file:

    for each in file.readlines():
        splitWord = each.split()
        wordlist.append(splitWord)


global word
word = random.choice(wordlist)[0]
print(word)

letterList = [*word]
print(letterList)
guessLetter = input("Guess the letters:")

def guessingLetters():
    for letter in word:
        if letter not in guessLetter:
            return False
    return True

if guessingLetters():
    print("You Win!")
else:
    print("Not Done Yet!")

printedWord = []

    
for letter in word:
    printedWord.append("")

def printWord():
    global printedWord
    global guessLetter
    global word
    letter_num = 0
    for letter in word:
        if letter in guessLetter:
            printedWord[letter_num] = letter
        else:
            printedWord[letter_num] = "_"
        letter_num += 1
