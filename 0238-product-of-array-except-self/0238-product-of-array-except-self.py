class Solution(object):
    def productExceptSelf(self, nums):
        pre = []
        post =[]
        curr = 1
        for i in range(len(nums)):
            pre.append(curr)
            curr *= nums[i]
        curr = 1
        for i in range(len(nums)-1,-1,-1):
            post.insert(0, curr)
            curr *= nums[i]
        for i in range(len(nums)):
            nums[i] = pre[i] * post[i]
        return nums
