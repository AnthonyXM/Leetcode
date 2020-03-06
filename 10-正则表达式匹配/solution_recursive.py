# 大家当然愿意写简单又短的啦~如果未来计算机速度足够快的话，时间复杂度根本不是事儿，写的快才是王道

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 注意".*"可匹配任意字符串（匹配机制应该是先复制前面的"."
        if s == "" and (p == "" or (len(p)==2 and p[1] == "*")):
            return True
        
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[0]+p) or self.isMatch(s, p[2:])
        if len(s)>=1 and len(p)>=1 and (s[0] == p[0] or p[0] == "."):
            return self.isMatch(s[1:],p[1:])
        return False

a = Solution()
print(a.isMatch("","c*c*"))