import random
l=["stone","paper","scissor"]


while True:
    ccount=0
    ucount=0
    uc=int(input('''    
Game Start.....
1 Yes
2 NO | Exit
        '''))
    if uc==1:
        for i in range(1,6): # for 5 round'
            userInput=int(input('''
1 Stone
2 Scissor
3 Paper         
                '''))
            if userInput==1:
                uchoice="stone"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
               print("Computer Value",Cchoice)
               print("User Value",uchoice)
               print("Game Draw")
               ucount=ucount+1
               ccount=ccount+1
            elif(uchoice=="stone" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="stone") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User1 Value",uchoice)
                print("Computer win")
                ccount=ccount+1

        if ucount==ccount:
            print("Final Game Draw...")
            print("User score",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final You Win Game ...")
            print("User score",ucount)
            print("Computer Score",ccount)
        elif ucount<ccount:
            print("Final Computer lose Game...")
            print("User score",ucount)
            print("Computer Score",ccount)

        

# else:
    # break