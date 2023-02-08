
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def push(self, value):
        if self.minNode and self.minNode.value < value:
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
        else:
            self.minNode = Node(value = value, next = self.minNode)
        self.top = Node(value = value, next = self.top)

    
    def pop(self):
        if self.top == None:
            return "Satck is empty!"
        else:
            self.minNode = self.minNode.next
            popped = self.top.value
            self.top = self.top.next

            return popped

    
    def min(self):
        if self.minNode == None:
            return "Stack is empty"
        else:
            return self.minNode.value

    def printStack(self):
        if self.top == None:
            return "Stack is empty!!"
        else:
            tempNode = self.top
            while tempNode:
                print(tempNode.value, end = "  ")
                tempNode = tempNode.next



cStack = Stack()

cStack.push(5)
cStack.push(6)
cStack.push(3)
cStack.push(7)

cStack.printStack()
print()
print(cStack.min())
print()

cStack.pop()
cStack.printStack()
print()
print(cStack.min())
print()

# cStack.pop()
# cStack.printStack()
# print()
# print(cStack.min())
# print()

# cStack.pop()
# cStack.printStack()
# print()
# print(cStack.min())
# print()

# cStack.pop()
# cList.printStack()
# print()

# cStack.pop()
# print(cStack.printStack())

