package com.blind75.strings;

import java.util.HashMap;
import java.util.Map;

public class LongestSubString {

  public int lengthOfLongestSubstring(String s) {
    var startIndex = 0;
    var maxLength = 0;
    Map<Character, Integer> letterIndexes = new HashMap<>();

    for (var currentIndex = 0; currentIndex < s.length(); currentIndex++) {
      var letter = s.charAt(currentIndex);
      if (letterIndexes.containsKey(letter)) {
        maxLength = Math.max(maxLength, currentIndex - startIndex);
        startIndex = Math.max(startIndex, letterIndexes.get(letter) + 1);
      }
      letterIndexes.put(letter, currentIndex);
    }
    return maxLength;
  }

}
