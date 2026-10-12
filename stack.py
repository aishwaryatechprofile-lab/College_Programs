```python
# Stack implementation using List

stack = [0] * 5
top = -1
size = int(input("Enter max size of stack: "))

while True:
    print("\n--Stack Menu--")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if top == size - 1:
            print("Stack overflow")
        else:
            element = int(input("Enter element: "))
            top = top + 1
            stack[top] = element
            print("Element pushed:", element)

    elif choice == 2:
        if top == -1:
            print("Stack underflow")
        else:
            print("Popped element:", stack[top])
            top = top - 1

    elif choice == 3:
        if top == -1:
            print("Stack is Empty")
        else:
            print("Top element:", stack[top])

    elif choice == 4:
        if top == -1:
            print("Stack is Empty")
        else:
            print("Stack elements:")
            for i in range(top, -1, -1):
                print(stack[i])

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
