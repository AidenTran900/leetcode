class Solution:
    def profitableSchemes(
        self, 
        n: int, 
        minProfit: int, 
        group: list[int], 
        profit: list[int]
    ) -> int:

        length = len(group)
        MOD = 10**9 + 7
        
        # value: count
        # row: profit
        # col: people used
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for crime in range(length):
            people = group[crime]
            gain = profit[crime]

            for used in range(n - people, -1, -1):
                for cur_profit in range(minProfit + 1):
                    new_profit = min(minProfit, cur_profit + gain)
                    total_people = used + people

                    dp[total_people][new_profit] = (
                        dp[total_people][new_profit] + dp[used][cur_profit]
                    ) % MOD

        return sum(dp[used][minProfit] for used in range(n + 1)) % MOD