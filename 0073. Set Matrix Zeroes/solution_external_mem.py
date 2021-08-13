class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = []
        cols = []
        
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if val == 0:
                    rows.append(row_idx)
                    cols.append(col_idx)
                            
        for row_idx, col_idx in zip(rows, cols):
            for i in range(len(matrix[0])):
                matrix[row_idx][i] = 0
            for i in range(len(matrix)):
                matrix[i][col_idx] = 0