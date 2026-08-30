class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        i,j = source[0], source[1]
        x,y = target[0], target[1]
        if(((i&1 and j&1) or (not(i&1) and not(j&1))) and ((x&1 and y&1) or (not(x&1) and not(y&1))) or
            ((i&1 and not(j&1)) or (not(i&1) and j&1)) and ((x&1 and not(y&1)) or (not(x&1) and y&1))):    
            if(abs(x-i) == abs(y-j)):
                return 1
            return 2

            # dia = [[ 0 for i in range(8)] for j in range(8)]
            # for n in range(1,8):
            #     if(source[0]+n<=8 and source[1]+n <= 8 and source[0]+n == target[0] and source[1]+n == target[1]):
            #         return 1
            #     if(source[0]-n>0 and source[1]-n > 0 and source[0]-n == target[0] and source[1]-n == target[1]):
            #         return 1
            #     if(source[0]-n>0 and source[1]+n <= 8 and source[0]-n == target[0] and source[1]+n == target[1]):
            #         return 1
            #     if(source[0]+n<=8 and source[1]-n >0 and source[0]+n == target[0] and source[1]-n == target[1]):
            #         return 1
            # return 2
        return -1
            