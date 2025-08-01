import random as ra

Inputs = ["Scissors", "Paper", "Rock"]

ScoreToWin = int(input("Enter score needed to win : "))

PlayerScore = 0
ComputerScore = 0

while PlayerScore != ScoreToWin and ComputerScore != ScoreToWin:

    PlayInp = Inputs[int(input("Enter the number to : [1 = Scissor : 2 = Paper : 3 = Rock]")) - 1]

    CompInp = Inputs[ra.randint(0,2)]
    print(f"Computer plays : {CompInp}.")

    if (PlayInp == "Scissors" and CompInp == "Paper") or (PlayInp == "Paper" and CompInp == "Rock") or (PlayInp == "Rock" and CompInp == "Scissors"):
        PlayerScore += 1
        print(f"Player : {PlayerScore}")
        print(f"Computer : {ComputerScore}")
    elif(PlayInp == CompInp):
        print("Draw !!")
    else:
        ComputerScore +=1
        print(f"Computer : {ComputerScore}")
        print(f"Player : {PlayerScore}")

if PlayerScore == ScoreToWin:
    print("The player wins !!")
else:
    print("Computer wins !!")