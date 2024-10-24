from typing import List

import pytest

from src.linkedlists.merge_k_list.k_lists_merger import KListsMerger
from src.linkedlists.merge_k_list.k_lists_merger_fp import KListsMergerFP
from src.linkedlists.merge_k_list.k_lists_merger_imp import KListsMergerImp
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


@pytest.fixture(params=[
    #KListsMergerImp,
    KListsMergerFP
])
def k_list_merger(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("lists, exp_merged_list", [
    (
            # Input lists
            [[1, 4, 5], [2, 6]],
            # expected list
            [1, 2, 4, 5, 6]
    ),
    (
            # Input lists
            [[1, 4, 5], [1, 3, 4], [2, 6]],
            # expected list
            [1, 1, 2, 3, 4, 4, 5, 6]
    )
])
def test_should_return_the_merged_linked_list_from_multiples_linked_list(k_list_merger: KListsMerger,
                                                                         lists: List[List[int]],
                                                                         exp_merged_list: List[int]):
    lists: List[ListNode] = [array_2_linked_list(_list) for _list in lists]
    mergedList = k_list_merger.merge_k_lists(lists)
    assert linked_list_2_array(mergedList) == exp_merged_list


@pytest.mark.parametrize("lists, exp_merged_list", [
    ([], []),
    [[[]], []]
])
def test_should_return_none_if_the_list_is_empty(k_list_merger: KListsMerger,
                                                 lists: List[List[int]],
                                                 exp_merged_list: List[int]):
    lists: List[ListNode] = [array_2_linked_list(_list) for _list in lists]
    mergedList = k_list_merger.merge_k_lists(lists)
    assert linked_list_2_array(mergedList) == exp_merged_list
