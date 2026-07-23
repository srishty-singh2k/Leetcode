class Solution(object):
    def longestConsecutive(self, nums):
        #O(n log n)
        nums.sort()
        maxLen = 0
        for i in range(len(nums)-1):
            if nums[i+1] == 1+nums[i]:
                currLen = 1
                while nums[i+1] == 1+nums[i]:
                    currLen += 1
                    i+=1
                maxLen = max(maxLen, currLen)
        return maxLen
                
        # O(n)
        # maxLen = 0
        # sett = set(nums)
        # for n in sett:
        #     if n-1 not in sett:
        #         currLen = 1
        #         start = n
        #         while start+1 in sett:
        #             currLen +=1
        #             start += 1
        #         maxLen = max(maxLen, currLen)
        # return maxLen
