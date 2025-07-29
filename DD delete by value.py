class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp

    def delete_by_value(self, val):
        temp = self.head
        if temp is None:
            return
        if temp.data == val:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        while temp and temp.data != val:
            temp = temp.next
        if temp is None:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def display(self):
        temp = self.head
        print("Doubly linked List:")
        while temp:
            print(temp.data, end="<--->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
n = int(input("Enter the number of element to insert at end:"))
for i in range(n):
    val = int(input(f"Enter Element {i+1}:"))
    dll.iae(val)

dll.display()

del_val = int(input("Enter the value to delete:"))
dll.delete_by_value(del_val)
dll.display()
