class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}

        # 1. create frequency map
        for i, num in enumerate(nums):
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        # 2. sort frequency map
        sort_nums = sorted(set(nums), key=lambda x : freq_map[x], reverse=True)

        return sort_nums[:k]