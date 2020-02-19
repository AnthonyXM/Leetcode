class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # 从“队列”中pop的下标
        max_length = 0 # 达到过的最长字串
        curr_length = 0 # 当前串长度（出入表均需维护）
        lookup = set() # 查找表
        for x in range(len(s)):
             # 每次往后查一个字符
            while s[x] in lookup: # 直到最后到s[x]的子串无重复元素
                lookup.remove(s[left])
                curr_length -= 1
                left += 1
            lookup.add(s[x])
            curr_length += 1
            if curr_length > max_length: max_length = curr_length
        return max_length

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))