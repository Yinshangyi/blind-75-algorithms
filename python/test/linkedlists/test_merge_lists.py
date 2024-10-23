from typing import Optional

import pytest

from src.linkedlists.merge_list.list_merger import ListMerger
from src.linkedlists.merge_list.list_merger_fp import ListMergerFP
from src.linkedlists.merge_list.list_merger_imp import ListMergerImp
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


@pytest.fixture(params=[
    ListMergerImp,
    ListMergerFP
])
def list_merger(request: pytest.FixtureRequest):
    return request.param()


def test_should_return_the_merged_list(list_merger: ListMerger):
    list1: Optional[ListNode] = array_2_linked_list([1, 2, 4])
    list2: Optional[ListNode] = array_2_linked_list([1, 3, 4])
    merged_list = list_merger.merge_two_lists(list1, list2)
    expected_merged_list = [1, 1, 2, 3, 4, 4]
    assert linked_list_2_array(merged_list) == expected_merged_list


def test_should_return_an_empty_list_when_both_lists_are_empty(list_merger: ListMerger):
    list1: Optional[ListNode] = array_2_linked_list([])
    list2: Optional[ListNode] = array_2_linked_list([])
    merged_list = list_merger.merge_two_lists(list1, list2)
    expected_merged_list = []
    assert linked_list_2_array(merged_list) == expected_merged_list


def test_should_return_an_the_first_list_when_the_second_list_is_empty(list_merger: ListMerger):
    list1: Optional[ListNode] = array_2_linked_list([0])
    list2: Optional[ListNode] = array_2_linked_list([])
    merged_list = list_merger.merge_two_lists(list1, list2)
    expected_merged_list = [0]
    assert linked_list_2_array(merged_list) == expected_merged_list
