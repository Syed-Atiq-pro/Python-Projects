import random
# game rock paper scissor 

# 1 = rock   #   ( comp = 0 and you = 1 ) or (comp = -1 and you = 0 ) or ( comp = 1 and you = -1 ) // loss
# 0 = paper   #  ( comp = 1 and you = 0 ) or (comp = 0 and you = -1 ) or ( comp = -1 and you = 1 ) // win
# -1 = scissor   # ( comp = 1 and you = 1 ) or ( comp = 0 and you = 0 ) or ( comp = -1 and you = -1 )  // tie




while(True):
    comp =  random.choice([-1,0,1])
    yourstr = input("Enter your choice : ")
    yourdict = { 's' : -1 , 'p' : 0 ,'r' : 1}
    revdict = { -1 : 'Scissor' , 0 : 'Paper' , 1 : 'Rock'}
    
    if  ( yourstr == 'e' ):
        print("Byee....")
        break

    else:

        you = yourdict[yourstr]
            
        if (( comp == 0 and you == 1 ) or (comp == -1 and you == 0 ) or ( comp == 1 and you == -1 )):
            print(f"computer choice {revdict[comp]} and you choice {revdict[you]}")
            print("you loss!")

        elif( ( comp == 1 and you == 0 ) or (comp == 0 and you == -1 ) or ( comp == -1 and you == 1 ) ):
            print(f"computer choice {revdict[comp]} and you choice {revdict[you]}")
            print("you win!")

        elif( ( comp == 1 and you == 1 ) or ( comp == 0 and you == 0 ) or ( comp == -1 and you == -1 ) ):
            print(f"computer choice {revdict[comp]} and you choice {revdict[you]}")
            print("tie!")

        else:
            print("some thing went wrong!")

