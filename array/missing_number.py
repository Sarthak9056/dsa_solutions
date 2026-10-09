# Leetode Problem Number - 268

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sumval = sum(nums)
        exp = (n*(n+1))//2
        return exp-sumval
