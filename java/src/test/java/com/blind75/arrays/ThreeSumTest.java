package com.blind75.arrays;


import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ThreeSumTest {

    @DisplayName("Given an integer array of 6 nums, three Sum should return all the triplets that equals 0")
    @Test
    void test_find_three_sum_6_items() {
        var nums = new int[]{-1, 0, 1, 2, -1, -4};
        var expectedResult = List.of(List.of(-1, -1, 2), List.of(-1, 0, 1));
        var result = new ThreeSum().findThreeSum(nums);
        assertEquals(expectedResult, result);
    }

    @DisplayName("Given an integer array of 3 nums, three Sum should return all the triplets that equals 0")
    @Test
    void test_find_three_sum_3_items() {
        var nums = new int[]{0, 1, 1};
        List<List<Integer>> expectedResult = Collections.emptyList();
        var result = new ThreeSum().findThreeSum(nums);
        assertEquals(expectedResult, result);
    }


}