from typing import List

from src.arrays.three_sums.three_sums_finder import ThreeSumsFinder


class ThreeSumsFinderImp(ThreeSumsFinder):

    def three_sum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result: List[List[int]] = []

        for index, first_val in enumerate(sorted_nums):
            if index > 0 and sorted_nums[index - 1] == sorted_nums[index]:
                continue

            left_pt = index + 1
            right_pt = len(sorted_nums) - 1

            while left_pt < right_pt:
                left_val, right_val = sorted_nums[left_pt], sorted_nums[right_pt]
                three_sum = first_val + left_val + right_val
                if three_sum > 0:
                    right_pt -= 1
                elif three_sum < 0:
                    left_pt += 1
                else:
                    result.append([first_val, left_val, right_val])
                    left_pt += 1
                    while sorted_nums[left_pt] == sorted_nums[left_pt - 1] and left_pt < right_pt:
                        left_pt += 1
        return result
