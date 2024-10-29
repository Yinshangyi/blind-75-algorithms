from typing import List

from src.arrays.merge_sort.merge_sort import MergeSort


class MergeSortImp(MergeSort):

    def sort(self, array: List[int]) -> List[int]:
        if len(array) <= 1:
            return array

        mid_pt = len(array) // 2
        left_arr = array[0:mid_pt]
        right_arr = array[mid_pt:]

        left_sorted_arr = self.sort(left_arr)
        right_sorted_arr = self.sort(right_arr)

        return self.merge(left_sorted_arr, right_sorted_arr)

    def merge(self, left_arr: List[int], right_arr: List[int]):
        sorted_array = []
        left_pt, right_pt = 0, 0

        while left_pt < len(left_arr) and right_pt < len(right_arr):
            if left_arr[left_pt] < right_arr[right_pt]:
                sorted_array.append(left_arr[left_pt])
                left_pt += 1
            else:
                sorted_array.append(right_arr[right_pt])
                right_pt += 1
        sorted_array += left_arr[left_pt:]
        sorted_array += right_arr[right_pt:]
        return sorted_array
