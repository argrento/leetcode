class Solution:
    def neighbours(self, x, y):
        steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for step in steps:
            x_next = x + step[0]
            y_next = y + step[1]
            if x_next < len(self.grid[0]) and x_next > -1 and \
               y_next < len(self.grid)    and y_next > -1:
                yield (x_next, y_next)
    
    def count(self, x: int, y: int, color: int) -> int:
        r = 0
        self.grid[x][y] = color
        for x_n, y_n in self.neighbours(x, y):
            if self.grid[x_n][y_n] == 1:
                r += self.count(x_n, y_n, color)
        return r + 1
                   
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        has_zero = False
        result = -1
        color = 2
        areas = {0: 0}
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if grid[x][y] == 1:
                    area = self.count(x, y, color)
                    areas[color] = area
                    color += 1
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if self.grid[x][y] == 0:
                    has_zero = True
                    colors = []
                    subresult = 1
                    for (x_next, y_next) in self.neighbours(x, y):
                        c = self.grid[x_next][y_next]
                        if c not in colors:
                            subresult += areas[c]
                            colors.append(c)
                    result = max(result, subresult)
                                   
        return result if has_zero else len(grid)*len(grid)
