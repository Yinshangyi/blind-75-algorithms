package com.blind75.strings;

public class LongestPalinSubString {

    public String longestPalindrome(String inputString) {
        var longestPalin = "";
        for (int pointer = 0; pointer < inputString.length(); pointer++) {
            var longestPalin1 = expandFromMiddle(inputString, pointer, pointer);
            var longestPalin2 = expandFromMiddle(inputString, pointer, pointer + 1);
            var longestOfTwoPalins = longestPalin1.length() > longestPalin2.length()?
                    longestPalin1 : longestPalin2;
            if (longestOfTwoPalins.length() > longestPalin.length()) {
                longestPalin = longestOfTwoPalins;
            }

        }
        return longestPalin;
    }

    private static String expandFromMiddle(String inputString, int left, int right) {
        var longestPalin = "";
        while (left >= 0 && right < inputString.length() && inputString.charAt(left) == inputString.charAt(right)) {
            var wordLength = (right - left) + 1;
            if (wordLength > longestPalin.length()) {
                longestPalin = inputString.substring(left, right + 1);
            }
            left -= 1;
            right += 1;
        }
        return longestPalin;
    }
}
