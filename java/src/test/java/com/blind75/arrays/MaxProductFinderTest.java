package com.blind75.arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class MaxProductFinderTest {

  @Test
  void maxProduct1() {
    int[] array = new int[]{2, 3, -2, 4};
    int maxProduct = new MaxProductFinder().maxProduct(array);
    assertEquals(6, maxProduct);
  }

  @Test
  void maxProduct2() {
    int[] array = new int[]{-2, 0, -1};
    int maxProduct = new MaxProductFinder().maxProduct(array);
    assertEquals(0, maxProduct);
  }

  @Test
  void maxProduct3() {
    int[] array = new int[]{-4, -3, -2};
    int maxProduct = new MaxProductFinder().maxProduct(array);
    assertEquals(12, maxProduct);
  }

  @Test
  void maxProduct4() {
    int[] array = new int[]{2, 0, 2, 3, -5};
    int maxProduct = new MaxProductFinder().maxProduct(array);
    assertEquals(6, maxProduct);
  }

}