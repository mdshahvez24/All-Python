# def game():
#     return 6

# score = game()
# with open("hiscore.txt") as f:
#     hiscore = int(f.read())

#     if hiscore<score:

#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

def game():
    return 44677

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))