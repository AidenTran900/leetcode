class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        mid = (right + left) // 2
        smallest = nums[mid]

        while left <= right:
            mid = (right + left) // 2
            smallest = min(smallest, nums[mid])

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1


        return smallest