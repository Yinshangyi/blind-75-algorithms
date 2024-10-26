from typing import List

import pytest

from src.strings.group_anagram.grp_anagram_finder import GroupAnagramFinder
from src.strings.group_anagram.grp_anagram_finder_fp import GroupAnagramFinderFP
from src.strings.group_anagram.grp_anagram_finder_imp import GroupAnagramFinderImp


@pytest.fixture(params=[
    GroupAnagramFinderImp,
    GroupAnagramFinderFP
])
def group_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_str, exp_groups", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    ([""], [[""]]),
    (["a"], [["a"]])
])
def test_should_return_groups_of_anagrams(group_finder: GroupAnagramFinder, input_str: List[str],
                                          exp_groups: List[List[str]]):
    groups = group_finder.group_anagrams(input_str)
    assert groups == exp_groups
