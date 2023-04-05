package com.blind75.strings;

import java.util.*;

public class GroupAnagram {
    public List<List<String>> groupAnagrams(List<String> input) {
        Map<Integer, List<String>> anagramGroups = new HashMap<>();
        for (var word : input) {
            var asciiCode = getAsciiCodeSumFromString(word);
            anagramGroups.putIfAbsent(asciiCode, new ArrayList<>());
            anagramGroups.get(asciiCode).add(word);
        }
        return mapValue2Lists(anagramGroups);
    }

    private int getAsciiCodeSumFromString(String word) {
        var asciiSum = 0;
        for (var letter : word.getBytes()) {
            asciiSum += (int) letter;
        }
        return asciiSum;
    }

    private List<List<String>> mapValue2Lists(Map<Integer, List<String>> map) {
        return map.entrySet().stream()
                .map(entry -> entry.getValue())
                .toList();
    }
}
