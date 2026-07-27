class Solution(object):
    def isValidSudoku(self, board):
        eleList = []
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if board[r][c] != '.':
                    eleList.extend([(r,element),(element,c),(r//3,c//3,element)])

        return len(eleList) == len(set(eleList))