package com.blind75.arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class MaxSubArrayTest {

  @Test
  void maxSubArray1() {
    var nums = new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    var maxSum = new MaxSubArray().maxSubArray(nums);
    assertEquals(6, maxSum);
  }

  @Test
  void maxSubArray2() {
    var nums = new int[]{5, 4, -1, 7, 8};
    var maxSum = new MaxSubArray().maxSubArray(nums);
    assertEquals(23, maxSum);
  }

  @Test
  void maxSubArray3() {
    var nums = new int[]{-1};
    var maxSum = new MaxSubArray().maxSubArray(nums);
    assertEquals(-1, maxSum);
  }

}