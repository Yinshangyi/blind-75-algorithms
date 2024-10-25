from typing import List

import pytest

from src.linkedlists.reorder_list.list_reorder_imp import ListReOrdererImp
from src.linkedlists.reorder_list.list_reorderer import ListReOrderer
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


@pytest.fixture(params=[
    ListReOrdererImp
])
def list_orderer(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_nodes, exp_nodes", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
])
def test_should_return_re_ordered_list(list_orderer: ListReOrderer, input_nodes: List[int], exp_nodes: List[int]):
    input_node: ListNode = array_2_linked_list(input_nodes)
    list_orderer.reorder_list(input_node)
    expected_output_list = exp_nodes
    assert linked_list_2_array(input_node) == expected_output_list
