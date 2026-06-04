class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        i = 0
        profit = 0
        for r in range(1, n):
            if prices[i] > prices[r]:
                i = r
            else:
                profit = max(profit, prices[r] - prices[i])
        return profit

example = Solution()
print(example.maxProfit([7,1,5,3,6,4]))