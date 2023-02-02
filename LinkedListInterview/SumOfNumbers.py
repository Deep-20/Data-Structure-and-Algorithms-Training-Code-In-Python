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

    # Sum of Numbers using Linked List
    def sumOfNumbers(self, second):
        sumList = SLL()
        sum = 0
        carry = 0
        pointer1 = self.head
        pointer2 = second.head

        while pointer2 or pointer1:
            sum = carry
            if pointer1:
                sum = sum + pointer1.value
                pointer1 = pointer1.next
            if pointer2:
                sum = sum + pointer2.value
                pointer2 = pointer2.next

            sumList.add(int(sum % 10))

            carry = int(sum / 10)

        if carry == 1:
            sumList.insertSLL(carry, -1)

        return sumList


firstNumber = SLL()

firstNumber.createSLL(2)
firstNumber.insertSLL(3,-1)
print(firstNumber)


secondNumber = SLL()

secondNumber.createSLL(3)
secondNumber.insertSLL(8,-1)
print(secondNumber)

print(firstNumber.sumOfNumbers(secondNumber))

