class Solution:
    def trap(self, height: List[int]) -> int:
        # PREFIX-SUFFIX TC=O(n) SC=O(1)/O(n)ifPrecomputeBoth
        maxL=[0]
        for i in range(len(height)-1):
            maxL.append(max(maxL[i],height[i]))
        maxR=0
        water = 0
        for i in range(len(height)-1,-1,-1):
            water += min(maxL[i],maxR)-height[i] if (min(maxL[i],maxR)>height[i]) else 0
            maxR=max(maxR,height[i])
        return water

        
        # TWO-POINTERS TC=O(n) SC=O(1)
        # if len(height)<=2:
        #     return 0
        # l=0
        # r=len(height)-1
        # maxL=height[l]
        # maxR=height[r]
        # water = 0
        # while(l<r):
        #     if height[l]<=height[r]:
        #         l+=1
        #         water += (maxL-height[l]) if (maxL>height[l]) else 0
        #         maxL = max(maxL,height[l])
        #     else:
        #         r-=1
        #         water += (maxR-height[r]) if (maxR>height[r]) else 0 
        #         maxR = max(maxR,height[r])
        # return water