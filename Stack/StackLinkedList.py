class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.value))
            node = node.next
        return "\n".join(values)

    #isEmpty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    #push
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    #pop
    def pop(self):
        if self.head == None:
            return "Stack is Empty!!"
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped

    #peek
    def peek(self):
        if self.head == None:
            return "Stack is empty!!"
        else:
            return self.head.value

    #delete
    def delete(self):
        self.head = None

stack = Stack()

# print(stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# print(stack.isEmpty())
# print(stack.pop())
# print("----")
# print(stack)

# print(stack.peek())
# print("----")
# print(stack)

stack.delete()
print(stack)