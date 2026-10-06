class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # 1 sort
        nums.sort()

        # 2 sliding window
        last = nums[0]

        count = 1
        greatest = count
        
        for i, num in enumerate(nums):
            if num == last + 1:
                count += 1
                greatest = max(greatest, count)
            elif num != last:
                count = 1
                
            last = num


        return greatest