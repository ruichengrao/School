import random
GUESS = 6 
wordlist = []
letterList = []

with open("words.txt") as file:

    for each in file.readlines():
        splitWord = each.split()
        wordlist.append(splitWord)



word = random.choice(wordlist)



def duringGame():
   for i in word:
       if i in letterList:
           wordlist.append(i)
       else:
           wordlist.append("_")

guessLetter = input("Guess the letters")