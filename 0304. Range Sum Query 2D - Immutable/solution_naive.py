class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = deepcopy(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = 0
        for row_id in range(row1, row2+1):
            for col_id in range(col1, col2+1):
                summ += self.m[row_id][col_id]
        return summ
