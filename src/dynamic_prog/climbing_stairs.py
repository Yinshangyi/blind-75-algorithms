class Solution:
    def climbStairs(self, n: int) -> int:
        firstValue = 1
        secondValue = 1
        for n in range(n-1):
            temp = firstValue
            firstValue = firstValue + secondValue
            secondValue = temp
        return firstValue
