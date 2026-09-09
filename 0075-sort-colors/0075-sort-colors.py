from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        m=0
        r=len(nums)-1
        while(l<r and m<=r):
            if nums[m]==2:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
            elif nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            else:
                m+=1