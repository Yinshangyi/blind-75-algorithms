from typing import List, Set

from src.arrays.contains_duplicates.duplicate_finder import DuplicateFinder


class DuplicateFinderFP(DuplicateFinder):

    def contains_duplicate(self, nums: List[int]) -> bool:
        # @formatter:off
        def helper(_nums: List[int], visited: Set[int]) -> bool:
            match _nums:
                case []: return False
                case [head, *tail] if head in visited: return True
                case [head, *tail]: return helper(tail, visited | {head})
        return helper(nums, set())



