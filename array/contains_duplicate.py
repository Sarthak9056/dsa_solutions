#LeetCode #217 - Contains Duplicate (Easy)
# Pattern: Hashing - track seen values in a set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
