package com.blind75.arrays;

import java.util.Arrays;

public class MaxProductFinder {

    public int maxProduct(int[] nums) {
        var result = Arrays.stream(nums).max().getAsInt();
        var maxProd = 1;
        var minProd = 1;
        for (int num : nums) {
            var tmpMax = maxProd;
            maxProd = maxThreeInt(num * maxProd, num * minProd, num);
            minProd = minThreeInt(num * tmpMax, num * minProd, num);
            result = Math.max(maxProd, result);
        }
        return result;
    }

    private int maxThreeInt(int value1, int value2, int value3) {
        return Math.max(Math.max(value1, value2), value3);
    }

    private int minThreeInt(int value1, int value2, int value3) {
        return Math.min(Math.min(value1, value2), value3);
    }

}
