from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        leftIndex = 0
        rightIndex = len(height) - 1
        while leftIndex < rightIndex:
            currentWidth = rightIndex - leftIndex
            currentHeight = min(height[leftIndex], height[rightIndex])
            currentArea = currentWidth * currentHeight
            maxArea = max(maxArea, currentArea)

            if height[leftIndex] > height[rightIndex]:
                rightIndex -= 1
            else:
                leftIndex += 1
        return maxArea
