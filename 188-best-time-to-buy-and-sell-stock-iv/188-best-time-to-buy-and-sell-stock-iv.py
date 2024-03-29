class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if l == 0:
            return 0
        
        dp = [[0]*l for _ in range(k+1)]
        for n in range(1, k+1):
            max_val = -prices[0]
            for i in range(1, l):
                max_val = max(max_val, dp[n-1][i-1] - prices[i])
                dp[n][i] = max(max_val + prices[i], dp[n][i-1])
        return dp[-1][-1]
        