from typing import List

import pytest

from src.graphs.num_islands.island_finder import IslandFinder
from src.graphs.num_islands.island_finder_fp import IslandFinderFP
from src.graphs.num_islands.island_finder_imp import IslandFinderImp


@pytest.fixture(params=[
    IslandFinderImp,
    IslandFinderFP
])
def island_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("grid, exp_number_island", [
    (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            1
    ),
    (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            3
    )
])
def test_should_return_the_number_of_islands(island_finder: IslandFinder,
                                             grid: List[List[str]], exp_number_island: int):
    assert island_finder.get_islands_number(grid) == exp_number_island
