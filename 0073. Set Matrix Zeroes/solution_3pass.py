class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if val == 0:
                    matrix[row_idx][col_idx] = 'z'
                    
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if val == 'z':
                    # set elements to zero
                    for idx in range(len(matrix)):
                        if matrix[idx][col_idx] != 'z':
                            matrix[idx][col_idx] = 0
                    for idx in range(len(matrix[0])):
                        if matrix[row_idx][idx] != 'z':
                            matrix[row_idx][idx] = 0
                            
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if val == 'z':
                    matrix[row_idx][col_idx] = 0
