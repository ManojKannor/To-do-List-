from createTable import create_Table
from add import add
from ViewTask import view_task
from setCompleted import setComplete
from deleteTask import delete_Task
tableNames = []

def OperationPanel(tableName):
    exit = True
    while exit:
        print("1. Add task")
        print("2. Delete task")
        print("3. set Task Completed")
        print("4. View All Task")
        print("5. Exit")
        choice = int(input("Select : "))
        match choice:
            case 1: 
                add(tableName)
            case 2:
                view_task(tableName)
                delete_Task(tableName)
            case 3:
                view_task(tableName)
                setComplete(tableName)
            case 4:
                view_task(tableName)
            case 5: 
                exit = False
                


def userChecker():
    userInput = input("Enter the Your table name : ")
    with open("tableNames.txt","r") as files:
        lines = files.readlines()
        for line in lines:
            part = line.strip().split(",")
        for p in part:
            tableNames.append(p)
        
       # print(data)
    for table in tableNames:
        if userInput.lower() == table.lower():
            flag = table
            break
        else:
            flag = -1
    
    if flag == -1:
        print("Your table not found !")
    else:
        OperationPanel(flag)


def panel():
    exit = True
    while exit:
        print("1. create Todo List")
        print("2. Operations")
        print("5. Exit")
        choice = int(input("select : "))

        match choice:
            case 1:
                tableName = input("Enter the table Name : ")
                with open("tableNames.txt","a") as files:
                    files.write(f"{tableName},")
                create_Table(tableName)
            
            case 2:
                userChecker()
            case 5:
                exit = False


panel()