# LeetCode Problem Number - 238

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        answer = [1]*n
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        for i in range(n-1,-1,-1):
            answer[i] *= right
            right *= nums[i]

        return answer
