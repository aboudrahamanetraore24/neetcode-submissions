class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        n, best, min_seen = len(prices),0, prices[0]
        for l in range(1, n):
            if prices[l] < min_seen:
                min_seen = prices[l]
            best = max(best, prices[l]-min_seen)
        return best