class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break
    
    # Create Circular DLL
    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node

    # Insertion in CDLL
    def insertCDLL(self, value, location):
        if self.head == None:
            print("Circular DLL is empty!!")
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.tail.next = node
                self.head = node
            elif location == -1:
                node.next = self.tail.next
                node.prev = self.tail
                self.tail.next = node
                self.head.prev = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                
                if tempNode == self.tail:
                    node.next = self.tail.next
                    node.prev = self.tail
                    self.tail.next = node
                    self.head.prev = node
                    self.tail = node
                else:
                    node.next = tempNode.next
                    node.prev = tempNode
                    tempNode.next.prev = node
                    tempNode.next = node

    # Traversal in CDLL
    def traverseCDLL(self):
        if self.head == None:
            print("No nodes exist in linked list!!")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value)
                if tempNode == self.tail:
                    return
                tempNode = tempNode.next

    # Reverse Traverse in CLL
    def reverseTraverseCLL(self):
        if self.head == None:
            print("No node exists in linked list!!")
        else:
            tempNode = self.tail
            while True:
                print(tempNode.value)
                if tempNode == self.head:
                    return
                tempNode = tempNode.prev

    # Search in CDLL
    def searchCDLL(self, value):
        if self.head == None:
            print("Linked list is empty!!")
        else:
            tempNode = self.head
            index = 0
            while True:
                if tempNode.value == value:
                    return str(value) + ' found at index ' + str(index)
                elif tempNode == self.tail:
                    return "Value not found!!"
                
                tempNode = tempNode.next
                index = index + 1

    # Delete from CDLL
    def deleteCDLL(self, location):
        if self.head == None:
            print("Nothing to delete. Linked list is empty!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = self.tail
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = self.head
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                
                if tempNode.next == self.tail:
                    self.tail.prev.next = self.head
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                else:
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode

    # Delete entire CDLL
    def deleteEntireCDLL(self):
        if self.head == None:
            print("Linked list is already empty!!")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


circularDLL = CircularDLL()

circularDLL.createDLL(2)

print([node.value for node in circularDLL])

circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(3,2)
circularDLL.insertCDLL(4,-1)

print([node.value for node in circularDLL])

# circularDLL.traverseCDLL()

# circularDLL.reverseTraverseCLL()

# print(circularDLL.searchCDLL(2))

# circularDLL.deleteCDLL(4)
# print([node.value for node in circularDLL])

circularDLL.deleteEntireCDLL()
print([node.value for node in circularDLL])