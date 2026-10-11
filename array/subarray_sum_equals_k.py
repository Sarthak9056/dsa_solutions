# LeetCode Problem Number - 560

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0:1}
        for i in nums:
            prefix += i
            count += seen.get(prefix-k, 0)
            seen[prefix] = seen.get(prefix, 0)+1
        return count
        
