class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    # is Empty
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # Insertion (Enqueue)
    def enqueue(self, value):
        self.items.append(value)
    
    # Deletion (dequeue)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            return self.items.pop(0)

    # Peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            return self.items[0]

    # Delete
    def delete(self):
        self.items = None

customQueue = Queue()

# print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)

print(customQueue)

# print(customQueue.dequeue())

# print(customQueue)

# print(customQueue.peek())

customQueue.delete()
print(customQueue)