# ROOCK PAPER SCISSOR GAME (USING PYTHON MODULE)
import random
l=["rock","paper","scissor"]

# ROCK VS PAPER --> PAPER WIN
# ROCK  VS SCISSOR --> ROCK WIN
# PAPER VS SCISSOR --> SCISSOR WIN


while True :  #mein isko bar bar terminate nahi karna chahta jab game end ho toh fir se suru ho jae
    ccount=0
    ucount=0

    uc=int(input('''
game start.....
1 yes
2 no | exit
:-->
    '''))  #yahha humne pucha game khelna hai ki nahi user se
    if uc==1:
       for a in range (1,6): #yaha game pach baar chalega

           userinput=int(input('''
           1 rock
           2 scissor
           3 paper
           :--->''')) #agar 5 baar input chala toh apn pach baar input dege
           print()



           if userinput==1:
              uchoice="rock"
           elif userinput==2:
                uchoice="scissor"
           elif userinput==3:
                uchoice="paper" #yeah user ki choice hai 1,2,3  wo kya lena chahta hai


           cchoice=random.choice(l) #return a random element from list ,yeah kyu kia kyu ki ab hame comouter ki choice chahi e
           if cchoice==uchoice: #yaha computer and apni value same hai
              print("computer value :-->",cchoice)
              print("user value:-->",uchoice)
              print("game draw")
              ucount=ucount+1
              ccount=ccount+1
           elif (uchoice=="rock" and cchoice=="scissor") or (uchoice =="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice =="paper"): #and--> return true if both statement is true ,or-->return true if one of the statement is true
                print ("computer value:--> ",cchoice)
                print ("user value:--> ",uchoice)
                print ("you win....")
                ucount=ucount+1
           else:
                print("computer value :--> ",cchoice)
                print("user value:-->",uchoice)
                print("computer win.....")
                ccount=ccount+1

           if ucount==ccount:
              print()
              print("final game draw...")
              print(" game score")
              print("user score",ucount)
              print("computer score",ccount)
           elif ucount > ccount:
                print()
                print("final you win the game...")
                print()
                print(" game score")
                print (" user score :-->",ucount)
                print("computer score:-->",ccount)
           else:
                print()
                print("final computer win the game....")
                print()
                print(" game score")
                print("user score:-->",ucount)
                print("computer score:-->",ccount)
           print ("******************************************************")


    else:
        break



