class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        # first BFS start
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    r, c = i + di, j + dj
                    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1

        