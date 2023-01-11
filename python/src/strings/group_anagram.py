from typing import List


class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagramGroups = {}
        for word in words:
            # Sort the letter in the string
            wordArray = [wordArray for wordArray in word]
            wordArray.sort()
            sortedWord = "".join(wordArray)
            if sortedWord not in anagramGroups:
                anagramGroups[sortedWord] = []
            anagramGroups[sortedWord].append(word)
        return list(anagramGroups.values())