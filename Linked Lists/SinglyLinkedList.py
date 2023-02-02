class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insertion in linked list:
    def insertInSingleLinkedList(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            elif location == -1:
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                # node.next = tempNode.next
                # tempNode.next = node
                nextNode = tempNode.next
                tempNode.next = node
                node.next = nextNode
                if tempNode == self.tail:
                    self.tail = node

    # Traversal in single linked list
    def traverseSingleLinkedList(self):
        if self.head == None:
            print("No values found!!")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    # Searching in Singly Linked List
    def search(self, value):
        if self.head == None:
            return "Linked list is empty"
        else:
            temp = self.head
            index = 0
            while temp is not None:
                if temp.value == value:
                    return (str(value) + " found at index " + str(index))
                temp = temp.next
                index = index + 1
            return "Value not found in list!!"
    
    # Delete a node 
    def deleteNode(self, location):
        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    #Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("Singly linked List does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()

#print([node.value for node in singlyLinkedList])

singlyLinkedList.insertInSingleLinkedList(0, 0)
singlyLinkedList.insertInSingleLinkedList(1, 1)
singlyLinkedList.insertInSingleLinkedList(2, 2)
singlyLinkedList.insertInSingleLinkedList(3, 3)
singlyLinkedList.insertInSingleLinkedList(2.5, 3)

print([node.value for node in singlyLinkedList])

#singlyLinkedList.traverseSingleLinkedList()
#print(singlyLinkedList.search(4))

singlyLinkedList.deleteNode(2)
print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
