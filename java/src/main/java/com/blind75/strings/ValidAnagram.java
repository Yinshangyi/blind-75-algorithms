package com.blind75.strings;

import java.util.Arrays;
import java.util.List;

public class ValidAnagram {
    public boolean isAnagram(String input1, String input2) {
        if (input1.length() != input2.length()) {
            return false;
        }
        var array1 = input1.getBytes();
        var array2 = input2.getBytes();
        Arrays.sort(array1);
        Arrays.sort(array2);
        for (int i = 0; i < array1.length; i++) {
            if (array1[i] != array2[i]) {
                return false;
            }
        }
        return true;
    }
}
