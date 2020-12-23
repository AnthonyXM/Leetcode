from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [0 for x in range(len(nums))]
        # 初始化
        dp[0] = 1

        for i in range(1,len(nums)):
            curr = nums[i]
            b = [dp[x] for x in range(i) if nums[x] < nums[i]]
            dp[i] = max(b) + 1 if b!=[] else 1
        
        return max([dp[x] for x in range(len(nums))])

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size<2:
            return size
        
        cell = [nums[0]]
        for num in nums[1:]:
            if num>cell[-1]:
                cell.append(num)
                continue
            
            l,r = 0,len(cell)-1
            while l<r:
                mid = l + (r - l) // 2
                if cell[mid]<num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num
        return len(cell)

        
a = Solution2()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))