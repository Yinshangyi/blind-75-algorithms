class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        str1Array = [char for char in str1]
        str2Array = [char for char in str2]
        str1Array.sort()
        str2Array.sort()
        return str1Array == str2Array