# LeetCode Problem Number - 128

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        freq = 1
        s = set(nums)
        output = []
        if len(nums) == 0:
            return 0
        for i in sorted(s):
            if i+1 in s:
                freq += 1
            else:
                freq = 1
            output.append(freq)
        return max(output)