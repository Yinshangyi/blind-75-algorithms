package com.blind75.strings;

import java.util.ArrayList;
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
        var openingParenthesis = new ArrayList<Character>(parenthesisMap.values());
        var closingParenthesis = new ArrayList<Character>(parenthesisMap.keySet());

        for (var characterByte : inputString.getBytes()) {
            var character = Character.valueOf((char) characterByte);
            if (openingParenthesis.contains(character)) {
                stack.push(character);
            } else if (closingParenthesis.contains(character)) {
                if (stack.isEmpty()) {
                    return false;
                }
                var charFromStack = stack.pop();
                if (!charFromStack.equals(parenthesisMap.get(character)))
                    return false;
            }
        }
        if (stack.empty()) {
            return true;
        }
        return false;
    }
}
