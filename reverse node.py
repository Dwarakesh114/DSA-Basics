''' consider a single linked list with insert at end nodes after insertion reverse the node to print
input 11-22-33-44-55-null
output 55-44-33-22-11-null'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        print(f"{data} inserted at end.")

    def display_reverse(self):
        def reverse_traverse(node):
            if node:
                reverse_traverse(node.next)
                print(node.data, end='---')
        if not self.head:
            print("LL-Empty")
            return
        reverse_traverse(self.head)
        print("null")

ll = LinkedList()
while True:
    print("\n LinkedList - Insert at end & Reverse Display")
    print("1.Insert")
    print("2.Display in Reverse")
    print("3.Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        data = int(input("Enter a value to insert:"))
        ll.iae(data)
    elif choice == '2':
        ll.display_reverse()
    elif choice == '3':
        print("Exit")
        break
    else:
        print("Enter only 1/2/3")
