package com.blind75.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
    public List<List<Integer>> findThreeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int firstIndex = 0; firstIndex < nums.length; firstIndex++) {
            if (firstIndex > 0 && nums[firstIndex] == nums[firstIndex - 1])
                continue;
            var secondIndex = firstIndex + 1;
            var thirdIndex = nums.length - 1;
            while (secondIndex < thirdIndex) {
                var threeSum = nums[firstIndex] + nums[secondIndex] + nums[thirdIndex];
                if (threeSum > 0) {
                    thirdIndex--;
                } else if (threeSum < 0) {
                    secondIndex++;
                } else {
                    result.add(List.of(nums[firstIndex], nums[secondIndex], nums[thirdIndex]));
                    secondIndex++;
                    while (secondIndex < thirdIndex && nums[secondIndex] == nums[secondIndex - 1]) {
                        secondIndex++;
                    }
                }
            }
        }
        return result;
    }
}
