class Solution(object):
    def isAnagram(self, s, t):
        #TC=O(n) SC=0(26)
        if len(s) != len(t):
             return False
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        return all(x == 0 for x in count)

        #TC=O(n logn) SC=O(2n)
        #return sorted(s) == sorted(t)

        # TC=O(n) SC=O(2k)  k=no of distinct char
        # has hashing and associated overhead
        # if len(s) != len(t):
        #     return False
        # mapS = {}
        # mapT = {}
        # for i in range(len(s)):
        #     mapS[s[i]] = 1+ mapS.get(s[i],0)
        #     mapT[t[i]] = 1+ mapT.get(t[i],0)
        # return mapS == mapT
        