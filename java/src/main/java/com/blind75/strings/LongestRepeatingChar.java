package com.blind75.strings;

import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingChar {

    private Map<Character, Integer> charsCounter;

    public int characterReplacement(String inputString, int numReplacements) {
        var left = 0;
        var right = 0;
        var result = 0;
        charsCounter = new HashMap<>();

        while (right < inputString.length()) {
            var letter = inputString.charAt(right);

            charsCounter.putIfAbsent(letter, 0);
            charsCounter.put(letter, charsCounter.get(letter) + 1);

            var wordLength = (right - left) + 1;
            var highestCharOccurence = getHighestCharOccurence();

            while ((wordLength - highestCharOccurence) > numReplacements) {
                var numOccurenceFirstChar = charsCounter.get(inputString.charAt(0));
                charsCounter.put(inputString.charAt(left), numOccurenceFirstChar - 1);
                left++;
                wordLength = (right - left) + 1;
            }

            wordLength = (right - left) + 1;
            result = Math.max(result, wordLength);
            right++;
        }
        return result;
    }

    private int getHighestCharOccurence() {
        var highestCharOccurence = 0;
        for (var entry : charsCounter.entrySet()) {
            highestCharOccurence = Math.max(highestCharOccurence, entry.getValue());
        }
        return highestCharOccurence;
    }
}
