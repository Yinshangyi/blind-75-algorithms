import pytest

from src.linkedlists.cycle.cycle_finder import CycleFinder
from src.linkedlists.cycle.cycle_finder_fp import CycleFinderFP
from src.linkedlists.cycle.cycle_finder_imp import CycleFinderImp
from src.linkedlists.utils import ListNode
from test.linkedlists.utils import array_2_linked_list


@pytest.fixture(params=[
    CycleFinderImp,
    CycleFinderFP
])
def cycle_finder(request: pytest.FixtureRequest):
    return request.param()


def test_should_return_true_if_one_node_points_to_a_previous_node(cycle_finder: CycleFinder):
    input_list: ListNode = array_2_linked_list([3, 2, 0, -4])
    # Make the last node next pointer to the second node
    input_list.next.next.next.next = input_list.next
    list_has_cycle = cycle_finder.has_cycle(input_list)
    assert list_has_cycle


def test_should_return_false_if_there_is_no_cycle(cycle_finder: CycleFinder):
    input_list: ListNode = array_2_linked_list([1])
    list_has_cycle = cycle_finder.has_cycle(input_list)
    assert not list_has_cycle
