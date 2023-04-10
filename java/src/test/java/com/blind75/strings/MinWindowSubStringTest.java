package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Map;

public class MinWindowSubStringTest {
    @Test
    public void testMinWindowSubString1() {
        var subString1 = "ADOBECODEBANC";
        var subString2 = "ABC";
        var minWindow = new MinWindowSubString().minWindow(subString1, subString2);
        Assertions.assertEquals("BANC", minWindow);
    }

    @Test
    public void testMinWindowSubString2() {
        var subString1 = "a";
        var subString2 = "aa";
        var minWindow = new MinWindowSubString().minWindow(subString1, subString2);
        Assertions.assertEquals("", minWindow);
    }

    @Test
    public void testMinWindowSubString3() {
        var subString1 = "AUIABVC";
        var subString2 = "ABC";
        var minWindow = new MinWindowSubString().minWindow(subString1, subString2);
        Assertions.assertEquals("ABVC", minWindow);
    }

    @Test
    public void testMinWindowSubString4() {
        var subString1 = "a";
        var subString2 = "b";
        var minWindow = new MinWindowSubString().minWindow(subString1, subString2);
        Assertions.assertEquals("", minWindow);
    }

    @Test
    public void testMinWindowSubString5() {
        var subString1 = "bba";
        var subString2 = "ab";
        var minWindow = new MinWindowSubString().minWindow(subString1, subString2);
        Assertions.assertEquals("ba", minWindow);
    }

    @Test
    void doesWindowContainsAllChars1() {
        Map<Character, Integer> charCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 1
        );

        Map<Character, Integer> targetCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 1
        );
        var windowOk = new MinWindowSubString().doesWindowContainsAllChars(charCounter, targetCounter);
        Assertions.assertTrue(windowOk);
    }

    @Test
    void doesWindowContainsAllChars2() {
        Map<Character, Integer> charCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 0
        );

        Map<Character, Integer> targetCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 1
        );
        var windowOk = new MinWindowSubString().doesWindowContainsAllChars(charCounter, targetCounter);
        Assertions.assertFalse(windowOk);
    }

    @Test
    void doesWindowContainsAllChars3() {
        Map<Character, Integer> charCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 2
        );

        Map<Character, Integer> targetCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 2
        );
        var windowOk = new MinWindowSubString().doesWindowContainsAllChars(charCounter, targetCounter);
        Assertions.assertTrue(windowOk);
    }
    @Test
    void doesWindowContainsAllChars4() {
        Map<Character, Integer> charCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 2,
                Character.valueOf('c'), 1
        );

        Map<Character, Integer> targetCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 1
        );
        var windowOk = new MinWindowSubString().doesWindowContainsAllChars(charCounter, targetCounter);
        Assertions.assertTrue(windowOk);
    }

    @Test
    void doesWindowContainsAllChars5() {
        Map<Character, Integer> charCounter = Map.of(
                Character.valueOf('a'), 1
        );

        Map<Character, Integer> targetCounter = Map.of(
                Character.valueOf('a'), 1,
                Character.valueOf('b'), 1,
                Character.valueOf('c'), 1
        );
        var windowOk = new MinWindowSubString().doesWindowContainsAllChars(charCounter, targetCounter);
        Assertions.assertFalse(windowOk);
    }
}
