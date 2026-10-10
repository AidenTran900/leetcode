class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.execute(nums[1:]), 
            self.execute(nums[:-1])
        )
        

    def execute(self, nums):
        best_prev = 0
        best_prev2 = 0

        for num in nums:
            temp = best_prev
            best_prev = max(best_prev2 + num, best_prev)
            best_prev2 = temp

        return best_prev
