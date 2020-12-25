"""
没啥好说的，贪心+排序+双指针
"""


from typing import List

# greedy，排序后用最大的s去找最大合适的g，64ms，77.53%；15.9MB，9.43%
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        g_index, s_index = len(g)-1, len(s)-1
        count = 0
        while s_index >= 0 and g_index >= 0:
            while s[s_index] < g[g_index] and g_index >= 0:
                g_index -= 1
            if g_index < 0:
                break
            count += 1
            s_index -= 1
            g_index -= 1
        return count


a = Solution()
print(a.findContentChildren([1,2,3],[]))