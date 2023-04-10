package com.blind75.strings;

import java.util.HashMap;
import java.util.Map;

public class MinWindowSubString {

    private Map<Character, Integer> getTargetCounter(String subString) {
        Map<Character, Integer> counter = new HashMap<>();
        for (var characterByte : subString.getBytes()) {
            var character = Character.valueOf((char) characterByte);
            counter.putIfAbsent(character, 0);
            counter.put(character, counter.get(character) + 1);
        }
        return counter;
    }

    public String minWindow(String subString1, String subString2) {
        Map<Character, Integer> charCounter = new HashMap<>();
        Map<Character, Integer> targetCounter = getTargetCounter(subString2);
        var left = 0;
        var right = 0;
        var minWord = "";

        while (right < subString1.length()) {
            var currentChar = Character.valueOf(subString1.charAt(right));
            var currentWord = subString1.substring(left, right + 1);

            if (subString2.contains(currentChar.toString())) {
                charCounter.putIfAbsent(currentChar, 0);
                charCounter.put(currentChar, charCounter.get(currentChar) + 1);
            }

            while (doesWindowContainsAllChars(charCounter, targetCounter)) {
                currentWord = subString1.substring(left, right + 1);
                if (currentWord.length() < minWord.length() || minWord.isEmpty()) {
                    minWord = currentWord;
                }
                var leftChar = Character.valueOf(subString1.charAt(left));
                if (subString2.contains(leftChar.toString())) {
                    charCounter.put(leftChar, charCounter.get(leftChar) - 1);
                }
                left++;
            }
            right++;
        }
        return minWord;
    }

    public boolean doesWindowContainsAllChars(Map<Character, Integer> charCounter,
                                              Map<Character, Integer> targetCounter) {
        if (charCounter.keySet().size() != targetCounter.keySet().size()) {
            return false;
        }
        return charCounter.entrySet().stream()
                .allMatch(entry -> entry.getValue() >= targetCounter.get(entry.getKey()));
    }
}
