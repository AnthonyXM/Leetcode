# 双指针

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, m = 0, len(height)-1, 0
        while i < j:
            if (j-i)*(min(height[i],height[j]))>m:
                m = (j-i)*(min(height[i],height[j]))
            if height[i] > height[j]: # 右边短
                j-=1
            else:
                i+=1
        return m