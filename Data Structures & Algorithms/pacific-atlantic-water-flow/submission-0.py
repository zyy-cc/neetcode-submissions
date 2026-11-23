class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nr = len(heights)
        nc = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, visited):
            # only valid position is added in visited
            visited.add((r, c))

            for dr, dc in directions:
                nr2 = r + dr
                nc2 = c + dc
                if not (0 <= nr2 < nr and 0 <= nc2 < nc):
                    continue

                if (nr2, nc2) in visited:
                    continue

                if heights[nr2][nc2] >= heights[r][c]:
                    dfs(nr2, nc2, visited)

        # Pacific:
        # top row
        for c in range(nc):
            dfs(0, c, pacific)

        # left column
        for r in range(nr):
            dfs(r, 0, pacific)

        # Atlantic:
        # bottom row
        for c in range(nc):
            dfs(nr - 1, c, atlantic)

        # right column
        for r in range(nr):
            dfs(r, nc - 1, atlantic)

        res = []

        # 5. pacific atlantic intersection
        for r in range(nr):
            for c in range(nc):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res