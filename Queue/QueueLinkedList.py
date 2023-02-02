class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)
    
    #Enqueue
    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    #isEmpty
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            popped = self.linkedList.head.value
            if self.linkedList.head.next == None:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return popped

    #peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            return self.linkedList.head

    #delete
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

customQueue = Queue()

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)

print(customQueue)
print("------------------")
print(customQueue.dequeue())
print(customQueue)

print("------------------")

print(customQueue.peek())

customQueue.delete()
print(customQueue)