from typing import List

from src.arrays.container_most_water.most_water_finder import MostWaterFinder


class MostWaterFinderFP(MostWaterFinder):

    def max_area(self, heights: List[int]) -> int:
        # @formatter:off
        def helper(_heights: List[int], best_area: int) -> int:
            match _heights:
                case [val]: return max(val, best_area)
                case [left, *mid, right]:
                    area = (len(_heights) - 1) * min(left, right)
                    new_best_area = max(area, best_area)
                    if left <= right:
                        return helper(mid + [right], new_best_area)
                    else:
                        return helper([left] + mid, new_best_area)
        return helper(heights, 0)
