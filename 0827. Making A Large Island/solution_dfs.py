class Solution:
    def count(self, grid: List[List[int]], start_y: int, start_x: int) -> int:
        visited = [[start_x, start_y]]
        queue = [[start_x, start_y]]
        
        while queue:
            x, y = queue[0]
            del queue[0]
 
            if [x, y] not in visited:
                visited.append([x, y])

            steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for step in steps:
                x_next = x + step[0]
                y_next = y + step[1]
                
                if x_next < len(grid[0]) and x_next > -1 and \
                   y_next < len(grid)    and y_next > -1 and \
                   [x_next, y_next] not in visited and \
                   grid[x_next][y_next] == 1:
                    #print([x_next, y_next], grid[x_next][y_next])
                    queue.append([x_next, y_next])
                    
        #print(grid, visited)
        return len(visited)
                   
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        has_zero = False
        result = -1
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[y][x] = 1
                    result = max(result, self.count(grid, x, y))
                    grid[y][x] = 0
                    
        return result if has_zero else len(grid)*len(grid[0])
