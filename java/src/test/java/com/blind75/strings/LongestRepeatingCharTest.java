package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class LongestRepeatingCharTest {

    @Test
    public void testCharacterReplacement1() {
        var inputString = "ABAB";
        var num_replacements = 2;
        var longestSubstring = new LongestRepeatingChar().characterReplacement(inputString, num_replacements);
        Assertions.assertEquals(4, longestSubstring);
    }

    @Test
    public void testCharacterReplacement2() {
        var inputString = "AABABBA";
        var num_replacements = 1;
        var longestSubstring = new LongestRepeatingChar().characterReplacement(inputString, num_replacements);
        Assertions.assertEquals(4, longestSubstring);
    }
}

