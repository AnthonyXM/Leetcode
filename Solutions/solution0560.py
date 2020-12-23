"""
前缀和的思路是：

首先我们肯定需要计算连续子列和，
在暴力双重循环遍历子列和中，前缀和一直在被重复计算，
而只要有一个前缀和的list，所有的子列和都可以在 O(1) 得到。

注意到条件是 sum(j+1)-sum(i)=k , 移项得到 sum(i)=sum(j+1)-k ,
j+1 是循环变量，我们需要遍历 0<=i<=j ，
通过创建一个相同前缀和出现次数的哈希表（map）来实现 O(1) 的遍历。

同时我们注意到一个特例：空列是不符合题意的（至少test case是这样说的），
这个特例可以通过一个很巧妙的方法解决：
因为这个情况只会出现在 i=j+1 的时候（空列），
我们选择在循环到 j+1 时才将 sum(j+1) 加入map。
"""

from typing import List


class Solution:
    @staticmethod
    def subarray_sum(nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        prefix_sum = {0:1}
        s = 0
        count = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in prefix_sum:
                count += prefix_sum[s - k]
            if s in prefix_sum:
                prefix_sum[s] += 1
            else:
                prefix_sum[s] = 1
        return count


a = Solution()
print(a.subarray_sum([1],0))