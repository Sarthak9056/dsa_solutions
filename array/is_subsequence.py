# Leetcode Problem Number - 392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0

        for ch in s:
            pos = t.find(ch, k)

            if pos == -1:
                return False

            k = pos + 1

        return True
        
