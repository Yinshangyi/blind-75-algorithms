package com.blind75.strings;

import java.util.List;
import java.util.Map;
import java.util.Stack;

public class ValidParenthesis {

    private Map<Character, Character> parenthesisMap = Map.of(
            ')', '(',
            '}', '{',
            ']', '['
    );

    public boolean isValid(String inputString) {
        var stack = new Stack<Character>();
        var openingParenthesis = List.of(parenthesisMap.values());
        for (var character : inputString.getBytes()) {

        }
        return true;
    }
}
