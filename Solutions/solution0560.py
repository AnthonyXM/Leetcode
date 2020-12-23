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