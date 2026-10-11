class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        # NEG = float('-inf')

        # def solve(i, started):
        #     if i == n:
        #         return 0 if started else NEG 

        #     if started:
        #         return max(0, nums[i] + solve(i + 1, True))
        #     else:
        #         return max(solve(i + 1, False), nums[i] + solve(i + 1, True))

        cache = [0] * n
        cache[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            cache[i] = nums[i] + max(
                0, 
                cache[i + 1]
            )

        return max(cache)