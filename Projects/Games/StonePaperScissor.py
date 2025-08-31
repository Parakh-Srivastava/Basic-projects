import random as ra

Elements = ["Stone", "Paper", "Scissor"]

def Inp():

    ComputerInput = Elements[ra.randint(0,2)]
    PlayerInput = Elements[int(input("1 : Stone || 2 : Paper || 3 : Scissors --->")) - 1]
    return ComputerInput, PlayerInput
    
CompPoint = 0
PlayerPoint = 0

while CompPoint != 5 and PlayerPoint != 5:
    
    CI, PI = Inp()
    
    print(f"Computer's Point = {CompPoint} || Player's Points = {PlayerPoint}")
    print(f"Computer plays -----> {CI}")

    if CI == PI:
        print("Draw Round !!")
    elif CI == "Stone" and PI == "Scissors":
        print("Computer wins !!")
        CompPoint += 1
    elif CI == "Paper" and PI == "Stone":
        print("Computer wins !!")
        CompPoint += 1
    elif CI == "Scissors" and PI == "Paper":
        print("Computer wins !!")
        CompPoint += 1
    else:
        print("Player wins!!")
        PlayerPoint += 1

if CompPoint == 5:
    print("Computer wins the game !!")
else:
    print("Player wins the game !!")