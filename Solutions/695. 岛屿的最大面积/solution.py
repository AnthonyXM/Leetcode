from typing import List

class Solution:
    def area(self, grid: List[List[int]], i: int, j: int):
        ans = 1
        grid[i][j] = 0
        if i>=1 and grid[i-1][j] == 1:
            ans += self.area(grid, i-1, j)
        if i<len(grid)-1 and grid[i+1][j] == 1:
            ans += self.area(grid, i+1, j)
        if j>=1 and grid[i][j-1] == 1:
            ans += self.area(grid, i, j-1)
        if j<len(grid[i])-1 and grid[i][j+1] == 1:
            ans += self.area(grid, i, j+1)
        return ans


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    temp = self.area(grid, i, j)
                    if temp > ans:
                        ans = temp
        return ans

a = Solution()
print(a.maxAreaOfIsland([[1,1],[1,0]]))