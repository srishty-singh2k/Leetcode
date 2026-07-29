class Solution(object):
    def twoSum(self, nums, target):
        #TC=O(n) SC=O(n)
        comp = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if  diff in comp:
                return [i,comp[diff]]
            else:
                comp[nums[i]]=i

        #TC=O(n^2) SC=O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j])==target:
        #             return [i,j]
