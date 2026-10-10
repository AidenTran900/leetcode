class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def solve(step):
            if step > n:
                return 0

            if step in cache:
                return cache[step]

            if step == n:
                return 1

            cache[step] = solve(step + 1) + solve(step+2)
            return cache[step]

        return solve(0)
