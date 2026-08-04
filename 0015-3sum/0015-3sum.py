class Solution(object):
    def threeSum(self, nums):
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
        if len(z) >= 3:
            res.add((0,0,0))
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return [list(x) for x in res]


        # TC=O(nlogn + n^2)  SC=O(1)
        # nums.sort()
        # res=[]
        # for i in range(len(nums)):
        #     if i!= 0 and nums[i] == nums[i-1]:
        #         continue
        #     l = i+1
        #     r=len(nums)-1
        #     while(l<r):
        #         if nums[l]+nums[r]+nums[i]==0:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             while l<r and nums[l]==nums[l-1]:
        #                 l+=1
        #             r-=1
        #             while r>l and nums[r] ==nums[r+1]:
        #                 r-=1
        #         elif nums[l]+nums[r]+nums[i] <0:
        #             l+=1
        #         else:
        #             r-=1
        # return res
        