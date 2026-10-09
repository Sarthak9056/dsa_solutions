# Leetode Problem Number - 71

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0])
        m = len(matrix)
        rows = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in col:
                    matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        
