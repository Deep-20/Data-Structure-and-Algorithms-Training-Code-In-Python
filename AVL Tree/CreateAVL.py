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


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

# Search in AVL
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

# Helper function 1
def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

# Helper Function 2
def getBalance(rootNode):
    if not rootNode:
        return 0
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# Rotate Right Function
def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode

    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChilf))
    newRoot.height = 1 + max(getHeight(newRoot.rightChild), getHeight(newRoot.leftChild))

    return newRoot 

# Rotate Left Function
def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode

    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))

    return newRoot

# Insert Node function
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    else:
        if nodeValue < rootNode.data:
            rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
        else:
            rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
        
        rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
        balance = getBalance(rootNode)
        if balance > 1 and nodeValue < rootNode.leftChild.data:
            return rightRotate(rootNode)
        if balance > 1 and nodeValue > rootNode.leftChild.data:
            rootNode.leftChild = leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance < -1 and nodeValue > rootNode.rightChild.data:
            return leftRotate(rootNode)
        if balance < -1 and nodeValue < rootNode.rightChild.data:
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)

        return rootNode


# Helper Function 1 for deleting node
def getMinValueNode(rootNode):
    if not rootNode or rootNode.leftChild == None:
        return rootNode
    else:
        return getMinValueNode(rootNode.leftChild)

# Delete Node
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    else:
        if nodeValue < rootNode.data:
            rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
        else:
            if rootNode.leftChild == None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            elif rootNode.rightChild == None:
                temp = rootNode.leftChild
                rootNode = None
                return temp
            tempNode = getMinValueNode(rootNode.rightChild)
            rootNode.data = tempNode.data
            rootNode.rightChild = deleteNode(rootNode.rightChild, tempNode.data)
        rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
        balance = getBalance(rootNode)
        if balance > 1 and getBalance(rootNode.leftChild) >= 0:
            return rightRotate(rootNode)
        if balance < -1 and getBalance(rootNode.rightChild) <= 0:
            return leftRotate(rootNode)
        if balance > 1 and getBalance(rootNode.leftChild) < 0:
            rootNode.leftChild = leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance < -1 and getBalance(rootNode.rightChild) > 0:
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)

        return rootNode


# Delete entire AVL Tree
def deleteAVLTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None



newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)

newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)