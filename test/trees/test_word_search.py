from src.trees.word_search import WordDictionary


def testSearchWord1():
    wordDictionary = WordDictionary();
    wordsToAdd = ["bad", "dad", "mad", "pad"]
    wordsToSearch = ["bad", "dad", "mad", "pad"]
    for word in wordsToAdd:
        wordDictionary.addWord(word)
    wordsFound = []
    for word in wordsToSearch:
        isWordFound = wordDictionary.search(word)
        wordsFound.append(isWordFound)
    assert wordsFound == [True, True, True, True]


def testSearchWord2():
    wordDictionary = WordDictionary();
    wordDictionary.addWord("abc")
    isWordFound = wordDictionary.search("a.c")
    assert isWordFound == True


def testSearchWord3():
    wordDictionary = WordDictionary();
    wordsToAdd = ["bad", "dad", "mad", "pad"]
    wordsToSearch = ["...", "d.d", "m..", "..d"]
    for word in wordsToAdd:
        wordDictionary.addWord(word)
    wordsFound = []
    for word in wordsToSearch:
        isWordFound = wordDictionary.search(word)
        wordsFound.append(isWordFound)
    assert wordsFound == [True, True, True, True]


def testSearchWord4():
    wordDictionary = WordDictionary();
    wordsToAdd = ["bad", "dad", "mad", "pad"]
    wordsToSearch = ["b..", "dz.", "zoo", "..z"]
    for word in wordsToAdd:
        wordDictionary.addWord(word)
    wordsFound = []
    for word in wordsToSearch:
        isWordFound = wordDictionary.search(word)
        wordsFound.append(isWordFound)
    assert wordsFound == [True, False, False, False]
