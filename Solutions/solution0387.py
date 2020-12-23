"""
解法一：哈希表储存字符索引
储存字符首次出现位置，重复出现计 len(s) ，
最后找所有索引最小的，如果是 len(s) 表示没找到，返回-1。
时间216ms，超过20%；内存14.7MB，超过11%

解法二：暴力枚举
看到提示“你可以假定该字符串只包含小写字母。”，
那么直接遍历26个小写字母，找出现过 & 首次出现位置=最后出现位置 & 索引最小的字符
时间44ms，超过98.94%；内存15MB，超过5.51%
"""

# class Solution:
#     @staticmethod
#     def firstUniqChar(s: str) -> int:
#         char_dic = {}
#         for i in range(len(s)):
#             if s[i] in char_dic:
#                 char_dic[s[i]] = len(s)
#             else:
#                 char_dic[s[i]] = i
#         index = len(s)
#         for i in range(len(s)):
#             if char_dic[s[i]] < index:
#                 index = i
#         return index if index < len(s) else -1


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        index = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            _ = s.find(c)
            if _ != -1 and _ == s.rfind(c) and _ < index:
                index = _
        return index if index < len(s) else -1


a = Solution()
print(a.firstUniqChar("loveleetcode"))