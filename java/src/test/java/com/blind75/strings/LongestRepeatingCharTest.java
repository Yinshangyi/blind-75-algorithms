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

    @Test
    public void testCharacterReplacement3() {
        var inputString = "ABAA";
        var num_replacements = 0;
        var longestSubstring = new LongestRepeatingChar().characterReplacement(inputString, num_replacements);
        Assertions.assertEquals(2, longestSubstring);
    }

    @Test
    public void testCharacterReplacement4() {
        var inputString = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGN" +
                "NSBNCJQOF";
        var num_replacements = 4;
        var longestSubstring = new LongestRepeatingChar().characterReplacement(inputString, num_replacements);
        Assertions.assertEquals(7, longestSubstring);
    }


}

