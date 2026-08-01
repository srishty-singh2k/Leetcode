class Solution(object):
    def productExceptSelf(self, nums):
        #TC=O(2n) SC=O(n)
        pre = [1]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i-1])

        post = 1
        for i in range(len(nums)-1,-1,-1):
            pre[i]=pre[i]*post
            post *= nums[i]

        return pre

        #TC=O(3n) SC=O(2n)
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
