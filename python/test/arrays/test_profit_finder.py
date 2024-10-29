import pytest

from src.arrays.profit_finder.profit_finder import ProfitFinder
from src.arrays.profit_finder.profit_finder_fp import ProfitFinderFP
from src.arrays.profit_finder.profit_finder_imp import ProfitFinderImp


@pytest.fixture(params=[
    ProfitFinderImp,
    #ProfitFinderFP
])
def profit_finder(request: pytest.FixtureRequest):
    return request.param()


def test_should_return_best_profit_is_5(profit_finder: ProfitFinder):
    prices = [7, 1, 5, 3, 6, 4]
    bestDayToSell = profit_finder.get_max_profit(prices)
    assert bestDayToSell == 5


def test_should_return_best_profit_is_0(profit_finder: ProfitFinder):
    prices = [7, 6, 4, 3, 1]
    bestDayToSell = profit_finder.get_max_profit(prices)
    assert bestDayToSell == 0
