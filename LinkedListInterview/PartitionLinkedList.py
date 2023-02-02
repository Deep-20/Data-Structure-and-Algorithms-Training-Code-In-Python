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

    # Delete a node 
    def deleteNode(self, location):
        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


    # Partition linked link on X
    def partitionSLL(self, x):
        pointer1 = self.head
        partition = SLL()

        while pointer1:
            if pointer1.value >= x:
                if partition.head == None:
                    partition.createSLL(pointer1.value)
                else:
                    partition.insertSLL(pointer1.value, -1)
            else:
                if partition.head == None:
                    partition.createSLL(pointer1.value)
                else:
                    partition.insertSLL(pointer1.value, 0)
            pointer1 = pointer1.next 
        
        return partition


sll = SLL()

sll.createSLL(0)

sll.insertSLL(1,1)
sll.insertSLL(1,1)
sll.insertSLL(2,2)
sll.insertSLL(4,3)
sll.insertSLL(4,1)
sll.insertSLL(6,2)
sll.insertSLL(7,-1)

print(sll)

# sll.deleteNode(-1)
# print(sll)


print(sll.partitionSLL(2))