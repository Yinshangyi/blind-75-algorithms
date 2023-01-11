from typing import List


class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.isLastLetter = False


class AutoComplete:
    def __init__(self):
        self.rootNode = TrieNode(None)

    def insert(self, word: List[str]):
        currentNode = self.rootNode
        for letter in word:
            if letter not in currentNode.children:
                currentNode.children[letter] = TrieNode(letter)
            currentNode = currentNode.children[letter]
        currentNode.isLastLetter = True

    def getLastNodeFromPrefixString(self, wordPrefix: str) -> TrieNode:
        def helper(rootNode: TrieNode, wordPrefix: str, acc: str = ""):
            if acc == wordPrefix:
                return rootNode
            for childNode in rootNode.children.values():
                currentWord = acc + childNode.value
                return helper(childNode, wordPrefix, currentWord)
        return helper(self.rootNode, wordPrefix)

    def getWordsStartingWith(self, wordPrefix: str) -> List[str]:
        def helper(rootNode: TrieNode, word: str = "") -> List[str]:
            if rootNode.isLastLetter:
                return word
            for childNode in rootNode.children.values():
                currentWord = word + childNode.value
                foundWord = helper(childNode, currentWord)

        startingNode = self.getLastNodeFromPrefixString(wordPrefix)
        allWords = helper(startingNode)
        return allWords
