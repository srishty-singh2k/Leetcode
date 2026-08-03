class Solution(object):
    def twoSum(self, numbers, target):
        l= 0
        r = len(numbers)-1
        while(l<r):
            nums = numbers[l]+numbers[r]
            if nums == target:
                break
            elif nums>target:
                r-=1
            elif nums<target:
                l+=1

        return l+1,r+1