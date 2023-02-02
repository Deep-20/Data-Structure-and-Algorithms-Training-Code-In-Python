class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " ".join(values)

    def enqueue(self, data):
        newNode = Node(data)

        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
    
    def dequeue(self):
        if self.LinkedList.head == None:
            print("Nothing to delete. Queue is empty!!")
        else:
            popped = self.LinkedList.head.data
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
        
            return popped
    
    def peek(self):
        if self.LinkedList.head == None:
            print("Nothing to delete. Queue is empty!!")
        else:
            return self.LinkedList.head.data
    
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

class TreeNode:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

# Pre Order Traversal Tree
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)


# In Order Traversal Tree
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)



# Post Order Traversal Tree
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)



# Level Order Traversal Tree
def levelOrderTraversal(rootNode):
    if not rootNode:
        return "Tree is empty!!"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

# Searching for a node in Binary Tree
def searchBT(rootNode, value):
    if not rootNode:
        return "Binary Tree does not exist!!"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == value:
                return "Node present in Binary Tree!!"
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

        return "Node not found!"

# Inserting node in Binary Tree
def insertBT(rootNode, nodeValue):
    if not rootNode:
        newBT = TreeNode(nodeValue)
        return newBT
    else:
        newNode = TreeNode(nodeValue)
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            else:
                root.leftChild = newNode
                return "Successfully Inserted"
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)
            else:
                root.rightChild = newNode
                return "Successfully Inserted"        


# Get deepest node
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)
        
        deepestNode = root
        return deepestNode

# Delete Deepest Node
def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root== deepestNode:                          # If rootNode of tree is deepest Node
                root = None
                return
            if root.rightChild:
                if root.rightChild == deepestNode:
                    root.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild == deepestNode:
                    root.leftChild == None
                    return
                else:
                    customQueue.enqueue(root.leftChild)
            
# Delete Node in Binary Tree
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "Binary tree deosn't exist!!"
    else:
        if searchBT(rootNode, node.data) == "Node present in Binary Tree!!":
            deepestNode = getDeepestNode(rootNode)
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.data == node.data:
                    root.data = deepestNode.data
                    deleteDeepestNode(rootNode, deepestNode)
                    return "Node deleted Successfully!"
                if root.leftChild is not None:
                    customQueue.enqueue(root.leftChild)
                if root.rightChild is not None:
                    customQueue.enqueue(root.rightChild)
        else:
            return "Node not present in Binaryy Tree!"


# Delete entire Bianry Tree
def deleteBT(rootNode):
    if not rootNode:
        return "Tree doesn't exist!!"
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

hotLeft = TreeNode("Coffee")
hotRight = TreeNode("Tea")

coldLeft = TreeNode("Fanta")
coldRight = TreeNode("Cola")

newBT.leftChild.leftChild = hotLeft
newBT.leftChild.rightChild = hotRight

newBT.rightChild.leftChild = coldLeft
newBT.rightChild.rightChild = coldRight

# preOrderTraversal(newBT)
# inOrderTraversal(newBT)
# postOrderTraversal(newBT)
# levelOrderTraversal(newBT)

# print(searchBT(newBT, "Beer"))
# print(insertBT(newBT, "Cappuccino"))
# levelOrderTraversal(newBT)

# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data)

# deleteDeepestNode(newBT, deepestNode)
# levelOrderTraversal(newBT)


# levelOrderTraversal(newBT)
# print("---------------------------")
# print(deleteNodeBT(newBT, hotLeft))
# levelOrderTraversal(newBT)

deleteBT(newBT)
levelOrderTraversal(newBT)

