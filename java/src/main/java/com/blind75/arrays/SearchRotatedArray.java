package com.blind75.arrays;

public class SearchRotatedArray {

    public int search(int[] array, int target) {
        var left = 0;
        var right = array.length - 1;

        while (left <= right) {
            var middle = (left + right) / 2;
            if (array[middle] == target) {
                return middle;
            }

            // If middle is in the left subarray
            if (array[left] <= array[middle]) {
                if (target > array[middle] || target < array[left]) {
                    left = middle + 1;
                } else {
                    right = middle - 1;
                }
            }
            // If middle is in the right subarray
            else {
                if (target < array[middle] || target > array[right]) {
                    right = middle - 1;
                }
                else {
                    left = middle + 1;
                }
            }

        }
        return -1;
    }
}
