from typing import List

class Solution:
    # 尝试在一个函数里解决但失败了，好像很麻烦的样子，不如主函数分个类来算 （因为思路是寻找第k个数，对于总个数为偶数的本身就需要找两次）
    def findKTH(self, nums1: List[int], nums2: List[int], k: int) -> float:
        # k为从1开始的序数！
        m = len(nums1)
        n = len(nums2)
        if m < n:
            return self.findKTH(nums2, nums1, k) # 这一行把运行时间降低了一半...不知道为啥 初步理解是为了适配test case（可能比较长的数列普遍比较小而紧凑？）
        # 边界条件1：某一数列为空
        if m == 0:
            return nums2[k-1]
        if n == 0:
            return nums1[k-1]
        # 边界条件2：找第1个数
        if k == 1:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]
        if nums1[(k//2 - 1) if (k//2 <= m) else (m - 1)] < nums2[(k//2 - 1) if (k//2 <= n) else (n - 1)]: # 说明 1的前k//2个数都不可能是第k个数，直接舍去
            return self.findKTH((nums1[k//2:] if (k//2 <= m) else []), nums2, ((k - k//2) if (k//2 <= m) else (k - m)))
        if nums1[(k//2 - 1) if (k//2 <= m) else (m - 1)] >= nums2[(k//2 - 1) if (k//2 <= n) else (n - 1)]: # 说明 2的前k//2个数都不可能是第k个数，直接舍去
            return self.findKTH(nums1, (nums2[k//2:] if (k//2 <= n) else []), ((k - k//2) if (k//2 <= n) else (k - n)))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total & 0x1:
            return self.findKTH(nums1, nums2, total//2 + 1)
        else:
            return (self.findKTH(nums1, nums2, total//2 + 1) + self.findKTH(nums1, nums2, total//2)) / 2

a = Solution()
print(a.findMedianSortedArrays([1],[2,3,4,5,6,7,8]))