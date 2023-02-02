class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #push
    def push(self, value):
        self.list.append(value)
        return "Element has been successfully inserted!!"

    #pop
    def pop(self):
        if self.list == []:
            return "No element to Pop out!!"
        else:
            return self.list.pop() 
    
    #peek
    def peek(self):
        if self.list == []:
            return "Stack is empty!!"
        else:
            return self.list[-1]

    #delete
    def delete(self):
        self.list = None

stack = Stack()
# print(stack.isEmpty())

stack.push(0)
stack.push(1)
stack.push(2)

print(stack)

# print("------------")

# print(stack.pop())

# print("------------")
# print(stack)


# print("-----------")
# print(stack.peek())

stack.delete()

print("-----------")
print(stack)