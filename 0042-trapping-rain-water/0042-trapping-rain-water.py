class Solution(object):
    def trap(self, height):
        #TC=O(2n) SC=O(n)
        res=0
        pre = []
        maxPre = 0
        for i in range(len(height)):
            pre.append(maxPre)
            maxPre=max(maxPre,height[i])
        maxPost = 0
        for i in range(len(height)-1,-1,-1):
            water = min(pre[i],maxPost)-height[i]
            if water>0:
                res += water
            maxPost = max(maxPost,height[i])
        return res