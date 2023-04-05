package com.blind75.arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class MinRotatedArrayTest {

  @Test
  public void find_min_element_1() {
    int[] nums = new int[]{3, 4, 5, 1, 2};
    int minElement = new MinRotatedArray().findMin(nums);
    assertEquals(1, minElement);
  }

  @Test
  public void find_min_element_2() {
    int[] nums = new int[]{3, 4, 5, 1, 2};
    int minElement = new MinRotatedArray().findMin(nums);
    assertEquals(1, minElement);
  }

  @Test
  public void find_min_element_3() {
    int[] nums = new int[]{20, 30, 10, 11, 12};
    int minElement = new MinRotatedArray().findMin(nums);
    assertEquals(10, minElement);
  }

}