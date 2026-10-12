# Leetcode Problem Number - 125

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        d = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for i in s:
            if i not in d:
                s = s.replace(i, '')
        rev = s[::-1]
        if s == rev:
            return True
        else:
            return False