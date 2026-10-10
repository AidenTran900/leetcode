class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up approach (top of stairs and accumulating downwards)

        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one