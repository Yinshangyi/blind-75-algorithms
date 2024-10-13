from typing import List, Set


class DuplicateFinderImp:
    def contains_duplicate(self, nums: List[int]) -> bool:
        visited: Set[int] = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False


