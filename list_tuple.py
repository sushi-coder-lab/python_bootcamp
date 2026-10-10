
print("================= TODO APP =================")

def options():
    print("Choose an option")
    print("1. Add an item")
    print("2. Delete an item at index")
    print("3. Remove the last item")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

arr = []

def addTask(task):
    arr.append(task)


while True:
    options()
    select = input("Select an option: ")

    if select == "1":
        task = input("Enter your task: ")
        addTask(task)

    elif select == "2":
        if arr:
            index = int(input("Which task do you want to remove? "))
            if 1 <= index <= len(arr):
                arr.pop(index - 1)
                print("Task deleted successfully")
                print(arr)
                break
            else:
                print("Invalid index")
                break
        else:
            print("Task list is empty")
            break

    elif select == "3":
        if arr:
            arr.pop()
            print("Last task removed")
            print(arr)
            break
        else:
            print("Task list is empty")
            break

    elif select == "4":
        arr.sort()
        print(arr)
        break

    elif select == "5":
        print(arr)
        break

    elif select == "6":
        print("Exiting app...")
        break

    else:
        print("Invalid option")
