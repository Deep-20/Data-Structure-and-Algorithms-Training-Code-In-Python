class majorStack:
    def __init__(self):
        self.majorStack = []

class Stack:
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

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
