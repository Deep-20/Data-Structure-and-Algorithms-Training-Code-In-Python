class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    # Insertion in Doubly Linked List
    def insertDLL(self, value, location):
        node = Node(value)
        if self.head == None:
            print("Head reference is None!!")
        else:
            if location == 0:
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == -1:
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                
                if tempNode == self.tail:
                    node.next = None
                    node.prev = self.tail
                    self.tail.next = node
                    self.tail = node
                else:
                    node.prev = tempNode
                    node.next = tempNode.next
                    tempNode.next.prev = node
                    tempNode.next = node

    # Traverse Doubly LL
    def traverseDLL(self):
        if self.head == None:
            print("No node exists in Linked List!!")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal in DLL
    def reverseTraverseDLL(self):
        if self.head == None:
            print("No nodes exist in Linked List!!")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Searching in DLL
    def searchDLL(self, value):
        if self.head == None:
            print("Linked List os empty. Node not found!!")
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == value:
                    return str(value) +  " found at index " + str(index)
                    
                index = index + 1
                tempNode = tempNode.next
            return "Node not found!!"

    # Delete from DLL
    def deleteDLL(self, location):
        if self.head == None:
            print("Linked list is empty. Nothing to delete!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                
                if tempNode.next == self.tail:
                    self.tail = tempNode
                    tempNode.next = None
                else:
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode

    # Delete entire DLL
    def deleteEntireDLL(self):
        if self.head == None:
            print("Linked list is already empty!!")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None  
                tempNode = tempNode.next
            self.head = None
            self.tail = None
                

doublyLL = doublyLinkedList()

doublyLL.createDLL(2)

doublyLL.insertDLL(0,0)
doublyLL.insertDLL(1,1)
doublyLL.insertDLL(3,2)
doublyLL.insertDLL(4,-1)

print([node.value for node in doublyLL])

# doublyLL.traverseDLL()
# doublyLL.reverseTraverseDLL()

# print(doublyLL.searchDLL(5))

# doublyLL.deleteDLL(0)
# print([node.value for node in doublyLL])

doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])

