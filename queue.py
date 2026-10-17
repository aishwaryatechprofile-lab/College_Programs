MAX=2
queue=[0]*MAX
front=-1
rear=-1
while True:
    print("1.Insertion")
    print("2.Deletion")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter choice : "))
    if choice==1:
        if rear>=MAX-1:
            print("Underflow")
        else:
            num=int(input("Enter element : "))
            if front==-1 and rear==-1:
                front=0
                rear=0
            else:
                rear=rear+1
            queue[rear]=num
            print("Element inserted:",num)
    elif choice==2:
        if front==-1 and front>rear:
            print("underflow")
        else:
            print("Deleted element: ",queue[front])
            front=front+1
    elif choice==3:
        if front==-1 and front>rear:
            print("queue empty")

        else:
            print("queue elements:",queue[front:rear+1])
    elif choice==4:
        print("Program terminated")
        break
    else:
        print("Invalid choice")