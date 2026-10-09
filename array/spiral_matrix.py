# Leetode Problem Number - 54

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. top row, left -> right
            for j in range(left, right + 1):
                output.append(matrix[top][j])
            top += 1

            # 2. right column, top -> bottom
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            # 3. bottom row, right -> left  (guarded)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    output.append(matrix[bottom][j])
                bottom -= 1

            # 4. left column, bottom -> top  (guarded)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1

        return output
