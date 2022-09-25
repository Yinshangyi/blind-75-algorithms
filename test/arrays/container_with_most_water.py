from src.arrays.container_with_most_water import Solution


def test_container_with_most_water():
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    best_amount = Solution().maxArea(heights)
    expected_best_amount = 49
    assert best_amount == expected_best_amount