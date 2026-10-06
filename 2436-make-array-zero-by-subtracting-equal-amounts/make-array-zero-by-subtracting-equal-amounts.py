import heapq

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # we know every unique element must be subtracted by something
        # only count unique nums because all will be reduced to 0 in 1 operation
        return len({x for x in nums if x > 0})