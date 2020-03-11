# 三数之和为0 = 两数之和为...
# 两数之和为... = 存在一个数是...
from typing import List
import copy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for x in range(len(nums)):
            if nums[x] in dic:
                dic[nums[x]] += [x]
            else:
                dic[nums[x]] = [x]
        
        ans = []
        for x in range(len(nums)):
            curr_value = nums[x]
            dic[curr_value].remove(x)
            curr_dic = copy.deepcopy(dic)
            for y in range(x+1, len(nums)):
                v = nums[y]
                curr_dic[v].remove(y)
                if -v-curr_value in curr_dic and curr_dic[-v-curr_value] != []:
                    ans += [[curr_value, v, nums[z]] for z in curr_dic[-v-curr_value]]
        
        for x in ans:
            x.sort()
        c = len(ans)
        x = 0
        while x < c:
            y = x+1
            while y < c:
                if ans[x][0]==ans[y][0] and ans[x][1] == ans[y][1]:
                    del ans[y]
                    y -= 1
                    c -= 1
                y += 1
            x += 1

        return ans

a = Solution()
print(a.threeSum([12,-14,-5,12,-2,9,0,9,-3,-3,-14,-6,-4,13,-11,-8,0,5,-7,-6,-10,-13,-7,-14,-3,0,12,5,-8,7,3,-11,0,6,9,13,-8,-6,7,4,6,0,13,-13,-1,9,-13,6,-1,-13,-15,-4,-11,-15,-11,-7,1,-14,13,8,0,2,4,-15,-15,-2,5,-8,7,-11,11,-10,4,1,-15,10,-5,-13,2,1,11,-6,4,-15,-5,8,-7,3,1,-9,-4,-14,0,-15,8,0,-1,-2,7,13,2,-5,11,13,11,11]))
        