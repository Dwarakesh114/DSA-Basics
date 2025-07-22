
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iap(self, data, pos):
        newnode = Node(data)
        if pos <= 0:
            print("Position must be >= 1")
            return
        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            print(f"{data} inserted at position 1")
            return
        current = self.head
        count = 1
        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range.")
            return
        newnode.next = current.next
        current.next = newnode
        print(f"{data} inserted at position {pos}")

    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current = current.next
        print()

ll = LinkedList()
while True:
    print("\nLinkedList - Insert at Position")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = int(input("Enter a value to insert: "))
        pos = int(input("Enter position to insert: "))
        ll.iap(data, pos)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        print("Exit the operation")
        break
    else:
        print("Enter only 1 / 2 / 3")
