# creating a game called guess the number 
# in it we have to guess the number genrated by computer from one to hundred in minimum chances

from random import randint
# Here we are importing the randint from random to genrate number between 1 to 100

def Guess(comp):
    guesses = 0
    while(True):
        you = int(input("Enter the number  :"))
       

        if you == comp:
            print("You Got It! ")
            print(f"You are guess the number in {guesses} Guesses!")
            break 

        elif you > comp:
            print("Try somthing smaller value")

        elif you < comp :
            print("Try somthing bigger value")

        else:
            print("Something went wrong!")

        guesses += 1


Comp = randint(1,100)

Guess(Comp)
