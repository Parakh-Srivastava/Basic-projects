import random as ra

Elements = ["Stone", "Paper", "Scissor"]

computerInput = Elements[ra.randint(0,2)]
playerInput = Elements[int(input("1 : Stone || 2 : Paper || 3 : Scissors --->"))]

if computerInput == playerInput:
    print("Draw Round !!")
elif {computerInput == "Stone" and playerInput == "Scissor"} or 