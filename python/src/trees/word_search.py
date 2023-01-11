class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastLetter = False
        self.longestWordLength = 0


class WordDictionary:

    def __init__(self):
        self.rootNode = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.rootNode
        for letter in word:
            if letter not in currentNode.children:
                currentNode.children[letter] = TrieNode()
            currentNode = currentNode.children[letter]
        currentNode.isLastLetter = True
        self.rootNode.longestWordLength = max(self.rootNode.longestWordLength, len(word))

    def search(self, word: str) -> bool:
        def dfs(startLetterIndex: int, rootNode: TrieNode) -> bool:
            currentNode = rootNode
            for letterIndex in range(startLetterIndex, len(word)):
                letter = word[letterIndex]
                if letter == ".":
                    # loop over all children of the current letter
                    for childNode in currentNode.children.values():
                        # if the search is successful for the rest of the letters
                        if dfs(letterIndex + 1, childNode):
                            return True
                    return False
                if letter not in currentNode.children:
                    return False
                currentNode = currentNode.children[letter]
            return currentNode.isLastLetter
        if len(word) > self.rootNode.longestWordLength:
            return False
        return dfs(0, self.rootNode)

