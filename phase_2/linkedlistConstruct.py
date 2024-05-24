# Write a program to construct a linked-list for given list of 'n' values. And then print the linked-list (in space seperated manner)

class node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self.head = None

    #function adding new nodes  
    def append(self,data):
        new_node = node(data)
        if self.head == None:   
            self.head = new_node
            return self.head
        tail = self.head 
        while tail.next != None:
            tail = tail.next
        tail.next = new_node

    #function to insert the node at beginning
    def insertNodeathead(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    #function to delete the node at beginning
    def deleteNodeAtHead(self):
        if self.head == None:
            return None
        secondNode = self.head.next
        self.head.next = None
        return secondNode

    #function to insert the node at ending
    def insertNodeAtTail(self,data):
        new_node = node(data)
        if self.head == None:
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return self.head
    
    #function to delete the node at ending
    def deleteNodeAtTail(self):
        curr = self.head
        if curr == None or curr.next == None:
            return None
        while curr.next.next:
            curr = curr.next
        curr.next = None
        return self.head


    #function to print the linkedlist
    def printLL(self):
        curr = self.head
        while curr != None:
            print(curr.data, end = " ")
            curr = curr.next

    def lenOFList(self):
            if not self.head:
                return 0
            curr = self.head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count


n = int(input())
elements = list(map(int, input().split()[:n]))
link_list = linkedList()
for i in elements:
    link_list.append(i)
a = link_list.lenOFList()
print(a)