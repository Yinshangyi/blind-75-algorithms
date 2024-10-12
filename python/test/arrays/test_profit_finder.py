import pytest

from src.arrays.profit_finder.profit_finder import ProfitFinder
from src.arrays.profit_finder.profit_finder_impl import ProfitFinderImpl


@pytest.fixture(params=[ProfitFinderImpl])
def profit_finder(request: pytest.FixtureRequest):
    return request.param()


def test_should_return_best_profit_is_5(profit_finder: ProfitFinder):
    prices = [7, 1, 5, 3, 6, 4]
    bestDayToSell = profit_finder.maxProfit(prices)
    assert bestDayToSell == 5


def test_should_return_best_profit_is_0(profit_finder: ProfitFinder):
    prices = [7, 6, 4, 3, 1]
    bestDayToSell = profit_finder.maxProfit(prices)
    assert bestDayToSell == 0
