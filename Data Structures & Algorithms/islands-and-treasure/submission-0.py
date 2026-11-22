class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))

        step = 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    r, c = i + di, j + dj

                    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 2147483647):
                        grid[r][c] = step
                        queue.append((r, c))
            step += 1
        
        
        