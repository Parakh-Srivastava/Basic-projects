import random as ra

def ContinueGambling(Amount):
    inp = input("Do you wanna play again !?")
    inputLower = inp.lower()

    if inputLower[0] == 'y':
        casino(Amount, int(input("Enter the betting amount : $")))
    elif inputLower[0] == 'n':
        print("Exiting casino !!")
        return
    else:
        print("invalid output !!")
        ContinueGambling(Amount)

def casino(Amount, BillingAmount):
    if(Amount > 0):
        slot1 = ra.randint(1, 3)
        slot2 = ra.randint(1, 3)
        slot3 = ra.randint(1, 3)
        print(f"{slot1} | {slot2} | {slot3}")
        
        if slot1 == slot2 == slot3:
            print("Congratulations you win !!!")
            Amount += (BillingAmount * 999)
            print(f"You have now ${Amount}")
            ContinueGambling(Amount)
        else:
            print("you lose !!")
            Amount -= BillingAmount
            print(f"You have now ${Amount}")
            ContinueGambling(Amount)
    else:
        print("Insufficient Balance")
        return
        
def main():
    InitialAmount = int(input("Enter the amount you have : $"))
    BettingAmount = int(input("Enter the betting amount : $"))
    casino(InitialAmount, BettingAmount)

if __name__ == "__main__":
    main()