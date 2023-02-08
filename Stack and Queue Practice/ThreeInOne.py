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
        
list1 = []

stack1 = Stack()
stack1.push(1)
stack1.push(1)

stack2 = Stack()
stack2.push(3)
stack2.push(2)


stack3 = Stack()
stack3.push(4)
stack3.push(5)
stack3.push(6)


list1.append(stack1)
list1.append(stack2)
list1.append(stack3)

for i in list1:
    print(i)

print("-------------------------")

print(stack3.pop())
for i in list1:
    print(i)



