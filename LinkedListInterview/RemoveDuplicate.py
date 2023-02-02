class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self):
        values = ([str(node.value) for node in self])
        return " --> ".join(values)
    
    def createSLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = None
    
    def insertSLL(self, value, location):
        if self.head == None:
            print("Linked list does't exist")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = None
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


    # def searching and deleting duplicates
    def searchAndDeleteDuplicates(self):
        duplicateSet = set()
        tempNode = self.head
        # index = 0

        duplicateSet.add(tempNode.value)

        while tempNode:
            if tempNode.next == self.tail:
                if tempNode.next.value in duplicateSet:
                    tempNode.next = None
                    self.tail = tempNode
                break
            else:
                if tempNode.next.value in duplicateSet:
                    tempNode.next = tempNode.next.next
                else:
                    duplicateSet.add(tempNode.value)
                    tempNode = tempNode.next            
                
            
sll = SLL()

sll.createSLL(0)

sll.insertSLL(1,1)
sll.insertSLL(1,1)
sll.insertSLL(2,2)
sll.insertSLL(4,3)
sll.insertSLL(4,1)
sll.insertSLL(6,2)
sll.insertSLL(7,5)

print(sll)

sll.searchAndDeleteDuplicates()

print(sll)
                

    
