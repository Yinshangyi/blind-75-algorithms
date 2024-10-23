from typing import List

import pytest

from src.arrays.container_most_water.most_water_finder import MostWaterFinder
from src.arrays.container_most_water.most_water_finder_fp import MostWaterFinderFP
from src.arrays.container_most_water.most_water_finder_imp import MostWaterFinderImp


@pytest.fixture(params=[
    MostWaterFinderImp,
    MostWaterFinderFP
])
def area_finder(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize("heights, expected_area", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_should_return_the_maximum_water_area(area_finder: MostWaterFinder, heights: List[int], expected_area: int):
    best_amount = area_finder.max_area(heights)
    assert best_amount == expected_area
