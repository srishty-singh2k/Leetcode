class Solution(object):
    def shuffle(self, nums, n):
        #TC=O(n)  SC=O(1)
        bit = 12  #  2**12 = 1024>10**3
        for i in range(n):
            nums[i] = nums[i] << bit
            nums[i] = nums[i+n] | nums[i]
        j=(2*n)-1
        for i in range(n-1,-1,-1):
            y = nums[i] & (2**bit - 1)
            x = nums[i] >> bit
            nums[j] = y
            nums[j-1] = x
            j -=2
        return nums


        
        #TC = O(n)  SC=O(n)
        # res=[]
        # for i in range(n):
        #     res.append(nums[i])
        #     res.append(nums[i+n])
        # return res
        