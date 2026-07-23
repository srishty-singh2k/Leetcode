class Solution(object):
    def longestConsecutive(self, nums):
        maxLen = 0
        sett = set(nums)
        for n in sett:
            if n-1 not in sett:
                currLen = 1
                start = n
                while start+1 in sett:
                    currLen +=1
                    start += 1
                maxLen = max(maxLen, currLen)
        return maxLen
