

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinnkedList:
    def __init__(self):
        self.head=None
    def iab(self,data):
        newnode=Node(data)
        newnode.next=self.head
        if self.head:
            self.head.prev=newnode
        self.head=newnode
    def dab(self):
        if not self.head:
            print("Cant perform delete in an empty list....")
        print(f"Deleted:{self.head.next}")
        self.head=self.head.next
        if self.head:
            self.head.prev=None
            

    
    def backtraverse(self):
        print("values for traversig backward........")
        temp=self.head
        if not temp:
            print("Empty list")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end='<---->')
            temp=temp.prev
        print("None")
    def display(self):
        temp=self.head
        print("Doubly Linked List: ")
        while temp:
            print(temp.data, end="<->")
            temp=temp.next
        print("None") 
dll=DoublyLinnkedList()
n=int(input("Enter the no.of elements to insert at end: "))
for i in range(n):
    val=int(input(f"Enter element {i+1} : "))
    dll.iab(val)
dll.display()
d=int(input("\n How many times you want to perform del op: "))
for _ in  range(d):
    dll.dab()
dll.backtraverse()