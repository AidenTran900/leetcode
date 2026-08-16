class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if m == 0: return
        n = len(grid[0])

        islands = 0

        def recurse(i, j):
            if i < 0: return
            if i > m - 1: return
            if j < 0: return
            if j > n - 1: return

            if grid[i][j] == "0": return

            grid[i][j] = "0"

            recurse(i + 1, j) # Right
            recurse(i - 1, j) # Left
            recurse(i, j + 1) # Up
            recurse(i, j - 1) # Down

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    recurse(i, j)

        return islands