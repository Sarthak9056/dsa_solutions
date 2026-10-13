# Leetcode Problem Number - 977

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        output = []
        for x in nums:
            output.append(x*x)
        return sorted(output)