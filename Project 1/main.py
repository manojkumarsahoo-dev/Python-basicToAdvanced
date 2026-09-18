import random

print('''
For Snake type s
For water type w
For gun type g
''')
#  1 is for snake
# -1 is for water
#  0 is for gun

computer = random.choice([1,0,-1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake",-1: "Water",0:"Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer==you):
    print("Draw")
else:
    if(computer ==-1 and you ==1):
        print("You Win!")
    elif(computer ==-1 and you ==0):
        print("You Lose!")    
    elif(computer ==1 and you ==-1):
        print("You Lose!")    
    elif(computer ==1 and you ==0):
        print("You Win")    
    elif(computer ==0 and you ==1):
        print("You Lose!")    
    elif(computer ==0 and you ==-1):
        print("You Win!")
    else :
        print("Something Went Wrong")        