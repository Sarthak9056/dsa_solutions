# LeetCode Problem Number - 152

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max   # flip
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            best = max(best, cur_max)
        return best
