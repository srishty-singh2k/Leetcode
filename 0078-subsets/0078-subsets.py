class Solution(object):
    def subsets(self, nums):
        #TC=O((2^n)*n[for list copy]) SC=O((2^n)*n + n[auxiliary])
        res=[]
        def sub(i,curr):
            if i==len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            sub(i+1,curr)
            curr.pop()
            sub(i+1,curr)
        sub(0,[])
        return res