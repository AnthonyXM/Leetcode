# 动态规划，注意初始条件
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 注意".*"可匹配任意字符串（匹配机制应该是先复制前面的"."
        if s == "" and p == "": # 空串都可匹配空串
            return True
        if p == "": # 空串不能匹配任何非空串
            return False

        # dp[i][j]代表s的前i位能否被p的前j位匹配
        dp = [[0 for x in range(len(p)+1)] for y in range(len(s)+1)]
        # 初始条件
        dp[0][0] = 1
        dp[0][1] = 0
        for x in range(2, len(p)+1):
            if p[x-1] == '*': dp[0][x] = dp[0][x-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] # "*"匹配为0个字符
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = (dp[i][j-1] or dp[i-1][j] or dp[i][j-2])
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[-1][-1] == 1
        
a = Solution()
print(a.isMatch("aaa","aaaa"))