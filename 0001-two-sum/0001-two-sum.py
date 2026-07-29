class Solution(object):
    def twoSum(self, nums, target):
        
        #TC=O(n^2) SC=O(1)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]
