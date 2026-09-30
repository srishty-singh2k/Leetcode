class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        i=0
        while(i<len(nums)):
            if nums[i]==0:
                i+=1
            else:
                count=0
                while(i<len(nums) and nums[i]==1):
                    count+=1
                    i+=1
                maxCount = max(maxCount,count)
        return maxCount