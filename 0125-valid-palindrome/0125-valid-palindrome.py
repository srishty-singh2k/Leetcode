class Solution(object):
    def isPalindrome(self, s):
        #TC=O(n) SC=O(1)
        l=0
        r=len(s)-1
        while(l<=r):
            if not s[l].isalnum():
                l+=1
                continue
            elif not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

        #TC=O(3n) SC=O(2n)
        #filtered = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        #return filtered == filtered[::-1]