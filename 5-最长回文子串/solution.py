class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: 
            return ""
        if len(s) == 1: 
            return s
        if len(s) == 2:
            if s[0] == s[1]: 
                return s
            else:
                return s[0]
        # 建立dp表并初始化
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for x in range(len(s)): # 所有长度为1的子串必定回文
            dp[x][x] = 1
        for x in range(len(s)-1): # 判断长度为2的子串
            dp[x][x+1] = 1 if s[x] == s[x+1] else 0
        # 开始以子串长度遍历
        for x in range(2,len(s)):
            for i in range(len(s)-x):
                dp[i][i+x] = dp[i+1][i+x-1] if s[i] == s[i+x] else 0
        # 决定返回值
        for j in range(len(s)-1,-1,-1):
            for i in range(len(s)-j):
                if dp[i][j+i] == 1: return s[i:j+i+1]
            
a = Solution()
print(a.longestPalindrome("abcda"))