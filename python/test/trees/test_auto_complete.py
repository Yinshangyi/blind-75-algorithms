from src.trees.auto_complete import AutoComplete


def testGetLastNodeFromPrefix():
    autoComplete = AutoComplete()
    autoComplete.insert("hello")
    autoComplete.insert("hi")
    autoComplete.insert("hey")
    lastNode = autoComplete.getLastNodeFromPrefixString("he")
    assert lastNode == autoComplete.rootNode.children["h"].children["e"]


def testGetWordsStartingWith1():
    autoComplete = AutoComplete()
    autoComplete.insert("hello")
    autoComplete.insert("hi")
    autoComplete.insert("hey")
    autoComplete.insert("bonjour")
    foundWords = autoComplete.getWordsStartingWith("h")
    assert foundWords == ["hello", "hi", "hey"]


def testGetWordsStartingWith2():
    autoComplete = AutoComplete()
    autoComplete.insert("hi")
    autoComplete.insert("hey")
    autoComplete.insert("beautiful")
    autoComplete.insert("bonjour")
    autoComplete.insert("bonsoir")
    foundWordsStartingWithB = autoComplete.getWordsStartingWith("b")
    foundWordsStartingWithBon = autoComplete.getWordsStartingWith("bon")
    assert foundWordsStartingWithB == ["beautiful", "bonjour", "bonsoir"]
    assert foundWordsStartingWithBon == ["bonjour", "bonsoir"]

    foundWords = autoComplete.getWordsStartingWith("h")
    assert foundWords == ["hello", "hi", "hey"]
