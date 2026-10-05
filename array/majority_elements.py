# LeetCode Problem Number - 169

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = int(len(nums)/2)
        for i in set(nums):
            if nums.count(i)>n:
                return i
