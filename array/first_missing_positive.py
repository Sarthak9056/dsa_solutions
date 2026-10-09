# Leetode Problem Number - 41

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        seen = set(nums)
        i =1
        while i in seen:
            i += 1
        return i
