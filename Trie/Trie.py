class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert String in Trie
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        
        current.endOfString = True

    # Seatch for string in Trie
    def searchTrie(self, word):
        if self.root.endOfString == True:
            return False
        else:
            current = self.root
            for i in word:
                node = current.children.get(i)
                if node == None:
                    return False
                else:
                    current = node
            if current.endOfString == True:
                return True
            else:
                return False


# Delete String
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")

# print(newTrie.root.children)
print(newTrie.searchTrie("App"))

print(deleteString(newTrie.root, "App", 0))

print(newTrie.searchTrie("App"))

