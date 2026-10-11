# LeetCode Problem Number - 228

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        output = []
        i, n = 0, len(nums)
        while i < n:
            start = nums[i]
            # walk forward while the next value is consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            output.append(str(start) if start == end else f"{start}->{end}")
            i += 1
        return output
