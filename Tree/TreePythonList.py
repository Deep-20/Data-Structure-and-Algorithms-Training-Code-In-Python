class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # Inserting node in Binary tree
    def insertBT(self, value):
        if self.lastUsedIndex == self.maxSize - 1:
            return "List is full!!"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1

    # Searching 
    def searchBT(self, value):
        index = 1
        while index < self.maxSize:
            if self.customList[index] == value:
                return "Value found in Binary Tree!!"
            index = index + 1
        return "Value not found!!"

    # Pre Order Traversal
    def preOrderTraversal(self, index):
        if self.lastUsedIndex == 0:
            return "Binary Tree is empty!!"
        elif index > self.lastUsedIndex:
            return
        else:
            print(self.customList[index])
            self.preOrderTraversal(2 * index)
            self.preOrderTraversal((2 * index) + 1)


    # Inorder Traversal
    def inorderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.inorderTraversal(2 * index)
            print(self.customList[index])
            self.inorderTraversal((2 * index) + 1)
    
    #Post Order Traversal
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        else:
            self.postOrderTraversal(2 * index)
            self.postOrderTraversal((2 * index) + 1)
            print(self.customList[index])


    # Level Order Traversal
    def levelOrderTraversal(self, index):
        while index <= self.lastUsedIndex:
            print(self.customList[index])
            index = index + 1

    # Delete node from binary tree
    def deleteNodeBT(self, value):
        if self.lastUsedIndex == 0:
            return "Nothing to delete!!"

        deepestNode = self.customList[self.lastUsedIndex]
        index = 1
        while index <= self.lastUsedIndex:
            if self.customList[index] == value:
                self.customList[index] = deepestNode
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return
            index = index + 1

    # Delete entire Binary Tree
    def deleteBT(self):
        self.customList = None



newBT = BinaryTree(8)

newBT.insertBT("Drinks")
newBT.insertBT("Hot")
newBT.insertBT("Cold")
newBT.insertBT("Tea")
newBT.insertBT("Coffee")

# print(newBT.searchBT("Hot"))

# newBT.preOrderTraversal(1)

# newBT.inorderTraversal(1)

# newBT.postOrderTraversal(1)

# newBT.levelOrderTraversal(1)

# newBT.deleteNodeBT("Hot")
# newBT.levelOrderTraversal(1)

newBT.deleteBT()
newBT.levelOrderTraversal(1)