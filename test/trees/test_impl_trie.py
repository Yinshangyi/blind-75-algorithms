from src.trees.impl_trie import Trie


def testInsertWordInTrie():
    trie = Trie();
    trie.insert("apple");
    assert list(trie.rootNode.children.keys())[0] == "a"


def testSearchInTrie():
    trie = Trie();
    trie.insert("apple");
    isWordinTrie = trie.search("app");
    assert isWordinTrie == False


def testSearchNotInTrie():
    trie = Trie();
    trie.insert("apple");
    isWordinTrie = trie.search("apple");
    assert isWordinTrie == True


def testStartWithInTrie():
    trie = Trie();
    trie.insert("apple")
    wordStartWithInTrie = trie.startsWith("app")
    assert wordStartWithInTrie == True


def testStartWithNotInTrie():
    trie = Trie();
    trie.insert("apple")
    wordStartWithInTrie = trie.startsWith("abc")
    assert wordStartWithInTrie == False
