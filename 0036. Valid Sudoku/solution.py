class Solution:
    def check(self, tokens: List[str]):
        seen = set()
        for token in tokens:
            if token == '.':
                continue
            else:
                if token not in seen:
                    seen.add(token)
                else:
                    return False
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check lines
        for line in board:
            if not self.check(line):
                return False
        
        # check columns
        for col_idx in range(9):
            column = [line[col_idx] for line in board]
            if not self.check(column):
                return False
            
        # check 3x3 blocks
        for block_x in range(3):
            for block_y in range(3):
                block = [board[x][y] for x in range(block_x*3, block_x*3+3) 
                                     for y in range(block_y*3, block_y*3+3)]
                if not self.check(block):
                    return False
            
        return True