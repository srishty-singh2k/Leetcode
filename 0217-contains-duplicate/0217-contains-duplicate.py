class Solution(object):
    def containsDuplicate(self, nums):
        newNums = set()
        for n in nums:
            if n in newNums:
                return True
            else:
                newNums.add(n)
        return False