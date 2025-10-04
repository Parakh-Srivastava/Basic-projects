directoryPlace = "C:/Users/parak/Documents/GitHub/Basic-projects/Projects/ToDoList/todolist.txt"

with open(directoryPlace, "r") as f:
    
    List = f.readlines()
    Tasks = []
    
    for i in range(len(List)):
        Tasks.append(List[i].strip())

def ListRead():
    
    for i in range(len(Tasks)):
        print(f"{i + 1}: {Tasks[i]}")

def ListAdd():

    inp = input("Enter the task :- ")    
    
    if len(Tasks) == 0:
        with open(directoryPlace, "a") as f:
            f.write(f"{inp}")
        Tasks.append(inp)
    else:
        with open(directoryPlace, "a") as f:
            f.write(f"\n{inp}")
        Tasks.append(inp)
    print("\n")
    if len(Tasks) != 0: 
        ListRead()

def DeleteList():
    
    Tasknum = int(input("Enter the task number you wanna delete : "))
    
    if Tasknum > len(Tasks):
        
        print(f"Invalid Output, there are only {len(Tasks)} tasks.")
    
    else:

        #popping the index selected
        Tasks.pop(Tasknum - 1)
        
        # We first clear the whole file
        with open(directoryPlace, "r+") as f:
            f.truncate(0)

        # Since all the data is already stored in Task array, we then add it one by one to the .txt file
        if len(Tasks) != 0:
            with open(directoryPlace, "a") as f:
                f.write(f"{Tasks[0]}")
                
            for i in range(1, len(Tasks)):
                with open(directoryPlace, "a") as f:
                    f.write(f"\n{Tasks[i]}")
        if len(Tasks) != 0: 
            ListRead()

def ListEdit():
    
    Tasknum = int(input("Enter the task number you want to edit : "))
    
    if Tasknum > len(Tasks):
        print(f"Invalid Output, there are only {len(Tasks)} tasks.")

    elif len(Tasks) == 0:
        print("No tasks to edit")

    else:    
        print(f"Original task : {Tasks[Tasknum - 1]}")
        Tasks[Tasknum - 1] = input("Write the edited version : ")
        
        with open(directoryPlace, "r+") as f:
            f.truncate(0)
        
        with open(directoryPlace, "a") as f:
            f.write(f"{Tasks[0]}")

        for i in range(1, len(Tasks)):
            with open(directoryPlace, "a") as f:
                f.write(f"\n{Tasks[i]}")
        print("\n")
        if len(Tasks) != 0: 
            ListRead()

def choosingList(inp):
    
    match inp:
        case 1:
            ListRead()
            choosingList(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n:-")))
        
        case 2:
            ListAdd()
            choosingList(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n:-")))
        
        case 3:
            
            if len(Tasks) == 0:
                print("There are no task present to delete.")
            
            else:
                DeleteList()
            choosingList(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n:-")))
        
        case 4:
            
            if len(Tasks) == 0:
                print("There are no task present to edit.")
            
            else:
                ListEdit()
            choosingList(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n:-")))
        
        case 5:
            print("Exiting !!")
            return
        
        case _:
            choosingList(int(input("Invalid output, try again : ")))

def main():

    try:
        choosingList(int(input("\n1) View Tasks \n2) Add new Task \n3) Delete a Task \n4) Edit a task \n5) Exit the program!!\n:-")))

    except Exception:
        print("Invalid Output!!")
        main()

if __name__ == "__main__":
    print("\n\t\t\tWELCOME TO THE TASK MANAGER !!")
    main()