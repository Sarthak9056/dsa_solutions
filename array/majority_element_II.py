# LeetCode Problem Number - 229

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        output = []
        app = len(nums)//3
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        for j,c in counter.items():
            if c > app:
                output.append(j)
        return output
