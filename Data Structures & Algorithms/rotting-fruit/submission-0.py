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
        
        def bfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 2
                queue.append((i,j))
                return 1
            return 0

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                fresh -= bfs(i - 1, j)
                fresh -= bfs(i + 1, j)
                fresh -= bfs(i, j - 1)
                fresh -= bfs(i, j + 1)
            minutes += 1
        
        return minutes if fresh == 0 else -1

        