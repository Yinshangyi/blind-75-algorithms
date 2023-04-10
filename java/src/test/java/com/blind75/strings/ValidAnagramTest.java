package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ValidAnagramTest {

    @Test
    public void testValidAnagramTest1() {
        var input1 = "anagram";
        var input2 = "nagaram";
        var isInput2AnagramOfInput1 = new ValidAnagram().isAnagram(input1, input2);
        Assertions.assertTrue(isInput2AnagramOfInput1);
    }

    @Test
    public void testValidAnagramTest2() {
        var input1 = "rat";
        var input2 = "car";
        var isInput2AnagramOfInput1 = new ValidAnagram().isAnagram(input1, input2);
        Assertions.assertFalse(isInput2AnagramOfInput1);
    }

}
