#Jason Luis 
#December 16, 2023 
#This program is an 8-Ball that will give an answer to each question it is being asked. 

#Variables

from os import name
import random
from tkinter.messagebox import QUESTION 

Question = input("Question: ")

Answer = ("") 

#8-Ball Code 

random_number = random.randint(1,10) 

if random_number == 1:
    Answer = "Yes - Definitely" 
elif random_number == 2: 
    Answer = "It is decidedly so"
elif random_number == 3:
    Answer = "Without a doubt"
elif random_number == 4:
    Answer = "Reply hazy, try again"
elif random_number == 5: 
    Answer = "Ask again later"
elif random_number == 6:
    Answer = "Better not tell you now"
elif random_number == 7:
    Answer = "The Outlook is not so good"
elif random_number == 8:
    Answer = "Very Doubtful" 
else: 
    Answer = "Try Again" 

#Output of the program 

print("\nMagic 8-Ball:", Answer)



