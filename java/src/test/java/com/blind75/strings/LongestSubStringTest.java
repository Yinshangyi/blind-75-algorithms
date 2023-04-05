package com.blind75.strings;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class LongestSubStringTest {

  @Test
  void longestSubstring1() {
    var inputString = "abcabcbb";
    var longestSubString = new LongestSubString().lengthOfLongestSubstring(inputString);
    assertEquals(3, longestSubString);
  }

  @Test
  void longestSubstring2() {
    var inputString = "pwwkew";
    var longestSubString = new LongestSubString().lengthOfLongestSubstring(inputString);
    assertEquals(3, longestSubString);
  }
}