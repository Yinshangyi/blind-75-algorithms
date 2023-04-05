package com.blind75.arrays;

public class MinRotatedArray {

  public int findMin(int[] nums) {
    var leftPointer = 0;
    var rightPointer = nums.length - 1;
    while (leftPointer <= rightPointer) {
      var middle = (rightPointer + leftPointer) / 2;
      if (nums[leftPointer] <= nums[rightPointer]) {
        break;
      }
      if (nums[middle] >= nums[leftPointer]) {
        leftPointer = middle + 1;
      } else {
        rightPointer = middle;
      }
    }
    return nums[leftPointer];
  }

}
