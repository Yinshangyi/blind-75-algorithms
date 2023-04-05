package com.blind75.arrays;

import java.util.Arrays;

public class DuplicateFinder {

  public boolean containsDuplicates(int[] array) {
    Arrays.sort(array);
    for (int i = 0; i < array.length; i++) {
      if(i > 0 && array[i] == array[i-1])
        return true;
    }
    return false;
  }

}
