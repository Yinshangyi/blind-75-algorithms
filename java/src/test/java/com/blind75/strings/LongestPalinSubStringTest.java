package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.List;

public class LongestPalinSubStringTest {
    @Test
    public void testLongestPalinSubString1() {
        var inputString = "babad";
        var longestSubstring = new LongestPalinSubString().longestPalindrome(inputString);
        Assertions.assertTrue(List.of("bab", "aba").contains(longestSubstring));
    }

    @Test
    public void testLongestPalinSubString2() {
        var inputString = "cbbd";
        var longestSubstring = new LongestPalinSubString().longestPalindrome(inputString);
        Assertions.assertEquals("bb", longestSubstring);
    }

    @Test
    public void testLongestPalinSubString3() {
        var inputString = "a";
        var longestSubstring = new LongestPalinSubString().longestPalindrome(inputString);
        Assertions.assertEquals("a", longestSubstring);
    }

    @Test
    public void testLongestPalinSubString4() {
        var inputString = "ac";
        var longestSubstring = new LongestPalinSubString().longestPalindrome(inputString);
        Assertions.assertEquals("a", longestSubstring);
    }

    @Test
    public void testLongestPalinSubString5() {
        var inputString = "abb";
        var longestSubstring = new LongestPalinSubString().longestPalindrome(inputString);
        Assertions.assertEquals("bb", longestSubstring);
    }

}
