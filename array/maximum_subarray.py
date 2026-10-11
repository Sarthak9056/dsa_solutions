# LeetCode Problem Number - 53

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = cur = nums[0]
        for i in nums[1:]:
            cur = max(i, cur+i)
            best = max(cur, best)
        return best

