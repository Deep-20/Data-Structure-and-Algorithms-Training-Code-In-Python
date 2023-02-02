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

    # Addition of node to linked list
    def add(self, value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        
        return self.tail

    # Checking for intersection
    def intersection(self, ll):
        referenceList = []
        node = self.head

        while node!= self.tail:
            referenceList.append(node.next)
            node = node.next

        node = ll.head
        while node != ll.tail:
            if node.next in referenceList:
                return "Lists are intersecting!!"
            node = node.next

        return "Lists are not intersecting"

    # Helper function to add same element to lists
    def helper(self, list2, value):
        tempNode = Node(value)
        self.tail.next = tempNode
        self.tail = tempNode
        self.tail.next = None

        list2.tail.next = tempNode
        list2.tail = tempNode
        list2.tail.next = None

        return list2


list1 = SLL()
list1.createSLL(0)

list2 = SLL()
list2.createSLL(1)

list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
list1.add(6)

list2.add(4)
list2.add(3)
list2.add(6)
list2.add(7)

list2 = list1.helper(list2, 11)
list2 = list1.helper(list2, 14)

print(list1)
print(list2)

print(list1.intersection(list2))