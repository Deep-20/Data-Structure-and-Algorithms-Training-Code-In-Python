class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]            # +1 as we would not be using 0 index
        self.heapSize = 0
        self.maxSize = size + 1

# Peek method
def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

# Size of Binary Heap
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


# Level Order Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


# Making adjustemnts when inserting node
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    else:
        if heapType == "Min":
            if rootNode.customList[index] < rootNode.customList[parentIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[parentIndex]
                rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)
        elif heapType == "Max":
            if rootNode.customList[index] > rootNode.customList[parentIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[parentIndex]
                rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    
# Insert Node
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full!!"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
        return "Value has been successfully inserted."


# Heapify method for extraction(deletion) of node
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
        elif heapType == "Max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]

    heapifyTreeExtract(rootNode, swapChild, heapType)

# Extract Method
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

# Delete Entire Binary Heap
def deleteHeap(rootNode):
    rootNode.customList = None


newHeap = Heap(5)

# print(sizeOfHeap(newHeap))

insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")

print(extractNode(newHeap, "Max"))
print("----------")
levelOrderTraversal(newHeap)
print("----------")
deleteHeap(newHeap)
levelOrderTraversal(newHeap)