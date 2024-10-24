from typing import List

import pytest

from src.linkedlists.remove_n_items.n_items_remover import NItemsRemover
from src.linkedlists.remove_n_items.n_items_remover_imp import NItemsRemoverImp
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list, linked_list_2_array


@pytest.fixture(params=[
    NItemsRemoverImp
])
def item_remover(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("input_list, k, exp_list", [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2])
])
def test_should_return_a_list_with_n_item_removed_from_the_input_list(item_remover: NItemsRemover,
                                                                      input_list: List[int],
                                                                      k: int,
                                                                      exp_list: List[int]):
    input_list: ListNode = array_2_linked_list(input_list)
    listWithRemovedElements: ListNode = item_remover.remove_nth_from_end(input_list, k)
    assert linked_list_2_array(listWithRemovedElements) == exp_list
