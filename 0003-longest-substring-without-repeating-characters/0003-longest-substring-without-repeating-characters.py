class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSub = 1 if len(s)>0 else 0
        for i in range(len(s)):
            sub = 0
            seen = set()
            j=i
            while(j<len(s) and s[j] not in seen):
                seen.add(s[j])
                j+=1
                sub+=1
            maxSub=max(maxSub,sub)
        return maxSub