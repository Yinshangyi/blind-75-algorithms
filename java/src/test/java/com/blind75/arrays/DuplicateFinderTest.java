package com.blind75.arrays;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class DuplicateFinderTest {

  @DisplayName("Return true when there are duplicates in the input data")
  @Test
  void containsDuplicates1() {
    int[] inputArray = new int[]{1, 2, 3, 1};
    boolean hasDuplicate = new DuplicateFinder().containsDuplicates(inputArray);
    assertTrue(hasDuplicate);
  }

  @DisplayName("Return false when there are no duplicates in the input data")
  @Test
  void containsDuplicates2() {
    int[] inputArray = new int[]{1, 2, 3, 5};
    boolean hasDuplicate = new DuplicateFinder().containsDuplicates(inputArray);
    assertFalse(hasDuplicate);
  }
}