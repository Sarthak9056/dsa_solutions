# LeetCode Problem Number - 88

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i,j,k = m-1,n-1,m+n-1  #put the m-1 value in i for the its maximum index value
        while j>=0:  # check the nums of elemnets in nums2
            if i>=0 and nums1[i]>nums2[j]: #checks elements in nums1 and compare nums1 last value with nums2 last value
                nums1[k] = nums1[i] 
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

