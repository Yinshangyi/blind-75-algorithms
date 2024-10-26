from functools import reduce
from typing import List

from src.strings.group_anagram.grp_anagram_finder import GroupAnagramFinder


class GroupAnagramFinderFP(GroupAnagramFinder):

    def group_anagrams(self, words: List[str]) -> List[List[str]]:
        def helper(groups: dict[int, List[str]], word: str) -> dict[int, List[str]]:
            ascii_values = [ord(char) for char in word]
            ascii_sum = sum(ascii_values)
            new_group = groups.get(ascii_sum, []) + [word]
            return {**groups, ascii_sum: new_group}

        groups_dict = reduce(helper, words, {})
        return list(groups_dict.values())
