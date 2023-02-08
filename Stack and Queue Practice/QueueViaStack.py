class Stack:
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        values = reversed(self.stack)
        values = [str(x) for x in values]
        return str(values)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!!"
        else:
            popped = self.stack[-1]
            self.stack.pop()

            return popped

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, value):
        self.stack1.push(value)
    
    def dequeue(self):
        if not self.stack1.stack:
            return "Stack is emptyy!!"
        for i in range(len(self.stack1.stack)):
            self.stack2.push(self.stack1.pop())

        popped = self.stack2.stack.pop()
        
        for i in range(len(self.stack2.stack)):
            self.stack1.push(self.stack2.pop())
        
        return popped


    def printQueue(self):
        for value in self.stack1.stack:
            print(value, end = " ")

customQueue = Queue()

customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)

customQueue.printQueue()
print()

print(customQueue.dequeue())
print(customQueue.dequeue())


    
