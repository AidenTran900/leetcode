# I tried practicing DP reduction

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

    # BRUTE FORCE O(2^N)

        # NEG = float('-inf')

        # def solve(i, started):
        #     if i == n:
        #         return 0 if started else NEG 

        #     if started:
        #         return max(0, nums[i] + solve(i + 1, True))
        #     else:
        #         return max(solve(i + 1, False), nums[i] + solve(i + 1, True))

    # MEMOIZED O(N) time, O(N) space

        # cache = [0] * n
        # cache[n - 1] = nums[n - 1]

        # for i in range(n - 2, -1, -1):
        #     cache[i] = nums[i] + max(
        #         0, 
        #         cache[i + 1]
        #     )

        # return max(cache)

    # TWO VARIABLES O(N) time, O(1) space
        # we know that we can overwrite cache[i+1] with cache[i]. This means we can store as a single variable, cur
        # since we do not store entire cache, we cannot do max(cache). In this case, we have to keep another variable that stores the best so far

        cur = nums[n-1]
        best = cur

        for i in range(n - 2, -1, -1):
            cur = nums[i] + max(
                0, 
                cur
            )
            best = max(cur, best)

        return best