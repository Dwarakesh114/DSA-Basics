class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):  
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            print(f"{data} inserted at end /will be first node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        print(f"{data} inserted last")

    def delete_begin(self):
        if self.head is None:
            print("Empty-LL")
        else:
            print("Deleted node from beginning:", self.head.data)
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Empty-LL")
        elif self.head.next is None:
            print("Deleted last node:", self.head.data)
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            print("Deleted node at end:", current.next.data)
            current.next = None

    def deletevalue(self, key):
        if self.head is None:
            print("Empty-LL")
            return
        if self.head.data == key:
            print(f"Deleted node with value {key} from beginning")
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if current.next is None:
            print(f"Value {key} not found")
        else:
            print(f"Deleted node with value {key}")
            current.next = current.next.next

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
   
    print("1. Insert")
    print("2. Display")
    print("3. Delete by value")
    print("4. Delete at end")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        key = int(input("Enter the value you want to delete: "))
        ll.deletevalue(key)
        ll.display()
    elif choice == "4":
        ll.delete_end()
        ll.display()
    elif choice == '5':
        print("Exit")
        
    
