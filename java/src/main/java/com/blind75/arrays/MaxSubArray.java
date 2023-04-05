package com.blind75.arrays;

public class MaxSubArray {

  public int maxSubArray(int[] nums) {
    var maxSum = nums[0];
    var currentSum = 0;
    for (int num : nums) {
      if (currentSum < 0) {
        currentSum = 0;
      }
      currentSum += num;
      maxSum = Math.max(maxSum, currentSum);
    }
    return maxSum;
  }

}
