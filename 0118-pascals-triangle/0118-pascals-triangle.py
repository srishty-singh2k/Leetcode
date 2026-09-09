class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        if numRows==0:
            return []
        for i in range(1,numRows):
            curr = [1]
            for j in range(i-1):
                curr.append(res[i-1][j]+res[i-1][j+1])
            curr.append(1)
            res.append(curr)
        return res
