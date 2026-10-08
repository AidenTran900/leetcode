class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        nums.sort()
        last = -1
        
        for num in nums:
            if last + 1 != num:
                return last + 1

            last = num

        return last + 1

        