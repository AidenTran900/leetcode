class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        returned = []
        for fixed in range(len(nums)):
            left = fixed + 1
            right = len(nums) - 1

            # If our fixed number is the same as the last, skip
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            while left < right:
                tot = nums[fixed] + nums[left] + nums[right]

                if tot == 0:
                    returned.append([nums[fixed], nums[left], nums[right]])

                    # If our left number is the same as the last, skip
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # If our right number is the same as the last, skip
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif tot > 0:
                    right -= 1

                else: # tot < 0
                    left += 1

        
        return returned