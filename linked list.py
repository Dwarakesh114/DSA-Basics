"""
 linked lists : nonp contagious ds
memory allocate 
access

1.single linked list
2.double linked list
3.circular  singel/double linked list

single linked list 

head---> node1---> node2---> tail/null

class node:
        def__init__(self,data):
                self.data=data
                self.next=None
                
                
Insertion
1.At begin
2.At end
3.At location"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iab(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        print(f"{data} inserted from begin.")

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
    print("\n LinkedList - Insert AT begin....")
    print("1.Insert")
    print("2.Display")
    print("3.Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        data = int(input("enter a value to insert :"))
        ll.iab(data)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        print("Exit the operation")
        break
    else:
        print("enter only ....1/2/3")
