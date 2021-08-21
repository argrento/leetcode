class Solution:
    def can_place(self, board: List[List[str]], x: int, y: int, num: str):
        # check row
        if any(num == n for n in board[x]):
            return False

        # check column
        if any(num == n for n in list(zip(*board))[y]):
            return False

        # check box
        box_r, box_c = (x // 3) * 3, (y // 3) * 3
        for r in range(box_r, box_r + 3):
            for c in range(box_c, box_c + 3):
                if num == board[r][c]:
                    return False

        return True

    def get_empty(self, board: List[List[str]]):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    return r, c
        return -1, -1

    def solve(self, board: List[List[str]]):
        r, c = self.get_empty(board)
        if r == -1 and c == -1:
            return True

        for num in [str(n) for n in range(1, 10)]:
            if self.can_place(board, r, c, num):
                board[r][c] = num
                if self.solve(board):
                    return True
                board[r][c] = '.'
        return False
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
        
        