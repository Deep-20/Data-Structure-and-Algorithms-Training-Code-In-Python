# Set of Plates with Linked List

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.count += 1

    def pop(self):
        if self.count == 0:
            return -1
        else:
            popped = self.top.value
            self.top = self.top.next
            self.count -= 1

            return popped
    
    def printStack(self):
        tempNode = self.top
        while tempNode:
            print(tempNode.value, end = "  ")
            tempNode = tempNode.next

class SetOfStack:

    def __init__(self, threshold = None):
        self.setOfStack = []
        self.threshold = threshold

    def push(self, value):
        if not self.setOfStack or self.setOfStack[-1].count == self.threshold:
            self.setOfStack.append(Stack())
            self.setOfStack[-1].push(value)
        else:
            self.setOfStack[-1].push(value)
    
    def pop(self):
        if not self.setOfStack:
            return "No stacks found!!"
        else:
            value = self.setOfStack[-1].pop()
            while value == -1:
                self.setOfStack.pop()
                value = self.setOfStack[-1].pop()
            
            if self.setOfStack[-1].count == 0:
                self.setOfStack.pop()

            return value

    def popAt(self, index):
        if self.setOfStack[index] == None:
            return "Stack not found!!"
        else:
            if self.setOfStack[index].count == 0:
                return "Stack is empty!!"
            else:
                value = self.setOfStack[index].pop()
                if self.setOfStack[index].count == 0:
                    self.setOfStack.pop(index)

                return value

    def printSetOfStack(self):
        if not self.setOfStack:
            print("No stacks found!!")
        else:
            for stack in self.setOfStack:
                stack.printStack()
                print()
        return


customSetOfStacks = SetOfStack(3)

customSetOfStacks.push(3)
customSetOfStacks.push(5)
customSetOfStacks.push(7)

customSetOfStacks.push(9)
customSetOfStacks.push(11)

customSetOfStacks.printSetOfStack()

# customSetOfStacks.pop()
# customSetOfStacks.pop()

# customSetOfStacks.pop()
# customSetOfStacks.pop()

# customSetOfStacks.printSetOfStack()

# print(customSetOfStacks.pop())

# customSetOfStacks.printSetOfStack()

# customSetOfStacks.popAt(0)

# customSetOfStacks.popAt(1)
# customSetOfStacks.popAt(1)

# customSetOfStacks.popAt(0)

# customSetOfStacks.printSetOfStack()