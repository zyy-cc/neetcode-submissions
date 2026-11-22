class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(grid, i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                left = dfs(grid, i - 1, j)
                right = dfs(grid, i + 1, j)
                up = dfs(grid, i, j - 1)
                down = dfs(grid, i, j + 1)
                return 1 + left + right + up + down

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(grid, i, j)
                    max_area = max(area, max_area)
        return max_area

        