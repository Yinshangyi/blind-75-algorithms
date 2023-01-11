class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastLetter = False


class Trie:

    def __init__(self):
        self.rootNode = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.rootNode
        for letter in word:
            if letter not in currentNode.children:
                currentNode.children[letter] = TrieNode()
            currentNode = currentNode.children[letter]
        currentNode.isLastLetter = True

    def search(self, word: str) -> bool:
        currentNode = self.rootNode
        for letter in word:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        return currentNode.isLastLetter

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.rootNode
        for letter in prefix:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        return True
