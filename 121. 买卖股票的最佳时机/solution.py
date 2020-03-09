class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, s = 0, 0
        for x in range(len(prices)-1):
            s += prices[x+1]-prices[x]
            if s > m:
                m = s
            if s < 0:
                s = 0
        return m