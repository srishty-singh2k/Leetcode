class Solution(object):
    def isAnagram(self, s, t):
        #TC=O(n logn) SC=O(2n)
        #return sorted(s) == sorted(t)

        # TC=O(n) SC=O(2k)  k=no of distinct char
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}
        for i in range(len(s)):
            mapS[s[i]] = 1+ mapS.get(s[i],0)
            mapT[t[i]] = 1+ mapT.get(t[i],0)
        return mapS == mapT
        