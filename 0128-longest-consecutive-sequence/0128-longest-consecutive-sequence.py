class Solution(object):
    def longestConsecutive(self, nums):
        # SET W/O Repeated checks TC=O(n) SC=O(n) ---> TLE 81/85
        s = set(nums)
        maxSeq = 0
        for n in list(s):
            if n-1 not in s:
                seq = 1
                while (n+1 in s):
                    seq+=1
                    n +=1
                maxSeq = max(maxSeq, seq)
        return maxSeq

        # SORTING TC=O(n logn) SC=O(n)
        # nums=list(set(nums))
        # nums.sort()
        # maxSeq = 0 if len(nums)==0 else 1
        # i=0
        # seq=1
        # while(i<len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         seq+=1
        #     else:
        #         seq=1
        #     i+=1
        #     maxSeq = max(maxSeq,seq)
        # return maxSeq

        # SET TC=O(n^2) SC=O(n)   ----> TLE 74/85
        # s = set(nums)
        # maxSeq = 0
        # for n in nums:
        #     seq = 1
        #     while (n+1 in s):
        #         seq+=1
        #         n +=1
        #     maxSeq = max(maxSeq, seq)
        # return maxSeq
