class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #push
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!!"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            return self.list[-1]

    #delete
    def delete(self):
        self.list = None


stack = Stack(4)

print(stack.isEmpty())
print(stack.isFull())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.push(5))

print(stack)

print(stack.pop())
print(stack.peek())

stack.delete()
print(stack)