print('1.Add Task')
print('2.Remove Task')
print('3.Mark Task As Completed')
print('4.View Completed Tasks')
print("5.Exit")
choice = int(input("Choose One of the following(1-5): "))

tasks = []
completed_tasks = []
while choice!=5:
    if choice == 1:
        add_task = input("Enter task to Add: ")
        tasks.append(add_task)
        print("Task Added Successfully!!")
        print("-------------------------------------------------")
    elif choice == 2:
        counter = 0
        for task in tasks:
            print(counter,task)
            counter+=1
        index = int(input("Enter Number Of Task To remove: "))
        tasks.pop(index)
        print("Task Removed Successfully.")        
        print("-------------------------------------------------")
    elif choice == 3:
        counter = 0
        for task in tasks:
            print(counter,task)
            counter+=1
        completed = int(input("Enter Number Of Task Which is Complete: "))
        tasks.pop(completed)
        value = tasks[completed]
        completed_tasks.append(value)
        print("Task Successfully Marked As Complete.")
        print("-------------------------------------------------")
    elif choice == 4:
        print(completed_tasks)
        print("-------------------------------------------------")
  
    print("What Do You want to do next: ")
    print('1.Add Task')
    print('2.Remove Task')
    print('3.Mark Task As Completed')
    print('4.View Completed Tasks')
    print("5.Exit")
    choice = int(input("Choose One of the following(1-5): "))
    