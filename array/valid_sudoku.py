# LeetCode Problem Number - 36

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                elif val in board[i][j+1:]:
                    return False
                elif val in [board[k][j] for k in range(i+1,n)]:
                    return False
                br,bc = (i//3)*3, (j//3)*3
                for r in range(br,br+3):
                    for c in range(bc,bc+3):
                        if (r,c) != (i,j) and board[r][c] == val:
                            return False
                
        return True
                