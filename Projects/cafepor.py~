Items = ["Coffee", "ice tea", "cappachino", "milk shake", "latte"]
prices = [2.69, 3.79, 3.90, 1.70, 2.25]
def menu():
    for i in range(0,len(Items)):
        print(f"{i + 1}. {Items[i]} = ${prices[i]}.","\t")
    print(f"{(len(Items) + 1)}. Exit.")
menu()
Bill = []
totalBill = 0
inp = int(input("Enter the S.no to select the option :"))
while(inp != 6):
    if(inp < 7 and inp > 0):
        quantity = int(input(f"How many of {Items[inp - 1]}s :"))
        totalBill += (quantity * prices[inp - 1])
        localBill = (quantity * prices[inp - 1])
        Bill.append([Items[inp - 1], quantity, localBill])
        localBill = 0
    else:
        print("Enter the the numbers from the menu !!")
    inp = int(input("\nAny thing else :"))
print("")
for i in range(0,len(Bill)):
    print(f"{Bill[i][0]} x{Bill[i][1]} = ${Bill[i][2]}")
print(f"\nYour total bill = ${totalBill}!")