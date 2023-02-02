class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)
    
    #Enqueue
    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    #isEmpty
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            popped = self.linkedList.head.value
            if self.linkedList.head.next == None:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return popped

    #peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty!!"
        else:
            return self.linkedList.head

    #delete
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Insert Node in BST (Self Made Funstion)
def insertBST(rootNode, data):
    if rootNode.data == None:
        rootNode.data = data
        print("INserted Node")
        return
    else:
        newNode = BSTNode(data)
        tempNode = rootNode
        while True:
            if newNode.data <= tempNode.data and tempNode.leftChild == None:
                tempNode.leftChild = newNode
                print("INserted Node")
                return
            elif newNode.data > tempNode.data and tempNode.rightChild == None:
                tempNode.rightChild = newNode
                print("INserted Node")
                return
            if newNode.data <= tempNode.data:
                tempNode = tempNode.leftChild
            else:
                tempNode = tempNode.rightChild

# Inser Node in BST (Course Function)
def insertNode(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
        return
    elif value <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(value)
            return
        else:
            insertNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(value)
            return
        else:
            insertNode(rootNode.rightChild, value)

# Pre Orer Traversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

# Inorder Traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

# Post Order Traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

# Level Order Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.data)
            if root.leftChild != None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild != None:
                customQueue.enqueue(root.rightChild)

# Search in BST
def searchBST(rootNode, value):
    if rootNode.data == value:
        print("Value Found!!")
        return
    elif value <= rootNode.data:
        if value == rootNode.leftChild.data:
            print("Value found!")
            return
        else:
            searchBST(rootNode.leftChild, value)
    else:
        if value == rootNode.rightChild.data:
            print("Value found")
            return
        else:
            searchBST(rootNode.rightChild, value)

# Helper function to delete node
def minValueNode(bstNode):
    currNode = bstNode
    while currNode.leftChild is not None:
        currNode = currNode.leftChild
    return currNode

# Delete Node function
def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    else:
        if value < rootNode.data:
            rootNode.leftChild = deleteNode(rootNode.leftChild, value)
        elif value > rootNode.data:
            rootNode.rightChild = deleteNode(rootNode.rightChild, value)
        else:
            if rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            
            if rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp

            temp = minValueNode(rootNode.rightChild)
            rootNode.data = temp.data
            rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
        
        return rootNode


# Delete Entire BST
def deleteEntireBST(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None


newBST = BSTNode(None)
# insertBST(newBST, 70)
# insertBST(newBST, 50)
# print(newBST.data)
# print(newBST.leftChild.data)

# insertNode(newBST, 70)
# insertNode(newBST, 60)
# print(newBST.data)
# print(newBST.leftChild.data)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)

# searchBST(newBST, 60)

# deleteNode(newBST, 70)
# levelOrderTraversal(newBST)

deleteEntireBST(newBST)
levelOrderTraversal(newBST)