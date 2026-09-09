class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # TC=O(m*n) SC=O(1) m=Rows;n=Cols
        # isRowZero = 0 in matrix[0]
        # isColZero = any(matrix[i][0] == 0 for i in range(len(matrix)))
        # for i in range(1,len(matrix)):
        #     for j in range(1,len(matrix[0])):
        #         if matrix [i][j]==0:
        #             matrix[0][j]=0
        #             matrix[i][0]=0        
        # for i in range(1,len(matrix)):
        #     if matrix[i][0]==0:
        #         for j in range(len(matrix[0])):
        #             matrix[i][j]=0
        # for j in range(1,len(matrix[0])):
        #     if matrix[0][j]==0:
        #         for i in range(len(matrix)):
        #             matrix[i][j]=0
        # if isRowZero:
        #     for j in range(len(matrix[0])):
        #         matrix[0][j]=0
        # if isColZero:
        #     for i in range(len(matrix)):
        #         matrix[i][0]=0 

        # TC=O(m*n*(m+n)) SC=O(1)  Failed at 208/211 had -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for x in range(len(matrix)):
                        matrix[x][j]=-10 if matrix[x][j]!=0 else 0
                    for y in range(len(matrix[0])):
                        matrix[i][y]=-10 if matrix[i][y]!=0 else 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-10:
                    matrix[i][j]=0
