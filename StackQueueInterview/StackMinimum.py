class Stack:
    def __init__(self):
        self.stack = []
        self.stackMin = []
    
    def __str__(self):
        values = reversed(self.stack)
        values = [str(x) for x in values]
        return "\n".join(values)
    
    def push(self, value):
        self.stack.append(value)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            popped = self.stack.pop()
            return popped

    def min(self):
        if self.isEmpty():
            return "Stack is empty!!"
        else:
            