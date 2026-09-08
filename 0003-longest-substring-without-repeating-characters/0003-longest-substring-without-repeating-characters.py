class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TC=O(n) SC=O(m)
        maxSub = 0
        l=0
        seen=set()
        for r in range(len(s)):
            while(s[r] in seen):
                seen.remove(s[l])
                l+=1
            maxSub = max(maxSub,r-l+1)
            seen.add(s[r])
        return maxSub


        # TC=O(n*m) SC=O(m) m=No of unique ele
        # for i in range(len(s)):
        #     sub = 0
        #     seen = set()
        #     j=i
        #     while(j<len(s) and s[j] not in seen):
        #         seen.add(s[j])
        #         j+=1
        #         sub+=1
        #     maxSub=max(maxSub,sub)
        # return maxSub