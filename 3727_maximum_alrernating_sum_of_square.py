# Leetcode Problem Number - 3727

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        first = 0
        last = len(nums)-1
        score = 0
        nums.sort()
        while first < last:
            score += (nums[last]*nums[last]) - (nums[first]*nums[first])
            first += 1
            last -= 1
        if first == last:
            score += nums[first]*nums[first]
        return score