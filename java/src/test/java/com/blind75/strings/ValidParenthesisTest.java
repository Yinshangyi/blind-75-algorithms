package com.blind75.strings;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ValidParenthesisTest {
    @Test
    public void validParenthesis1() {
        var inputString = "()";
        var areParenthesisValid = new ValidParenthesis().isValid(inputString);
        Assertions.assertEquals(true, areParenthesisValid);
    }

    @Test
    public void validParenthesis2() {
        var inputString = "()[]{}";
        var areParenthesisValid = new ValidParenthesis().isValid(inputString);
        Assertions.assertEquals(true, areParenthesisValid);
    }

    @Test
    public void validParenthesis3() {
        var inputString = "(]";
        var areParenthesisValid = new ValidParenthesis().isValid(inputString);
        Assertions.assertEquals(false, areParenthesisValid);
    }

    @Test
    public void validParenthesis4() {
        var inputString = ")([]";
        var areParenthesisValid = new ValidParenthesis().isValid(inputString);
        Assertions.assertEquals(false, areParenthesisValid);
    }



}
