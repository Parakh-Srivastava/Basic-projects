List = []
goback = 1
while goback == 1:
    inp = int(input("If you wanna add please type 1.\nIf you wanna Edit press 2.\nIf you wanna delete press 3."))
    if(inp == 1):
        add = input("Enter what do you want to note :")
        List.append(add)
        print(List)
    elif(inp == 2):    
        print("Which element do you want to edit ? ( 1 to", len(List), ").")
        edit = int(input())
        List.pop(edit - 1)
        List.insert(edit - 1, input("Enter the edited version :"))
        print(List)
    elif(inp == 3):
        print("Which element do you want to remove ? ( 1 to", len(List), ").")
        edit = int(input())
        List.pop(edit - 1)
        print(List)
    else:
        print("Enter the values which are given in the option !!!")
    goback = int(input("Do you want to make another change? (yes = 1 ; no = Any other 'logical' button)"))