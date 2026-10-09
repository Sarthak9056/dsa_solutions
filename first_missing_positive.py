# Leetode Problem Number - 41

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 1
        while True:
            if i not in nums:
                break
            i += 1
        return i
