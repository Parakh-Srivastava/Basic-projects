with open("todolist.txt", "r") as f:
    
    List = f.readlines()
    Tasks = []
    
    for i in range(0, len(List)):
        Tasks.append(List[i].strip())

def ListRead():
    
    for i in range(0, len(Tasks)):
        print(f"{i + 1}) {Tasks[i]}")

def ListAdd():

    inp = input("Enter the task :- ")    
    
    if len(Tasks) == 0:
        with open("todolist.txt", "a") as f:
            f.write(f"{inp}")
        Tasks.append(inp)
    else:
        with open("todolist.txt", "a") as f:
            f.write(f"\n{inp}")
        Tasks.append(inp)
    print("\n")
    ListRead()

def DeleteList():
    
    Tasknum = int(input("Enter the task number you wanna delete : "))
    Tasks.pop(Tasknum - 1)
    
    with open("todolist.txt", "r+") as f:
        f.truncate(0)
    
    if len(Tasks) == 0:
        print("")
    else:
        with open("todolist.txt", "a") as f:
            f.write(f"{Tasks[0]}")
            
        for i in range(1, len(Tasks)):
            with open("todolist.txt", "a") as f:
                f.write(f"\n{Tasks[i]}")
            ListRead()

def ListEdit():
    
    Tasknum = int(input("Enter the task number you want to edit : "))
    print(f"Original task : {Tasks[Tasknum - 1]}")
    Tasks[Tasknum - 1] = input("Write the edited version : ")
    
    with open("todolist.txt", "r+") as f:
        f.truncate(0)
    
    with open("todolist.txt", "a") as f:
        f.write(f"{Tasks[0]}")

    for i in range(1, len(Tasks)):
        with open("todolist.txt", "a") as f:
            f.write(f"\n{Tasks[i]}")
        print("\n")
        ListRead()

def main(inp):
    
    if inp == 1:
       ListRead()
       main(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n")))
    
    elif inp == 2:
        ListAdd()
        main(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n")))
    
    elif inp == 3:
        
        if len(Tasks) == 0:
            print("There are no task present to delete.")
        
        else:
            DeleteList()
        main(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n")))
    
    elif inp == 4:
        
        if len(Tasks) == 0:
            print("There are no task present to edit.")
        
        else:
            ListEdit()
        main(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n")))
    
    elif inp == 5:
        return
    
    else:
        main(int(input("Invalid output, try again : ")))


if __name__ == "__main__":
    print("\n\t\t\t\t\t\t\tWELCOME TO THE TASK MANAGER !!")
    
    main(int(input("Choose the serial number of the action you want to perform : \n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n")))