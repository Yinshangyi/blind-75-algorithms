from typing import List

import pytest

from src.linkedlists.reverse_list.list_reverser import ListReverser
from src.linkedlists.reverse_list.list_reverser_imp import ListReverserImp
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


@pytest.fixture(params=[
    ListReverserImp
])
def list_reverser(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_list, exp_list", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], [])
])
def test_should_return_the_reversed_linkedin_list(list_reverser: ListReverser, input_list: List[int],
                                                  exp_list: List[int]):
    input_nodes: ListNode = array_2_linked_list(input_list)
    reversed_nodes: ListNode = list_reverser.reverse_list(input_nodes)
    assert linked_list_2_array(reversed_nodes) == exp_list
