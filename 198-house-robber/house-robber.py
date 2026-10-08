class Solution:
    def rob(self, nums: list[int]) -> int:
        # cases
            # you rob the house (if i>last+1)
            # you skip the house

        prev0 = 0
        prev1 = 0

        for num in nums:
            temp = prev0
            prev0 = max(prev1 + num, prev0)
            prev1 = temp

        return prev0