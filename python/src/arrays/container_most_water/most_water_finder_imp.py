from typing import List

from src.arrays.container_most_water.most_water_finder import MostWaterFinder


class MostWaterFinderImp(MostWaterFinder):

    def max_area(self, heights: List[int]) -> int:
        best_area = 0
        left_pt = 0
        right_pt = len(heights) - 1
        while left_pt < right_pt:
            area = (right_pt - left_pt) * min(heights[left_pt], heights[right_pt])
            best_area = max(best_area, area)
            if heights[left_pt] <= heights[right_pt]:
                left_pt += 1
            elif heights[left_pt] > heights[right_pt]:
                right_pt -= 1
        return best_area
