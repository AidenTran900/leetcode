class Solution:
    def rob(self, nums: list[int]) -> int:
        # cases
            # you rob the house (if i>last+1)
            # you skip the house

        best_prev = 0 # total up to previous house
        best_prev2 = 0 # total up to 2 houses back

        for num in nums:
            temp = best_prev
            best_prev = max(best_prev2 + num, best_prev)
            best_prev2 = temp

        return best_prev