class Solution(object):
    def isPalindrome(self, s):
        return [c.lower() for c in s if c.isalpha() or c.isdigit()] == [c.lower() for c in s if c.isalpha() or c.isdigit()][::-1]