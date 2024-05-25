class Node:
    def __init__(self,data) -> None:
        self.pre = None
        self.data = data
        self.next = None


class doubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    #function to insert the data in DLL
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node 
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        new_node.pre = tail

    #function to insert the node in begining
    def insertAtHead(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.pre = new_node
        self.head = new_node


    #function to print DLL
    def printDLL(self):
        if not self.head:
            return 
        curr = self.head
        while curr:
            print(curr.data,end=" ")
            curr = curr.next
        print()

    def Reverse(self):
        if not self.head or not self.head.next:
            return self.head
        curr = self.head
        pre = None
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        self.head = pre
        return self.head


dll = doubleLinkedList()
n = int(input("Enter the number of elements to append: "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    dll.append(data)


dll.printDLL()

dll.insertAtHead(10)
dll.Reverse()

dll.printDLL()