class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # choices:
            # right
            # down
        
        # brute force
            # def solve(x, y):
            #     if y < 0 or x >= n:
            #         return 0
                
            #     if y == 0 and x == n - 1:
            #         return 1
                
            #     return solve(x + 1, y) + solve(x, y - 1)

            # return solve(0, m - 1)

        # dp

        cache = [[1] * n for _ in range(m)]

        for c in range(1, n):
            for r in range(1, m):
                cache[r][c] = cache[r - 1][c] + cache[r][c - 1]

        return cache[m-1][n-1]