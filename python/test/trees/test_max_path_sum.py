import pytest

from src.trees.max_path_sum.max_path_finder_imp import MaxPathFinderImp


@pytest.fixture(params=[
    MaxPathFinderImp
])
def path_finder(request: pytest.FixtureRequest):
    return request.param()
