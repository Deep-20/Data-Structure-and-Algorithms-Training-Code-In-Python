
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of Circular Linked List
    def createCircularSLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = node

    # Insertion in Circular SLL
    def insertCSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            return "Head reference is None!!"
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                newNode.next = tempNode.next
                tempNode.next = newNode
                if tempNode == self.tail:
                    self.tail = newNode

    # Traversing Circular SLL
    def traverseCSLL(self):
        if self.head is None:
            print("CSLL is empty!!")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value)
                if tempNode.next == self.head:
                    break
                tempNode = tempNode.next
                
    
    # Searching a node in CSLL
    def searchCSLL(self, value):
        if self.head == None:
            return "CSLL is empty. Node not Found!!"
        else:
            tempNode = self.head
            index = 0
            while True:
                if tempNode.value == value:
                    return value, "found at index ", index
                elif tempNode == self.tail:
                    return "Value not found in CSLL!!"
                tempNode = tempNode.next
                index = index + 1
    
    # Deleting from a Circular SLL
    def deleteCSSL(self, location):
        if self.head == None:
            print("Nothing to delete. List is empty!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    tempNode.next = self.tail.next
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    if tempNode.next == self.head:
                        return "Location value greater than number of nodes!!"
                    index = index + 1
                
                if tempNode.next == self.tail:
                    tempNode.next = tempNode.next.next
                    self.tail = tempNode
                else:
                    tempNode.next = tempNode.next.next

    # Delete entire Circular SLL
    def deleteEntireCSSL(self):
        if self.head == None:
            print("List is already empty!!")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

circularSLL = CircularSLL()
circularSLL.createCircularSLL(0)

# print([node.value for node in circularSLL])

circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,0)
circularSLL.insertCSLL(4,-1)
print([node.value for node in circularSLL])

# circularSLL.traverseCSLL()
# print(circularSLL.searchCSLL(6))

# print(circularSLL.deleteCSSL(8))
# print([node.value for node in circularSLL])

circularSLL.deleteEntireCSSL()
print([node.value for node in circularSLL])