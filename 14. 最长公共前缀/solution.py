# 没啥好说的...
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        r = ""
        c = 0
        while True:
            s = ""
            for x in range(len(strs)):
                if len(strs[x]) == c:
                    return r
                if s == "":
                    s = strs[x][c]
                else:
                    if s != strs[x][c]:
                        return r
            r += s
            c -=- 1
        return r

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))