class Solution(object):
    def productExceptSelf(self, nums):
        #SC=O(1)
        res=[]
        curr = 1
        for n in nums:
            res.append(curr)
            curr *= n
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res



        #SC=O(n)
        # pre = []
        # post =[]
        # curr = 1
        # for i in range(len(nums)):
        #     pre.append(curr)
        #     curr *= nums[i]
        # curr = 1
        # for i in range(len(nums)-1,-1,-1):
        #     post.insert(0, curr)
        #     curr *= nums[i]
        # for i in range(len(nums)):
        #     nums[i] = pre[i] * post[i]
        # return nums
