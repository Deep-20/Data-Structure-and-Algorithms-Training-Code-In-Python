# from LinkedList import LinkedList

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

    def __len__(self):
        tempNode = self.head
        length = 0
        while tempNode:
            tempNode = tempNode.next
            length = length + 1
        return length
    
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
                newNode.next = None
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
    
    # Return nth till Last node
    def subLinkedList(self, ll, n):
        if self.head == None:
            print("Linked list is empty!!")
        else:
            tempNode = self.head
            index = 0
            while index < n - 1:
                tempNode = tempNode.next
                index = index + 1
            
            if tempNode == self.tail:
                return "Value of N greater than number of nodes in linked list"
            else:
                if n == 0:
                    return self
                else:
                    ll.createSLL(tempNode.next.value)
                    tempNode = tempNode.next.next
                    while tempNode:
                        ll.insertSLL(tempNode.value, -1)
                        tempNode = tempNode.next
                    return ll
    
    # Return nth to last node
    def nthToLast(self, n):
        if self.head == None:
            print("No element in list")
        else:
            if len(self) - n < 0:
                print("Value of n is greater than size of list")
            else:
                tempNode = self.head
                index = 0
                while index < len(self) - n - 1:
                    tempNode = tempNode.next
                    index = index + 1
                return tempNode.next.value

    def nthToLastBetter(self, n):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(n):
            if pointer2 is None:
                break
            else:
                pointer2 = pointer2.next
        
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        return pointer1.value


        
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

# newLL = SLL()
# print(sll.subLinkedList(newLL,0))

# print(sll.nthToLast(4))
print(sll.nthToLastBetter(8))