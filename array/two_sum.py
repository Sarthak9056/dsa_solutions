# LeetCode #1 - Two Sum (Easy)
# Pattern: Hashing - one pass with a dictionary of seen values
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}                      # value -> index
        for i, n in enumerate(nums):
            if target - n in seen:     # complement seen before?
                return [seen[target - n], i]
            seen[n] = i
