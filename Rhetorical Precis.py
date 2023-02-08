author = input("Author: ")
author_split = author.split(" ")
author_last = author_split[1]
A = input("article,book review, essay, column, editorial, journals: ")
title  = input("Title: ")
B = input("argues, arugment, asserts, assertion, suggests, suggestion, claims, questions, explains, explanation: ")
Thesis = input("Thesis: ")
gender = input("his/her: ")
C = input("comparing, contrasting, telling, explaining, illustrating, demonstrating, defining, describing, list")
two = input("By doing what: ")
D = input(" show, point out, suggest, inform, persuade, convince")
three = input('Purpose of the article: ')
three1 = input("In order to ____:") 
E = input("formal, informal, sarcastic, humorous, contemptuous")
audience = input("Audience directed towards: ")


print(author + ", in the " + A +  " " + title + ", " + B + " that " + Thesis + ". " + author_last + " supports " + gender + " " + B + " by " + C + two + ". The author's purpose is to " + D + " in order to " +  three1 + " The author writes in " + E + " tone for " + audience + ".")