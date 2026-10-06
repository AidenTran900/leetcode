class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0

        while (max(nums) > 0):
            smallest = min([x for x in nums if x > 0])
            for i, num in enumerate(nums):
                nums[i] -= smallest
            
            operations += 1
        
        return operations
        