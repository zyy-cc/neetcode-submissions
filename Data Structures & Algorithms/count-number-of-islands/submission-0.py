class Solution:
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return 
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    counter += 1
        return counter

        