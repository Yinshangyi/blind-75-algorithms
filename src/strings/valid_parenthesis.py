from collections import deque


class Solution:
    def isValid(self, string: str) -> bool:
        closeOpenMap = {"}": "{", "]": "[", ")": "("}
        stack = deque()
        for char in string:
            if char in closeOpenMap:
                if stack and stack[-1] == closeOpenMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
