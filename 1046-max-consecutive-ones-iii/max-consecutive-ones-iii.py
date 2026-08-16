class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        largest = 0
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k: # keep movin left until zeroes is <= k
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            largest = max(largest, right - left + 1)
        
        return largest