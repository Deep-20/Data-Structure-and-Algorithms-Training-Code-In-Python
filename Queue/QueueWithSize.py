class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    #isFull
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    #isEmpty
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    #Enqueue
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top == self.maxSize - 1:
                self.top = 0
            else:
                self.top = self.top + 1
                if self.start == -1:
                    self.start = 0

            self.items[self.top] = value

    #dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            popped = self.items[self.start]
            self.items[self.start] = None
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start == self.maxSize - 1:
                self.start = 0
            else:
                self.start = self.start + 1
            return popped

    #peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            return self.items[self.start]

    # Delete
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(3)

# print(customQueue.isFull())

# print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
# print(customQueue.enqueue(4))

print(customQueue)

# print(customQueue.dequeue())

# print(customQueue.peek())
# print(customQueue)

customQueue.delete()
print(customQueue)