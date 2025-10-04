item = {
    "chicken" : 200.45,
    "carrot" : 50.67,
    "peas" : 20.12,
    "brinjal" : 15.09
}

listItems = list(item.keys())
print("Items in stock :")

for i in range(len(listItems)):
    print(listItems[i])

itemsBought = {

}

cond = True
while cond == True:
    inp = input("Enter the item you wanna buy from the list : ")

    if inp.lower() in item.keys():
        noOfItem = int(input(f"How many of {inp.capitalize()}s do you need : "))
        tempList = {
            inp.lower() : noOfItem,
        }
        itemsBought.update(tempList)

        YN = input("Do you want to buy anything else : ")
        if YN[0] == 'n' or YN[0] =='N':
            break

    else:
        print("Item not in stock !!")

print(itemsBought )