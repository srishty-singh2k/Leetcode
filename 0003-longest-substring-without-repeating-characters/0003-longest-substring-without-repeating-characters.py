class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        maxSub = 1
        l=0
        r=1
        seen=set(s[0])
        while(l<len(s) and r<len(s)):
            if s[r] in seen:
                while(s[r] in seen):
                    seen.remove(s[l])
                    l+=1
            maxSub = max(maxSub,r-l+1)
            seen.add(s[r])
            r+=1
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