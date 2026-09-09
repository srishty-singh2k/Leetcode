class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # TC=O(n) SC=O(1)
        # l=0
        # m=0
        # r=len(nums)-1
        # while(l<r and m<=r):
        #     if nums[m]==2:
        #         nums[m],nums[r]=nums[r],nums[m]
        #         r-=1
        #     elif nums[m]==0:
        #         nums[l],nums[m]=nums[m],nums[l]
        #         l+=1
        #         m+=1
        #     else:
        #         m+=1

        # FREQ
        from collections import Counter
        count = Counter(nums)
        i=0
        for _ in range(count[0]):
            nums[i]=0
            i+=1
        for _ in range(count[1]):
            nums[i]=1
            i+=1
        for _ in range(count[2]):
            nums[i]=2
            i+=1