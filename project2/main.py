# hand cricket

import random

choice = input("Enter the choice:")

if choice == "batting":
    yourScore = 0
    while(True):
        comp = random.randint(1,11)
        you = int(input("Enter the number:"))
        print(f"computer ={comp} and you = {you}")
        if comp == you :
            print("you out!")
            print(f"your score is {yourScore}")
            break
        yourScore += you
        with open("batting.txt","w") as f:
            f.write(f"Your batting score is {str(yourScore)}")

elif choice == "bowling":
    score = 0
    while(True):
        comp = random.randint(1,11)
        you = int(input("Enter the number:"))
        print(f"computer ={comp} and you = {you}")
        if comp == you :
            print("you win")
            print(f"computer score is {score}")
            break
        score += comp
        with open("bowling.txt","w") as f:
            f.write(f"Computers batting score :{str(yourScore)}")

else:
    print("Select only \'batting\' or \'bowling\'")








