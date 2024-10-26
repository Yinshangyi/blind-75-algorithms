from typing import List

from src.strings.group_anagram.grp_anagram_finder import GroupAnagramFinder


class GroupAnagramFinderImp(GroupAnagramFinder):

    def group_anagrams(self, words: List[str]) -> List[List[str]]:
        groups: dict[int, List[str]] = {}
        for word in words:
            ascii_values = [ord(char) for char in word]
            ascii_sum = sum(ascii_values)
            if ascii_sum not in groups:
                groups[ascii_sum] = []
            groups[ascii_sum].append(word)
        return list(groups.values())
