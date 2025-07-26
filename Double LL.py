'''Double LL
operations
1. Insertion - at behing,end,position
2. Deletion - by value 
3. Traversal - forword/ backword

head<-->node1<-->node2<-->node3<-->null

node:
class node :
        def __init__ (self,data):
                self.data=data
                self.next=None
                self.prev=None'''



'''At th end insertion on DLL'''

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode =node(data)
        if self.head is None:
            self.head=newnode
            return
        temp= self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        
        
    def display(self):
            temp=self.head
            print("Doubly linked List:")
            while temp:
                print(temp.data, end="<--->")
                temp=temp.next
            print("None")   

dll=DoublyLinkedList()
n=int(input("Enter the number of element to insert at end:"))
for i in range(n):
    val=int(input(f"Enter Element {i+1}:"))
    dll.iae(val)
dll.display()