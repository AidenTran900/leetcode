class Solution:
    def canJump(self, nums: list[int]) -> bool:

        n = len(nums)
        
        # brute force

            # cases:
                # jump 1 ... nums[i] times
                # reach 0, cannot skip

            # def solve(i):
            #     if i >= n:
            #         return False
            #     if i == n-1:
            #         return True

            #     jumps = nums[i]

            #     if jumps == 0:
            #         return False
                
            #     can_reach = False
            #     for jump in range(1, jumps+1):
            #         can_reach = solve(i + jump) or can_reach

            #     return can_reach
                
            # return solve(0)
        
        # DP
            # start from the goal
            # next index, set to new goal if reachable
            # repeat

        goal = n - 1
        for i in range(n - 2, -1, -1):
            jumps = nums[i]

            if i + jumps >= goal:
                goal = i

        return goal == 0


            