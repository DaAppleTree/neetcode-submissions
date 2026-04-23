class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi = [], []
        m = prices[0]
        for i in range(0, len(prices), 1):
            if prices[i] < m:
                m = prices[i]
            lo.append(m)

        m = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > m:
                m = prices[i]
            hi.insert(0,m)
        
        m = hi[0] - lo[0]
        for i in range(len(prices)):
            if hi[i] - lo[i] > m:
                m = hi[i] - lo[i]
        return m
        