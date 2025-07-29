class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def iab(self, data):
        newnode = Node(data)
        newnode.next=self.head

        if self.head:
            self.head.prev=newnode
        self.head=newnode
       

    def backtraverse(self):
        print("Values for traversing backward...")
        temp=self.head
        if not temp:
            print("Empty list")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end='<--->')
            temp = temp.prev
        print("None")


        
    def display(self):
        temp = self.head
        print("Double  Linked List:")
        while temp:
            print(temp.data, end="<--->")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()

n = int(input("Enter the number of elements to insert at end : "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    dll.iab(value)

dll.display()
dll.backtraverse()