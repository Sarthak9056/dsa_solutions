# LeetCode Problem Number - 75

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = [0,0,0]
        for i in nums:
            count[i] += 1
        i = 0
        for x in range(3):
            for _ in range(count[x]):
                nums[i] = x
                i += 1
