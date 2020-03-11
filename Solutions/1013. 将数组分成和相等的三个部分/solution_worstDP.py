from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        dp = [[0 for x in range(len(A))] for y in range(len(A))]
        for x in range(len(A)):
            dp[x][x] = A[x]
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                dp[i][j] = dp[i][j-1] + dp[j][j]
        dic = {} # [dp值: [需验证的i]]
        for j in range(len(A)-2):
            if dp[0][j] not in dic:
                dic[dp[0][j]] = [j]
            else:
                dic[dp[0][j]] += [j]
        for i in range(2, len(A)):
            if dp[i][len(A)-1] in dic:
                e = dic[dp[i][len(A)-1]]
                for x in range(len(e)):
                    if dp[e[x]+1][i-1] == dp[i][len(A)-1] and dic[dp[i][len(A)-1]][x]+1 < i:
                        return True
        return False

a = Solution()
print(a.canThreePartsEqualSum([1,1,1,1]))