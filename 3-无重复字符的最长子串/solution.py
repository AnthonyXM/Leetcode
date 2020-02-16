class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i = 0
        j = 0
        length = 1
        while j < len(s) - 1:
            # 先尝试增加长度，条件：j+1位不与i~j位重复，倒序检索
            # 若不重复则j++
            # 若重复，则直接整跳到重复位的后一位并开始滑动
            k = -1
            while j < len(s) - 1: # 增加长度的循环,不能继续增加长度时终止
                for x in range(j, i - 1, -1):
                    if s[x] == s[j+1]:
                        k = x
                        break
                if k != -1: # 若k不是-1，说明j+1位和k位重复，直接整跳到重复位的后一位并开始滑动
                    i = k + 1
                    j = i + length - 1
                    break
                else:
                    j += 1
                    length += 1
            # 不清楚当前子串是否存在重复位
            while j < len(s) - 1: # 滑动的循环，滑动至一个合法位置时终止
                test = []
                for x in range(j, i - 1, -1):
                    if s[x] in test: # x是重复位
                        i = x + 1
                        j = i + length - 1
                        break
                    else:
                        test.append(s[x])
                