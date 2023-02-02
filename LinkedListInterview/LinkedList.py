from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
    
    # __str__() for printing node
    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break
        
    def __str__(self):
        values = [str(node.value) for node in self]
        return " --> ".join(values)

    # Length of linked list
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result = result + 1
            node = node.next
        
        return result

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

    # Generate Linked List
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        
        return self


customLL = LinkedList()
customLL.generate(10, 0, 99)

print(customLL)
print(len(customLL))