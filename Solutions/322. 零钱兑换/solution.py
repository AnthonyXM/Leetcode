from typing import List

class Solution:
    def __init__(self):
        self.ans = 32767

    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins)==0 or amount==0:
            return -1
        coins.sort()
        self.CoinChange(coins, amount, 0, len(coins)-1)
        return self.ans if self.ans!=32767 else -1
        
    def CoinChange(self, coins: List[int], curr_amount: int, count: int, curr_depth: int) -> None:
        if curr_amount == 0:
            self.ans =  min(self.ans, count)
            return
        if curr_depth == -1:
            return
        for x in range(curr_amount//coins[curr_depth],-1,-1):
            if count + x >= self.ans:
                return
            self.CoinChange(coins, curr_amount-x*coins[curr_depth], count+x, curr_depth-1)


b = Solution()
# print(b.coinChange([3,7,405,436],8839))
# print(b.coinChange([1,7,10],14))
print(b.coinChange([80,149,71,111],8683))